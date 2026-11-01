# Fresh Solutions: a compiled-state hybrid metaheuristic engine for hard combinatorial optimisation

Status: first evidence-constrained draft
Date: 2026-11-01

## Abstract

Fresh Solutions is a general hybrid metaheuristic engine extracted from a compiled-state landscape
optimisation architecture. A problem adapter supplies discrete variables, options, exact and batched
evaluation, feasibility, and reversible moves. The engine supplies exact resident state, exact CPU local
search, batched population search, a population-to-local handoff, and replayable checkpoints. We test the
transfer claim on four public QAPLIB/TSPLIB instances. The QAP results are within 7.4–7.6% of the known
optima on 12- and 20-facility instances; the 2-opt TSP results are within 15.0% and 23.0% on 52- and
100-city instances. All reported assignments replay exactly. These are first-pass transfer results, not
claims of benchmark leadership.

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
seed: 3
```

Every reported assignment is replayed through its adapter and checked against the recorded objective.

## 5. Results

| Instance | Library | Size | Objective | Optimum | Gap | Wall |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| tai12a | QAPLIB | 12 | 241,016 | 224,416 | 7.397% | 0.351 s |
| tai20a | QAPLIB | 20 | 757,090 | 703,482 | 7.620% | 0.746 s |
| berlin52 | TSPLIB | 52 | 8,670 | 7,542 | 14.956% | 0.571 s |
| kroA100 | TSPLIB | 100 | 26,180 | 21,282 | 23.015% | 1.126 s |

All four assignments replay exactly. The TSP improvement from swap-only to 2-opt changed berlin52 from
17,216 (128.268% gap) to 8,670 (14.956% gap) under the reported configuration.

## 6. Limitations

- Four instances only; no full QAPLIB/TSPLIB campaign.
- One seed and one configuration; no variance study.
- TSP 2-opt is basic; no Lin–Kernighan or advanced local search.
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
- `paper2/evidence/public.json` — assignments, configs, objectives, gaps, wall times.
- `fresh-solutions` — released engine v0.2.0.

## 8. Conclusion

The compiled-state/adapter architecture transfers to public QAP and TSP instances with exact replay and
modest, honest quality on a first pass. The next step is a multi-seed, multi-instance campaign and
specialised neighbourhoods, not a claim of leadership from four runs.
