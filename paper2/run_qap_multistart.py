#!/usr/bin/env python3
"""Run multi-start robust tabu on the large QAPLIB tail."""

from __future__ import annotations

import json
import os
import random
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402
from fresh_solutions.adapters.qap_tabu import QapTabuConfig, run_qap_tabu  # noqa: E402

QAP_ROOT = Path(os.environ.get("QAPLIB_ROOT", "benchmarks/qaplib/QAPLIB"))
OUT = ROOT / "evidence" / "qap-multistart-converged.jsonl"
CAP = None
STARTS = 5


def optima() -> dict[str, float]:
    """Read QAPLIB known optima/best-known values."""
    values: dict[str, float] = {}
    for path in QAP_ROOT.glob("*.qap"):
        try:
            first = path.read_text().splitlines()[0].split()
            optimum = float(first[1])
            best = float(first[2])
            values[path.stem] = optimum if optimum >= 0 else best
        except (IndexError, ValueError):
            continue
    return values


def run(task: tuple[str, int, float, int]) -> dict[str, object]:
    """Run one random start."""
    name, size, optimum, start = task
    problem = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{name}.dat")
    initial = problem.random_assignment(random.Random(1000 * start + len(name)))
    started = time.perf_counter()
    result = run_qap_tabu(
        problem,
        QapTabuConfig(
            iterations=1_000_000,
            patience=10_000,
            seed=start,
            max_seconds=CAP,
        ),
        initial,
    )
    wall = time.perf_counter() - started
    gap = 100.0 * (result.objective - optimum) / optimum if optimum else abs(result.objective)
    return {
        "instance": name,
        "size": size,
        "known_optimum": optimum,
        "start": start,
        "objective": result.objective,
        "optimality_gap_percent": gap,
        "wall_seconds": wall,
        "stop_reason": result.stop_reason,
        "assignment": result.assignment,
    }


def main() -> int:
    """Run the large-QAP multi-start campaign."""
    known = optima()
    tasks: list[tuple[str, int, float, int]] = []
    for path in sorted(QAP_ROOT.glob("*.dat")):
        try:
            size = int(path.read_text().split()[0])
        except (IndexError, ValueError):
            continue
        if size > 100 and path.stem in known:
            tasks.extend(
                (path.stem, size, known[path.stem], start) for start in range(1, STARTS + 1)
            )
    records: list[dict[str, object]] = []
    with ProcessPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(run, task): task for task in tasks}
        for index, future in enumerate(as_completed(futures), 1):
            records.append(future.result())
            if index % 5 == 0:
                print(index, "/", len(tasks), flush=True)
    records.sort(key=lambda record: (str(record["instance"]), int(record["start"])))
    OUT.write_text("\n".join(json.dumps(record) for record in records) + "\n", encoding="utf-8")
    for name in sorted({str(record["instance"]) for record in records}):
        rows = [record for record in records if record["instance"] == name]
        gaps = [float(record["optimality_gap_percent"]) for record in rows]
        print(name, "best", min(gaps), "mean", statistics.mean(gaps))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
