#!/usr/bin/env python3
"""Run the broad QAPLIB/TSPLIB convergence panel and write replayable evidence."""

from __future__ import annotations

import argparse
import gzip
import json
import os
import platform
import re
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy
import scipy

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))
sys.path.insert(0, str(ROOT))

from broad_summary import summarise as summarise_rows  # noqa: E402
from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.adapters.qap_tabu import QapTabuConfig, run_qap_tabu  # noqa: E402
from fresh_solutions.adapters.tsp_lk import TspLkConfig, run_tsp_lk  # noqa: E402

TSP_ROOT = Path(os.environ.get("TSPLIB_ROOT", "benchmarks/tsplib"))
QAP_ROOT = Path(os.environ.get("QAPLIB_ROOT", "benchmarks/qaplib/QAPLIB"))
SEEDS = (1, 2, 3, 4, 5)
CAP = 600.0
TSP_KICKS = 10000
TSP_PATIENCE = 100
QAP_ITERATIONS = 1_000_000
QAP_PATIENCE = 10_000


def provenance() -> dict[str, object]:
    """Return software and hardware provenance for the run."""
    try:
        import numba

        numba_version = numba.__version__
    except ImportError:
        numba_version = None
    return {
        "solver_version": os.environ.get("FRESH_SOLUTIONS_VERSION", "v0.8.0"),
        "solver_commit": os.environ.get("FRESH_SOLUTIONS_COMMIT", "unknown"),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "numpy": numpy.__version__,
        "scipy": scipy.__version__,
        "numba": numba_version,
        "tsplib_root": str(TSP_ROOT),
        "qaplib_root": str(QAP_ROOT),
        "tsplib_commit": os.environ.get("TSPLIB_COMMIT", "unknown"),
        "qaplib_commit": os.environ.get("QAPLIB_COMMIT", "unknown"),
        "tsp": {
            "candidate_count": 16,
            "max_depth": 4,
            "kicks": TSP_KICKS,
            "patience": TSP_PATIENCE,
            "max_seconds": CAP,
        },
        "qap": {
            "iterations": QAP_ITERATIONS,
            "patience": QAP_PATIENCE,
            "max_seconds": CAP,
        },
    }


def tsp_optima() -> dict[str, float]:
    """Read TSPLIB known optima."""
    values: dict[str, float] = {}
    for line in (TSP_ROOT / "solutions").read_text().splitlines():
        match = re.match(r"(\S+)\s*:\s*([0-9.]+)", line.strip())
        if match:
            values[match.group(1)] = float(match.group(2))
    return values


def qap_optima() -> dict[str, float]:
    """Read QAPLIB known optima or best-known values."""
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


def nearest_neighbour(problem: TravellingSalesman, start: int) -> dict[int, int]:
    """Build a deterministic nearest-neighbour tour."""
    size = problem.variable_count
    distances = problem.distances
    unseen = set(range(size))
    unseen.remove(start)
    tour = [start]
    current = start
    while unseen:
        current = min(unseen, key=lambda city: (distances[current][city], city))
        tour.append(current)
        unseen.remove(current)
    return dict(enumerate(tour))


def run_tsp(task: tuple[str, int, float, int]) -> dict[str, object]:
    """Run one TSP task."""
    name, size, optimum, seed = task
    problem = TravellingSalesman.from_tsplib(TSP_ROOT / f"{name}.tsp")
    initial = nearest_neighbour(problem, seed % problem.variable_count)
    started = time.perf_counter()
    result = run_tsp_lk(
        problem,
        TspLkConfig(
            candidate_count=16,
            max_depth=4,
            kicks=TSP_KICKS,
            patience=TSP_PATIENCE,
            seed=seed,
            max_seconds=CAP,
        ),
        initial,
    )
    wall = time.perf_counter() - started
    gap = 100.0 * (result.objective - optimum) / optimum
    return {
        "instance": name,
        "family": "tsp",
        "size": size,
        "known": optimum,
        "seed": seed,
        "initial_objective": problem.evaluate(initial).objective,
        "objective": result.objective,
        "gap": gap,
        "wall": wall,
        "stop": result.stop_reason,
        "assignment": result.assignment,
    }


def run_qap(task: tuple[str, int, float, int]) -> dict[str, object]:
    """Run one QAP task."""
    name, size, optimum, seed = task
    problem = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{name}.dat")
    started = time.perf_counter()
    result = run_qap_tabu(
        problem,
        QapTabuConfig(
            iterations=QAP_ITERATIONS,
            patience=QAP_PATIENCE,
            seed=seed,
            max_seconds=CAP,
        ),
    )
    wall = time.perf_counter() - started
    gap = 100.0 * (result.objective - optimum) / optimum if optimum else abs(result.objective)
    return {
        "instance": name,
        "family": "qap",
        "size": size,
        "known": optimum,
        "seed": seed,
        "objective": result.objective,
        "gap": gap,
        "wall": wall,
        "stop": result.stop_reason,
        "assignment": result.assignment,
    }


def main() -> int:
    """Run the campaign and write compressed records plus summary."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="evidence/broad-converged.json.gz")
    parser.add_argument("--summary", default="evidence/broad-converged-summary.json")
    parser.add_argument("--workers", type=int, default=24)
    args = parser.parse_args()
    tsp_known = tsp_optima()
    qap_known = qap_optima()
    tsp_tasks: list[tuple[str, int, float, int]] = []
    qap_tasks: list[tuple[str, int, float, int]] = []
    skipped: list[dict[str, object]] = []
    for path in sorted(TSP_ROOT.glob("*.tsp")):
        match = re.search(r"DIMENSION\s*:\s*(\d+)", path.read_text(errors="ignore"))
        size = int(match.group(1)) if match else 0
        if size <= 1000 and path.stem in tsp_known:
            tsp_tasks.extend((path.stem, size, tsp_known[path.stem], seed) for seed in SEEDS)
        else:
            skipped.append(
                {
                    "family": "tsp",
                    "instance": path.stem,
                    "size": size,
                    "reason": "size>1000" if size > 1000 else "no known optimum",
                }
            )
    for path in sorted(QAP_ROOT.glob("*.dat")):
        if path.stem not in qap_known:
            skipped.append({"family": "qap", "instance": path.stem, "reason": "no known optimum"})
            continue
        try:
            size = int(path.read_text().split()[0])
        except (IndexError, ValueError):
            skipped.append({"family": "qap", "instance": path.stem, "reason": "parse"})
            continue
        qap_tasks.extend((path.stem, size, qap_known[path.stem], seed) for seed in SEEDS)
    tasks = [("tsp", task) for task in tsp_tasks] + [("qap", task) for task in qap_tasks]
    provenance_data = provenance()
    records: list[dict[str, object]] = []
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(run_tsp if kind == "tsp" else run_qap, task): (kind, task)
            for kind, task in tasks
        }
        for index, future in enumerate(as_completed(futures), 1):
            kind, task = futures[future]
            try:
                records.append(future.result())
            except Exception as error:
                records.append(
                    {
                        "instance": task[0],
                        "family": kind,
                        "seed": task[3],
                        "error": f"{type(error).__name__}: {error}",
                    }
                )
            if index % 50 == 0:
                print(index, "/", len(tasks), flush=True)
    records.sort(
        key=lambda record: (
            str(record.get("family")),
            str(record.get("instance")),
            record.get("seed", 0),
        )
    )
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        json.dump(records, handle)
    summary_rows = summarise_rows(records)
    successful = [record for record in records if "gap" in record]
    errors = [record for record in records if "error" in record]
    provenance_data["scheduled_runs"] = len(records)
    provenance_data["successful_runs"] = len(successful)
    provenance_data["parse_errors"] = len(errors)
    provenance_data["skipped"] = skipped
    (ROOT / args.summary).write_text(json.dumps(summary_rows, indent=2) + "\n", encoding="utf-8")
    (ROOT / "evidence" / "broad-converged-provenance.json").write_text(
        json.dumps(provenance_data, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary_rows, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
