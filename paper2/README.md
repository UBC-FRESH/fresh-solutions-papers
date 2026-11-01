# Paper 2 public evidence

Pilot public-library transfer smoke test using Fresh Solutions v0.2.0. **Not a converged benchmark.**

## Instances

- `tai12a` — QAPLIB, size 12, known optimum **224416**
- `tai20a` — QAPLIB, size 20, known optimum **703482**
- `tai25a` — QAPLIB, size 25, optimum **1167256**
- `tai30a` — QAPLIB, size 30, best known **1818146**
- `berlin52` — TSPLIB EUC_2D, size 52, optimum **7542**
- `kroA100` — TSPLIB EUC_2D, size 100, optimum **21282**
- `kroB100` — TSPLIB EUC_2D, size 100, optimum **22141**
- `ch150` — TSPLIB EUC_2D, size 150, optimum **6528**

## Run

```bash
PYTHONPATH=fresh-solutions python paper2/run_multiseed.py
PYTHONPATH=fresh-solutions python paper2/replay_multiseed.py
```

Evidence: `paper2/evidence/public.json`.

## Results

Config: population 32, generations 50, local iterations 10,000, seeds 1–5.

| Instance | Size | Mean gap | Median gap | Worst gap | Mean wall |
| --- | ---: | ---: | ---: | ---: | ---: |
| tai12a | 12 | 8.897% | 8.039% | 11.616% | 0.360 s |
| tai20a | 20 | 7.185% | 7.102% | 9.394% | 0.734 s |
| tai25a | 25 | 5.249% | 5.980% | 6.174% | 1.038 s |
| tai30a | 30 | 5.679% | 5.937% | 6.678% | 1.359 s |
| berlin52 | 52 | 10.196% | 11.058% | 14.956% | 0.611 s |
| kroA100 | 100 | 21.490% | 21.958% | 29.997% | 1.095 s |
| kroB100 | 100 | 17.108% | 17.325% | 20.004% | 1.094 s |
| ch150 | 150 | 56.259% | 56.173% | 61.612% | 1.591 s |

These are **pilot, under-converged** transfer results, not leadership claims. All 40 assignments replay
exactly. A budget audit found tai12a stuck at a local optimum and ch150 improving from 61.6% to 12.2%
with 100k local iterations. See `notes/reports/p8-convergence-audit.md`. Do not use this table as a final
benchmark result.

Draft: `paper2/paper2-draft.md`.
