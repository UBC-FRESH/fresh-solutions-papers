"""Replay every convergence-controlled public assignment exactly."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402

RECORDS = json.loads((ROOT / "evidence" / "converged.json").read_text(encoding="utf-8"))
ADAPTERS = {
    "tai12a": QuadraticAssignment.from_qaplib(ROOT / "instances" / "tai12a.dat"),
    "tai20a": QuadraticAssignment.from_qaplib(ROOT / "instances" / "tai20a.dat"),
    "tai25a": QuadraticAssignment.from_qaplib(ROOT / "instances" / "tai25a.dat"),
    "tai30a": QuadraticAssignment.from_qaplib(ROOT / "instances" / "tai30a.dat"),
    "berlin52": TravellingSalesman.from_tsplib(ROOT / "instances" / "berlin52.tsp"),
    "kroA100": TravellingSalesman.from_tsplib(ROOT / "instances" / "kroA100.tsp"),
    "kroB100": TravellingSalesman.from_tsplib(ROOT / "instances" / "kroB100.tsp"),
    "ch150": TravellingSalesman.from_tsplib(ROOT / "instances" / "ch150.tsp"),
}
for record in RECORDS:
    adapter = ADAPTERS[record["instance"]]
    assignment = {int(key): value for key, value in record["assignment"].items()}
    evaluation = adapter.evaluate(assignment)
    if abs(evaluation.objective - record["objective"]) > 1e-9:
        raise SystemExit(f"replay mismatch: {record['instance']} {record['seed']}")
print(f"replayed {len(RECORDS)} converged records exactly")
