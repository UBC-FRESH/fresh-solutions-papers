#!/usr/bin/env python3
"""Replay every recorded QAP-tabu assignment and check its objective."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402


def main() -> int:
    """Re-evaluate every recorded assignment."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="qap-tabu.json")
    args = parser.parse_args()
    records = json.loads((ROOT / "evidence" / args.input).read_text(encoding="utf-8"))
    failures = 0
    for record in records:
        problem = QuadraticAssignment.from_qaplib(
            ROOT / "instances" / f"{record['instance']}.dat"
        )
        assignment = {int(key): value for key, value in record["assignment"].items()}
        objective = problem.evaluate(assignment).objective
        if objective != record["objective"]:
            failures += 1
            print(
                f"FAIL {record['instance']} seed={record['seed']}: "
                f"{record['objective']} != {objective}"
            )
    print(f"{len(records) - failures}/{len(records)} exact replays")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
