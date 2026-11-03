#!/usr/bin/env python3
"""Validate the Paper 2 evidence files and replay the convergence incumbents."""

from __future__ import annotations

import gzip
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

PROVENANCE = ROOT / "evidence" / "provenance-2026-11-03.json"
FRAMEWORK = ROOT / "evidence" / "framework-use.json"
TSP = ROOT / "evidence" / "tsp-convergence-10k.json"
QAP_EXPANDED = ROOT / "evidence" / "qap-expanded-100k.json"
BROAD = ROOT / "evidence" / "broad-converged.json.gz"
BROAD_SUMMARY = ROOT / "evidence" / "broad-converged-summary.json"


def require(record: dict[str, object], keys: tuple[str, ...], label: str) -> None:
    """Raise if a required field is absent."""
    missing = [key for key in keys if key not in record]
    if missing:
        raise SystemExit(f"{label}: missing {missing}")


def replay_qap(rows: list[dict[str, object]]) -> int:
    """Replay framework QAP incumbents exactly."""
    checked = 0
    for row in rows:
        require(
            row,
            (
                "instance",
                "seed",
                "framework",
                "baseline_cpu_seconds",
                "converged_on_patience",
            ),
            "framework",
        )
        framework = row["framework"]
        if not isinstance(framework, dict):
            raise SystemExit("framework: framework field is not an object")
        require(
            framework,
            (
                "assignment",
                "objective",
                "replay_objective",
                "exact_replay",
                "iterations",
                "cpu_seconds",
                "stop_reason",
            ),
            "framework.framework",
        )
        problem = QuadraticAssignment.from_qaplib(ROOT / "instances" / f"{row['instance']}.dat")
        assignment = {int(key): value for key, value in framework["assignment"].items()}
        evaluation = ResidentAssignment(problem, assignment).evaluate()
        if abs(evaluation.objective - float(framework["objective"])) > 1e-6:
            raise SystemExit(f"framework replay mismatch: {row['instance']} seed {row['seed']}")
        if not bool(framework["exact_replay"]):
            raise SystemExit(f"framework record not marked exact: {row['instance']}")
        if not bool(row["converged_on_patience"]):
            raise SystemExit(f"framework run not plateau-stopped: {row['instance']}")
        checked += 1
    return checked


def replay_tsp(rows: list[dict[str, object]]) -> int:
    """Replay TSP convergence incumbents exactly."""
    checked = 0
    for row in rows:
        require(
            row,
            (
                "instance",
                "seed",
                "objective",
                "optimality_gap_percent",
                "kicks",
                "kicks_budget",
                "patience",
                "stop_reason",
                "wall_seconds",
                "assignment",
                "converged_on_patience",
                "exact_replay",
            ),
            "tsp",
        )
        problem = TravellingSalesman.from_tsplib(ROOT / "instances" / f"{row['instance']}.tsp")
        assignment = {int(key): value for key, value in row["assignment"].items()}
        evaluation = ResidentAssignment(problem, assignment).evaluate()
        if abs(evaluation.objective - float(row["objective"])) > 1e-6:
            raise SystemExit(f"TSP replay mismatch: {row['instance']} seed {row['seed']}")
        if row["stop_reason"] != "patience" or not bool(row["converged_on_patience"]):
            raise SystemExit(f"TSP run not plateau-stopped: {row['instance']}")
        if not bool(row["exact_replay"]):
            raise SystemExit(f"TSP record not marked exact: {row['instance']}")
        if int(row["kicks"]) > int(row["kicks_budget"]):
            raise SystemExit(f"TSP kick count exceeds cap: {row['instance']}")
        checked += 1
    return checked


def main() -> int:
    """Validate provenance, convergence records, broad records, and summary."""
    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    require(
        provenance,
        ("solver_commit", "python", "platform", "qap_framework_workers", "tsp_workers"),
        "provenance",
    )
    framework = json.loads(FRAMEWORK.read_text(encoding="utf-8"))
    require(framework, ("qap", "qap_summary", "workers", "patience", "max_iterations"), "framework")
    qap_checked = replay_qap(framework["qap"])
    expanded = json.loads(QAP_EXPANDED.read_text(encoding="utf-8"))
    if len(expanded) != 100:
        raise SystemExit(f"expanded QAP panel has {len(expanded)} records, expected 100")
    for row in expanded:
        require(
            row,
            ("instance", "seed", "objective", "optimality_gap_percent", "exact_replay"),
            "qap-expanded",
        )
        if not bool(row["exact_replay"]):
            raise SystemExit(f"expanded QAP record not exact: {row['instance']}")
    tsp_rows = json.loads(TSP.read_text(encoding="utf-8"))
    tsp_checked = replay_tsp(tsp_rows)
    with gzip.open(BROAD, "rt", encoding="utf-8") as handle:
        broad = json.load(handle)
    successful = [row for row in broad if "gap" in row]
    require(
        successful[0], ("instance", "family", "seed", "size", "gap", "stop", "assignment"), "broad"
    )
    summary = json.loads(BROAD_SUMMARY.read_text(encoding="utf-8"))
    if not isinstance(summary, list) or not summary:
        raise SystemExit("broad summary is not a non-empty list")
    require(summary[0], ("family", "band", "runs", "patience_runs", "cap_runs"), "broad.summary")
    print(
        f"validated provenance; replayed {qap_checked} QAP and {tsp_checked} TSP incumbents; "
        f"broad records {len(broad)} with {len(summary)} summary rows"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
