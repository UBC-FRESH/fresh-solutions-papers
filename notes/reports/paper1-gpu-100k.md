# Paper 1 100k-generation GPU-GA record

Status: headline accelerated result; not a public/independent-model baseline
Date: 2026-11-02
Record: `evidence/ws4-tsa24-gpu-ga-100000-r7/record.json`

## Result

- Solver: WS4 GPU-GA, population 64, **100,000 generations**, seed 7.
- Instance: full TSA24 landscape, 208,255 blocks, 20 periods.
- Objective: **517.8619818205188**.
- Exact CPU replay: **517.8619818205188**.
- Search 856.10 s; wall 941.51 s; max RSS 8,260 MB.
- Initial seed: 1,722,144,291.336651.
- Five-seed 100k campaign: 512.574–518.621; mean 515.682; median 515.938; worst 518.621;
  all exact replay; 4,004.77 s wall for five runs.

## Scaling

| Generations | Objective | Wall |
| ---: | ---: | ---: |
| 1,000 | 8,588,725.370498 | 23.13 s |
| 10,000 | 76,540.740733 | 157.34 s |
| 100,000 | 517.861982 | 941.51 s |
| CPU-SA 100k (independent search) | 335,044,976.675435 | 1,875.12 s |

The GPU-GA path is the headline: it reaches the maximum even-flow regime on the 208k operable-block
instance in about 16 minutes. The 517.86 total is dominated by the deliberate level aspiration
(515.14); the flow term is 2.72. The realized level is about 51.3–52.4M m³/period against a 70M
aspiration. The CPU-SA baseline is a separate search path on the same model, not an independent
model, and it is untuned.

## Boundary

- TSA24 is a public frozen artifact, but it has no explicit LICENSE and no independent model baseline.
- No independent model comparison.
- The 100k result is not a global-optimality proof.
