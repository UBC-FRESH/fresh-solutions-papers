# Paper 2 working manuscript and evidence

**DO NOT SUBMIT.** This directory contains the working Paper 2 manuscript and its internal benchmark
evidence. The paper is a working draft, not a submission-ready article.

Working manuscript (LaTeX): `paper2-manuscript.tex`

Target: **Journal of Heuristics** for the harness/reference-adapter contribution. Fallback:
**SoftwareX** or **JORS**. **COR** requires an additional methodological contribution beyond the
current evidence.

Compiled PDF: `paper2-manuscript.pdf` — 23 pages, 8,755 source words.

Evidence release: Fresh Solutions **v0.9.3** (campaign generated at v0.8.0; all 60 convergence incumbents replayed exactly under v0.9.3).

## What changed in P12

- The QAP panel is convergence-controlled: ten seeds, 100,000-iteration patience, 1,000,000 cap.
- All 40 QAP runs stopped on `patience` and replayed exactly.
- A framework-managed QAP tabu path matched the standalone and production objectives on all 40 runs.
- TSP is convergence-controlled: five seeds, 10,000 kicks, 1,000-kick patience.
- All 20 TSP runs stopped on `patience`, reached the known optimum, and replayed exactly.
- The earlier 20-kick and 2,000-kick tables are retained as short-budget checks, not convergence
  evidence.

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
```

Final QAP framework-use campaign:

```bash
FRAMEWORK_SEEDS=10 FRAMEWORK_PATIENCE=100000 FRAMEWORK_WORKERS=40 \
  python3 paper2/run_framework_use.py
python3 paper2/analyze_framework_use.py
python3 paper2/replay_framework_use.py
```

Final TSP convergence campaign:

```bash
python3 paper2/run_tsp_convergence.py --kicks 10000 --patience 1000 \
  --seeds 1,2,3,4,5 --workers 20
python3 paper2/replay_tsp_convergence.py
python3 paper2/check_evidence.py
python3 paper2/broad_summary.py
```

## QAP robust tabu

Expanded convergence panel: 20 QAPLIB instances, five seeds, 100,000-iteration patience. All 100
runs plateau-stopped and replayed exactly; mean gap 0.274%, worst 1.583%, 37/100 optima. See
`evidence/qap-expanded-100k.json`. Independent BLS baseline on the same panel: mean 0.116%, worst
1.369%, 76/100 optima; BLS is stronger than tabu on 14 instance means and weaker on `chr22a`. SciPy
FAQ is a second, weaker external baseline: mean 25.44%, median 2.55%, worst 246.34%.

Final convergence panel: ten seeds, 100,000-iteration patience, 1,000,000-iteration cap. All 40 runs
plateau-stopped and replayed exactly. The CPU ratio is the framework-managed path divided by the
private-array delta path.

| Instance | Mean gap | Median gap | Worst gap | Mean iter. | CPU ratio |
| --- | ---: | ---: | ---: | ---: | ---: |
| tai12a | 0.000% | 0.000% | 0.000% | 100,186 | 1.327 |
| tai20a | 0.030% | 0.000% | 0.304% | 147,748 | 1.170 |
| tai25a | 0.077% | 0.000% | 0.402% | 175,611 | 1.181 |
| tai30a | 0.245% | 0.391% | 0.491% | 161,046 | 1.279 |

Overall framework CPU overhead: **1.239** (95% bootstrap CI 1.168–1.310). The paired order is
alternated by seed.

The earlier fixed-budget table (10,000/20,000 iterations) is retained in the evidence but is not the
convergence table. At 10,000 fixed iterations the means were 0.000%, 0.403%, 0.786%, and 0.792%.

### Independent baseline

SciPy `quadratic_assignment` (`faq`, `maxiter=10000`, SciPy 1.18.1), five seeds:

| Instance | SciPy mean gap | Tabu mean gap | SciPy mean wall (s) |
| --- | ---: | ---: | ---: |
| tai12a | 9.026% | 0.000% | 0.001 |
| tai20a | 4.642% | 0.030% | 0.002 |
| tai25a | 4.474% | 0.077% | 0.003 |
| tai30a | 2.289% | 0.245% | 0.005 |

The baseline is much faster and much worse. This is a time-quality comparison, not an equal-budget
comparison, and not a claim of universal dominance.

## TSP iterated Lin–Kernighan

An expanded 20-instance TSPLIB panel from nearest-neighbour starts is in progress; the four-instance
generic-local-search-start panel remains the controlled framework evidence.

Final convergence campaign: five seeds, 10,000 kicks, 1,000-kick patience. All 20 runs
plateau-stopped, reached the known optimum, and replayed exactly.

| Instance | Or-opt mean gap | ILK mean gap | ILK worst gap | Plateau | Mean wall |
| --- | ---: | ---: | ---: | ---: | ---: |
| berlin52 | 6.433% | 0.000% | 0.000% | 5/5 | 754.3 s |
| kroA100 | 7.323% | 0.000% | 0.000% | 5/5 | 605.0 s |
| kroB100 | 3.696% | 0.000% | 0.000% | 5/5 | 688.4 s |
| ch150 | 8.229% | 0.000% | 0.000% | 5/5 | 603.9 s |

Short-budget checks:

- 2,000 kicks / 200 patience: 19/20 optima, ch150 mean 0.015%, worst 0.077%.
- 20 kicks: the optimum on three of four instances (15/20 runs), ch150 mean 0.383%.

### Kicks ablation

Five seeds per instance. `lk-only` is the sequential exchange without double-bridge kicks;
`ilk-5` and `ilk-20` add that many kicks.

| Instance | LK-only mean gap | ILK-5 mean gap | ILK-20 mean gap |
| --- | ---: | ---: | ---: |
| berlin52 | 2.580% | 0.000% | 0.000% |
| kroA100 | 1.075% | 0.062% | 0.000% |
| kroB100 | 0.780% | 0.172% | 0.000% |
| ch150 | 2.203% | 0.558% | 0.383% |

The kicks are material; all 60 ablation tours replay exactly.

## Broad panels and LKH

- QAP broad: 134 parseable QAPLIB instances, five seeds, 552/670 patience stops, 318 optima,
  median 0.000%, mean 1.823%, worst 36.4%.
- TSP broad: 78 TSPLIB instances, five seeds, 236/390 patience stops, 183 optima, median 0.000%,
  mean 0.100%. Large tail remains weak.
- External LKH large tail: 71/100 optima, mean 0.092%, median 0%, worst 1.930%. LKH is external
  research-use software, not bundled, capability-only comparison.

## Evidence files

- `evidence/framework-use.json`
- `evidence/framework-use-summary.json`
- `evidence/framework-use-analysis.json`
- `evidence/framework-use-patience50k.json`
- `evidence/framework-use-patience100k.json`
- `evidence/framework-use-sensitivity.json`
- `evidence/tsp-convergence-10k.json`
- `evidence/tsp-convergence-10k-summary.json`
- `evidence/tsp-convergence-2k.json`
- `evidence/tsp-lk.json`
- `evidence/qap-tabu*.json`
- `evidence/broad-converged.json.gz`
- `evidence/provenance-2026-11-03.json`
- `evidence/lkh-provenance.json`

No tag or release has been created. The evidence release remains a candidate until maintainer
approval.
