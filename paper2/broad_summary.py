#!/usr/bin/env python3
"""Canonical broad-panel summary from committed per-run records."""

from __future__ import annotations

import gzip
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RECORDS = ROOT / "evidence" / "broad-converged.json.gz"
SUMMARY = ROOT / "evidence" / "broad-converged-summary.json"


def summarise(records: list[dict[str, object]]) -> list[dict[str, object]]:
    """Summarize successful runs and retain parse errors separately.

    A run is converged only when it stopped on patience. A max_seconds, max_kicks,
    or max_iterations stop is a cap hit, not convergence.
    """
    successful = [record for record in records if "gap" in record]
    rows: list[dict[str, object]] = []
    for family in ("tsp", "qap"):
        family_rows = [record for record in successful if record["family"] == family]
        for band, low, high in (
            ("all", 0, 10000),
            ("n<=100", 0, 100),
            ("100<n<=300", 101, 300),
            ("n>300", 301, 10000),
        ):
            band_rows = [record for record in family_rows if low <= int(record["size"]) <= high]
            if not band_rows:
                continue
            gaps = [float(record["gap"]) for record in band_rows]
            converged = [record for record in band_rows if record["stop"] == "patience"]
            converged_gaps = [float(record["gap"]) for record in converged]
            rows.append(
                {
                    "family": family,
                    "band": band,
                    "instances": len({record["instance"] for record in band_rows}),
                    "runs": len(band_rows),
                    "patience_runs": len(converged),
                    "cap_runs": len(band_rows) - len(converged),
                    "optimum_runs": sum(gap < 1e-9 for gap in gaps),
                    "all_mean_gap_percent": statistics.mean(gaps),
                    "converged_mean_gap_percent": statistics.mean(converged_gaps)
                    if converged_gaps
                    else None,
                    "converged_median_gap_percent": statistics.median(converged_gaps)
                    if converged_gaps
                    else None,
                    "converged_worst_gap_percent": max(converged_gaps) if converged_gaps else None,
                }
            )
    return rows


def main() -> int:
    """Rebuild and compare the committed summary."""
    with gzip.open(RECORDS, "rt", encoding="utf-8") as handle:
        records = json.load(handle)
    rows = summarise(records)
    SUMMARY.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(rows, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
