#!/usr/bin/env python3
"""Replay the convergence-controlled TSP campaign through the adapter."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import TravellingSalesman  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

EVIDENCE = ROOT / "evidence" / "tsp-convergence-10k.json"


def main() -> int:
    """Replay every tour and print the count."""
    rows = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    for row in rows:
        problem = TravellingSalesman.from_tsplib(ROOT / "instances" / f"{row['instance']}.tsp")
        assignment = {int(key): value for key, value in row["assignment"].items()}
        state = ResidentAssignment(problem, assignment)
        evaluation = state.evaluate()
        if abs(evaluation.objective - float(row["objective"])) > 1e-6:
            raise SystemExit(f"replay mismatch: {row['instance']} seed {row['seed']}")
    print(f"replayed {len(rows)} TSP incumbents exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
