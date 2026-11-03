#!/usr/bin/env python3
"""Compare whole-schedule evaluation with exact incremental deltas on TSA24.

The whole-schedule path is too slow to run repeatedly on all 208,255 operable
blocks, so this diagnostic uses the first 5,000 blocks of the recorded 100k
schedule. The scope is written into the output.
"""

from __future__ import annotations

import json
import os
import random
import statistics
import sys
import time
from pathlib import Path

WS4_ROOT = Path(os.environ["WS4_ROOT"])
TSA24_ROOT = Path(os.environ["TSA24_ROOT"])
PAPERS_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WS4_ROOT))

from ws4.opt.engine import OptimizeConfig, Optimizer, load_schedule_csv  # noqa: E402
from ws4.opt.objective import load_targets  # noqa: E402

SUBSET_BLOCKS = int(os.environ.get("SUBSET_BLOCKS", "5000"))
MOVES = int(os.environ.get("MOVES", "50"))
FULL_MOVES = int(os.environ.get("FULL_MOVES", "5"))
SCHEDULE = Path(
    os.environ.get(
        "TSA24_SCHEDULE",
        str(PAPERS_ROOT / "evidence/ws4-tsa24-gpu-ga-100000-r7/schedule.csv"),
    )
)
OUT = PAPERS_ROOT / "evidence/ws4-tsa24-eval-ablation.json"


def main() -> int:
    """Run the diagnostic evaluation-path ablation."""
    targets_path = TSA24_ROOT / "config/ws4/targets/evenflow_tsa24.yaml"
    targets = load_targets(targets_path)
    optimizer = Optimizer.from_dataset(
        TSA24_ROOT / "build/compiled",
        OptimizeConfig(years=200, targets_path=str(targets_path), iterations=1, threads=1),
    )
    complete = load_schedule_csv(SCHEDULE)
    blocks = list(complete)[:SUBSET_BLOCKS]
    schedule = {block: complete[block] for block in blocks}
    candidates = optimizer.candidates()
    started = time.perf_counter()
    baseline = optimizer._evaluate(schedule, targets)
    baseline_s = time.perf_counter() - started
    evaluator = optimizer.delta_evaluator(targets)
    if evaluator is None:
        raise RuntimeError("TSA24 targets do not support the delta evaluator")
    started = time.perf_counter()
    evaluator.reset(schedule)
    reset_s = time.perf_counter() - started
    if abs(evaluator.objective - baseline) > 1e-6:
        raise RuntimeError("incremental baseline differs from full baseline")

    rng = random.Random(17)
    delta_times: list[float] = []
    full_times: list[float] = []
    moved = 0
    for block in blocks:
        options = candidates.get(block, [])
        current = schedule.get(block)
        choices = [chain for chain in options if chain != current]
        if len(options) < 2 or not choices:
            continue
        schedule[block] = rng.choice(choices)
        started = time.perf_counter()
        evaluator.delta([block], schedule)
        evaluator.apply([block], schedule)
        delta_times.append(time.perf_counter() - started)
        moved += 1
        if moved <= FULL_MOVES:
            started = time.perf_counter()
            optimizer._evaluate(schedule, targets)
            full_times.append(time.perf_counter() - started)
        if moved >= MOVES:
            break
    started = time.perf_counter()
    final = optimizer._evaluate(schedule, targets)
    final_s = time.perf_counter() - started
    error = abs(evaluator.objective - final)
    payload = {
        "scope": f"{SUBSET_BLOCKS}-block subset of TSA24 100k seed-7 schedule",
        "moves": moved,
        "full_baseline_s": baseline_s,
        "full_final_s": final_s,
        "reset_s": reset_s,
        "full_move_mean_s": statistics.mean(full_times),
        "delta_apply_mean_s": statistics.mean(delta_times),
        "speedup": statistics.mean(full_times) / statistics.mean(delta_times),
        "full_objective": final,
        "incremental_objective": evaluator.objective,
        "absolute_error": error,
        "exact": error <= 1e-6,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
