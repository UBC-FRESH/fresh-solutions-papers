#!/usr/bin/env python3
"""Run a convergence-controlled TSP ILK campaign from Or-opt starts.

The default budget is deliberately large: 100,000 double-bridge kicks with a
1,000-kick plateau rule. A run that hits the kick cap is reported as
non-converged; the script does not relabel cap hits as convergence.
"""

from __future__ import annotations

import argparse
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

from fresh_solutions.adapters import TravellingSalesman  # noqa: E402
from fresh_solutions.adapters.tsp_lk import TspLkConfig, run_tsp_lk  # noqa: E402

CASES = (
    ("berlin52", 7542.0, "optimum"),
    ("kroA100", 21282.0, "optimum"),
    ("kroB100", 22141.0, "optimum"),
    ("ch150", 6528.0, "optimum"),
)
STARTS = ROOT / "evidence" / "converged.json"


def run_task(task: tuple[str, float, str, int, int, int]) -> dict[str, object]:
    """Run one TSP seed.

    Parameters
    ----------
    task : tuple
        Instance name, known value, value kind, seed, kick budget, and patience.

    Returns
    -------
    dict of str to object
        One replayable record.
    """
    name, optimum, optimum_kind, seed, kicks, patience = task
    starts = json.loads(STARTS.read_text(encoding="utf-8"))
    start = next(
        row
        for row in starts
        if row["family"] == "tsp" and row["instance"] == name and row["seed"] == seed
    )
    problem = TravellingSalesman.from_tsplib(ROOT / "instances" / f"{name}.tsp")
    initial = {int(key): value for key, value in start["assignment"].items()}
    started = time.perf_counter()
    result = run_tsp_lk(
        problem,
        TspLkConfig(
            candidate_count=16,
            max_depth=4,
            kicks=kicks,
            patience=patience,
            seed=seed,
        ),
        initial,
    )
    wall = time.perf_counter() - started
    gap = 100.0 * (result.objective - optimum) / optimum
    return {
        "instance": name,
        "seed": seed,
        "known_optimum": optimum,
        "optimum_kind": optimum_kind,
        "initial_gap_percent": start["optimality_gap_percent"],
        "objective": result.objective,
        "optimality_gap_percent": gap,
        "wall_seconds": wall,
        "kicks_budget": kicks,
        "patience": patience,
        **{
            key: value
            for key, value in result.to_dict().items()
            if key not in {"assignment", "objective"}
        },
        "assignment": result.assignment,
        "converged_on_patience": result.stop_reason == "patience",
    }


def summarize(records: list[dict[str, object]]) -> list[dict[str, object]]:
    """Summarize records by instance."""
    summaries: list[dict[str, object]] = []
    for name, _, optimum_kind in CASES:
        rows = [row for row in records if row["instance"] == name]
        if not rows:
            continue
        gaps = [float(row["optimality_gap_percent"]) for row in rows]
        walls = [float(row["wall_seconds"]) for row in rows]
        summaries.append(
            {
                "instance": name,
                "runs": len(rows),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "best_gap_percent": min(gaps),
                "worst_gap_percent": max(gaps),
                "mean_wall_seconds": statistics.mean(walls),
                "converged_runs": sum(bool(row["converged_on_patience"]) for row in rows),
                "kicks_budget": int(rows[0]["kicks_budget"]),
                "patience": int(rows[0]["patience"]),
                "optimum_kind": optimum_kind,
            }
        )
    return summaries


def main() -> int:
    """Run the TSP convergence campaign and write per-run and summary evidence."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--kicks", type=int, default=100_000)
    parser.add_argument("--patience", type=int, default=1_000)
    parser.add_argument("--seeds", default="1,2,3,4,5")
    parser.add_argument("--instances", default="")
    parser.add_argument("--workers", type=int, default=min(40, os.cpu_count() or 1))
    parser.add_argument("--output", default="tsp-convergence.json")
    parser.add_argument("--summary", default="tsp-convergence-summary.json")
    args = parser.parse_args()
    seeds = tuple(int(value) for value in args.seeds.split(",") if value)
    selected = set(args.instances.split(",")) if args.instances else None
    starts = json.loads(STARTS.read_text(encoding="utf-8"))
    available = {(row["instance"], row["seed"]) for row in starts if row["family"] == "tsp"}
    tasks = [
        (name, optimum, optimum_kind, seed, args.kicks, args.patience)
        for name, optimum, optimum_kind in CASES
        if selected is None or name in selected
        for seed in seeds
        if (name, seed) in available
    ]
    records: list[dict[str, object]] = []
    with ProcessPoolExecutor(
        max_workers=max(1, min(args.workers, len(tasks))),
        mp_context=multiprocessing.get_context("spawn"),
    ) as executor:
        futures = {executor.submit(run_task, task): task for task in tasks}
        for index, future in enumerate(as_completed(futures), 1):
            records.append(future.result())
            if index % 4 == 0 or index == len(tasks):
                print(f"completed {index}/{len(tasks)}", flush=True)
    records.sort(key=lambda row: (str(row["instance"]), int(row["seed"])))
    summaries = summarize(records)
    for row in summaries:
        print(
            f"{row['instance']}: mean={row['mean_gap_percent']:.3f}% "
            f"worst={row['worst_gap_percent']:.3f}% "
            f"converged={row['converged_runs']}/{row['runs']} "
            f"wall={row['mean_wall_seconds']:.1f}s",
            flush=True,
        )
    (ROOT / "evidence" / args.output).write_text(
        json.dumps(records, indent=2) + "\n",
        encoding="utf-8",
    )
    (ROOT / "evidence" / args.summary).write_text(
        json.dumps(summaries, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
