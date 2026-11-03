#!/usr/bin/env python3
"""Run SciPy FAQ as an independent baseline on the large QAPLIB tail."""

from __future__ import annotations

import json
import os
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

QAP_ROOT = Path(os.environ.get("QAPLIB_ROOT", "benchmarks/qaplib/QAPLIB"))
CASES = (
    ("esc128", 0.0),
    ("tai150b", 0.0),
    ("tai256c", 0.0),
    ("tho150", 0.0),
)
SEEDS = (1, 2, 3, 4, 5)
MAXITER = 10000


def optima() -> dict[str, float]:
    """Read QAPLIB known optima/best-known values."""
    values: dict[str, float] = {}
    for path in QAP_ROOT.glob("*.qap"):
        try:
            parts = path.read_text().splitlines()[0].split()
            optimum = float(parts[1])
            best = float(parts[2])
            values[path.stem] = optimum if optimum >= 0 else best
        except (IndexError, ValueError):
            continue
    return values


def main() -> int:
    """Run SciPy FAQ and write per-run and summary evidence."""
    known = optima()
    records = []
    summary = []
    for name, _ in CASES:
        problem = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{name}.dat")
        flows = np.asarray(problem.flows, dtype=float)
        distances = np.asarray(problem.distances, dtype=float)
        optimum = known[name]
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
                    "objective": objective,
                    "optimality_gap_percent": gap,
                    "wall_seconds": wall,
                    "assignment": assignment,
                    "method": "scipy.optimize.quadratic_assignment:faq",
                    "maxiter": MAXITER,
                    "scipy_version": scipy.__version__,
                }
            )
            gaps.append(gap)
            walls.append(wall)
        summary.append(
            {
                "instance": name,
                "runs": len(gaps),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "worst_gap_percent": max(gaps),
                "mean_wall_seconds": statistics.mean(walls),
            }
        )
        print(name, f"mean={statistics.mean(gaps):.3f}% worst={max(gaps):.3f}%")
    (ROOT / "evidence" / "qap-scipy-large.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / "qap-scipy-large-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
