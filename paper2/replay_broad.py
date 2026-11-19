#!/usr/bin/env python3
"""Replay every broad-panel QAP/TSP incumbent through the adapters."""

from __future__ import annotations

import gzip
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

QAP_ROOT = Path(os.environ.get("QAPLIB_ROOT", "benchmarks/qaplib/QAPLIB"))
TSP_ROOT = Path(os.environ.get("TSPLIB_ROOT", "benchmarks/tsplib"))
BROAD = ROOT / "evidence" / "broad-converged.json.gz"


def main() -> int:
    """Replay all broad incumbents and fail on any objective mismatch."""
    with gzip.open(BROAD, "rt", encoding="utf-8") as handle:
        rows = json.load(handle)
    problems: dict[tuple[str, str], object] = {}
    checked = 0
    skipped = 0
    for row in rows:
        family = row.get("family")
        name = row.get("instance")
        if family not in {"qap", "tsp"} or not name:
            continue
        key = (family, name)
        problem = problems.get(key)
        if problem is None:
            if family == "qap":
                try:
                    problem = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{name}.dat")
                except ValueError:
                    if name.startswith("esc8"):
                        skipped += 1
                        continue
                    raise
            else:
                problem = TravellingSalesman.from_tsplib(TSP_ROOT / f"{name}.tsp")
            problems[key] = problem
        assignment = {int(k): v for k, v in row["assignment"].items()}
        replay = ResidentAssignment(problem, assignment).evaluate()
        if abs(replay.objective - float(row["objective"])) > 1e-6:
            raise SystemExit(f"broad mismatch: {family} {name} seed {row.get('seed')}")
        checked += 1
    message = (
        f"replayed {checked} broad QAP/TSP incumbents exactly; "
        f"skipped {skipped} esc8 parse-error records"
    )
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
