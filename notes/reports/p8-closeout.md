# P8 close-out: Paper 2 multi-seed campaign

Status: complete
Date: 2026-11-01
Issue: #27

## Result

Paper 2 evidence now covers eight public QAPLIB/TSPLIB instances with five seeds each.

Config: Fresh Solutions v0.2.0, population 32, generations 50, local iterations 10,000, seeds 1–5.

Mean gaps:

- QAP: 5.249%–8.897%
- TSP: 10.196%–56.259%
- ch150 is the weak case at 56.259% mean gap.

All 40 assignments replay exactly.

## Deliverables

- `paper2/run_multiseed.py`
- `paper2/replay_multiseed.py`
- `paper2/evidence/multiseed.json`
- `paper2/evidence/multiseed-summary.json`
- Updated `paper2/paper2-draft.md`
- Updated `paper2/README.md`

## Verification

- 40/40 assignments replay exactly.
- Tests, Sphinx `-W`, and workflow validator pass.

## Limits

One configuration, no per-instance tuning, basic 2-opt; not a full benchmark campaign or leadership claim.
