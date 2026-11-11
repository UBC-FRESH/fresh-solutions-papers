"""Replay the WS4 TSA24 100k-generation GPU-GA record with the exact CPU evaluator."""

from __future__ import annotations

import json
import os
from pathlib import Path

from ws4.opt.engine import OptimizeConfig, Optimizer, load_schedule_csv
from ws4.opt.incremental import IncrementalObjective
from ws4.opt.objective import load_targets

HERE = Path(__file__).resolve().parent
INSTANCE = Path(os.environ["TSA24_ROOT"])
RECORD = json.loads((HERE / "record.json").read_text(encoding="utf-8"))
TARGETS = INSTANCE / "config/ws4/targets/evenflow_tsa24.yaml"
if not TARGETS.exists():
    TARGETS = INSTANCE / "evenflow_tsa24.yaml"
COMPILED = INSTANCE / "build/compiled"
if not COMPILED.exists():
    COMPILED = INSTANCE / "compiled"
OPTIMIZER = Optimizer.from_dataset(
    COMPILED,
    OptimizeConfig(years=200, targets_path=str(TARGETS), iterations=1, threads=1),
)
EVALUATOR = IncrementalObjective(OPTIMIZER, load_targets(TARGETS))
EVALUATOR.reset(load_schedule_csv(HERE / RECORD["result"]["schedule_path"]))
expected = RECORD["result"]["objective"]
print(json.dumps({"objective": EVALUATOR.objective, "expected": expected}, indent=2))
if abs(EVALUATOR.objective - expected) > 1e-6:
    raise SystemExit(1)
