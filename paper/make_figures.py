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
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
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


def matched_search() -> None:
    """Plot the matched CPU/CUDA implementation comparison."""
    path = ROOT / "paper" / "evidence" / "tsa24-matched-search.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    runs = data["runs"]
    generations = [int(run["generations"]) for run in runs]
    cpu_time = [float(run["cpu"]["search_s"]) for run in runs]
    cuda_time = [float(run["cuda"]["search_s"]) for run in runs]
    cpu_obj = [float(run["cpu"]["objective"]) for run in runs]
    cuda_obj = [float(run["cuda"]["objective"]) for run in runs]

    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.2))
    time_ax, obj_ax = axes

    time_ax.plot(generations, cpu_time, marker="o", color="black", label="CPU torch path")
    time_ax.plot(generations, cuda_time, marker="s", color="tab:blue", label="CUDA path")
    time_ax.set_xscale("log")
    time_ax.set_yscale("log")
    time_ax.set_xticks(generations, [str(g) for g in generations])
    time_ax.set_xlabel("Generations")
    time_ax.set_ylabel("Search time (s, log scale)")
    time_ax.set_title("(a) Search time")
    time_ax.grid(alpha=0.25)
    time_ax.legend(loc="upper left", frameon=False, fontsize=8)

    obj_ax.plot(generations, cpu_obj, marker="o", color="black", label="CPU torch path")
    obj_ax.plot(generations, cuda_obj, marker="s", color="tab:blue", label="CUDA path")
    obj_ax.set_xscale("log")
    obj_ax.set_yscale("log")
    obj_ax.set_xticks(generations, [str(g) for g in generations])
    obj_ax.set_xlabel("Generations")
    obj_ax.set_ylabel("Objective (log scale)")
    obj_ax.set_title("(b) Objective")
    obj_ax.grid(alpha=0.25)
    obj_ax.text(
        0.04,
        0.06,
        "CPU objective 5.0% lower\nat 100 generations",
        transform=obj_ax.transAxes,
        fontsize=8,
        color="black",
    )
    save("matched-search.pdf")


def main() -> int:
    """Generate the two result figures used by the manuscript."""
    FIG.mkdir(parents=True, exist_ok=True)
    scaling()
    matched_search()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
