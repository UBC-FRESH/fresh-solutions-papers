#!/usr/bin/env python3
"""Replay every recorded Lin-Kernighan tour exactly."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import TravellingSalesman  # noqa: E402


def main() -> int:
    """Re-evaluate every recorded assignment."""
    records = json.loads((ROOT / "evidence" / "tsp-lk.json").read_text(encoding="utf-8"))
    failures = 0
    for record in records:
        problem = TravellingSalesman.from_tsplib(ROOT / "instances" / f"{record['instance']}.tsp")
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
