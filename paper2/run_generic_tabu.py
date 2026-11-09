#!/usr/bin/env python3
"""Run the P13.3 generic tabu/LNS prototype on QAP and TSP.

The runner drives :mod:`generic_tabu`, which uses only the ``ProblemAdapter``
contract and ``ResidentAssignment``.  It checkpoints every completed run, replays
each incumbent exactly, and reports the gap to the adapter-specific reference
evidence already in ``paper2/evidence``.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing
import os
import random
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402
from fresh_solutions.engine import ResidentAssignment  # noqa: E402
from generic_tabu import GenericTabuConfig, run_generic_tabu  # noqa: E402

QAP_CASES = ("tai12a", "tai20a", "tai25a", "tai30a")
TSP_CASES = ("berlin52", "kroA100", "kroB100", "ch150")
MANIFEST = ROOT / "benchmarks" / "manifest.json"
DEFAULT_OUTPUT = ROOT / "evidence" / "generic-tabu.json"
DEFAULT_SUMMARY = ROOT / "evidence" / "generic-tabu-summary.json"
DEFAULT_CHECKPOINT = ROOT / "evidence" / "generic-tabu.jsonl"
REFERENCE_FILES = {
    "qap": (
        "qap-expanded-100k-summary.json",
        "qap_tabu",
        {"iterations": 1_000_000, "patience": 100_000},
    ),
    "tsp": (
        "tsp-expanded-10k-summary.json",
        "tsp_lk",
        {"kicks": 10_000, "patience": 1_000},
    ),
}


def load_known() -> dict[str, float]:
    """Return known optimum values for the target instances.

    Returns
    -------
    dict of str to float
        Instance name to known objective.
    """
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    known = {
        str(row["name"]): float(row["known"])
        for row in manifest["instances"]
        if row["name"] in set(QAP_CASES) | set(TSP_CASES)
    }
    missing = (set(QAP_CASES) | set(TSP_CASES)) - set(known)
    if missing:
        raise SystemExit(f"manifest is missing known values for {sorted(missing)}")
    return known


def load_references() -> dict[str, dict[str, object]]:
    """Read the adapter-specific reference summaries.

    Returns
    -------
    dict of str to dict of str to object
        Keyed by ``"<family>:<instance>"`` with reference gaps, times, and budget.
    """
    references: dict[str, dict[str, object]] = {}
    for family, (filename, name, budget) in REFERENCE_FILES.items():
        rows = json.loads((ROOT / "evidence" / filename).read_text(encoding="utf-8"))
        for row in rows:
            references[f"{family}:{row['instance']}"] = {
                "reference_name": name,
                "reference_budget": budget,
                "reference_mean_gap_percent": float(row["mean_gap_percent"]),
                "reference_best_gap_percent": float(row["best_gap_percent"]),
                "reference_mean_wall_seconds": float(row["mean_wall_seconds"]),
            }
    return references


def config_signature(config: GenericTabuConfig) -> str:
    """Return a stable signature for checkpoint compatibility.

    Parameters
    ----------
    config : GenericTabuConfig
        Search configuration.

    Returns
    -------
    str
        Compact signature of every budget and move setting.
    """
    return (
        f"i{config.iterations}-p{config.patience}-n{config.proposals}"
        f"-t{config.min_tenure}:{config.max_tenure}-{config.tabu_attribute}"
        f"-k{config.perturb_after}:{config.perturb_interval}:{config.perturb_moves}"
        f"-s{config.max_seconds}"
    )


def build_problem(family: str, name: str) -> QuadraticAssignment | TravellingSalesman:
    """Build the target adapter.

    Parameters
    ----------
    family : str
        ``"qap"`` or ``"tsp"``.
    name : str
        Instance name.

    Returns
    -------
    QuadraticAssignment or TravellingSalesman
        Parsed public benchmark instance.
    """
    if family == "qap":
        return QuadraticAssignment.from_qaplib(ROOT / "instances" / f"{name}.dat")
    if family == "tsp":
        return TravellingSalesman.from_tsplib(ROOT / "instances" / f"{name}.tsp")
    raise SystemExit(f"unsupported family: {family}")


def run_task(
    task: tuple[str, str, float, int, str, GenericTabuConfig],
) -> dict[str, object]:
    """Run one generic search seed and return a replayable record.

    Parameters
    ----------
    task : tuple
        Family, instance, known optimum, seed, start kind, and configuration.

    Returns
    -------
    dict of str to object
        Per-run evidence, including the exact replay result.
    """
    family, name, known, seed, start, config = task
    problem = build_problem(family, name)
    initial = None
    if start == "random":
        initial = problem.random_assignment(random.Random(seed * 1_000_003 + 17))
    started = time.perf_counter()
    result = run_generic_tabu(problem, config, initial=initial)
    runner_wall = time.perf_counter() - started
    assignment = dict(result.assignment)
    replay = ResidentAssignment(problem, assignment).evaluate()
    gap = 100.0 * (result.objective - known) / known
    return {
        "family": family,
        "instance": name,
        "adapter": problem.name,
        "size": problem.variable_count,
        "seed": seed,
        "start": start,
        "known_optimum": known,
        "objective": result.objective,
        "feasible": result.feasible,
        "optimality_gap_percent": gap,
        "evaluations": result.evaluations,
        "iterations": result.iterations,
        "iterations_budget": config.iterations,
        "patience": config.patience,
        "proposals": config.proposals,
        "min_tenure": config.min_tenure,
        "max_tenure": config.max_tenure,
        "tabu_attribute": config.tabu_attribute,
        "perturb_after": config.perturb_after,
        "perturb_interval": config.perturb_interval,
        "perturb_moves": config.perturb_moves,
        "accepted": result.accepted,
        "tabu_rejections": result.tabu_rejections,
        "tabu_overrides": result.tabu_overrides,
        "perturbations": result.perturbations,
        "stop_reason": result.stop_reason,
        "converged_on_patience": result.stop_reason == "patience",
        "cap_hit": result.stop_reason in {"max_iterations", "max_seconds"},
        "wall_seconds": result.wall_seconds,
        "cpu_seconds": result.cpu_seconds,
        "runner_wall_seconds": runner_wall,
        "assignment": {str(key): value for key, value in sorted(assignment.items())},
        "replay_objective": replay.objective,
        "replay_feasible": replay.feasible,
        "exact_replay": abs(replay.objective - result.objective) <= 1e-6
        and replay.feasible == result.feasible,
        "run_signature": config_signature(config),
    }


def load_checkpoint(path: Path, signature: str) -> list[dict[str, object]]:
    """Load compatible completed runs from a JSONL checkpoint.

    Parameters
    ----------
    path : Path
        Checkpoint path.
    signature : str
        Current configuration signature.

    Returns
    -------
    list of dict of str to object
        Compatible records.
    """
    if not path.exists():
        return []
    records: list[dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if record.get("run_signature") == signature:
            records.append(record)
    return records


def summarize(
    records: list[dict[str, object]],
    order: tuple[tuple[str, str], ...],
    references: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    """Summarize per-run records by instance.

    Parameters
    ----------
    records : list of dict of str to object
        Completed per-run records.
    order : tuple of tuple of str
        ``(family, instance)`` order.
    references : dict of str to dict of str to object
        Adapter-specific reference statistics.

    Returns
    -------
    list of dict of str to object
        One summary row per instance.
    """
    summaries: list[dict[str, object]] = []
    for family, name in order:
        rows = [row for row in records if row["family"] == family and row["instance"] == name]
        if not rows:
            continue
        gaps = [float(row["optimality_gap_percent"]) for row in rows]
        reference = references.get(f"{family}:{name}", {})
        reference_gap = reference.get("reference_mean_gap_percent")
        summaries.append(
            {
                "family": family,
                "instance": name,
                "size": rows[0]["size"],
                "runs": len(rows),
                "best_gap_percent": min(gaps),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "worst_gap_percent": max(gaps),
                "optimum_runs": sum(gap < 1e-9 for gap in gaps),
                "patience_runs": sum(bool(row["converged_on_patience"]) for row in rows),
                "cap_hit_runs": sum(bool(row["cap_hit"]) for row in rows),
                "mean_wall_seconds": statistics.mean(float(row["wall_seconds"]) for row in rows),
                "mean_cpu_seconds": statistics.mean(float(row["cpu_seconds"]) for row in rows),
                "mean_evaluations": statistics.mean(int(row["evaluations"]) for row in rows),
                "exact_replay_runs": sum(bool(row["exact_replay"]) for row in rows),
                "gap_to_reference_pp": (
                    statistics.mean(gaps) - float(reference_gap)
                    if reference_gap is not None
                    else None
                ),
                **reference,
            }
        )
    return summaries


def main() -> int:
    """Run the generic tabu panel with checkpointing and exact replay."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--instances", default="", help="Comma-separated subset")
    parser.add_argument("--seeds", default="1,2,3,4,5")
    parser.add_argument("--iterations", type=int, default=20_000)
    parser.add_argument("--patience", type=int, default=5_000)
    parser.add_argument("--proposals", type=int, default=16)
    parser.add_argument("--min-tenure", type=int, default=5)
    parser.add_argument("--max-tenure", type=int, default=15)
    parser.add_argument("--tabu-attribute", choices=("move", "variable"), default="move")
    parser.add_argument("--perturb-after", type=int, default=1_000)
    parser.add_argument("--perturb-interval", type=int, default=1_000)
    parser.add_argument("--perturb-moves", type=int, default=5)
    parser.add_argument("--max-seconds", type=float, default=None)
    parser.add_argument("--start", choices=("initial", "random"), default="random")
    parser.add_argument("--workers", type=int, default=min(40, os.cpu_count() or 1))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY))
    parser.add_argument("--checkpoint", default=str(DEFAULT_CHECKPOINT))
    args = parser.parse_args()

    selected = set(args.instances.split(",")) if args.instances else None
    order = tuple(
        (family, name)
        for family, names in (("qap", QAP_CASES), ("tsp", TSP_CASES))
        for name in names
        if selected is None or name in selected
    )
    seeds = tuple(int(value) for value in args.seeds.split(",") if value)
    known = load_known()
    references = load_references()
    configs = {
        seed: GenericTabuConfig(
            iterations=args.iterations,
            patience=args.patience,
            seed=seed,
            proposals=args.proposals,
            min_tenure=args.min_tenure,
            max_tenure=args.max_tenure,
            tabu_attribute=args.tabu_attribute,
            perturb_after=args.perturb_after,
            perturb_interval=args.perturb_interval,
            perturb_moves=args.perturb_moves,
            max_seconds=args.max_seconds,
        )
        for seed in seeds
    }
    signature = config_signature(configs[seeds[0]])
    if any(config_signature(config) != signature for config in configs.values()):
        raise SystemExit("all seeds must share one configuration signature")

    checkpoint = Path(args.checkpoint)
    records = load_checkpoint(checkpoint, signature)
    done = {(str(row["instance"]), int(row["seed"])) for row in records}
    tasks = [
        (family, name, known[name], seed, args.start, configs[seed])
        for family, name in order
        for seed in seeds
        if (name, seed) not in done
    ]
    checkpoint.parent.mkdir(parents=True, exist_ok=True)
    with (
        checkpoint.open("a", encoding="utf-8") as handle,
        ProcessPoolExecutor(
            max_workers=max(1, min(args.workers, len(tasks))) if tasks else 1,
            mp_context=multiprocessing.get_context("spawn"),
        ) as executor,
    ):
        futures = {executor.submit(run_task, task): task for task in tasks}
        for index, future in enumerate(as_completed(futures), 1):
            record = future.result()
            records.append(record)
            done.add((str(record["instance"]), int(record["seed"])))
            handle.write(json.dumps(record) + "\n")
            handle.flush()
            if index % 5 == 0 or index == len(tasks):
                print(f"completed {index}/{len(tasks)} new runs", flush=True)

    records.sort(key=lambda row: (str(row["family"]), str(row["instance"]), int(row["seed"])))
    summaries = summarize(records, order, references)
    Path(args.output).write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    Path(args.summary).write_text(json.dumps(summaries, indent=2) + "\n", encoding="utf-8")

    print("instance            mean_gap%  ref_gap%  delta_pp  wall_s  patience")
    for row in summaries:
        reference_gap = row["reference_mean_gap_percent"]
        delta = row["gap_to_reference_pp"]
        print(
            f"{row['instance']:<18} {float(row['mean_gap_percent']):>8.3f}"
            f" {float(reference_gap):>9.3f}"
            f" {float(delta):>9.3f}"
            f" {float(row['mean_wall_seconds']):>7.1f}"
            f" {row['patience_runs']}/{row['runs']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
