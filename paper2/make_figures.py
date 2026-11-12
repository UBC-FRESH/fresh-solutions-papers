#!/usr/bin/env python3
"""Generate Paper 2 figures from committed evidence."""

from __future__ import annotations

import gzip
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
FIG = ROOT / "figures"


def save(name: str) -> None:
    """Save the current figure."""
    plt.tight_layout()
    plt.savefig(FIG / name, bbox_inches="tight")
    plt.close()


def qap_expanded() -> None:
    """Plot the expanded QAP mean and worst gaps."""
    rows = json.loads((ROOT / "evidence" / "qap-expanded-100k-10seed-summary.json").read_text())
    sizes = [row["size"] for row in rows]
    means = [row["mean_gap_percent"] for row in rows]
    worst = [row["worst_gap_percent"] for row in rows]
    _fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.errorbar(
        sizes,
        means,
        yerr=[[0] * len(means), [w - m for w, m in zip(worst, means, strict=True)]],
        fmt="o",
        capsize=2,
    )
    ax.set_xlabel("QAP size n")
    ax.set_ylabel("Optimality gap (%)")
    ax.set_title("Expanded QAP panel: mean and worst gap")
    ax.grid(alpha=0.25)
    save("qap-expanded.pdf")


def framework_overhead() -> None:
    """Plot paired framework CPU overhead with bootstrap intervals."""
    rows = json.loads((ROOT / "evidence" / "framework-use-analysis.json").read_text())["instances"]
    labels = [row["instance"] for row in rows]
    means = [row["mean_cpu_overhead_ratio"] for row in rows]
    lows = [row["cpu_overhead_ratio_ci95"][0] for row in rows]
    highs = [row["cpu_overhead_ratio_ci95"][1] for row in rows]
    _fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.errorbar(
        range(len(rows)),
        means,
        yerr=[
            [m - low for m, low in zip(means, lows, strict=True)],
            [h - m for m, h in zip(means, highs, strict=True)],
        ],
        fmt="o",
        capsize=3,
    )
    ax.axhline(1.0, color="black", linewidth=0.8, linestyle="--")
    ax.set_xticks(range(len(rows)), labels)
    ax.set_ylabel("Framework / standalone CPU ratio")
    ax.set_title("Framework-managed state overhead")
    ax.grid(alpha=0.25)
    save("framework-overhead.pdf")


def broad_gaps() -> None:
    """Plot empirical gap distributions for the broad QAP/TSP panel."""
    with gzip.open(ROOT / "evidence" / "broad-converged.json.gz", "rt") as handle:
        records = json.load(handle)
    _fig, ax = plt.subplots(figsize=(6.4, 3.2))
    for family, color in (("tsp", "tab:blue"), ("qap", "tab:orange")):
        gaps = sorted(
            max(float(row["gap"]), 1e-4)
            for row in records
            if row.get("family") == family and "gap" in row
        )
        y = [index / len(gaps) for index in range(1, len(gaps) + 1)]
        ax.plot(gaps, y, label=family.upper(), color=color)
    ax.set_xscale("log")
    ax.set_xlabel("Optimality gap (%), log scale")
    ax.set_ylabel("Empirical CDF")
    ax.set_title("Broad panel gap distributions")
    ax.legend()
    ax.grid(alpha=0.25)
    save("broad-gaps.pdf")


def tsp_budget() -> None:
    """Plot the ch150 short-budget comparison."""
    data = []
    for filename, label in (
        ("tsp-lk.json", "20 kicks"),
        ("tsp-convergence-2k.json", "2,000 kicks"),
        ("tsp-convergence-10k.json", "10,000 kicks"),
    ):
        rows = json.loads((ROOT / "evidence" / filename).read_text())
        gaps = [float(row["optimality_gap_percent"]) for row in rows if row["instance"] == "ch150"]
        data.append((label, sum(gaps) / len(gaps)))
    _fig, ax = plt.subplots(figsize=(5.4, 3.0))
    ax.bar(
        [label for label, _ in data],
        [value for _, value in data],
        color=["tab:red", "tab:orange", "tab:blue"],
    )
    ax.set_ylabel("ch150 mean gap (%)")
    ax.set_title("TSP budget sensitivity")
    ax.grid(axis="y", alpha=0.25)
    save("tsp-budget.pdf")


def main() -> int:
    """Generate all available figures."""
    FIG.mkdir(exist_ok=True)
    qap_expanded()
    framework_overhead()
    broad_gaps()
    tsp_budget()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
