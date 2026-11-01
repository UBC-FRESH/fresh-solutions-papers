#!/usr/bin/env python3
"""Measure the contribution of double-bridge kicks to Lin-Kernighan."""

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
    ("berlin52", 7542.0),
    ("kroA100", 21282.0),
    ("kroB100", 22141.0),
    ("ch150", 6528.0),
)
CONFIGS = (
    ("lk-only", 0),
    ("ilk-5", 5),
    ("ilk-20", 20),
)


def main() -> int:
    """Run the ablation and write per-run and summary evidence."""
    converged = json.loads((ROOT / "evidence" / "converged.json").read_text(encoding="utf-8"))
    records = []
    summary = []
    for name, optimum in CASES:
        problem = TravellingSalesman.from_tsplib(ROOT / "instances" / f"{name}.tsp")
        starts = {
            row["seed"]: row
            for row in converged
            if row["family"] == "tsp" and row["instance"] == name
        }
        for label, kicks in CONFIGS:
            gaps = []
            walls = []
            for seed in sorted(starts):
                initial = {int(key): value for key, value in starts[seed]["assignment"].items()}
                started = time.perf_counter()
                result = run_tsp_lk(
                    problem,
                    TspLkConfig(candidate_count=16, max_depth=4, kicks=kicks, seed=seed),
                    initial,
                )
                wall = time.perf_counter() - started
                gap = 100.0 * (result.objective - optimum) / optimum
                records.append(
                    {
                        "instance": name,
                        "config": label,
                        "seed": seed,
                        "objective": result.objective,
                        "optimality_gap_percent": gap,
                        "wall_seconds": wall,
                        "accepted_kicks": result.accepted_kicks,
                        "improvements": result.improvements,
                        "assignment": result.assignment,
                    }
                )
                gaps.append(gap)
                walls.append(wall)
            summary.append(
                {
                    "instance": name,
                    "config": label,
                    "runs": len(gaps),
                    "mean_gap_percent": statistics.mean(gaps),
                    "worst_gap_percent": max(gaps),
                    "mean_wall_seconds": statistics.mean(walls),
                }
            )
            print(
                f"{name} {label}: mean={statistics.mean(gaps):.3f}% "
                f"worst={max(gaps):.3f}% wall={statistics.mean(walls):.2f}s"
            )
    (ROOT / "evidence" / "tsp-lk-ablation.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / "tsp-lk-ablation-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
