# FHOPS tiny7 SA baseline

First P3 replayable benchmark record.

- Instance: FHOPS `examples/tiny7`
- Solver: FHOPS simulated annealing, 200 iterations, seed 42
- Objective: **4295.774752**
- Assignments: 23
- Exact replay: **4295.774752**
- Hard violations: **0**
- Schedule: `assignments.csv`
- SHA-256: `c5664677bb9137de7b91754e95fa1fd49217cc2e87103d02628c8a73e9ea4b58`
- Record: `record.json`

Replay requires the FHOPS checkout and its dependencies:

```bash
PYTHONPATH="$FHOPS_ROOT/src" python evidence/fhops-tiny7-sa-200-r42/replay.py
```

This is a **baseline reproduction**, not a WS4-vs-FHOPS architecture comparison.
