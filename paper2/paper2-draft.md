# Fresh Solutions: a compiled-state hybrid metaheuristic engine for hard combinatorial optimisation

Status: first evidence-constrained draft
Date: 2026-11-01

## Abstract

Fresh Solutions is a general hybrid metaheuristic engine extracted from a compiled-state landscape
optimisation architecture. A problem adapter supplies discrete variables, options, exact and batched
evaluation, feasibility, and reversible moves. The engine supplies exact resident state, exact CPU local
search, batched population search, a population-to-local handoff, and replayable checkpoints. We test the
transfer claim on eight public QAPLIB/TSPLIB instances with five seeds each. Runs use an explicit patience
stopping rule with a 500,000-evaluation cap; all 40 runs stopped on patience. Mean QAP gaps are 5.2–8.9%
and mean TSP gaps are 3.7–8.2% against public known values. All 40 assignments replay exactly. These are
converged transfer results, not claims of benchmark leadership.

## 1. Introduction

Forest planning architectures often rely on problem-specific state and evaluation. A generic solver
should preserve the useful parts of that architecture without importing forestry concepts: discrete
candidate options, exact incremental accounting, batched evaluation, reversible local moves, and replay.

This paper asks whether that architecture transfers to public combinatorial libraries. The contribution
is the adapter/engine boundary and the evidence discipline, not a universal performance claim.

## 2. Architecture

### 2.1 Adapter contract

A problem adapter exposes:

- variables and option counts;
- deterministic initial/random assignments and mutation/crossover;
- exact `evaluate` and `evaluate_batch`;
- reversible `Change`, `apply`, and `undo`;
- schedule serialization and replay metadata.

### 2.2 Engine

The engine contains:

- `ResidentAssignment`, the authoritative exact state;
- `run_local_search`, exact simulated annealing over adapter proposals;
- `BatchBackend` / `CpuBatchBackend`;
- `run_population_search`, tournament selection, elitism, mutation, crossover;
- `run_hybrid_search`, which seeds exact local refinement from the population elite;
- `SearchCheckpoint`, which serializes and replays an incumbent.

No core module imports WS4.

## 3. Benchmark adapters

### 3.1 Quadratic assignment

QAPLIB instances are parsed into flow and distance matrices. A solution is a permutation of facilities
over locations. Moves swap facilities; crossover uses order crossover; evaluation is the exact
flow-distance sum.

### 3.2 Travelling salesman

TSPLIB `EUC_2D`/`CEIL_2D` instances are parsed into distance matrices. A solution is a city permutation;
moves reverse a segment (2-opt), mutation reverses segments, and crossover is order crossover.

## 4. Method

Released engine: Fresh Solutions v0.2.0.

Configuration:

```text
population: 32
generations: 50
local iterations per round: 10,000
seeds: 1, 2, 3, 4, 5
stability: 3 rounds without >=0.01% relative improvement
budgets: 30 rounds / 500,000 evaluations
```

Every reported assignment is replayed through its adapter and checked against the recorded objective.

## 5. Converged results

Five-seed distributions after the patience stopping rule; all 40 runs converged on patience.

| Instance | Library | Size | Mean gap | Median gap | Worst gap | Mean evals | Mean wall |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| tai12a | QAPLIB | 12 | 8.897% | 8.039% | 11.616% | 31,635 | 1.10 s |
| tai20a | QAPLIB | 20 | 7.185% | 7.102% | 9.394% | 37,636 | 2.43 s |
| tai25a | QAPLIB | 25 | 5.249% | 5.980% | 6.174% | 41,636 | 4.10 s |
| tai30a | QAPLIB | 30 | 5.679% | 5.937% | 6.678% | 41,636 | 5.28 s |
| berlin52 | TSPLIB | 52 | 6.433% | 5.754% | 11.522% | 71,639 | 5.02 s |
| kroA100 | TSPLIB | 100 | 7.323% | 7.293% | 13.847% | 105,642 | 12.51 s |
| kroB100 | TSPLIB | 100 | 3.696% | 2.823% | 7.272% | 105,642 | 12.81 s |
| ch150 | TSPLIB | 150 | 8.229% | 8.517% | 10.463% | 171,649 | 29.35 s |

All 40 assignments replay exactly. TSP Or-opt plus the convergence protocol changed the prior pilot
picture materially: kroB100 is within 3.7% mean gap and ch150 is within 8.2% mean gap. QAP remains
limited by the swap neighborhood; tai12a is a local optimum at 7.397%.

## 6. Limitations

- Eight instances and five seeds; all stopped on patience, which is not a global-optimality proof.
- One configuration; no per-instance tuning.
- QAP tai12a remains trapped at a local optimum; QAP neighborhoods are swap-only.
- TSP 3-opt/Lin–Kernighan is still absent.
- TSP 2-opt is basic; ch150 shows the weakness. No Lin–Kernighan or advanced local search.
- QAP moves are swaps; no robust tabu or specialised QAP neighbourhood.
- `CpuBatchBackend` is exact but CPU-only; no production GPU kernel.
- The engine is a transfer prototype, not a claim of state-of-the-art performance.
- No job-shop or VRP adapter in this evidence pass.

## 7. Reproducibility

```bash
PYTHONPATH=fresh-solutions python paper2/run_public_benchmarks.py
PYTHONPATH=fresh-solutions python paper2/replay_public.py
```

Artifacts:

- `paper2/instances/` — pinned public instances and provenance.
- `paper2/evidence/converged.json` — 40 assignments, gaps, stop evidence.
- `paper2/evidence/converged-summary.json` — per-instance distributions.
- `fresh-solutions` — released engine v0.2.0.

## 8. Conclusion

The compiled-state/adapter architecture transfers to public QAP and TSP instances with exact replay and
modest, honest quality on a first pass. The next step is a multi-seed, multi-instance campaign and
specialised neighbourhoods, not a claim of leadership from four runs.
