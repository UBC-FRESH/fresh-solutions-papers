#!/usr/bin/env python3
"""Assemble the minimum converged QAP-tabu budget per instance."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SELECTION = {
    "tai12a": "qap-tabu.json",
    "tai20a": "qap-tabu.json",
    "tai25a": "qap-tabu-20k.json",
    "tai30a": "qap-tabu.json",
}
SUMMARY = {
    "tai12a": "qap-tabu-summary.json",
    "tai20a": "qap-tabu-summary.json",
    "tai25a": "qap-tabu-20k-summary.json",
    "tai30a": "qap-tabu-summary.json",
}


def load(name: str) -> object:
    """Load one evidence file."""
    return json.loads((ROOT / "evidence" / name).read_text(encoding="utf-8"))


def main() -> int:
    """Write selected per-run and summary evidence."""
    selected_records = []
    selected_summary = []
    for instance, filename in SELECTION.items():
        records = [row for row in load(filename) if row["instance"] == instance]
        summaries = [row for row in load(SUMMARY[instance]) if row["instance"] == instance]
        selected_records.extend(records)
        selected_summary.extend(summaries)
    (ROOT / "evidence" / "qap-tabu-converged.json").write_text(
        json.dumps(selected_records, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "evidence" / "qap-tabu-converged-summary.json").write_text(
        json.dumps(selected_summary, indent=2) + "\n", encoding="utf-8"
    )
    for row in selected_summary:
        print(
            f"{row['instance']}: {row['budget_iterations']} iterations, "
            f"mean={row['mean_gap_percent']:.3f}%, worst={row['worst_gap_percent']:.3f}%"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
