# P6 close-out: Paper 2 public evidence and operation

Status: complete
Date: 2026-11-01
Issue: #23

## Result

The first public-library Paper 2 evidence pass is recorded.

Instances:

- QAPLIB `tai12a`, size 12, known optimum 224416.
- TSPLIB `berlin52`, size 52, optimum 7542.

Run:

- Fresh Solutions v0.1.0 hybrid engine.
- Population 16, generations 20, local iterations 200, seed 3.

Results:

| Instance | Objective | Known optimum | Gap |
| --- | ---: | ---: | ---: |
| tai12a | 251,340.000000 | 224,416 | 11.997% |
| berlin52 | 17,216.000000 | 7,542 | 128.268% |

Both assignments replay exactly through their adapters.

## Interpretation

- The QAP path is within 12% of the known optimum on a small public instance.
- The TSP path is far from the optimum because it uses swap moves, not 2-opt.
- This is a transfer/evidence pass, not a benchmark-leadership claim.
- No tuning campaign, no multiple-seed distribution, and no full QAPLIB/TSPLIB sweep.

## Maintenance

`notes/design/maintenance-cadence.md` records the release/benchmark review cadence.

## Verification

- Public assignments replay exactly.
- Paper 2 evidence is in `paper2/evidence/public.json`.
- Source instances and provenance are pinned in `paper2/instances/`.
