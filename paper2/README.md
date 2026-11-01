# Paper 2 public evidence

Public-library evidence pass using Fresh Solutions v0.2.0.

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

Config: population 32, generations 50, local iterations 3,000, seed 3.

| Instance | Objective | Known optimum | Gap |
| --- | ---: | ---: | ---: |
| tai12a | 241,016.000000 | 224,416 | **7.397%** |
| berlin52 | 9,033.000000 | 7,542 | **19.769%** |

The TSP result uses the v0.2.0 2-opt segment reversal. The previous swap-only result was 17,216
(128.268% gap).

These are honest first-pass transfer results, not leadership claims:

- QAP is within 7.4% of the known optimum on a 12-facility instance.
- TSP is within 19.8% on berlin52 with 2-opt, but no multi-seed or tuning campaign.
- No full QAPLIB/TSPLIB sweep.
