#!/usr/bin/env python3
"""Run the public Paper 2 QAP/TSP evidence pass."""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions import PopulationConfig, SearchConfig  # noqa: E402
from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.benchmark import run_benchmark  # noqa: E402


def main() -> int:
    """Run four public instances and write evidence records."""
    population = PopulationConfig(population=32, generations=50, seed=3)
    local = SearchConfig(iterations=10000, seed=3)
    cases = [
        (
            QuadraticAssignment.from_qaplib(ROOT / "instances" / "tai12a.dat"),
            "tai12a",
            224416.0,
            {"family": "qap", "source": "QAPLIB"},
        ),
        (
            QuadraticAssignment.from_qaplib(ROOT / "instances" / "tai20a.dat"),
            "tai20a",
            703482.0,
            {"family": "qap", "source": "QAPLIB"},
        ),
        (
            TravellingSalesman.from_tsplib(ROOT / "instances" / "berlin52.tsp"),
            "berlin52",
            7542.0,
            {"family": "tsp", "source": "TSPLIB"},
        ),
        (
            TravellingSalesman.from_tsplib(ROOT / "instances" / "kroA100.tsp"),
            "kroA100",
            21282.0,
            {"family": "tsp", "source": "TSPLIB"},
        ),
    ]
    records = []
    for adapter, name, optimum, metadata in cases:
        started = time.perf_counter()
        record = run_benchmark(adapter, name, population, local, metadata)
        wall = time.perf_counter() - started
        gap = 100.0 * (record.result.objective - optimum) / optimum
        enriched = record.to_dict()
        enriched["metadata"].update(
            {"known_optimum": optimum, "optimality_gap_percent": gap, "wall_seconds": wall}
        )
        records.append(enriched)
        print(f"{name}: objective={record.result.objective:.6f} gap={gap:.3f}% wall={wall:.3f}s")
    destination = ROOT / "evidence" / "public.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
