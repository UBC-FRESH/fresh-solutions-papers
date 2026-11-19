#!/usr/bin/env python3
"""Stamp campaign provenance on broad and large-QAP evidence without changing results."""

from __future__ import annotations

import gzip
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

PROVENANCE = json.loads((ROOT / "evidence" / "provenance-2026-11-03.json").read_text())
BROAD = ROOT / "evidence" / "broad-converged.json.gz"
MULTISTART = ROOT / "evidence" / "qap-multistart-converged.jsonl"
QAP_ROOT = Path(os.environ.get("QAPLIB_ROOT", "benchmarks/qaplib/QAPLIB"))
COMMON = {
    "solver_commit": PROVENANCE["solver_commit"],
    "replay_solver_commit": PROVENANCE.get("replay_solver_commit"),
    "provenance_file": "paper2/evidence/provenance-2026-11-03.json",
}


def stamp_broad() -> int:
    """Add campaign metadata to broad records and rewrite the gzip."""
    with gzip.open(BROAD, "rt", encoding="utf-8") as handle:
        records = json.load(handle)
    for record in records:
        record.update(COMMON)
        record["replay_status"] = "not_replayed_broad_screen"
    with gzip.open(BROAD, "wt", encoding="utf-8") as handle:
        json.dump(records, handle)
    return len(records)


def stamp_multistart() -> int:
    """Add metadata and exact-replay results to the large-QAP records."""
    rows = [
        json.loads(line)
        for line in MULTISTART.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    checked = 0
    for row in rows:
        row.update(COMMON)
        problem = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{row['instance']}.dat")
        assignment = {int(key): value for key, value in row["assignment"].items()}
        replay = ResidentAssignment(problem, assignment).evaluate()
        row["exact_replay"] = abs(replay.objective - float(row["objective"])) <= 1e-6
        row["replay_status"] = "exact" if row["exact_replay"] else "mismatch"
        checked += int(row["exact_replay"])
    MULTISTART.write_text(
        "\n".join(json.dumps(row) for row in rows) + "\n",
        encoding="utf-8",
    )
    return checked


def main() -> int:
    """Stamp both files and report counts."""
    broad = stamp_broad()
    exact = stamp_multistart()
    print(f"stamped {broad} broad records; replayed {exact}/20 large-QAP records exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
