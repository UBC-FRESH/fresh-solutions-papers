#!/usr/bin/env python3
"""Emit LaTeX rows for the framework-use and TSP convergence tables."""

from __future__ import annotations

import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QAP = ROOT / "evidence" / "framework-use.json"
TSP = ROOT / "evidence" / "tsp-convergence-10k.json"
TSP_FALLBACK = ROOT / "evidence" / "tsp-convergence-2k.json"


def qap_rows() -> list[str]:
    """Return QAP table rows from the final evidence."""
    payload = json.loads(QAP.read_text(encoding="utf-8"))
    rows: list[str] = []
    for summary in payload["qap_summary"]:
        rows.append(
            " & ".join(
                [
                    summary["instance"].replace("_", r"\_"),
                    f"{summary['mean_gap_percent']:.3f}",
                    f"{summary['median_gap_percent']:.3f}",
                    f"{summary['worst_gap_percent']:.3f}",
                    f"{summary['mean_iterations']:.0f}",
                    f"{summary['mean_cpu_overhead_ratio']:.3f}",
                    f"{summary['mean_wall_overhead_ratio']:.3f}",
                    "yes" if summary["all_patience_stops"] else "no",
                ]
            )
            + r" \\"
        )
    return rows


def tsp_rows() -> list[str]:
    """Return TSP table rows from the longest available campaign."""
    path = TSP if TSP.exists() else TSP_FALLBACK
    rows = json.loads(path.read_text(encoding="utf-8"))
    output: list[str] = []
    for name in ("berlin52", "kroA100", "kroB100", "ch150"):
        selected = [row for row in rows if row["instance"] == name]
        gaps = [float(row["optimality_gap_percent"]) for row in selected]
        walls = [float(row["wall_seconds"]) for row in selected]
        output.append(
            " & ".join(
                [
                    name,
                    str(len(selected)),
                    f"{statistics.mean(gaps):.3f}",
                    f"{max(gaps):.3f}",
                    (
                        f"{sum(bool(row['converged_on_patience']) for row in selected)}"
                        f"/{len(selected)}"
                    ),
                    f"{statistics.mean(walls):.1f}",
                ]
            )
            + r" \\"
        )
    return output


def main() -> int:
    """Print both tables."""
    print("% QAP framework-use")
    for row in qap_rows():
        print(row)
    print("% TSP convergence")
    for row in tsp_rows():
        print(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
