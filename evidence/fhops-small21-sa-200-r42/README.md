# FHOPS small21 SA baseline

Second P3 public baseline.

- Instance: FHOPS `examples/small21`
- Solver: FHOPS SA, 200 iterations, seed 42
- Objective: **15508.884819999994**
- Assignments: 90
- Exact replay: **15508.884819999994**
- Hard violations: **0**
- Schedule: `assignments.csv`
- Record: `record.json`

Replay:

```bash
PYTHONPATH="$FHOPS_ROOT/src" python evidence/fhops-small21-sa-200-r42/replay.py
```

This is a baseline reproduction, not a WS4/FHOPS architecture comparison.
