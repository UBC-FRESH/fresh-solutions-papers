#!/usr/bin/env python3
"""Analyze the framework-use evidence with paired overhead summaries."""

from __future__ import annotations

import json
import os
import random
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVIDENCE = Path(os.environ.get("FRAMEWORK_EVIDENCE", str(ROOT / "evidence" / "framework-use.json")))
OUT = Path(
    os.environ.get(
        "FRAMEWORK_ANALYSIS",
        str(ROOT / "evidence" / "framework-use-analysis.json"),
    )
)


def _quantile(values: list[float], fraction: float) -> float:
    """Return a linear-interpolated quantile of a non-empty list."""
    ordered = sorted(values)
    position = fraction * (len(ordered) - 1)
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def _bootstrap_mean_ci(values: list[float], seed: int = 17) -> tuple[float, float]:
    """Return a percentile bootstrap 95% CI for the mean."""
    rng = random.Random(seed)
    means = [statistics.mean(rng.choices(values, k=len(values))) for _ in range(10_000)]
    return _quantile(means, 0.025), _quantile(means, 0.975)


def main() -> int:
    """Read the evidence, summarize each instance, and write the analysis."""
    payload = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    records = payload["qap"]
    summaries: list[dict[str, object]] = []
    for name in ("tai12a", "tai20a", "tai25a", "tai30a"):
        rows = [row for row in records if row["instance"] == name]
        gaps = [float(row["framework_gap_percent"]) for row in rows]
        ratios = [float(row["wall_overhead_ratio"]) for row in rows]
        cpu_ratios = [float(row["cpu_overhead_ratio"]) for row in rows]
        lower, upper = _bootstrap_mean_ci(ratios)
        cpu_lower, cpu_upper = _bootstrap_mean_ci(cpu_ratios)
        summaries.append(
            {
                "instance": name,
                "runs": len(rows),
                "best_gap_percent": min(gaps),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "worst_gap_percent": max(gaps),
                "mean_iterations": statistics.mean(
                    int(row["framework"]["iterations"]) for row in rows
                ),
                "mean_baseline_wall_seconds": statistics.mean(
                    float(row["baseline_wall_seconds"]) for row in rows
                ),
                "mean_framework_wall_seconds": statistics.mean(
                    float(row["framework"]["wall_seconds"]) for row in rows
                ),
                "mean_wall_overhead_ratio": statistics.mean(ratios),
                "wall_overhead_ratio_ci95": [lower, upper],
                "mean_cpu_overhead_ratio": statistics.mean(cpu_ratios),
                "cpu_overhead_ratio_ci95": [cpu_lower, cpu_upper],
                "all_patience_stops": all(bool(row["converged_on_patience"]) for row in rows),
                "all_quality_matches": all(
                    bool(row["quality_matches_baseline"])
                    and bool(row["quality_matches_production"])
                    for row in rows
                ),
                "all_exact_replays": all(bool(row["framework"]["exact_replay"]) for row in rows),
            }
        )
    overall_ratios = [float(row["wall_overhead_ratio"]) for row in records]
    overall_cpu = [float(row["cpu_overhead_ratio"]) for row in records]
    lower, upper = _bootstrap_mean_ci(overall_ratios)
    cpu_lower, cpu_upper = _bootstrap_mean_ci(overall_cpu)
    analysis = {
        "source": str(EVIDENCE.relative_to(ROOT)),
        "instances": summaries,
        "overall": {
            "runs": len(records),
            "mean_wall_overhead_ratio": statistics.mean(overall_ratios),
            "wall_overhead_ratio_ci95": [lower, upper],
            "mean_cpu_overhead_ratio": statistics.mean(overall_cpu),
            "cpu_overhead_ratio_ci95": [cpu_lower, cpu_upper],
            "all_patience_stops": all(bool(row["converged_on_patience"]) for row in records),
            "all_quality_matches": all(
                bool(row["quality_matches_baseline"]) and bool(row["quality_matches_production"])
                for row in records
            ),
            "all_exact_replays": all(bool(row["framework"]["exact_replay"]) for row in records),
        },
        "tsp_replay_all_exact": payload["tsp_replay_all_exact"],
    }
    OUT.write_text(json.dumps(analysis, indent=2) + "\n", encoding="utf-8")
    for row in summaries:
        print(
            f"{row['instance']}: mean={row['mean_gap_percent']:.3f}% "
            f"best={row['best_gap_percent']:.3f}% worst={row['worst_gap_percent']:.3f}% "
            f"overhead={row['mean_wall_overhead_ratio']:.2f}x "
            f"patience={row['all_patience_stops']}"
        )
    print(
        f"overall overhead={analysis['overall']['mean_wall_overhead_ratio']:.2f}x "
        f"CI={analysis['overall']['wall_overhead_ratio_ci95']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
