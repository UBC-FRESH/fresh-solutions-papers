# Paper 1 thesis and contribution freeze

Status: P4.1 freeze
Date: 2026-11-01

## Thesis

For large spatially explicit landscape planning models, a **compiled-state architecture** can pair
exact incremental accounting with batched GPU population search and exact CPU local refinement, while
keeping every reported result replayable.

The architecture is the contribution. The reported benchmark effects are evidence.

## Contributions

1. **Compiled model and candidate/effect representation.** The model is compiled once; candidate chains,
   target cells, sparse effect rows, and resident state are separate, stable layers.
2. **Exact resident state plus batched evaluation.** CPU state is authoritative; the GPU path prices
   candidate-index genomes against the sparse effect table.
3. **Hybrid search.** GPU population search supplies elites; exact CPU local refinement can polish them.
4. **Evidence contract.** Every record carries source, instance, objective, feasibility, algorithm,
   seed, provenance, timings, schedule hash, exact replay, and target residuals.
5. **Cache identity and invalidation contract.** Pricing changes and table rebuilds are separated
   explicitly.

## Evidence available

- FHOPS tiny7 SA baseline: replayable public operational-planning record.
- FHOPS small21 SA baseline: replayable public operational-planning record.
- WS4 TSA24 GPU-GA architecture record: 1,000 generations, objective 8,588,725.370498415, exact CPU
  replay 8,588,725.370498514, search 9.381 s, wall 23.13 s, 208,255 blocks.
- Initial TSA24 seed objective: 1,722,144,291.336651, about 200× worse than the 1,000-generation result.

## What the paper may claim

- The architecture is exact and replayable on the TSA24 record.
- The GPU path is fast relative to the starting seed in this record.
- The evidence schema makes the result auditable.
- FHOPS is a public reproducibility baseline for operational planning.
- The workforce/landscape distinction makes a direct FHOPS comparison inappropriate.

## What the paper must not claim

- A controlled win over an optimized landscape baseline; P3 did not produce one.
- A general speedup over all forestry solvers.
- That TSA24 is a public benchmark; it is a local reconstructable fixture.
- That the FHOPS operational results are an architecture comparison.
- That 1,000 GPU generations are a converged even-flow solution.

## Required limitation language

The paper must state that the TSA24 run is a first architecture record, time-to-first-feasible was not
separately instrumented, and the seed comparison is not a matched optimized baseline.

## Evidence gates

A claim enters the paper only if it points to a schema-valid record with exact replay and provenance.
