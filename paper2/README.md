# Paper 2 public evidence

First public-library evidence pass using Fresh Solutions v0.1.0.

## Instances

- `tai12a` — QAPLIB, size 12, known optimum **224416**.
- `berlin52` — TSPLIB EUC_2D, size 52, optimum **7542**.

## Run

```bash
PYTHONPATH=fresh-solutions python paper2/run_public_benchmarks.py
PYTHONPATH=fresh-solutions python paper2/replay_public.py
```

Evidence: `paper2/evidence/public.json`.

## Results

| Instance | Objective | Known optimum | Gap |
| --- | ---: | ---: | ---: |
| tai12a | 251,340.000000 | 224,416 | **11.997%** |
| berlin52 | 17,216.000000 | 7,542 | **128.268%** |

These are honest first-pass transfer results, not leadership claims:

- The QAP path is within 12% of the known optimum on a 12-facility instance.
- The TSP path uses swap-only moves, not 2-opt, and is far from the optimum.
- The population is 16, generations 20, local iterations 200, seed 3; no tuning campaign.
