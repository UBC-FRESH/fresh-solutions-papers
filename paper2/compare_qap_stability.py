#!/usr/bin/env python3
"""Compare QAP-tabu budgets and write the stability summary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
THRESHOLD = 0.10


def main() -> int:
    """Compare means and flag the 0.10-point budget effect."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--small", default="qap-tabu-summary.json")
    parser.add_argument("--large", default="qap-tabu-20k-summary.json")
    parser.add_argument("--output", default="qap-tabu-stability-summary.json")
    parser.add_argument("--small-label", default="10k")
    parser.add_argument("--large-label", default="20k")
    args = parser.parse_args()
    small = {
        row["instance"]: row
        for row in json.loads((ROOT / "evidence" / args.small).read_text(encoding="utf-8"))
    }
    large = {
        row["instance"]: row
        for row in json.loads((ROOT / "evidence" / args.large).read_text(encoding="utf-8"))
    }
    rows = []
    for name in (name for name in small if name in large):
        delta = small[name]["mean_gap_percent"] - large[name]["mean_gap_percent"]
        rows.append(
            {
                "instance": name,
                f"mean_gap_{args.small_label}": small[name]["mean_gap_percent"],
                f"mean_gap_{args.large_label}": large[name]["mean_gap_percent"],
                f"improvement_{args.small_label}_to_{args.large_label}_points": delta,
                "converged_for_reporting": delta <= THRESHOLD,
            }
        )
    (ROOT / "evidence" / args.output).write_text(
        json.dumps(rows, indent=2) + "\n", encoding="utf-8"
    )
    for row in rows:
        print(
            f"{row['instance']}: {args.small_label}={row[f'mean_gap_{args.small_label}']:.3f}% "
            f"{args.large_label}={row[f'mean_gap_{args.large_label}']:.3f}% "
            f"delta={row[f'improvement_{args.small_label}_to_{args.large_label}_points']:.3f} "
            f"stable={row['converged_for_reporting']}"
        )
    return 0 if all(row["converged_for_reporting"] for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
