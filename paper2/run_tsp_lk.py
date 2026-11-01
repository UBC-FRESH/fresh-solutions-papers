#!/usr/bin/env python3
"""Run iterated Lin-Kernighan from the converged Or-opt tours."""

from __future__ import annotations

import json
import statistics
import sys
import time
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
CONFIG = {"candidate_count": 16, "max_depth": 4, "kicks": 20, "max_passes": 100}


def main() -> int:
    """Run the campaign and write per-run and summary evidence."""
    converged = json.loads((ROOT / "evidence" / "converged.json").read_text(encoding="utf-8"))
    records = []
    summaries = []
    for name, optimum, optimum_kind in CASES:
        problem = TravellingSalesman.from_tsplib(ROOT / "instances" / f"{name}.tsp")
        starts = {
            row["seed"]: row
            for row in converged
            if row["family"] == "tsp" and row["instance"] == name
        }
        gaps = []
        walls = []
        for seed in sorted(starts):
            start = starts[seed]
            initial = {int(key): value for key, value in start["assignment"].items()}
            started = time.perf_counter()
            result = run_tsp_lk(
                problem,
                TspLkConfig(**{**CONFIG, "seed": seed}),
                initial,
            )
            wall = time.perf_counter() - started
            gap = 100.0 * (result.objective - optimum) / optimum
            records.append(
                {
                    "instance": name,
                    "seed": seed,
                    "known_optimum": optimum,
                    "optimum_kind": optimum_kind,
                    "initial_objective": result.initial_objective,
                    "initial_gap_percent": start["optimality_gap_percent"],
                    "objective": result.objective,
                    "optimality_gap_percent": gap,
                    "wall_seconds": wall,
                    "assignment": result.assignment,
                    **{
                        key: value
                        for key, value in result.to_dict().items()
                        if key not in {"assignment", "objective"}
                    },
                    "config": {**CONFIG, "seed": seed},
                }
            )
            gaps.append(gap)
            walls.append(wall)
        summaries.append(
            {
                "instance": name,
                "runs": len(gaps),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "worst_gap_percent": max(gaps),
                "best_gap_percent": min(gaps),
                "mean_wall_seconds": statistics.mean(walls),
                "optimum_kind": optimum_kind,
            }
        )
        print(
            f"{name}: mean={statistics.mean(gaps):.3f}% "
            f"worst={max(gaps):.3f}% over {len(gaps)} seeds"
        )
    (ROOT / "evidence" / "tsp-lk.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / "tsp-lk-summary.json").write_text(
        json.dumps(summaries, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
