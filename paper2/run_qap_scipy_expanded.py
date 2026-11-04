#!/usr/bin/env python3
"""Run SciPy FAQ as an independent baseline on the expanded QAP panel."""

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
sys.path.insert(0, str(ROOT))

from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402
from run_qap_expanded import INSTANCES, QAP_ROOT, optimum  # noqa: E402

SEEDS = (1, 2, 3, 4, 5)
MAXITER = 10000


def main() -> int:
    """Run SciPy FAQ and write per-run and summary evidence."""
    records = []
    summaries = []
    for name in INSTANCES:
        known = optimum(name)
        problem = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{name}.dat")
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
            gap = 100.0 * (objective - known) / known
            gaps.append(gap)
            walls.append(wall)
            records.append(
                {
                    "instance": name,
                    "seed": seed,
                    "known_optimum": known,
                    "objective": objective,
                    "optimality_gap_percent": gap,
                    "wall_seconds": wall,
                    "assignment": assignment,
                    "method": "scipy.optimize.quadratic_assignment:faq",
                    "maxiter": MAXITER,
                    "scipy_version": scipy.__version__,
                }
            )
        summaries.append(
            {
                "instance": name,
                "runs": len(gaps),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "worst_gap_percent": max(gaps),
                "best_gap_percent": min(gaps),
                "mean_wall_seconds": statistics.mean(walls),
            }
        )
        print(name, f"mean={statistics.mean(gaps):.3f}%")
    (ROOT / "evidence" / "qap-scipy-expanded.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / "qap-scipy-expanded-summary.json").write_text(
        json.dumps(summaries, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
