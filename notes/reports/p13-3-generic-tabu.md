# P13.3 generic engine tabu/LNS layer

Status: complete, negative result
Date: 2026-11-09
Phase identifier: P13
Task: P13.3 (issue #84)
Branch: `feature/p13-publication-hardening`

## Question

Can a search layer that knows only the `ProblemAdapter` contract produce a credible result on
QAP and TSP, compared with the adapter-specific modules used elsewhere in Paper 2?

The answer from this prototype is **no**. The generic layer is substantially worse on every
instance tested. The framework evidence therefore still supports contract portability and
resident-state management, not a competitive generic search layer.

## What was implemented

- `paper2/generic_tabu.py`
  - `GenericTabuConfig` and `GenericTabuResult`.
  - Sampled tabu search: each iteration draws `proposals` moves from `adapter.propose`,
    evaluates every feasible candidate exactly through `ResidentAssignment`, and accepts the
    best admissible move.
  - Tabu memory on `(variable, value)` by default, with a `variable`-only option. The search
    records the values removed by the accepted move, so the immediate reverse move is tabu.
  - Aspiration when a tabu candidate beats the global best.
  - Optional LNS-style kick: a sequence of `perturb_moves` adapter proposals after a declared
    stagnation threshold, with a declared interval.
  - Patience, iteration, and wall-clock stopping rules.
  - No QAP/TSP import, no distance/flow matrix access, no private delta matrix, and no
    problem-specific branch inside the loop.
- `paper2/run_generic_tabu.py`
  - Runs the declared QAP/TSP panel, five seeds, checkpointed JSONL, per-run exact replay, and
    a summary with the gap to the adapter-specific reference.
- `paper2/replay_generic_tabu.py`
  - Independently replays every stored incumbent through the adapter and `ResidentAssignment`.

Only `ProblemAdapter` operations (`propose`, `apply`, `undo`, `evaluate`,
`initial_assignment`, `random_assignment`, `variable_count`) and `ResidentAssignment` are used
in the search.

## Command

```bash
python paper2/run_generic_tabu.py --workers 40
python paper2/replay_generic_tabu.py
ruff check paper2/generic_tabu.py paper2/run_generic_tabu.py paper2/replay_generic_tabu.py
ruff format --check paper2/generic_tabu.py paper2/run_generic_tabu.py paper2/replay_generic_tabu.py
```

The default run took 47 s wall time on 40 workers. The checkpoint is
`paper2/evidence/generic-tabu.jsonl`; a rerun skips completed `(instance, seed)` pairs with the
same configuration signature.

## Declared budget

| Setting | Value |
| --- | --- |
| Instances | `tai12a`, `tai20a`, `tai25a`, `tai30a`, `berlin52`, `kroA100`, `kroB100`, `ch150` |
| Seeds | 1, 2, 3, 4, 5 |
| Iterations | 20,000 |
| Patience | 5,000 iterations without a new best |
| Proposals per iteration | 16 |
| Tabu attribute | `(variable, value)` |
| Tenure | 5 to 15 iterations |
| LNS kick | after 1,000 stagnant iterations, at most once per 1,000 iterations, 5 proposals |
| Start | seeded random assignment from `adapter.random_assignment` |
| Wall-clock cap | none |
| Exact evaluations per run | 83,493 to 225,804 (mean 116,868) |

All 40 runs stopped on `patience`; there were no iteration-cap or wall-clock cap hits. All 40
incumbents replay exactly, and all are feasible.

## Results

Gap is to the known optimum. The reference is the adapter-specific published evidence:
`qap-expanded-100k-summary.json` (`qap_tabu`, 1,000,000 iterations, patience 100,000) and
`tsp-expanded-10k-summary.json` (`tsp_lk`, 10,000 kicks, patience 1,000). `delta_pp` is the
generic mean gap minus the reference mean gap, in percentage points.

| Instance | n | Best gap % | Mean gap % | Median gap % | Worst gap % | Optimum runs | Mean wall s | Mean CPU s | Ref mean gap % | delta_pp |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| tai12a | 12 | 0.000 | 1.265 | 0.000 | 3.843 | 3/5 | 5.3 | 5.2 | 0.000 | 1.265 |
| tai20a | 20 | 2.743 | 3.734 | 3.954 | 4.551 | 0/5 | 11.4 | 11.4 | 0.000 | 3.734 |
| tai25a | 25 | 4.157 | 5.070 | 5.316 | 5.529 | 0/5 | 14.9 | 14.8 | 0.073 | 4.997 |
| tai30a | 30 | 4.916 | 5.323 | 5.495 | 5.677 | 0/5 | 16.9 | 16.8 | 0.313 | 5.010 |
| berlin52 | 52 | 36.277 | 39.706 | 38.823 | 44.193 | 0/5 | 10.7 | 10.6 | 0.000 | 39.706 |
| kroA100 | 100 | 119.505 | 143.946 | 151.123 | 154.797 | 0/5 | 19.2 | 19.1 | 0.000 | 143.946 |
| kroB100 | 100 | 133.508 | 136.492 | 135.622 | 142.419 | 0/5 | 17.2 | 17.1 | 0.000 | 136.492 |
| ch150 | 150 | 173.958 | 191.768 | 191.774 | 202.834 | 0/5 | 33.0 | 32.9 | 0.000 | 191.768 |

Family mean of instance mean gaps:

- QAP: **3.848%** versus **0.097%** for the adapter-specific `qap_tabu` reference.
- TSP: **127.978%** versus **0.000%** for the adapter-specific `tsp_lk` reference.

The generic layer is not competitive. It is also not a like-for-like work comparison: the
generic runs use about 117,000 exact evaluations, while the reference modules spend much more
work per run, especially on TSP. A matched-budget control shows that the gap is not explained
only by the larger reference budget.

### Matched-budget control

For QAP, `paper2/evidence/qap-tabu-20k-summary.json` is the adapter-specific `qap_tabu` module at
the same 20,000-iteration cap. For TSP, `paper2/evidence/tsp-convergence-2k-summary.json` is the
adapter-specific `tsp_lk` module at only 2,000 kicks with patience 200. Both still dominate the
generic layer.

| Control | tai12a | tai20a | tai25a | tai30a | Mean |
| --- | ---: | ---: | ---: | ---: | ---: |
| `qap_tabu` 20k iterations, mean gap % | 0.000 | 0.370 | 0.685 | 0.700 | 0.439 |
| `generic_tabu` 20k iterations, mean gap % | 1.265 | 3.734 | 5.070 | 5.323 | 3.848 |

| Control | berlin52 | kroA100 | kroB100 | ch150 | Mean |
| --- | ---: | ---: | ---: | ---: | ---: |
| `tsp_lk` 2k kicks, patience 200, mean gap % | 0.000 | 0.000 | 0.000 | 0.015 | 0.004 |
| `generic_tabu` 20k iterations, mean gap % | 39.706 | 143.946 | 136.492 | 191.768 | 127.978 |

## Evidence paths

- `paper2/evidence/generic-tabu.json` — 40 per-run records with assignment, objective, budget,
  stop reason, counters, wall/CPU time, and exact-replay fields.
- `paper2/evidence/generic-tabu-summary.json` — per-instance summary with reference gaps.
- `paper2/evidence/generic-tabu.jsonl` — resumable checkpoint.
- `paper2/generic_tabu.py`, `paper2/run_generic_tabu.py`, `paper2/replay_generic_tabu.py`.

Verification output:

```text
replayed 40 generic-tabu incumbents exactly
```

## Limitations

- The reference comparison is not equal work. The adapter-specific QAP reference uses full
  neighbourhood scans and a Taillard delta matrix; the TSP reference uses Lin-Kernighan local
  search plus double-bridge kicks. The generic layer has neither.
- The generic layer samples 16 proposals per iteration instead of scanning a complete
  neighbourhood. This is the main structural reason for the QAP gap.
- TSP starts from a seeded random permutation because nearest-neighbour construction needs the
  distance matrix, which is outside the contract. The adapter-specific TSP evidence uses
  nearest-neighbour or Or-opt starts. The gap is far larger than a start-quality explanation;
  the generic layer also lacks a local-improvement engine.
- One configuration was tested. Tenure, proposal count, and perturbation settings were not
  tuned. Tuning could narrow the QAP gap but is unlikely to close a factor of eight against
  full-neighbourhood tabu, and much less the TSP gap.
- The LNS component is a generic kick built from adapter proposals, not a destroy-repair
  operator. No problem-specific neighbourhood was supplied.
- Only two families and eight instances were tested. No third adapter was involved.
- CPU only; no GPU path was exercised.

## Claim language

Do not claim that the generic engine is competitive, that it produces a headline-quality
result, or that it replaces the adapter-specific modules. Paper 2 should describe P13.3 as a
negative result: the adapter contract is sufficient to run a search, but a generic sampled
tabu/LNS layer is far weaker than adapter-specific tabu and Lin-Kernighan. The framework
contribution remains resident-state management and contract portability.

## Inputs relied on

- `AGENTS.md`
- `notes/plans/p13-publication-hardening-2026-11-08.md`
- `notes/issue-bodies/p13/03-generic-engine.md`
- `fresh-solutions/fresh_solutions/contracts.py`
- `fresh-solutions/fresh_solutions/engine.py`
- `fresh-solutions/fresh_solutions/adapters/qap.py`
- `fresh-solutions/fresh_solutions/adapters/tsp.py`
- `paper2/evidence/qap-expanded-100k-summary.json`
- `paper2/evidence/tsp-expanded-10k-summary.json`
- `paper2/evidence/qap-bls-expanded-summary.json`
- `paper2/evidence/qap-tabu-20k-summary.json`
- `paper2/evidence/tsp-convergence-2k-summary.json`
