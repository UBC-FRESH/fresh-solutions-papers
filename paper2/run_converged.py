#!/usr/bin/env python3
"""Run the convergence-controlled Paper 2 campaign."""

from __future__ import annotations

import json
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions import (  # noqa: E402
    ConvergenceConfig,
    PopulationConfig,
    SearchConfig,
    run_to_convergence,
)
from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402

SEEDS = (1, 2, 3, 4, 5)
CASES = (
    ("tai12a", "qap", 12, 224416.0, "optimum"),
    ("tai20a", "qap", 20, 703482.0, "optimum"),
    ("tai25a", "qap", 25, 1167256.0, "optimum"),
    ("tai30a", "qap", 30, 1818146.0, "best known"),
    ("berlin52", "tsp", 52, 7542.0, "optimum"),
    ("kroA100", "tsp", 100, 21282.0, "optimum"),
    ("kroB100", "tsp", 100, 22141.0, "optimum"),
    ("ch150", "tsp", 150, 6528.0, "optimum"),
)


def adapter(name: str, family: str) -> object:
    """Build one adapter."""
    if family == "qap":
        return QuadraticAssignment.from_qaplib(ROOT / "instances" / f"{name}.dat")
    return TravellingSalesman.from_tsplib(ROOT / "instances" / f"{name}.tsp")


def main() -> int:
    """Run the campaign and write convergence evidence."""
    population = PopulationConfig(population=32, generations=50, seed=1)
    local = SearchConfig(iterations=10000, seed=1)
    convergence = ConvergenceConfig(
        local_iterations_per_round=10000,
        patience_rounds=3,
        max_rounds=30,
        max_evaluations=500000,
    )
    records = []
    summaries = []
    for name, family, size, optimum, optimum_kind in CASES:
        problem = adapter(name, family)
        gaps = []
        evaluations = []
        walls = []
        converged = []
        for seed in SEEDS:
            started = time.perf_counter()
            result = run_to_convergence(
                problem,
                PopulationConfig(**{**population.__dict__, "seed": seed}),
                SearchConfig(**{**local.__dict__, "seed": seed}),
                convergence,
            )
            wall = time.perf_counter() - started
            gap = 100.0 * (result.objective - optimum) / optimum
            gap = max(gap, 0.0)
            gaps.append(gap)
            evaluations.append(result.evaluations)
            walls.append(wall)
            converged.append(result.converged)
            records.append(
                {
                    "instance": name,
                    "family": family,
                    "seed": seed,
                    "size": size,
                    "known_optimum": optimum,
                    "optimum_kind": optimum_kind,
                    "optimality_gap_percent": gap,
                    "wall_seconds": wall,
                    **result.to_dict(),
                }
            )
        summaries.append(
            {
                "instance": name,
                "family": family,
                "size": size,
                "runs": len(gaps),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "worst_gap_percent": max(gaps),
                "best_gap_percent": min(gaps),
                "mean_evaluations": statistics.mean(evaluations),
                "mean_wall_seconds": statistics.mean(walls),
                "converged_runs": sum(converged),
                "optimum_kind": optimum_kind,
            }
        )
        print(
            f"{name}: mean={statistics.mean(gaps):.3f}% median={statistics.median(gaps):.3f}% "
            f"worst={max(gaps):.3f}% converged={sum(converged)}/{len(converged)}"
        )
    (ROOT / "evidence").mkdir(parents=True, exist_ok=True)
    (ROOT / "evidence" / "converged.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / "converged-summary.json").write_text(
        json.dumps(summaries, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
