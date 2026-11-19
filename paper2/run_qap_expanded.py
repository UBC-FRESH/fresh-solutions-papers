#!/usr/bin/env python3
"""Run the expanded 20-instance QAP convergence panel."""

from __future__ import annotations

import json
import multiprocessing
import os
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402
from fresh_solutions.adapters.qap_tabu import QapTabuConfig, run_qap_tabu  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

QAP_ROOT = Path(os.environ.get("QAPLIB_ROOT", "benchmarks/qaplib/QAPLIB"))
SEEDS = tuple(int(value) for value in os.environ.get("QAP_EXPANDED_SEEDS", "1,2,3,4,5").split(","))
INSTANCES = (
    "tai12a",
    "tai20a",
    "tai25a",
    "tai30a",
    "tai35a",
    "tai40a",
    "tai50a",
    "bur26a",
    "bur26b",
    "bur26c",
    "bur26d",
    "bur26e",
    "bur26f",
    "bur26g",
    "bur26h",
    "chr12a",
    "chr15a",
    "chr18a",
    "chr20a",
    "chr22a",
)
ITERATIONS = int(os.environ.get("QAP_EXPANDED_ITERATIONS", "1000000"))
PATIENCE = int(os.environ.get("QAP_EXPANDED_PATIENCE", "100000"))
WORKERS = int(os.environ.get("QAP_EXPANDED_WORKERS", str(min(40, os.cpu_count() or 1))))
OUT = ROOT / "evidence" / os.environ.get("QAP_EXPANDED_OUT", "qap-expanded-100k.json")
SUMMARY = (
    ROOT / "evidence" / os.environ.get("QAP_EXPANDED_SUMMARY", "qap-expanded-100k-summary.json")
)


def optimum(name: str) -> float:
    """Read the QAPLIB optimum from the .sln sidecar."""
    text = (QAP_ROOT / f"{name}.sln").read_text(encoding="utf-8").split()
    return float(text[1])


def run_task(task: tuple[str, float, int]) -> dict[str, object]:
    """Run one QAP seed and return a replayable record."""
    name, known, seed = task
    problem = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{name}.dat")
    started = time.perf_counter()
    result = run_qap_tabu(
        problem,
        QapTabuConfig(iterations=ITERATIONS, patience=PATIENCE, seed=seed),
    )
    wall = time.perf_counter() - started
    assignment = dict(result.assignment)
    replay = ResidentAssignment(problem, assignment).evaluate()
    gap = 100.0 * (result.objective - known) / known
    return {
        "instance": name,
        "size": problem.variable_count,
        "seed": seed,
        "known_optimum": known,
        "objective": result.objective,
        "optimality_gap_percent": gap,
        "iterations": result.iterations,
        "stop_reason": result.stop_reason,
        "wall_seconds": wall,
        "assignment": assignment,
        "replay_objective": replay.objective,
        "exact_replay": abs(replay.objective - result.objective) <= 1e-6,
        "converged_on_patience": result.stop_reason == "patience",
    }


def main() -> int:
    """Run the panel in parallel and write per-run and summary evidence."""
    tasks = [(name, optimum(name), seed) for name in INSTANCES for seed in SEEDS]
    records: list[dict[str, object]] = []
    with ProcessPoolExecutor(
        max_workers=max(1, min(WORKERS, len(tasks))),
        mp_context=multiprocessing.get_context("spawn"),
    ) as executor:
        futures = {executor.submit(run_task, task): task for task in tasks}
        for index, future in enumerate(as_completed(futures), 1):
            records.append(future.result())
            if index % 10 == 0 or index == len(tasks):
                print(f"completed {index}/{len(tasks)}", flush=True)
    records.sort(key=lambda row: (str(row["instance"]), int(row["seed"])))
    summaries: list[dict[str, object]] = []
    for name in INSTANCES:
        rows = [row for row in records if row["instance"] == name]
        gaps = [float(row["optimality_gap_percent"]) for row in rows]
        summaries.append(
            {
                "instance": name,
                "size": rows[0]["size"],
                "runs": len(rows),
                "best_gap_percent": min(gaps),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "worst_gap_percent": max(gaps),
                "patience_runs": sum(bool(row["converged_on_patience"]) for row in rows),
                "optimum_runs": sum(gap < 1e-9 for gap in gaps),
                "mean_wall_seconds": statistics.mean(float(row["wall_seconds"]) for row in rows),
            }
        )
        print(
            f"{name}: mean={statistics.mean(gaps):.3f}% worst={max(gaps):.3f}% "
            f"patience={summaries[-1]['patience_runs']}/{len(rows)}",
            flush=True,
        )
    OUT.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    SUMMARY.write_text(json.dumps(summaries, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
