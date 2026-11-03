#!/usr/bin/env python3
"""Replay the framework-use QAP and TSP evidence through the adapters."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402


def main() -> int:
    """Replay every recorded incumbent and print a count."""
    payload = json.loads((ROOT / "evidence" / "framework-use.json").read_text(encoding="utf-8"))
    checked = 0
    for row in payload["qap"]:
        problem = QuadraticAssignment.from_qaplib(ROOT / "instances" / f"{row['instance']}.dat")
        assignment = {int(key): value for key, value in row["framework"]["assignment"].items()}
        state = ResidentAssignment(problem, assignment)
        evaluation = state.evaluate()
        expected = float(row["framework"]["objective"])
        if abs(evaluation.objective - expected) > 1e-6:
            raise SystemExit(f"QAP replay mismatch: {row['instance']} seed {row['seed']}")
        checked += 1
    tsp_rows = json.loads((ROOT / "evidence" / "tsp-lk.json").read_text(encoding="utf-8"))
    for row in tsp_rows:
        problem = TravellingSalesman.from_tsplib(ROOT / "instances" / f"{row['instance']}.tsp")
        assignment = {int(key): value for key, value in row["assignment"].items()}
        state = ResidentAssignment(problem, assignment)
        if abs(state.evaluate().objective - float(row["objective"])) > 1e-6:
            raise SystemExit(f"TSP replay mismatch: {row['instance']} seed {row['seed']}")
        checked += 1
    print(f"replayed {checked} incumbents exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
