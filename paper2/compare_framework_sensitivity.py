#!/usr/bin/env python3
"""Compare the 50k- and 100k-patience framework runs."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAIN = ROOT / "evidence" / "framework-use-patience50k.json"
LONG = ROOT / "evidence" / "framework-use-patience100k.json"
OUT = ROOT / "evidence" / "framework-use-sensitivity.json"


def main() -> int:
    """Write a per-seed stability comparison."""
    main_rows = json.loads(MAIN.read_text(encoding="utf-8"))["qap"]
    long_rows = json.loads(LONG.read_text(encoding="utf-8"))["qap"]
    main_index = {(row["instance"], row["seed"]): row for row in main_rows}
    comparisons: list[dict[str, object]] = []
    for row in long_rows:
        key = (row["instance"], row["seed"])
        if key not in main_index:
            continue
        short = main_index[key]
        short_objective = float(short["framework"]["objective"])
        long_objective = float(row["framework"]["objective"])
        comparisons.append(
            {
                "instance": row["instance"],
                "seed": row["seed"],
                "short_patience": int(short["patience"]),
                "long_patience": int(row["patience"]),
                "short_objective": short_objective,
                "long_objective": long_objective,
                "objective_delta": long_objective - short_objective,
                "short_iterations": int(short["framework"]["iterations"]),
                "long_iterations": int(row["framework"]["iterations"]),
                "short_stop": short["framework"]["stop_reason"],
                "long_stop": row["framework"]["stop_reason"],
                "stable": abs(long_objective - short_objective) <= 1e-6,
            }
        )
    all_stable = all(bool(row["stable"]) for row in comparisons)
    payload = {
        "short_patience": 50_000,
        "long_patience": 100_000,
        "comparisons": comparisons,
        "all_objectives_stable": all_stable,
        "all_long_runs_patience": all(row["long_stop"] == "patience" for row in comparisons),
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for row in comparisons:
        print(
            f"{row['instance']} seed {row['seed']}: "
            f"delta={row['objective_delta']:.6f} "
            f"stable={row['stable']} long={row['long_stop']}"
        )
    print(f"all stable: {all_stable}; all long patience: {payload['all_long_runs_patience']}")
    return 0 if all_stable and payload["all_long_runs_patience"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
