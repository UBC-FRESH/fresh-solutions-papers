"""Replay the public QAP/TSP evidence assignments exactly."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "fresh-solutions"))

from fresh_solutions.adapters import QuadraticAssignment, TravellingSalesman  # noqa: E402

records = json.loads((ROOT / "evidence" / "public.json").read_text(encoding="utf-8"))
adapters = {
    "tai12a": QuadraticAssignment.from_qaplib(ROOT / "instances" / "tai12a.dat"),
    "berlin52": TravellingSalesman.from_tsplib(ROOT / "instances" / "berlin52.tsp"),
}
for record in records:
    adapter = adapters[record["instance"]]
    assignment = {int(key): value for key, value in record["result"]["assignment"].items()}
    evaluation = adapter.evaluate(assignment)
    expected = record["result"]["objective"]
    print(f"{record['instance']}: replay={evaluation.objective} expected={expected}")
    if abs(evaluation.objective - expected) > 1e-9:
        raise SystemExit(1)
