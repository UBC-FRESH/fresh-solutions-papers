# Paper 2 public evidence

Public-library evidence pass using Fresh Solutions v0.2.0.

## Instances

- `tai12a` — QAPLIB, size 12, known optimum **224416**
- `tai20a` — QAPLIB, size 20, known optimum **703482**
- `berlin52` — TSPLIB EUC_2D, size 52, optimum **7542**
- `kroA100` — TSPLIB EUC_2D, size 100, optimum **21282**

## Run

```bash
PYTHONPATH=fresh-solutions python paper2/run_public_benchmarks.py
PYTHONPATH=fresh-solutions python paper2/replay_public.py
```

Evidence: `paper2/evidence/public.json`.

## Results

Config: population 32, generations 50, local iterations 10,000, seed 3.

| Instance | Size | Objective | Optimum | Gap | Wall |
| --- | ---: | ---: | ---: | ---: | ---: |
| tai12a | 12 | 241,016 | 224,416 | **7.397%** | 0.351 s |
| tai20a | 20 | 757,090 | 703,482 | **7.620%** | 0.746 s |
| berlin52 | 52 | 8,670 | 7,542 | **14.956%** | 0.571 s |
| kroA100 | 100 | 26,180 | 21,282 | **23.015%** | 1.126 s |

These are honest first-pass transfer results, not leadership claims. The QAP path is consistently
within 8%, and the TSP 2-opt path is within 23% on the 100-city instance. No multi-seed distribution
or full QAPLIB/TSPLIB sweep has been run.

Draft: `paper2/paper2-draft.md`.
