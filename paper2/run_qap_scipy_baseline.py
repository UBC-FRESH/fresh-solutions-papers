#!/usr/bin/env python3
"""Run an independent SciPy FAQ baseline on the QAP instances."""

from __future__ import annotations

import json
import statistics
import sys
import time
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import quadratic_assignment

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402

SEEDS = (1, 2, 3, 4, 5)
MAXITER = 10000
CASES = (
    ("tai12a", 224416.0, "optimum"),
    ("tai20a", 703482.0, "optimum"),
    ("tai25a", 1167256.0, "optimum"),
    ("tai30a", 1818146.0, "best known"),
)


def main() -> int:
    """Run SciPy FAQ and write per-run and summary evidence."""
    records = []
    summaries = []
    for name, optimum, optimum_kind in CASES:
        problem = QuadraticAssignment.from_qaplib(ROOT / "instances" / f"{name}.dat")
        flows = np.asarray(problem.flows, dtype=float)
        distances = np.asarray(problem.distances, dtype=float)
        gaps = []
        walls = []
        for seed in SEEDS:
            started = time.perf_counter()
            result = quadratic_assignment(
                flows,
                distances,
                method="faq",
                options={"maxiter": MAXITER, "rng": seed},
            )
            wall = time.perf_counter() - started
            assignment = {index: int(value) for index, value in enumerate(result.col_ind)}
            objective = problem.evaluate(assignment).objective
            gap = 100.0 * (objective - optimum) / optimum
            records.append(
                {
                    "instance": name,
                    "seed": seed,
                    "known_optimum": optimum,
                    "optimum_kind": optimum_kind,
                    "assignment": {str(key): value for key, value in assignment.items()},
                    "objective": objective,
                    "optimality_gap_percent": gap,
                    "wall_seconds": wall,
                    "method": "scipy.optimize.quadratic_assignment:faq",
                    "maxiter": MAXITER,
                    "scipy_version": scipy.__version__,
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
                "method": "scipy.optimize.quadratic_assignment:faq",
                "maxiter": MAXITER,
            }
        )
        print(
            f"{name}: mean={statistics.mean(gaps):.3f}% "
            f"worst={max(gaps):.3f}% over {len(gaps)} seeds"
        )
    (ROOT / "evidence" / "qap-scipy-faq.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / "qap-scipy-faq-summary.json").write_text(
        json.dumps(summaries, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
