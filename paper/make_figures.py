#!/usr/bin/env python3
"""Generate Paper 1 figures from committed evidence."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "paper" / "figures"


def load(rel: str) -> dict[str, object]:
    """Load one evidence record."""
    return json.loads((ROOT / "evidence" / rel / "record.json").read_text(encoding="utf-8"))


def save(name: str) -> None:
    """Save the current figure."""
    plt.tight_layout()
    plt.savefig(FIG / name, bbox_inches="tight")
    plt.close()


def scaling() -> None:
    """Plot seed-7 objective by GPU generation budget."""
    records = [
        (1_000, load("ws4-tsa24-gpu-ga-1000-r7")),
        (10_000, load("ws4-tsa24-gpu-ga-10000-r7")),
        (100_000, load("ws4-tsa24-gpu-ga-100000-r7")),
    ]
    _fig, ax = plt.subplots(figsize=(5.4, 3.0))
    ax.plot(
        [g for g, _ in records], [float(r["result"]["objective"]) for _, r in records], marker="o"
    )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("GPU generations")
    ax.set_ylabel("Objective (log scale)")
    ax.set_title("Seed-7 scaling")
    ax.grid(alpha=0.25)
    save("scaling.pdf")


def seeds() -> None:
    """Plot five-seed flow and level terms."""
    rows = []
    for seed in (1, 2, 3, 4, 5):
        record = load(f"ws4-tsa24-gpu-ga-100000-r{seed}")
        penalties = record["result"]["target_penalties"]
        rows.append((seed, float(penalties["flow"]), float(penalties["level"])))
    _fig, ax = plt.subplots(figsize=(5.4, 3.0))
    ax.bar([str(seed) for seed, _, _ in rows], [level for _, _, level in rows], label="level")
    ax.bar(
        [str(seed) for seed, _, _ in rows],
        [flow for _, flow, _ in rows],
        bottom=[level for _, _, level in rows],
        label="flow",
    )
    ax.set_xlabel("Seed")
    ax.set_ylabel("Objective term")
    ax.set_title("Five-seed objective decomposition")
    ax.legend()
    save("seed-terms.pdf")


def realized_level() -> None:
    """Plot realized level ranges against the 70M aspiration."""
    rows = []
    for seed in (1, 2, 3, 4, 5, 7):
        record = load(f"ws4-tsa24-gpu-ga-100000-r{seed}")
        penalties = record["result"]["target_penalties"]
        rows.append(
            (
                seed,
                float(penalties["realized_level_min_m3"]) / 1e6,
                float(penalties["realized_level_max_m3"]) / 1e6,
            )
        )
    _fig, ax = plt.subplots(figsize=(5.4, 3.0))
    for index, (_seed, low, high) in enumerate(rows):
        ax.plot([index, index], [low, high], color="tab:blue", linewidth=5, solid_capstyle="round")
        ax.scatter([index], [(low + high) / 2], color="tab:blue", zorder=3)
    ax.axhline(70.0, color="tab:red", linestyle="--", linewidth=1, label="70M aspiration")
    ax.set_xticks(range(len(rows)), [str(seed) for seed, _, _ in rows])
    ax.set_xlabel("Seed")
    ax.set_ylabel("Realized level (M m$^3$/period)")
    ax.set_title("Maximum-even-flow compromise")
    ax.legend()
    save("realized-level.pdf")


def ablation() -> None:
    """Plot the evaluation-path ablation."""
    data = json.loads((ROOT / "evidence" / "ws4-tsa24-eval-ablation.json").read_text())
    labels = ["warm full", "delta + apply"]
    values = [float(data["full_move_mean_s"]), float(data["delta_apply_mean_s"])]
    _fig, ax = plt.subplots(figsize=(4.8, 2.8))
    ax.bar(labels, values, color=["tab:red", "tab:blue"])
    ax.set_yscale("log")
    ax.set_ylabel("Seconds per move (log scale)")
    ax.set_title("Evaluation-path ablation")
    save("ablation.pdf")


def main() -> int:
    """Generate all figures."""
    FIG.mkdir(parents=True, exist_ok=True)
    scaling()
    seeds()
    realized_level()
    ablation()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
