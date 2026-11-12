#!/usr/bin/env python3
"""Replay every generic tabu incumbent through the adapter contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

EVIDENCE = ROOT / "evidence" / "generic-tabu.json"


def build_problem(family: str, name: str) -> QuadraticAssignment | TravellingSalesman:
    """Build the adapter for one replay row.

    Parameters
    ----------
    family : str
        ``"qap"`` or ``"tsp"``.
    name : str
        Instance name.

    Returns
    -------
    QuadraticAssignment or TravellingSalesman
        Parsed public benchmark instance.
    """
    if family == "qap":
        return QuadraticAssignment.from_qaplib(ROOT / "instances" / f"{name}.dat")
    if family == "tsp":
        return TravellingSalesman.from_tsplib(ROOT / "instances" / f"{name}.tsp")
    raise SystemExit(f"unsupported family: {family}")


def main() -> int:
    """Replay every stored incumbent and fail on any mismatch.

    Returns
    -------
    int
        Process exit status.
    """
    rows = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    for row in rows:
        problem = build_problem(str(row["family"]), str(row["instance"]))
        assignment = {int(key): value for key, value in row["assignment"].items()}
        evaluation = ResidentAssignment(problem, assignment).evaluate()
        if abs(evaluation.objective - float(row["objective"])) > 1e-6:
            raise SystemExit(
                f"replay mismatch: {row['instance']} seed {row['seed']}: "
                f"{evaluation.objective} != {row['objective']}"
            )
        if evaluation.feasible != bool(row["feasible"]):
            raise SystemExit(f"replay feasibility mismatch: {row['instance']}")
        if set(assignment) != set(range(problem.variable_count)):
            raise SystemExit(f"assignment does not cover every variable: {row['instance']}")
    print(f"replayed {len(rows)} generic-tabu incumbents exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
