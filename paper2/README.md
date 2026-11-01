# Paper 2 internal engineering notes

**DO NOT SUBMIT as publication evidence.** This directory contains smoke tests and benchmark-harness
checks. The QAP/TSP results are not a publication-grade benchmark campaign.

Evidence release: Fresh Solutions **v0.4.0**.

Convergence-controlled public-library evidence using Fresh Solutions v0.3.0, plus the v0.4.0 QAP
robust-tabu campaign.

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
PYTHONPATH=fresh-solutions python paper2/run_qap_tabu.py --iterations 10000
PYTHONPATH=fresh-solutions python paper2/replay_qap_tabu.py
```

Internal evidence: `paper2/evidence/converged.json` and `paper2/evidence/qap-tabu.json`.

## QAP robust tabu — v0.4.0

Five seeds. The certified budget is the smallest budget whose next doubling improves the mean gap by
≤0.10 percentage points, or where every seed reaches the known optimum.

| Instance | Certified budget | Mean gap | Median gap | Worst gap | Larger check |
| --- | ---: | ---: | ---: | ---: | ---: |
| tai12a | 10,000 | 0.000% | 0.000% | 0.000% | optimum on all seeds |
| tai20a | 10,000 | 0.403% | 0.470% | 0.470% | 20k: 0.370% |
| tai25a | 20,000 | 0.685% | 0.850% | 0.850% | 40k: 0.592% |
| tai30a | 40,000 | 0.407% | 0.407% | 0.678% | 80k: 0.348% |

All 20 selected assignments replay exactly. The larger-budget values are retained for transparency but
are not substituted into the headline table. This is a competitive-neighborhood result, not a
state-of-the-art claim.

### Independent baseline

SciPy `quadratic_assignment` (`faq`, `maxiter=10000`, SciPy 1.18.1), five seeds:

| Instance | SciPy mean gap | Tabu mean gap | SciPy mean wall (s) |
| --- | ---: | ---: | ---: |
| tai12a | 9.026% | 0.000% | 0.001 |
| tai20a | 4.642% | 0.403% | 0.002 |
| tai25a | 4.474% | 0.685% | 0.003 |
| tai30a | 2.289% | 0.407% | 0.005 |

The baseline is much faster and much worse. This is a time-quality comparison, not an equal-budget
comparison, and not a claim of universal dominance.
