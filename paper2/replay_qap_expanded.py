#!/usr/bin/env python3
"""Replay every expanded QAP incumbent through the adapter."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))
from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

QAP_ROOT = Path(os.environ.get("QAPLIB_ROOT", "benchmarks/qaplib/QAPLIB"))
ROWS = ROOT / "evidence" / os.environ.get("QAP_EXPANDED_EVIDENCE", "qap-expanded-100k-10seed.json")


def main() -> int:
    """Replay all 100 records."""
    rows = json.loads(ROWS.read_text(encoding="utf-8"))
    for row in rows:
        problem = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{row['instance']}.dat")
        assignment = {int(key): value for key, value in row["assignment"].items()}
        replay = ResidentAssignment(problem, assignment).evaluate()
        if abs(replay.objective - float(row["objective"])) > 1e-6:
            raise SystemExit(f"mismatch: {row['instance']} seed {row['seed']}")
    print(f"replayed {len(rows)} expanded QAP incumbents exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
