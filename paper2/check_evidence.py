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
TSP_EXPANDED = ROOT / "evidence" / "tsp-expanded-10k.json"
BLS = ROOT / "evidence" / "qap-bls-10seed.json"
GENERIC = ROOT / "evidence" / "generic-tabu.json"
LKH = ROOT / "evidence" / "lkh-large.json"
QAP_EXPANDED = ROOT / "evidence" / "qap-expanded-100k-10seed.json"
BROAD = ROOT / "evidence" / "broad-converged.json.gz"
BROAD_SUMMARY = ROOT / "evidence" / "broad-converged-summary.json"
MULTISTART = ROOT / "evidence" / "qap-multistart-converged.jsonl"


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
    if len(expanded) != 200:
        raise SystemExit(f"expanded QAP panel has {len(expanded)} records, expected 200")
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
    bls = json.loads(BLS.read_text(encoding="utf-8"))
    if len(bls) != 200:
        raise SystemExit(f"BLS panel has {len(bls)} records, expected 200")
    for row in bls:
        require(
            row,
            (
                "instance",
                "seed",
                "objective",
                "optimality_gap_percent",
                "exact_replay",
                "stop_reason",
            ),
            "bls",
        )
        if not bool(row["exact_replay"]):
            raise SystemExit(f"BLS record not exact: {row['instance']}")
        if row["stop_reason"] != "patience":
            raise SystemExit(f"BLS record not plateau-stopped: {row['instance']}")
    generic = json.loads(GENERIC.read_text(encoding="utf-8"))
    if len(generic) != 40:
        raise SystemExit(f"generic-tabu panel has {len(generic)} records, expected 40")
    for row in generic:
        require(
            row,
            (
                "instance",
                "seed",
                "objective",
                "optimality_gap_percent",
                "exact_replay",
                "stop_reason",
            ),
            "generic",
        )
        if not bool(row["exact_replay"]) or row["stop_reason"] != "patience":
            raise SystemExit(f"generic-tabu record invalid: {row['instance']}")
    lkh = json.loads(LKH.read_text(encoding="utf-8"))
    if len(lkh) != 100:
        raise SystemExit(f"LKH panel has {len(lkh)} records, expected 100")
    for row in lkh:
        require(row, ("instance", "seed", "objective", "optimality_gap_percent"), "lkh")
        if float(row["optimality_gap_percent"]) < -1e-9:
            raise SystemExit(f"negative LKH gap: {row['instance']}")
    if TSP_EXPANDED.exists():
        expanded_tsp = json.loads(TSP_EXPANDED.read_text(encoding="utf-8"))
        if len(expanded_tsp) != 100:
            raise SystemExit(f"expanded TSP panel has {len(expanded_tsp)} records, expected 100")
        cap_hits = 0
        for row in expanded_tsp:
            require(
                row,
                (
                    "instance",
                    "seed",
                    "objective",
                    "optimality_gap_percent",
                    "exact_replay",
                    "stop_reason",
                ),
                "tsp-expanded",
            )
            if not bool(row["exact_replay"]):
                raise SystemExit(f"expanded TSP record not exact: {row['instance']}")
            if row["stop_reason"] == "max_seconds":
                cap_hits += 1
            elif row["stop_reason"] != "patience":
                raise SystemExit(f"unexpected expanded TSP stop: {row['stop_reason']}")
        print(f"expanded TSP cap hits: {cap_hits}/100 (reported, not convergence)")
    with gzip.open(BROAD, "rt", encoding="utf-8") as handle:
        broad = json.load(handle)
    successful = [row for row in broad if "gap" in row]
    require(
        successful[0],
        ("instance", "family", "seed", "size", "gap", "stop", "assignment", "solver_commit"),
        "broad",
    )
    multi = [
        json.loads(line)
        for line in MULTISTART.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    for row in multi:
        require(
            row,
            ("instance", "objective", "assignment", "exact_replay", "solver_commit"),
            "multistart",
        )
        if not bool(row["exact_replay"]):
            raise SystemExit(f"large-QAP record not exact: {row['instance']}")
    summary = json.loads(BROAD_SUMMARY.read_text(encoding="utf-8"))
    if not isinstance(summary, list) or not summary:
        raise SystemExit("broad summary is not a non-empty list")
    require(summary[0], ("family", "band", "runs", "patience_runs", "cap_runs"), "broad.summary")
    print(
        f"validated provenance; replayed {qap_checked} QAP and {tsp_checked} TSP incumbents; "
        f"broad records {len(broad)} with {len(summary)} summary rows; "
        f"large-QAP records {len(multi)} exact; BLS records {len(bls)} exact; "
        f"generic-tabu records {len(generic)} exact; LKH records {len(lkh)} non-negative"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
