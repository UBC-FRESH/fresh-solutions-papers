# P7 close-out: Paper 2 evidence and writing

Status: complete
Date: 2026-11-01
Issue: #25

## Result

Paper 2 now has a four-instance public evidence table and a first transfer-paper draft.

Evidence:

| Instance | Objective | Optimum | Gap |
| --- | ---: | ---: | ---: |
| tai12a | 241,016 | 224,416 | 7.397% |
| tai20a | 757,090 | 703,482 | 7.620% |
| berlin52 | 8,670 | 7,542 | 14.956% |
| kroA100 | 26,180 | 21,282 | 23.015% |

Config: population 32, generations 50, local iterations 10,000, seed 3.

## Deliverables

- `paper2/paper2-draft.md`
- `paper2/evidence/public.json`
- `paper2/run_public_benchmarks.py`
- `paper2/replay_public.py`
- `paper2/instances/` with provenance

## Verification

- All four assignments replay exactly.
- Tests, Sphinx `-W`, and workflow validator pass.
- No leadership claim is made.

## Limits

Four instances, one seed, one configuration, basic 2-opt; no full QAPLIB/TSPLIB campaign or GPU backend.
