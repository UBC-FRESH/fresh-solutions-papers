#!/usr/bin/env python3
"""Run the five-seed QAP robust-tabu campaign."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402
from fresh_solutions.adapters.qap_tabu import QapTabuConfig, run_qap_tabu  # noqa: E402

SEEDS = (1, 2, 3, 4, 5)
CASES = (
    ("tai12a", 224416.0, "optimum"),
    ("tai20a", 703482.0, "optimum"),
    ("tai25a", 1167256.0, "optimum"),
    ("tai30a", 1818146.0, "best known"),
)


def main() -> int:
    """Run the campaign and write per-run and summary evidence."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--iterations", type=int, default=10000)
    parser.add_argument("--output", default="qap-tabu.json")
    parser.add_argument("--summary", default="qap-tabu-summary.json")
    parser.add_argument("--instances", default="")
    args = parser.parse_args()
    selected = set(args.instances.split(",")) if args.instances else None
    records = []
    summaries = []
    for name, optimum, optimum_kind in CASES:
        if selected is not None and name not in selected:
            continue
        problem = QuadraticAssignment.from_qaplib(ROOT / "instances" / f"{name}.dat")
        gaps = []
        walls = []
        for seed in SEEDS:
            started = time.perf_counter()
            result = run_qap_tabu(problem, QapTabuConfig(iterations=args.iterations, seed=seed))
            wall = time.perf_counter() - started
            gap = 100.0 * (result.objective - optimum) / optimum
            records.append(
                {
                    "instance": name,
                    "seed": seed,
                    "known_optimum": optimum,
                    "optimum_kind": optimum_kind,
                    **result.to_dict(),
                    "optimality_gap_percent": gap,
                    "wall_seconds": wall,
                    "budget_iterations": args.iterations,
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
                "budget_iterations": args.iterations,
            }
        )
        print(
            f"{name}: mean={statistics.mean(gaps):.3f}% "
            f"worst={max(gaps):.3f}% over {len(gaps)} seeds"
        )
    (ROOT / "evidence").mkdir(parents=True, exist_ok=True)
    (ROOT / "evidence" / args.output).write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / args.summary).write_text(
        json.dumps(summaries, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
