# Compiled spatial optimisation: GPU-accelerated hybrid metaheuristics for landscape harvest scheduling

Status: **NOT SUBMISSION-READY — no independent model baseline**
Date: 2026-11-01

## Abstract

Spatially explicit forest planning models are difficult not because the objective is exotic, but because
the model, the exact accounting state, and the search move are usually rebuilt together. This paper
describes a compiled-state architecture that separates four concerns: a stable compiled model, compact
candidate and sparse effect indexes, exact resident accounting, and batched GPU population search paired
with exact CPU local refinement. We report a first replayable architecture record on a 208,255-block
TSA24 landscape: a 1,000-generation GPU search reduced the objective from an initial
1,722,144,291.336651 to 8,588,725.370498415 in 9.381 s of search time (23.13 s wall), with an exact CPU
replay of 8,588,725.370498514. A 10,000-generation run reaches 76,540.740733, and a
100,000-generation run reaches **517.8619818205188**, and a five-seed 100k campaign spans
**512.574–518.621** (mean 515.682, median 515.938), all with exact CPU replay. An independent
CPU simulated-annealing search, given a 30-minute and 100,000-iteration budget on the same model,
reaches 335,044,976.675 and is still time-limited. The frozen TSA24 build, target, and seed are published as a public benchmark artifact
(`ws4-tsa24-evenflow-v1`). The contribution is the architecture and its evidence contract, not a universal
speed claim.

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

The paper reports an initial evidence record, a same-engine scaling baseline, an independent CPU-SA
search baseline, and a reproducibility contract. The CPU-SA baseline is time-limited, not converged;
the paper does not claim equal-time dominance.

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
| ws4-tsa24-cpu-sa-100000-r7 | tsa24-evenflow-w100 | ws4-cpu-sa ws4@f23d450 | 335044976.675435 | True | 1875.120 | 1875.120 |
| ws4-tsa24-gpu-ga-1000-r7 | tsa24-evenflow-w100 | ws4-gpu-ga ws4-gpu@f60ce64 | 8588725.370498 | True | 23.130 | 9.381 |
| ws4-tsa24-gpu-ga-10000-r7 | tsa24-evenflow-w100 | ws4-gpu-ga ws4-gpu@f60ce64 | 76540.740733 | True | 157.338 | 89.782 |
| ws4-tsa24-gpu-ga-100000-r1 | tsa24-evenflow-w100 | ws4-gpu-ga ws4-gpu@f60ce64 | 518.621452 | True | 804.004 | 781.565 |
| ws4-tsa24-gpu-ga-100000-r2 | tsa24-evenflow-w100 | ws4-gpu-ga ws4-gpu@f60ce64 | 512.574139 | True | 799.646 | 775.680 |
| ws4-tsa24-gpu-ga-100000-r3 | tsa24-evenflow-w100 | ws4-gpu-ga ws4-gpu@f60ce64 | 515.937717 | True | 797.826 | 776.739 |
| ws4-tsa24-gpu-ga-100000-r4 | tsa24-evenflow-w100 | ws4-gpu-ga ws4-gpu@f60ce64 | 514.745965 | True | 796.314 | 775.082 |
| ws4-tsa24-gpu-ga-100000-r5 | tsa24-evenflow-w100 | ws4-gpu-ga ws4-gpu@f60ce64 | 516.530106 | True | 798.116 | 776.468 |
| ws4-tsa24-gpu-ga-100000-r7 | tsa24-evenflow-w100 | ws4-gpu-ga ws4-gpu@f60ce64 | 517.861982 | True | 941.510 | 856.096 |

### 4.2 WS4 TSA24 architecture record and scaling baseline

- 208,255 blocks; 20 accounting periods.
- GPU-GA population 64, seed 7.
- 1,000 generations: objective **8,588,725.370498415**; exact CPU replay
  **8,588,725.370498514**; search 9.381 s; wall 23.13 s.
- 10,000 generations: objective **76,540.74073269201**; exact CPU replay
  **76,540.74073269201**; search 89.78 s; wall 157.34 s; max RSS 8,256 MB.
- 100,000 generations, seed 7: objective **517.8619818205188**; exact CPU replay
  **517.8619818205188**; search 856.10 s; wall 941.51 s; max RSS 8,260 MB.
- 100,000 generations, seeds 1–5: objectives **512.574, 515.938, 514.746, 516.530, 518.621**;
  mean **515.682**, median **515.938**, worst **518.621**; all exact replay.
- The five-seed campaign took **4,004.77 s** wall for all five runs.
- All schedules are schema-valid, hash-verified, and exactly replayed.
- Two independent 10,000-generation processes produced the identical schedule SHA-256.
- Initial oldest-first seed objective: 1,722,144,291.336651.

The 100,000-generation run is **3.3 million times** lower in objective than the initial seed and
**16,600 times** lower than the 1,000-generation run. The 10,000-generation result was a
same-engine scaling baseline; the 100,000-generation result is the accelerated-solver headline. This
is still not an independent model or public-landscape baseline.

### 4.3 Independent CPU-SA search baseline

The CPU simulated-annealing engine was run on the same frozen TSA24 model, target, initial seed, and
seed 7, with 100,000 iterations and a 30-minute cap.

- Algorithm: WS4 CPU-SA (`ws4@f23d450`), 32 threads.
- Objective: **335,044,976.675435**.
- Exact replay: **335,044,976.675435**.
- Wall: 1,875.12 s; memory: 8,969 MB.
- Stop: 30-minute time limit reached; **not converged**.

This is an independent search on the same model. It is not an independent model, and it is not an
equal-time comparison: the GPU-GA 100,000-generation run took 941.51 s and reached 517.86, while
the CPU-SA baseline spent 1,875 s and reached 335,044,976.68. The GPU path is orders of magnitude
stronger despite a shorter wall budget. That is evidence for the architecture, but the CPU-SA
parameters and convergence were not tuned to the same standard; it is not a universal dominance
proof.

### 4.4 FHOPS public baselines

Two FHOPS operational-planning baselines are replayable:

- tiny7: objective 4,295.774752, exact replay, hard violations 0;
- small21: objective 15,508.884819999994, exact replay, hard violations 0.

FHOPS models machine/block/day/shift operations, not multi-period landscape harvest scheduling. A direct
WS4/FHOPS comparison is rejected as a problem-contract mismatch.

## 5. Limitations

1. TSA24 is a public frozen artifact derived from public data, not an official benchmark with an independent model.
2. The 100,000-generation GPU run is near-zero objective but is not proven globally optimal.
3. Time-to-first-feasible was not separately instrumented; search elapsed is used conservatively.
4. The CPU-SA baseline is time-limited, not converged; there is no independent optimized model baseline.
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
keeping the GPU path fast: 100,000 generations reach 517.86 on the full instance in 941.51 s wall.
The CPU-SA baseline is much worse despite a larger wall budget. The next milestone is an independent model comparison on the public frozen
artifact.

## References to verify before submission

- Lockwood, C. & Moore, T. (1993). Harvest scheduling with spatial constraints: a simulated annealing
  approach. *Canadian Journal of Forest Research* 23: 468–478. DOI: 10.1139/x93-065.
- Boston, K. & Bettinger, P. (2002). Combining tabu search and genetic algorithm heuristic techniques to
  solve spatial harvest scheduling problems. *Forest Science* 48: 35–46.
- Bettinger, P., Graetz, D., Sessions, J., et al. (2002). Eight heuristic planning techniques applied to
  three increasingly difficult wildlife planning problems. *Silva Fennica* 36.
- Paradis, G. (2026). FHOPS: a reproducible optimisation and benchmarking stack for forest harvest
  operations. *SoftwareX* 36 (verify DOI and publication details).
