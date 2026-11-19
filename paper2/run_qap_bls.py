#!/usr/bin/env python3
"""Run the 20-instance, five-seed Breakout Local Search QAP panel.

The panel uses the same instances, seeds, move cap (1,000,000) and patience
(100,000 non-improving moves) as ``run_qap_expanded.py``.  Each record carries a
full assignment that the runner replays through the QAP adapter before it is
written.  Results are checkpointed after every completed run.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing
import os
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment  # noqa: E402
from qap_bls import NUMBA_AVAILABLE, QapBlsConfig, run_qap_bls  # noqa: E402

QAP_ROOT = Path(os.environ.get("QAPLIB_ROOT", "benchmarks/qaplib/QAPLIB"))
SEEDS = (1, 2, 3, 4, 5)
INSTANCES = (
    "tai12a",
    "tai20a",
    "tai25a",
    "tai30a",
    "tai35a",
    "tai40a",
    "tai50a",
    "bur26a",
    "bur26b",
    "bur26c",
    "bur26d",
    "bur26e",
    "bur26f",
    "bur26g",
    "bur26h",
    "chr12a",
    "chr15a",
    "chr18a",
    "chr20a",
    "chr22a",
)
DEFAULT_MOVES = 1_000_000
DEFAULT_PATIENCE = 100_000
_WARMED = False


def optimum(name: str) -> float:
    """Read the QAPLIB optimum from the ``.sln`` sidecar.

    Parameters
    ----------
    name : str
        QAPLIB instance name.

    Returns
    -------
    float
        Known optimum from the sidecar file.
    """
    tokens = (QAP_ROOT / f"{name}.sln").read_text(encoding="utf-8").split()
    return float(tokens[1])


def _warm_up() -> None:
    """Compile the BLS kernel once per worker process before timing."""
    global _WARMED
    if _WARMED:
        return
    if NUMBA_AVAILABLE:
        problem = QuadraticAssignment(
            flows=((0.0, 1.0, 2.0), (1.0, 0.0, 3.0), (2.0, 3.0, 0.0)),
            distances=((0.0, 2.0, 1.0), (2.0, 0.0, 4.0), (1.0, 4.0, 0.0)),
        )
        run_qap_bls(problem, QapBlsConfig(max_moves=20, patience=10, seed=1))
    _WARMED = True


def instance_type(name: str) -> str:
    """Return the QAPLIB structural type used to choose the published ``L0``.

    Parameters
    ----------
    name : str
        QAPLIB instance name.

    Returns
    -------
    str
        ``"II"`` for the unstructured ``tai`` family, ``"I"`` for the
        asymmetric ``bur`` family, and ``"III"`` otherwise.
    """
    if name.startswith("tai"):
        return "II"
    if name.startswith("bur"):
        return "I"
    return "III"


def default_strength(name: str, size: int) -> int:
    """Return the published initial jump magnitude for one instance family.

    Parameters
    ----------
    name : str
        QAPLIB instance name.
    size : int
        Number of locations.

    Returns
    -------
    int
        ``0.05 n`` for type II and ``0.15 n`` otherwise, with a floor of two.
    """
    fraction = 0.05 if instance_type(name) == "II" else 0.15
    return max(2, round(fraction * size))


def run_task(task: tuple[str, float, int, int, int]) -> dict[str, object]:
    """Run one QAP BLS seed and return a replayable record.

    Parameters
    ----------
    task : tuple of str, float, int, int, int
        Instance name, known optimum, seed, move cap, and patience.

    Returns
    -------
    dict of str to object
        Evidence record with timing, stopping reason, and exact replay.
    """
    name, known, seed, max_moves, patience = task
    _warm_up()
    problem = QuadraticAssignment.from_qaplib(QAP_ROOT / f"{name}.dat")
    started = time.perf_counter()
    cpu_started = time.process_time()
    result = run_qap_bls(
        problem,
        QapBlsConfig(
            max_moves=max_moves,
            patience=patience,
            seed=seed,
            initial_strength=default_strength(name, problem.variable_count),
        ),
    )
    wall = time.perf_counter() - started
    cpu = time.process_time() - cpu_started
    assignment = dict(result.assignment)
    replay = problem.evaluate(assignment)
    gap = 100.0 * (result.objective - known) / known
    size = problem.variable_count
    return {
        "instance": name,
        "size": size,
        "instance_type": instance_type(name),
        "seed": seed,
        "known_optimum": known,
        "optimum_kind": "optimum",
        "algorithm": "breakout-local-search",
        "objective": result.objective,
        "optimality_gap_percent": gap,
        "moves": result.moves,
        "evaluations": result.evaluations,
        "descent_moves": result.descent_moves,
        "perturbation_moves": result.perturbation_moves,
        "local_optima": result.local_optima,
        "random_perturbations": result.random_perturbations,
        "recency_perturbations": result.recency_perturbations,
        "directed_perturbations": result.directed_perturbations,
        "strong_perturbations": result.strong_perturbations,
        "final_strength": result.final_strength,
        "stop_reason": result.stop_reason,
        "converged_on_patience": result.stop_reason == "patience",
        "budget_moves": max_moves,
        "patience_moves": patience,
        "threshold": 2500,
        "initial_strength": result.initial_strength_used,
        "max_strength": result.max_strength_used,
        "min_tenure": result.min_tenure_used,
        "max_tenure": result.max_tenure_used,
        "wall_seconds": wall,
        "cpu_seconds": cpu,
        "assignment": assignment,
        "replay_objective": replay.objective,
        "exact_replay": abs(replay.objective - result.objective) <= 1e-6,
        "engine": result.engine,
    }


def _record_key(record: dict[str, object]) -> tuple[str, int]:
    """Return the ``(instance, seed)`` key of a checkpoint record.

    Parameters
    ----------
    record : dict of str to object
        Parsed checkpoint record.

    Returns
    -------
    tuple of str, int
        Instance name and seed.

    Raises
    ------
    ValueError
        When the record does not carry a string instance and integer seed.
    """
    instance = record["instance"]
    seed = record["seed"]
    if not isinstance(instance, str) or not isinstance(seed, int) or isinstance(seed, bool):
        raise ValueError("malformed checkpoint record")
    return instance, seed


def load_checkpoint(path: Path) -> list[dict[str, object]]:
    """Load completed records from a JSON Lines checkpoint.

    Parameters
    ----------
    path : Path
        Checkpoint path.

    Returns
    -------
    list of dict
        Completed records, in file order.
    """
    if not path.is_file():
        return []
    records: list[dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def summarize(
    records: list[dict[str, object]],
    instances: tuple[str, ...],
) -> list[dict[str, object]]:
    """Build per-instance summary rows.

    Parameters
    ----------
    records : list of dict
        Completed evidence records.
    instances : tuple of str
        Instance order for the table.

    Returns
    -------
    list of dict
        One summary row per instance that has records.
    """
    summaries: list[dict[str, object]] = []
    for name in instances:
        rows = [row for row in records if row["instance"] == name]
        if not rows:
            continue
        gaps = [float(row["optimality_gap_percent"]) for row in rows]
        walls = [float(row["wall_seconds"]) for row in rows]
        cpus = [float(row["cpu_seconds"]) for row in rows]
        moves = [int(row["moves"]) for row in rows]
        summaries.append(
            {
                "instance": name,
                "size": rows[0]["size"],
                "runs": len(rows),
                "best_gap_percent": min(gaps),
                "mean_gap_percent": statistics.mean(gaps),
                "median_gap_percent": statistics.median(gaps),
                "worst_gap_percent": max(gaps),
                "optimum_runs": sum(gap < 1e-9 for gap in gaps),
                "patience_runs": sum(bool(row["converged_on_patience"]) for row in rows),
                "cap_hit_runs": sum(row["stop_reason"] == "max_moves" for row in rows),
                "mean_moves": statistics.mean(moves),
                "mean_local_optima": statistics.mean(float(row["local_optima"]) for row in rows),
                "mean_wall_seconds": statistics.mean(walls),
                "mean_cpu_seconds": statistics.mean(cpus),
            }
        )
    return summaries


def print_table(summaries: list[dict[str, object]]) -> None:
    """Print the per-instance summary table.

    Parameters
    ----------
    summaries : list of dict
        Summary rows from :func:`summarize`.
    """
    for row in summaries:
        print(
            f"{row['instance']}: mean={float(row['mean_gap_percent']):.3f}% "
            f"worst={float(row['worst_gap_percent']):.3f}% "
            f"patience={row['patience_runs']}/{row['runs']} "
            f"wall={float(row['mean_wall_seconds']):.1f}s",
            flush=True,
        )


def main() -> int:
    """Run the panel in parallel and write per-run and summary evidence.

    Returns
    -------
    int
        Process exit status.  Non-zero when a replay fails or the panel is
        incomplete.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--moves", type=int, default=DEFAULT_MOVES)
    parser.add_argument("--patience", type=int, default=DEFAULT_PATIENCE)
    parser.add_argument("--seeds", default="1,2,3,4,5")
    parser.add_argument("--workers", type=int, default=min(40, os.cpu_count() or 1))
    parser.add_argument("--out", default="qap-bls-expanded.json")
    parser.add_argument("--summary", default="qap-bls-expanded-summary.json")
    parser.add_argument(
        "--checkpoint",
        default=str(ROOT.parent / "runtime" / "qap-bls-expanded.checkpoint.jsonl"),
    )
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--allow-reference", action="store_true")
    parser.add_argument("--instances", default="")
    args = parser.parse_args()

    if not NUMBA_AVAILABLE and not args.allow_reference:
        raise SystemExit(
            "numba is required for the serious BLS panel; install the optional extra "
            "or pass --allow-reference for a slow smoke test"
        )
    selected = set(args.instances.split(",")) if args.instances else set(INSTANCES)
    instances = tuple(name for name in INSTANCES if name in selected)
    seeds = tuple(int(value) for value in args.seeds.split(","))
    checkpoint = Path(args.checkpoint)
    checkpoint.parent.mkdir(parents=True, exist_ok=True)
    if args.no_resume and checkpoint.is_file():
        checkpoint.unlink()
    done = {_record_key(record) for record in load_checkpoint(checkpoint)}
    tasks = [
        (name, optimum(name), seed, args.moves, args.patience)
        for name in instances
        for seed in seeds
        if (name, seed) not in done
    ]
    records: list[dict[str, object]] = [
        record
        for record in load_checkpoint(checkpoint)
        if record["instance"] in instances and int(record["seed"]) in seeds
    ]
    if done:
        print(f"resuming with {len(done)} checkpoint records", flush=True)
    started = time.perf_counter()
    with ProcessPoolExecutor(
        max_workers=max(1, min(args.workers, max(1, len(tasks)))),
        mp_context=multiprocessing.get_context("spawn"),
    ) as executor:
        futures = {executor.submit(run_task, task): task for task in tasks}
        with checkpoint.open("a", encoding="utf-8") as sink:
            for index, future in enumerate(as_completed(futures), 1):
                record = future.result()
                records.append(record)
                sink.write(json.dumps(record) + "\n")
                sink.flush()
                if index % 10 == 0 or index == len(tasks):
                    print(f"completed {index}/{len(tasks)}", flush=True)
    campaign_wall = time.perf_counter() - started
    order = {name: index for index, name in enumerate(instances)}
    records.sort(key=lambda row: (order[str(row["instance"])], int(row["seed"])))
    summaries = summarize(records, instances)
    print_table(summaries)
    failures = sum(not bool(record["exact_replay"]) for record in records)
    cap_hits = sum(record["stop_reason"] == "max_moves" for record in records)
    total_cpu = sum(float(record["cpu_seconds"]) for record in records)
    print(
        f"campaign wall={campaign_wall:.1f}s cpu-sum={total_cpu:.1f}s "
        f"replay_failures={failures} cap_hits={cap_hits}",
        flush=True,
    )
    evidence_dir = ROOT / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    (evidence_dir / args.out).write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    (evidence_dir / args.summary).write_text(
        json.dumps(summaries, indent=2) + "\n", encoding="utf-8"
    )
    incomplete = len(records) != len(instances) * len(seeds)
    return 1 if failures or incomplete else 0


if __name__ == "__main__":
    raise SystemExit(main())
