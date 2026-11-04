#!/usr/bin/env python3
"""Run the Paper 2 framework-use experiment.

The experiment compares a QAP robust-tabu path whose incumbent is managed by
:class:`fresh_solutions.engine.ResidentAssignment` with the same delta-matrix
loop backed by a private array.  Quality must match exactly; wall time is
reported as the state-management overhead.  A TSP replay check exercises the
same adapter contract at the evidence boundary.
"""

from __future__ import annotations

import json
import multiprocessing
import os
import platform
import random
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.adapters.qap_tabu import (  # noqa: E402
    QapTabuConfig,
    _delta_matrix,
    _run_accelerated,
    _update_delta_matrix,
    run_qap_tabu,
)
from fresh_solutions.contracts import Change  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402

SEEDS = tuple(range(1, int(os.environ.get("FRAMEWORK_SEEDS", "10")) + 1))
QAP_CASES = (
    ("tai12a", 224416.0, "optimum"),
    ("tai20a", 703482.0, "optimum"),
    ("tai25a", 1167256.0, "optimum"),
    ("tai30a", 1818146.0, "best known"),
)
MAX_ITERATIONS = int(os.environ.get("FRAMEWORK_MAX_ITERATIONS", "1000000"))
PATIENCE = int(os.environ.get("FRAMEWORK_PATIENCE", "50000"))
WORKERS = int(os.environ.get("FRAMEWORK_WORKERS", str(min(40, os.cpu_count() or 1))))
OUT = Path(os.environ.get("FRAMEWORK_OUTPUT", str(ROOT / "evidence" / "framework-use.json")))
SUMMARY_OUT = Path(
    os.environ.get(
        "FRAMEWORK_SUMMARY_OUTPUT",
        str(ROOT / "evidence" / "framework-use-summary.json"),
    )
)
TSP_EVIDENCE = ROOT / "evidence" / "tsp-lk.json"


def run_framework_qap_tabu(
    problem: QuadraticAssignment,
    config: QapTabuConfig,
) -> dict[str, object]:
    """Run robust tabu with engine-managed resident state.

    Parameters
    ----------
    problem : QuadraticAssignment
        QAP adapter.
    config : QapTabuConfig
        Tabu settings.

    Returns
    -------
    dict of str to object
        Best assignment, objective, replay result, counters, and wall time.
    """
    rng = random.Random(config.seed)
    state = ResidentAssignment(problem)
    current = state.evaluate().objective
    best_objective = current
    best = dict(state.assignment)
    size = problem.variable_count
    assignment = [state.assignment[index] for index in range(size)]
    gains = _delta_matrix(problem, assignment)
    tabu_until = [[0 for _ in range(size)] for _ in range(size)]
    history = [current]
    evaluations = 1
    iterations = 0
    last_improvement = 0
    stop_reason = "max_iterations"
    started = time.monotonic()
    started_cpu = time.process_time()

    for iteration in range(1, config.iterations + 1):
        if config.max_seconds is not None and time.monotonic() - started >= config.max_seconds:
            stop_reason = "max_seconds"
            break
        iterations = iteration
        best_gain = float("-inf")
        best_move: tuple[int, int] | None = None
        for first in range(size):
            for second in range(first + 1, size):
                gain = gains[first][second]
                candidate = current - gain
                if tabu_until[first][second] > iteration and candidate >= best_objective:
                    continue
                if gain > best_gain:
                    best_gain = gain
                    best_move = (first, second)
        if best_move is None:
            break
        first, second = best_move
        change = Change(
            variable=first,
            before=assignment[first],
            after=assignment[second],
        )
        _update_delta_matrix(problem, assignment, gains, first, second)
        state.apply(change)
        evaluated = state.evaluate()
        evaluations += 1
        expected = current - best_gain
        if abs(evaluated.objective - expected) > 1e-6 * max(1.0, abs(expected)):
            raise RuntimeError(f"resident objective mismatch: {evaluated.objective} != {expected}")
        current = evaluated.objective
        tabu_until[first][second] = iteration + rng.randint(
            config.min_tenure if config.min_tenure is not None else max(1, size // 2),
            config.max_tenure if config.max_tenure is not None else size + size // 2,
        )
        if current < best_objective:
            best_objective = current
            best = dict(state.assignment)
            history.append(best_objective)
            last_improvement = iteration
        if config.patience is not None and iteration - last_improvement >= config.patience:
            stop_reason = "patience"
            break

    replay = problem.evaluate(best)
    return {
        "assignment": {str(key): value for key, value in sorted(best.items())},
        "objective": best_objective,
        "replay_objective": replay.objective,
        "exact_replay": abs(replay.objective - best_objective) <= 1e-6,
        "iterations": iterations,
        "evaluations": evaluations,
        "stop_reason": stop_reason,
        "wall_seconds": time.monotonic() - started,
        "cpu_seconds": time.process_time() - started_cpu,
        "history": history,
    }


def replay_tsp_evidence() -> list[dict[str, object]]:
    """Replay recorded TSP incumbents through the resident-state contract.

    Returns
    -------
    list of dict
        One replay row per recorded TSP incumbent.
    """
    rows = json.loads(TSP_EVIDENCE.read_text(encoding="utf-8"))
    replays: list[dict[str, object]] = []
    for row in rows:
        problem = TravellingSalesman.from_tsplib(ROOT / "instances" / f"{row['instance']}.tsp")
        assignment = {int(key): value for key, value in row["assignment"].items()}
        state = ResidentAssignment(problem, assignment)
        evaluation = state.evaluate()
        replays.append(
            {
                "instance": row["instance"],
                "seed": row["seed"],
                "objective": row["objective"],
                "replay_objective": evaluation.objective,
                "exact_replay": abs(evaluation.objective - row["objective"]) <= 1e-6,
            }
        )
    return replays


def run_qap_task(task: tuple[str, float, str, int]) -> dict[str, object]:
    """Run one paired baseline/framework/production seed.

    Parameters
    ----------
    task : tuple
        Instance name, known value, value kind, and seed.

    Returns
    -------
    dict of str to object
        One complete paired record.
    """
    name, optimum, optimum_kind, seed = task
    problem = QuadraticAssignment.from_qaplib(ROOT / "instances" / f"{name}.dat")
    config = QapTabuConfig(iterations=MAX_ITERATIONS, patience=PATIENCE, seed=seed)
    initial = problem.initial_assignment()
    if seed % 2 == 0:
        framework = run_framework_qap_tabu(problem, config)
        base_started = time.perf_counter()
        base_cpu_started = time.process_time()
        baseline = _run_accelerated(
            problem,
            config,
            [initial[index] for index in range(problem.variable_count)],
        )
        base_wall = time.perf_counter() - base_started
        base_cpu = time.process_time() - base_cpu_started
        execution_order = "framework_first"
    else:
        base_started = time.perf_counter()
        base_cpu_started = time.process_time()
        baseline = _run_accelerated(
            problem,
            config,
            [initial[index] for index in range(problem.variable_count)],
        )
        base_wall = time.perf_counter() - base_started
        base_cpu = time.process_time() - base_cpu_started
        framework = run_framework_qap_tabu(problem, config)
        execution_order = "baseline_first"
    production = run_qap_tabu(problem, config, initial)
    gap = 100.0 * (float(framework["objective"]) - optimum) / optimum
    return {
        "instance": name,
        "seed": seed,
        "known_optimum": optimum,
        "optimum_kind": optimum_kind,
        "max_iterations": MAX_ITERATIONS,
        "patience": PATIENCE,
        "execution_order": execution_order,
        "baseline_objective": baseline.objective,
        "baseline_iterations": baseline.iterations,
        "baseline_stop_reason": baseline.stop_reason,
        "baseline_wall_seconds": base_wall,
        "baseline_cpu_seconds": base_cpu,
        "production_objective": production.objective,
        "production_iterations": production.iterations,
        "production_stop_reason": production.stop_reason,
        "framework": framework,
        "framework_gap_percent": gap,
        "quality_matches_baseline": abs(baseline.objective - float(framework["objective"])) <= 1e-6,
        "quality_matches_production": abs(production.objective - float(framework["objective"]))
        <= 1e-6,
        "iterations_match_baseline": int(framework["iterations"]) == baseline.iterations,
        "stop_reason_matches_baseline": framework["stop_reason"] == baseline.stop_reason,
        "converged_on_patience": all(
            reason == "patience"
            for reason in (
                baseline.stop_reason,
                production.stop_reason,
                framework["stop_reason"],
            )
        ),
        "wall_overhead_ratio": float(framework["wall_seconds"]) / base_wall,
        "cpu_overhead_ratio": float(framework["cpu_seconds"]) / base_cpu,
    }


def summarize(records: list[dict[str, object]]) -> list[dict[str, object]]:
    """Summarize records by instance."""
    summaries: list[dict[str, object]] = []
    for name, _, _ in QAP_CASES:
        rows = [row for row in records if row["instance"] == name]
        gaps = [float(row["framework_gap_percent"]) for row in rows]
        base_walls = [float(row["baseline_wall_seconds"]) for row in rows]
        framework_walls = [float(row["framework"]["wall_seconds"]) for row in rows]
        cpu_ratios = [float(row["cpu_overhead_ratio"]) for row in rows]
        summaries.append(
            {
                "instance": name,
                "runs": len(rows),
                "best_gap_percent": min(gaps),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "worst_gap_percent": max(gaps),
                "mean_baseline_wall_seconds": statistics.mean(base_walls),
                "mean_framework_wall_seconds": statistics.mean(framework_walls),
                "mean_wall_overhead_ratio": statistics.mean(framework_walls)
                / statistics.mean(base_walls),
                "mean_cpu_overhead_ratio": statistics.mean(cpu_ratios),
                "mean_iterations": statistics.mean(
                    int(row["framework"]["iterations"]) for row in rows
                ),
                "all_quality_matches": all(
                    bool(row["quality_matches_baseline"])
                    and bool(row["quality_matches_production"])
                    for row in rows
                ),
                "all_patience_stops": all(bool(row["converged_on_patience"]) for row in rows),
                "all_exact_replays": all(bool(row["framework"]["exact_replay"]) for row in rows),
            }
        )
    return summaries


def main() -> int:
    """Run the ten-seed QAP comparison in parallel and replay TSP."""
    tasks = [
        (name, optimum, optimum_kind, seed)
        for name, optimum, optimum_kind in QAP_CASES
        for seed in SEEDS
    ]
    records: list[dict[str, object]] = []
    with ProcessPoolExecutor(
        max_workers=max(1, WORKERS),
        mp_context=multiprocessing.get_context("spawn"),
    ) as executor:
        futures = {executor.submit(run_qap_task, task): task for task in tasks}
        for index, future in enumerate(as_completed(futures), 1):
            records.append(future.result())
            if index % 4 == 0 or index == len(tasks):
                print(f"completed {index}/{len(tasks)}", flush=True)
    records.sort(key=lambda row: (str(row["instance"]), int(row["seed"])))
    summaries = summarize(records)
    for row in summaries:
        print(
            f"{row['instance']}: mean={row['mean_gap_percent']:.3f}% "
            f"overhead={row['mean_wall_overhead_ratio']:.2f}x "
            f"patience={row['all_patience_stops']}",
            flush=True,
        )

    tsp_replays = replay_tsp_evidence()
    payload = {
        "experiment": "framework-managed QAP tabu versus private-array delta path",
        "seeds": list(SEEDS),
        "patience": PATIENCE,
        "max_iterations": MAX_ITERATIONS,
        "workers": WORKERS,
        "hardware": {
            "platform": platform.platform(),
            "processor": platform.processor(),
            "cpu_count": os.cpu_count(),
            "python": sys.version,
        },
        "qap": records,
        "qap_summary": summaries,
        "tsp_replay": tsp_replays,
        "tsp_replay_all_exact": all(bool(row["exact_replay"]) for row in tsp_replays),
    }
    OUT.write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )
    SUMMARY_OUT.write_text(
        json.dumps(
            {
                "qap": summaries,
                "tsp_replay_all_exact": payload["tsp_replay_all_exact"],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"TSP replay exact: {payload['tsp_replay_all_exact']} over {len(tsp_replays)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
