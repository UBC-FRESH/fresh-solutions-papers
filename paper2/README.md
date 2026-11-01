# Paper 2 public evidence

Convergence-controlled public-library evidence using Fresh Solutions v0.3.0.

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
PYTHONPATH=fresh-solutions python paper2/run_converged.py
PYTHONPATH=fresh-solutions python paper2/replay_converged.py
```

Evidence: `paper2/evidence/public.json`.

## Results

Config: Fresh Solutions v0.3.0, population 32, generations 50, 10,000 local iterations per round,
seeds 1–5, patience 3 rounds, 30 rounds / 500,000 evaluation cap.

| Instance | Size | Mean gap | Median gap | Worst gap | Mean evals |
| --- | ---: | ---: | ---: | ---: | ---: |
| tai12a | 12 | 8.897% | 8.039% | 11.616% | 31,635 |
| tai20a | 20 | 7.185% | 7.102% | 9.394% | 37,636 |
| tai25a | 25 | 5.249% | 5.980% | 6.174% | 41,636 |
| tai30a | 30 | 5.679% | 5.937% | 6.678% | 41,636 |
| berlin52 | 52 | 6.433% | 5.754% | 11.522% | 71,639 |
| kroA100 | 100 | 7.323% | 7.293% | 13.847% | 105,642 |
| kroB100 | 100 | 3.696% | 2.823% | 7.272% | 105,642 |
| ch150 | 150 | 8.229% | 8.517% | 10.463% | 171,649 |

All 40 runs stopped on patience and all 40 assignments replay exactly. QAP remains swap-limited;
TSP Or-opt is the stronger transfer result. This is not a leadership claim.
