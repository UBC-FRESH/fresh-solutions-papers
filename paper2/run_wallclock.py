#!/usr/bin/env python3
"""Run a wall-clock-budgeted hybrid search on one public instance."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions import PopulationConfig, SearchConfig, run_local_search  # noqa: E402
from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.population import run_population_search  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    """Run one wall-clock-budgeted search."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--instance", required=True)
    parser.add_argument("--family", choices=("qap", "tsp"), required=True)
    parser.add_argument("--seconds", type=float, default=180.0)
    parser.add_argument("--seed", type=int, default=3)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.family == "qap":
        problem = QuadraticAssignment.from_qaplib(ROOT / "instances" / f"{args.instance}.dat")
    else:
        problem = TravellingSalesman.from_tsplib(ROOT / "instances" / f"{args.instance}.tsp")
    population = run_population_search(
        problem,
        PopulationConfig(population=32, generations=50, seed=args.seed),
    )
    best = population.assignment
    evaluation = problem.evaluate(best)
    evaluations = population.evaluations
    history = [(0.0, evaluation.objective)]
    start = time.monotonic()
    rounds = 0
    deadline = start + args.seconds
    while time.monotonic() < deadline:
        rounds += 1
        local = run_local_search(
            problem,
            SearchConfig(iterations=10000, seed=args.seed + rounds),
            initial=best,
        )
        evaluations += local.evaluations
        if local.feasible and local.objective < evaluation.objective:
            best = local.assignment
            evaluation = problem.evaluate(best)
        history.append((time.monotonic() - start, evaluation.objective))
        if rounds % 20 == 0:
            print(f"{args.instance}: rounds={rounds} best={evaluation.objective}", flush=True)
    payload = {
        "instance": args.instance,
        "family": args.family,
        "seed": args.seed,
        "seconds": time.monotonic() - start,
        "rounds": rounds,
        "evaluations": evaluations,
        "objective": evaluation.objective,
        "feasible": evaluation.feasible,
        "history": history,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"{args.instance}: final={evaluation.objective} rounds={rounds} evals={evaluations}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
