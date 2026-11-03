# Paper 2 internal engineering notes

**DO NOT SUBMIT as publication evidence.** This directory contains the internal benchmark-harness
evidence and draft. It is not a publication-grade campaign yet.

Evidence release: Fresh Solutions **v0.8.0**.

Working manuscript (LaTeX): `paper2-manuscript.tex`

Compiled PDF: `paper2-manuscript.pdf`

Draft: `paper2-draft.md` — **INTERNAL, NOT SUBMISSION-READY**.

Convergence-controlled public-library evidence using the pinned Fresh Solutions submodule, the QAP
robust-tabu campaign, the iterated Lin–Kernighan campaign, and the optional external LKH boundary.

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
PYTHONPATH=fresh-solutions python paper2/run_tsp_lk.py
PYTHONPATH=fresh-solutions python paper2/replay_tsp_lk.py
PYTHONPATH=fresh-solutions python paper2/run_tsp_lk_ablation.py
PYTHONPATH=fresh-solutions python paper2/replay_tsp_lk.py --input tsp-lk-ablation.json
```

Internal evidence: `paper2/evidence/converged.json`, `paper2/evidence/qap-tabu.json`, and
`paper2/evidence/tsp-lk.json`.

## QAP robust tabu

Five seeds. The certified budget is the smallest budget whose next doubling improves the mean gap by
≤0.10 percentage points, or where every seed reaches the known optimum.

| Instance | Certified budget | Mean gap | Median gap | Worst gap | Larger check |
| --- | ---: | ---: | ---: | ---: | ---: |
| tai12a | 10,000 | 0.000% | 0.000% | 0.000% | optimum on all seeds |
| tai20a | 10,000 | 0.403% | 0.470% | 0.470% | 20k: 0.370% |
| tai25a | 20,000 | 0.685% | 0.850% | 0.850% | 40k: 0.592% |
| tai30a | 10,000 | 0.792% | 0.792% | 1.139% | 20k: 0.700% |

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
| tai30a | 2.289% | 0.792% | 0.005 |

The baseline is much faster and much worse. This is a time-quality comparison, not an equal-budget
comparison, and not a claim of universal dominance.

## Iterated Lin–Kernighan — P10.1

Five seeds, starting from the converged Or-opt assignment. Config: 16 candidates, depth 4, 20
double-bridge kicks, 100 LK passes.

| Instance | Or-opt mean gap | LK mean gap | LK worst gap | LK mean wall (s) |
| --- | ---: | ---: | ---: | ---: |
| berlin52 | 6.433% | 0.000% | 0.000% | 12.18 |
| kroA100 | 7.323% | 0.000% | 0.000% | 8.46 |
| kroB100 | 3.696% | 0.000% | 0.000% | 11.67 |
| ch150 | 8.229% | 0.383% | 0.475% | 11.59 |

All 20 tours replay exactly. The LK path receives additional local-search time; this is a
quality-at-additional-cost result, not an equal-budget ablation. No state-of-the-art claim.

### Kicks ablation

Five seeds per instance. `lk-only` is the sequential exchange without double-bridge kicks;
`ilk-5` and `ilk-20` add that many kicks.

| Instance | LK-only mean gap | ILK-5 mean gap | ILK-20 mean gap |
| --- | ---: | ---: | ---: |
| berlin52 | 2.580% | 0.000% | 0.000% |
| kroA100 | 1.075% | 0.062% | 0.000% |
| kroB100 | 0.780% | 0.172% | 0.000% |
| ch150 | 2.203% | 0.558% | 0.383% |

The kicks are not cosmetic: they contribute the difference between a good LK local optimum and
near-optimum/optimum tours. All 60 ablation tours are replayable; see
`paper2/evidence/tsp-lk-ablation.json`.
