#!/usr/bin/env python3
"""Replay every expanded TSP incumbent through the adapter."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))
from fresh_solutions.adapters import TravellingSalesman  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

TSP_ROOT = Path(os.environ.get("TSPLIB_ROOT", "benchmarks/tsplib"))
ROWS = ROOT / "evidence" / "tsp-expanded-10k.json"


def main() -> int:
    """Replay all 100 records."""
    rows = json.loads(ROWS.read_text(encoding="utf-8"))
    for row in rows:
        problem = TravellingSalesman.from_tsplib(TSP_ROOT / f"{row['instance']}.tsp")
        assignment = {int(key): value for key, value in row["assignment"].items()}
        replay = ResidentAssignment(problem, assignment).evaluate()
        if abs(replay.objective - float(row["objective"])) > 1e-6:
            raise SystemExit(f"mismatch: {row['instance']} seed {row['seed']}")
    print(f"replayed {len(rows)} expanded TSP incumbents exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
