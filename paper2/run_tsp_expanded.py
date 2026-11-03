#!/usr/bin/env python3
"""Run the expanded 20-instance TSP convergence panel from nearest-neighbour starts."""

from __future__ import annotations

import json
import multiprocessing
import os
import re
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import TravellingSalesman  # noqa: E402
from fresh_solutions.adapters.tsp_lk import TspLkConfig, run_tsp_lk  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

TSP_ROOT = Path(os.environ.get("TSPLIB_ROOT", "benchmarks/tsplib"))
SEEDS = (1, 2, 3, 4, 5)
INSTANCES = (
    "att48",
    "berlin52",
    "bier127",
    "brazil58",
    "ch130",
    "ch150",
    "d198",
    "eil51",
    "eil76",
    "eil101",
    "fri26",
    "gr120",
    "gr137",
    "kroA100",
    "kroB100",
    "kroC100",
    "kroD100",
    "kroE100",
    "lin105",
    "pr76",
)
KICKS = int(os.environ.get("TSP_EXPANDED_KICKS", "10000"))
PATIENCE = int(os.environ.get("TSP_EXPANDED_PATIENCE", "1000"))
WORKERS = int(os.environ.get("TSP_EXPANDED_WORKERS", str(min(20, os.cpu_count() or 1))))
OUT = ROOT / "evidence" / "tsp-expanded-10k.json"
SUMMARY = ROOT / "evidence" / "tsp-expanded-10k-summary.json"


def optima() -> dict[str, float]:
    """Read TSPLIB known optima."""
    values: dict[str, float] = {}
    for line in (TSP_ROOT / "solutions").read_text(encoding="utf-8").splitlines():
        match = re.match(r"(\S+)\s*:\s*([0-9.]+)", line.strip())
        if match:
            values[match.group(1)] = float(match.group(2))
    return values


def nearest_neighbour(problem: TravellingSalesman, start: int) -> dict[int, int]:
    """Build a deterministic nearest-neighbour tour."""
    size = problem.variable_count
    unseen = set(range(size))
    unseen.remove(start)
    tour = [start]
    current = start
    while unseen:
        current = min(unseen, key=lambda city: (problem.distances[current][city], city))
        tour.append(current)
        unseen.remove(current)
    return dict(enumerate(tour))


def run_task(task: tuple[str, float, int]) -> dict[str, object]:
    """Run one TSP seed and return a replayable record."""
    name, known, seed = task
    problem = TravellingSalesman.from_tsplib(TSP_ROOT / f"{name}.tsp")
    initial = nearest_neighbour(problem, seed % problem.variable_count)
    initial_objective = problem.evaluate(initial).objective
    started = time.perf_counter()
    result = run_tsp_lk(
        problem,
        TspLkConfig(
            candidate_count=16,
            max_depth=4,
            kicks=KICKS,
            patience=PATIENCE,
            seed=seed,
        ),
        initial,
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
        "initial_objective": initial_objective,
        "initial_gap_percent": 100.0 * (initial_objective - known) / known,
        "objective": result.objective,
        "optimality_gap_percent": gap,
        "kicks": result.kicks,
        "kicks_budget": KICKS,
        "patience": PATIENCE,
        "stop_reason": result.stop_reason,
        "wall_seconds": wall,
        "assignment": assignment,
        "replay_objective": replay.objective,
        "exact_replay": abs(replay.objective - result.objective) <= 1e-6,
        "converged_on_patience": result.stop_reason == "patience",
    }


def main() -> int:
    """Run the panel in parallel and write per-run and summary evidence."""
    known = optima()
    tasks = [(name, known[name], seed) for name in INSTANCES for seed in SEEDS]
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
