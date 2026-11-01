#!/usr/bin/env python3
"""Run the multi-seed public QAP/TSP campaign."""

from __future__ import annotations

import json
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions import PopulationConfig, SearchConfig  # noqa: E402
from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.benchmark import run_benchmark  # noqa: E402

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
    """Run the campaign and write per-run and summary evidence."""
    population = PopulationConfig(population=32, generations=50, seed=1)
    local = SearchConfig(iterations=10000, seed=1)
    records = []
    summaries = []
    for name, family, size, optimum, optimum_kind in CASES:
        problem = adapter(name, family)
        gaps = []
        walls = []
        for seed in SEEDS:
            started = time.perf_counter()
            record = run_benchmark(
                problem,
                name,
                PopulationConfig(**{**population.__dict__, "seed": seed}),
                SearchConfig(**{**local.__dict__, "seed": seed}),
                {"family": family, "source": "QAPLIB" if family == "qap" else "TSPLIB"},
            )
            wall = time.perf_counter() - started
            gap = 100.0 * (record.result.objective - optimum) / optimum
            enriched = record.to_dict()
            enriched["metadata"].update(
                {
                    "seed": seed,
                    "size": size,
                    "known_optimum": optimum,
                    "optimum_kind": optimum_kind,
                    "optimality_gap_percent": gap,
                    "wall_seconds": wall,
                }
            )
            records.append(enriched)
            gaps.append(gap)
            walls.append(wall)
        summaries.append(
            {
                "instance": name,
                "size": size,
                "family": family,
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
            f"median={statistics.median(gaps):.3f}% worst={max(gaps):.3f}%"
        )
    (ROOT / "evidence").mkdir(parents=True, exist_ok=True)
    (ROOT / "evidence" / "multiseed.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / "multiseed-summary.json").write_text(
        json.dumps(summaries, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
