#!/usr/bin/env python3
"""Stamp campaign metadata on the expanded convergence evidence."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROV = json.loads((ROOT / "evidence" / "provenance-2026-11-03.json").read_text())
FILES = {
    "qap-expanded-100k.json": ("Intel Xeon Gold 6254; 40 workers", PROV["qap_framework_workers"]),
    "qap-bls-expanded.json": ("Intel Xeon Gold 6254; 40 workers", 40),
    "qap-bls-10seed.json": ("Intel Xeon Gold 6254; 40 workers", 40),
    "tsp-expanded-10k.json": ("Intel Xeon Gold 6254; 20 workers", PROV["tsp_workers"]),
    "generic-tabu.json": ("Intel Xeon Gold 6254; 40 workers", 40),
}


def main() -> int:
    """Stamp every record with solver/commit and campaign hardware."""
    for name, (hardware, workers) in FILES.items():
        path = ROOT / "evidence" / name
        rows = json.loads(path.read_text())
        for row in rows:
            row["solver_commit"] = PROV["solver_commit"]
            row["replay_solver_commit"] = PROV.get("replay_solver_commit")
            row["provenance_file"] = "paper2/evidence/provenance-2026-11-03.json"
            row["hardware"] = hardware
            row["campaign_workers"] = workers
        path.write_text(json.dumps(rows, indent=2) + "\n")
        print(name, len(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
