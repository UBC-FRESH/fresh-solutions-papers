#!/usr/bin/env python3
"""Replay every recorded Breakout Local Search incumbent through the QAP adapter."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402

QAP_ROOT = Path(os.environ.get("QAPLIB_ROOT", "benchmarks/qaplib/QAPLIB"))


def main() -> int:
    """Re-evaluate every recorded assignment and check its stored objective.

    Returns
    -------
    int
        Zero when every record replays exactly, otherwise one.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="qap-bls-expanded.json")
    args = parser.parse_args()
    records = json.loads((ROOT / "evidence" / args.input).read_text(encoding="utf-8"))
    problems: dict[str, QuadraticAssignment] = {}
    failures = 0
    for record in records:
        name = str(record["instance"])
        if name not in problems:
            problems[name] = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{name}.dat")
        problem = problems[name]
        assignment = {int(key): int(value) for key, value in record["assignment"].items()}
        objective = problem.evaluate(assignment).objective
        known = float(record["known_optimum"])
        gap = 100.0 * (objective - known) / known
        if abs(objective - float(record["objective"])) > 1e-6:
            failures += 1
            print(
                f"FAIL objective {name} seed={record['seed']}: {record['objective']} != {objective}"
            )
        if abs(gap - float(record["optimality_gap_percent"])) > 1e-9:
            failures += 1
            print(
                f"FAIL gap {name} seed={record['seed']}: "
                f"{record['optimality_gap_percent']} != {gap}"
            )
        if not bool(record["exact_replay"]):
            failures += 1
            print(f"FAIL flag {name} seed={record['seed']}: exact_replay is false")
    print(f"{len(records) - failures}/{len(records)} exact replays")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
