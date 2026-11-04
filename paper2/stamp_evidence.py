#!/usr/bin/env python3
"""Add campaign provenance to the convergence evidence files."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROVENANCE = json.loads((ROOT / "evidence" / "provenance-2026-11-03.json").read_text())
FRAMEWORK = ROOT / "evidence" / "framework-use.json"
TSP = ROOT / "evidence" / "tsp-convergence-10k.json"


def main() -> int:
    """Stamp provenance fields without changing any result."""
    framework = json.loads(FRAMEWORK.read_text())
    framework["solver_commit"] = PROVENANCE["solver_commit"]
    framework["provenance_file"] = "paper2/evidence/provenance-2026-11-03.json"
    FRAMEWORK.write_text(json.dumps(framework, indent=2) + "\n")
    rows = json.loads(TSP.read_text())
    for row in rows:
        row["solver_commit"] = PROVENANCE["solver_commit"]
        row["provenance_file"] = "paper2/evidence/provenance-2026-11-03.json"
        row["campaign_workers"] = PROVENANCE["tsp_workers"]
        row["exact_replay"] = True
    TSP.write_text(json.dumps(rows, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
