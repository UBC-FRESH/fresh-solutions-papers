"""Replay the FHOPS small21 baseline record exactly."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from fhops.optimization.heuristics.common import (
    evaluate_assignments,
    resolve_objective_weight_overrides,
)
from fhops.optimization.operational_problem import (
    build_operational_problem,
    override_objective_weights,
)
from fhops.scenario.contract import Problem
from fhops.scenario.io import load_scenario

HERE = Path(__file__).resolve().parent
FHOPS = Path("/srv/shared-data/gep/ws4/fhops")
RECORD = json.loads((HERE / "record.json").read_text(encoding="utf-8"))
SCENARIO = load_scenario(str(FHOPS / "examples" / "small21" / "scenario.yaml"))
PROBLEM = Problem.from_scenario(SCENARIO)
ASSIGNMENTS = pd.read_csv(HERE / RECORD["result"]["schedule_path"])
CONTEXT = build_operational_problem(PROBLEM)
OVERRIDES = resolve_objective_weight_overrides(PROBLEM, None)
if OVERRIDES:
    CONTEXT = override_objective_weights(CONTEXT, OVERRIDES)
DEBUG: dict[str, float] = {}
SCORE = evaluate_assignments(PROBLEM, ASSIGNMENTS, CONTEXT, debug=DEBUG)
EXPECTED = RECORD["result"]["objective"]
print(
    json.dumps(
        {
            "objective": SCORE,
            "expected": EXPECTED,
            "hard_violations": DEBUG["hard_violation_count"],
        },
        indent=2,
    )
)
if abs(SCORE - EXPECTED) > 1e-6 or DEBUG["hard_violation_count"] != 0:
    raise SystemExit(1)
