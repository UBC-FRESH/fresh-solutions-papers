#!/usr/bin/env python3
"""Run the optional external LKH backend on the large TSPLIB tail."""

from __future__ import annotations

import json
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
from fresh_solutions.adapters.lkh import LkhConfig, run_lkh  # noqa: E402

TSP_ROOT = Path(os.environ.get("TSPLIB_ROOT", "benchmarks/tsplib"))
SEEDS = (1, 2, 3, 4, 5)


def optima() -> dict[str, float]:
    """Read known TSPLIB optima."""
    values: dict[str, float] = {}
    for line in (TSP_ROOT / "solutions").read_text().splitlines():
        match = re.match(r"(\S+)\s*:\s*([0-9.]+)", line.strip())
        if match:
            values[match.group(1)] = float(match.group(2))
    return values


def run(task: tuple[str, float, int]) -> dict[str, object]:
    """Run one LKH task."""
    name, optimum, seed = task
    problem = TravellingSalesman.from_tsplib(TSP_ROOT / f"{name}.tsp")
    started = time.perf_counter()
    result = run_lkh(
        problem,
        LkhConfig(
            binary=os.environ["LKH_BINARY"],
            runs=1,
            seed=seed,
            timeout_seconds=600.0,
        ),
    )
    wall = time.perf_counter() - started
    gap = 100.0 * (result.objective - optimum) / optimum
    return {
        "instance": name,
        "size": problem.variable_count,
        "known_optimum": optimum,
        "seed": seed,
        "objective": result.objective,
        "optimality_gap_percent": gap,
        "wall_seconds": wall,
        "assignment": result.assignment,
        "backend": "LKH-3 external",
    }


def main() -> int:
    """Run the large-instance LKH campaign."""
    known = optima()
    tasks: list[tuple[str, float, int]] = []
    for path in sorted(TSP_ROOT.glob("*.tsp")):
        match = re.search(r"DIMENSION\s*:\s*(\d+)", path.read_text(errors="ignore"))
        size = int(match.group(1)) if match else 0
        if 300 < size <= 1000 and path.stem in known:
            tasks.extend((path.stem, known[path.stem], seed) for seed in SEEDS)
    records: list[dict[str, object]] = []
    with ProcessPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(run, task): task for task in tasks}
        for index, future in enumerate(as_completed(futures), 1):
            records.append(future.result())
            if index % 10 == 0:
                print(index, "/", len(tasks), flush=True)
    records.sort(key=lambda record: (str(record["instance"]), int(record["seed"])))
    gaps = [float(record["optimality_gap_percent"]) for record in records]
    summary = {
        "instances": len({str(record["instance"]) for record in records}),
        "runs": len(records),
        "optimum_runs": sum(gap < 1e-9 for gap in gaps),
        "mean_gap_percent": statistics.mean(gaps),
        "median_gap_percent": statistics.median(gaps),
        "worst_gap_percent": max(gaps),
        "mean_wall_seconds": statistics.mean(float(record["wall_seconds"]) for record in records),
    }
    (ROOT / "evidence" / "lkh-large.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / "lkh-large-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
