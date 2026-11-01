# Compiled spatial optimisation: GPU-accelerated hybrid metaheuristics for landscape harvest scheduling

Status: **NOT SUBMISSION-READY — no matched optimized landscape baseline**
Date: 2026-11-01

## Abstract

Spatially explicit forest planning models are difficult not because the objective is exotic, but because
the model, the exact accounting state, and the search move are usually rebuilt together. This paper
describes a compiled-state architecture that separates four concerns: a stable compiled model, compact
candidate and sparse effect indexes, exact resident accounting, and batched GPU population search paired
with exact CPU local refinement. We report a first replayable architecture record on a 208,255-block
TSA24 landscape: a 1,000-generation GPU search reduced the objective from an initial
1,722,144,291.336651 to 8,588,725.370498415 in 9.381 s of search time (23.13 s wall), with an exact CPU
replay of 8,588,725.370498514. We also report two replayable public FHOPS baseline records. The
comparison is deliberately limited: the TSA24 instance is reconstructable, not public, and the seed
comparison is not a matched optimized baseline. The contribution is the architecture and its evidence
contract, not a universal speed claim.

## 1. Introduction

Landscape harvest scheduling combines a long horizon, spatial constraints, and non-linear objectives.
Heuristic search is common because exact formulations are difficult at operational scale. The usual
implementation couples model evaluation, state maintenance, and search moves, so every experiment pays
for rebuilding structures that are stable across moves.

This paper asks whether separating those concerns changes what is practical. The proposed architecture
has five layers:

1. a compiled model;
2. a compact candidate index;
3. a sparse effect table over target cells;
4. exact resident accounting state;
5. a hybrid search loop.

The paper reports an initial evidence record and a reproducibility contract. It does not claim a
controlled benchmark win; that requires a matched optimized baseline that this phase did not produce.

## 2. Architecture

### 2.1 Compiled model and candidate index

The model is compiled once into blocks/fragments, strata, tracks, treatments, transitions, curves,
features, products, and accounts. Candidate chains are stored in a stable order. The order is part of the
contract because effect rows and genome option indices refer to it.

### 2.2 Sparse effect table

Every `(block, chain)` pair has a sparse row over the target cells it can change. The table also stores
the empty-schedule base totals and block row starts. A lean table can omit the full row index; the
population uses row starts instead.

Cache identity is explicit:

```text
dataset fingerprint
+ candidate set and row order
+ target-cell geometry
+ horizon and period width
+ seed-only extra rows
+ table format version
```

Changing weights, priorities, normalization, minima/maxima, or a flow band is a pricing change, not a
table rebuild. This distinction is a production requirement, not a performance footnote.

### 2.3 Resident exact state

The exact state is `[period, block, account]`, with separate product-event rows. A move applies cached
block/option deltas to the changed rows and period totals. Undo restores the prior rows exactly. The
state is authoritative; it is not a search-only approximation.

### 2.4 Hybrid search

The GPU population evaluates candidate-index genomes against the sparse table. The CPU path remains the
exact evaluator and local refinement path. The handoff is:

```text
GPU population -> elite schedule
               -> exact CPU state load
               -> exact local refinement
               -> exact replay
               -> refined elite as GPU seed
```

## 3. Evidence contract

Every reported record conforms to a machine-readable schema and carries:

- source citation, DOI/URL;
- instance identity, availability, and licence;
- objective, constraints, and feasibility definition;
- algorithm/version/config;
- seed, hardware, and software provenance;
- wall, cache-load, time-to-first-feasible, and time-to-best;
- schedule path and SHA-256;
- exact replay flag;
- per-target residuals.

A record with `exact_replay: false` is not evidence. The validator rejects missing schedules, hash
mismatches, and schema violations.

## 4. Results

### 4.1 Evidence table

The current records are generated from `evidence/*/record.json`:

<!-- evidence-table -->

| Record | Instance | Algorithm | Objective | Replay | Wall s | Best s |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| fhops-small21-sa-200-r42 | fhops-small21 | fhops-sa 1.1.0@135321b1f5a7 | 15508.884820 | True | 0.787 | 0.787 |
| fhops-tiny7-sa-200-r42 | fhops-tiny7 | fhops-sa 1.1.0@135321b1f5a7 | 4295.774752 | True | 0.269 | 0.269 |
| ws4-tsa24-gpu-ga-1000-r7 | tsa24-evenflow-w100 | ws4-gpu-ga ws4-gpu@f60ce64 | 8588725.370498 | True | 23.130 | 9.381 |

### 4.2 WS4 TSA24 architecture record

- 208,255 blocks; 20 accounting periods.
- GPU-GA population 64, 1,000 generations, seed 7.
- Initial oldest-first seed objective: 1,722,144,291.336651.
- GPU objective: 8,588,725.370498415.
- Exact CPU replay: 8,588,725.370498514.
- Search: 9.381 s. Wall: 23.13 s.
- Schedule SHA-256 verified; record schema-valid.

The seed-to-result improvement is large, but the seed is not an optimized control. It is a starting
point. The result is therefore an architecture record, not a comparative win.

### 4.3 FHOPS public baselines

Two FHOPS operational-planning baselines are replayable:

- tiny7: objective 4,295.774752, exact replay, hard violations 0;
- small21: objective 15,508.884819999994, exact replay, hard violations 0.

FHOPS models machine/block/day/shift operations, not multi-period landscape harvest scheduling. A direct
WS4/FHOPS comparison is rejected as a problem-contract mismatch.

## 5. Limitations

1. The TSA24 instance is a local reconstructable fixture, not a public benchmark.
2. The 1,000-generation GPU run is not a converged even-flow solution.
3. Time-to-first-feasible was not separately instrumented; search elapsed is used conservatively.
4. There is no matched optimized landscape baseline.
5. FHOPS baselines are not architecture comparisons.
6. The architecture is strongest for sparse local effects; dense global coupling is untested.
7. The effect-table cache invalidation contract is a design requirement, not yet a production service.

## 6. Reproducibility

- Benchmark records: `evidence/*/record.json`.
- Schedule hashes and replay scripts: alongside each record.
- Evidence validation: `python scripts/check_benchmark_record.py <record>`.
- Evidence table: `python scripts/build_evidence_tables.py`.
- Generic contracts: `fresh-solutions/` submodule.
- Architecture and adapter contracts: `notes/design/`.

## 7. Conclusion

A compiled-state architecture can make a 208,255-block landscape search exact and replayable while
keeping the GPU path fast enough to be interesting. The first record is strong enough to justify a
controlled benchmark programme, but not strong enough to claim a win. The next paper milestone is a
matched optimized baseline on a public or fully specified landscape instance.

## References to verify before submission

- Lockwood, C. & Moore, T. (1993). Harvest scheduling with spatial constraints: a simulated annealing
  approach. *Canadian Journal of Forest Research* 23: 468–478. DOI: 10.1139/x93-065.
- Boston, K. & Bettinger, P. (2002). Combining tabu search and genetic algorithm heuristic techniques to
  solve spatial harvest scheduling problems. *Forest Science* 48: 35–46.
- Bettinger, P., Graetz, D., Sessions, J., et al. (2002). Eight heuristic planning techniques applied to
  three increasingly difficult wildlife planning problems. *Silva Fennica* 36.
- Paradis, G. (2026). FHOPS: a reproducible optimisation and benchmarking stack for forest harvest
  operations. *SoftwareX* 36 (verify DOI and publication details).
