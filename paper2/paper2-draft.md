# Fresh Solutions: a compiled-state hybrid metaheuristic engine for hard combinatorial optimisation

Status: first evidence-constrained draft
Date: 2026-11-01

## Abstract

Fresh Solutions is a general hybrid metaheuristic engine extracted from a compiled-state landscape
optimisation architecture. A problem adapter supplies discrete variables, options, exact and batched
evaluation, feasibility, and reversible moves. The engine supplies exact resident state, exact CPU local
search, batched population search, a population-to-local handoff, and replayable checkpoints. We test the
transfer claim on eight public QAPLIB/TSPLIB instances with five seeds each. These are pilot runs under a
10,000-local-iteration budget, not converged benchmark results. The QAP runs plateau at a local optimum
under the swap neighborhood; the TSP 2-opt runs improve substantially with larger budgets. All 40 reported
assignments replay exactly. These are transfer smoke tests, not claims of benchmark leadership or
converged quality.

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
local iterations: 10,000
seeds: 1, 2, 3, 4, 5
```

Every reported assignment is replayed through its adapter and checked against the recorded objective.

## 5. Pilot transfer smoke test

**Not a converged benchmark.** Five-seed distributions at a 10,000-local-iteration budget; gaps are
relative to QAPLIB/TSPLIB known values. A convergence audit shows tai12a is stuck at a local optimum and
ch150 improves from 61.6% to 12.2% with 100k iterations.

| Instance | Library | Size | Mean gap | Median gap | Worst gap | Mean wall |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| tai12a | QAPLIB | 12 | 8.897% | 8.039% | 11.616% | 0.360 s |
| tai20a | QAPLIB | 20 | 7.185% | 7.102% | 9.394% | 0.734 s |
| tai25a | QAPLIB | 25 | 5.249% | 5.980% | 6.174% | 1.038 s |
| tai30a | QAPLIB | 30 | 5.679% | 5.937% | 6.678% | 1.359 s |
| berlin52 | TSPLIB | 52 | 10.196% | 11.058% | 14.956% | 0.611 s |
| kroA100 | TSPLIB | 100 | 21.490% | 21.958% | 29.997% | 1.095 s |
| kroB100 | TSPLIB | 100 | 17.108% | 17.325% | 20.004% | 1.094 s |
| ch150 | TSPLIB | 150 | 56.259% | 56.173% | 61.612% | 1.591 s |

All 40 assignments replay exactly. These numbers are not convergence evidence; see
`notes/reports/p8-convergence-audit.md`. The 2-opt change improved berlin52 over the v0.1.0 swap-only
result, but the 10k budget is insufficient for the TSP instances.

## 6. Limitations

- Eight instances and five seeds, but the runs are not converged.
- One configuration; no per-instance tuning or convergence stopping rule.
- tai12a is trapped at a local optimum; ch150 needs at least ~100k local iterations before its plateau.
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
- `paper2/evidence/multiseed.json` — 40 assignments and per-run gaps.
- `paper2/evidence/multiseed-summary.json` — per-instance distributions.
- `fresh-solutions` — released engine v0.2.0.

## 8. Conclusion

The compiled-state/adapter architecture transfers to public QAP and TSP instances with exact replay and
modest, honest quality on a first pass. The next step is a multi-seed, multi-instance campaign and
specialised neighbourhoods, not a claim of leadership from four runs.
