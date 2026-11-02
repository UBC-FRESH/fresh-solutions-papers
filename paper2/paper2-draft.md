# Fresh Solutions: a reproducible adapter framework for applied metaheuristics

Status: **INTERNAL DRAFT — NOT SUBMISSION-READY**
Date: 2026-11-02

## Abstract

Applying metaheuristics to hard combinatorial problems is often slowed less by the
choice of metaheuristic than by the engineering around it: problem-specific move
representations, exact incremental state, replayable evidence, stopping rules, and
benchmark bookkeeping are usually rebuilt for each project. Fresh Solutions is an
adapter-based framework that separates those concerns from the search engine. We
describe the architecture and evaluate it on QAPLIB and TSPLIB. The evidence is
deliberately mixed: small and medium instances are strong, while large instances
expose the limits of the current internal neighbourhoods. QAP robust tabu reaches
a median gap of 0% on the converged subset; iterated Lin–Kernighan reaches a median
gap of 0% on the converged TSP subset; external LKH remains substantially stronger
on large TSP. We argue that the framework's contribution is reproducible,
adapter-level application of known-good methods, not a universal state-of-the-art
solver claim.

## 1. Introduction

Operations-research practitioners rarely need a new metaheuristic. They need a
reliable way to apply known methods to a new problem, preserve exact feasibility
and objective accounting, and produce evidence that another person can replay.
That work is repetitive and easy to get subtly wrong.

Fresh Solutions is a response to that engineering problem. The framework provides:

- a problem-adapter contract;
- exact resident state and reversible moves;
- local, population, and hybrid search paths;
- checkpointing and exact replay;
- convergence and benchmark records;
- public-library adapters for QAP, TSP, and graph colouring.

The benchmark programme asks a narrow question: can a user add a problem-specific
neighbourhood and obtain credible, replayable evidence without rebuilding the
surrounding machinery? It does not claim that one move set dominates the
literature.

## 2. Architecture

### 2.1 Adapter boundary

An adapter supplies variables, options, exact and batch evaluation, feasibility,
mutation/crossover, and reversible moves. The engine sees only this interface.
A domain-specific method can be added as a module without changing the core.

### 2.2 Exact state and replay

Every reported incumbent is a complete assignment. Evaluation is exact, and the
stored assignment must re-evaluate to the stored objective. The benchmark scripts
therefore do not trust the optimizer's internal counter; they replay the result
through the adapter.

### 2.3 Search layers

The framework exposes three layers:

1. exact local search;
2. population search with crossover, mutation, and elitism;
3. a hybrid handoff from a population elite to exact local refinement.

The experiments below use the local layer plus adapter-specific neighbourhoods;
the population layer remains available but is not the source of the strongest
results.

### 2.4 Evidence protocol

A result is reportable only when it names:

- the pinned solver version or commit;
- the public instance and known/best-known value;
- the seed and budget;
- the stopping reason;
- the exact-replay result;
- the wall time and hardware context.

For publication-facing campaigns we use a patience rule: stop after a declared
number of iterations or kicks without a new best. Safety caps are recorded as
**cap hits**, not as convergence.

## 3. QAP evidence

### 3.1 Robust tabu

The QAP adapter uses robust tabu search over facility swaps, exact O(n) swap
deltas in the reference path, and Taillard delta-matrix updates for symmetric
instances. The accelerated path is optional and exposed through an optional
fast extra.

Five-seed certified results on the initial QAPLIB panel:

| Instance | Certified budget | Mean gap | Worst gap |
| --- | ---: | ---: | ---: |
| tai12a | 10,000 | 0.000% | 0.000% |
| tai20a | 10,000 | 0.403% | 0.470% |
| tai25a | 20,000 | 0.685% | 0.850% |
| tai30a | 40,000 | 0.407% | 0.678% |

The certified budget is the smallest budget whose next doubling improves the
five-seed mean by no more than 0.10 percentage points. This is a stability rule,
not a convergence proof.

### 3.2 Broad QAP panel

Across 134 parseable QAPLIB instances and five seeds, 552/670 runs stopped on
patience; 318 runs hit the known optimum. The converged subset has median gap
0.000% and mean 1.823%, with a worst case of 36.4%. The mean is pulled by a small
number of hard outliers; the median is not evidence that the tail is solved.

Large-QAP multi-start results (`n > 100`, five random starts, no time cap, all
runs stopped on patience):

| Instance | Best gap | Mean gap |
| --- | ---: | ---: |
| esc128 | 0.000% | 1.250% |
| tai150b | 2.008% | 2.976% |
| tai256c | 0.350% | 0.413% |
| tho150 | 0.166% | 0.507% |

This is a portfolio improvement over identity-start tabu. SciPy FAQ is an
independent external baseline on the same instances. It wins on `tai150b`
(1.861% vs 2.008%), but Fresh tabu wins on `esc128` (0.000% vs 12.500%),
`tai256c` (0.350% vs 120.481%), and `tho150` (0.166% vs 1.523%). The result is
mixed, not universal dominance.

## 4. TSP evidence

### 4.1 Or-opt and iterated Lin–Kernighan

The TSP adapter provides 2-opt and Or-opt moves. A separate iterated
Lin–Kernighan module implements candidate-list sequential edge exchange and
deterministic double-bridge kicks.

From converged Or-opt starts, five seeds give:

| Instance | Or-opt mean gap | ILK mean gap | ILK worst gap |
| --- | ---: | ---: | ---: |
| berlin52 | 6.433% | 0.000% | 0.000% |
| kroA100 | 7.323% | 0.000% | 0.000% |
| kroB100 | 3.696% | 0.000% | 0.000% |
| ch150 | 8.229% | 0.383% | 0.475% |

A kicks ablation isolates the contribution: LK-only means 0.780–2.580%, ILK-5
means 0.000–0.558%, and ILK-20 means 0.000–0.383%. The result is
quality-at-additional-cost; it is not an equal-budget ablation.

### 4.2 Broad TSP panel and the LKH boundary

Across 78 TSPLIB instances with `n <= 1000`, 236/390 runs stopped on patience;
183 hit the known optimum. The converged subset has median gap 0.000% and mean
0.100%. The large-instance tail is weak: only 3/100 runs above `n=300` reached
patience, and 97 hit the safety cap.

External LKH on the same large tail reaches 71/100 optima, mean gap 0.092%,
median 0%, worst 1.930%, at 4.88 s mean wall. LKH is optional external
research-use software, not bundled and not claimed as Fresh Solutions' own
heuristic.

The honest conclusion is that the internal TSP path is a small/medium solver;
large-TSP quality currently depends on LKH.

## 5. Applied case

TSA24/Prince George is a public-data applied case. The frozen build, target, and
seed are published as `ws4-tsa24-evenflow-v1` in
`https://github.com/UBC-FRESH/femic-tsa24-instance`, derived from public BC VRI,
FADM, and SiteProd data. The even-flow target is a WS4 scenario configuration,
not an official TSA decision.

The 1,000-generation GPU-GA record has objective 8,588,725.370498; the
10,000-generation same-engine baseline has 76,540.740733; the 100,000-generation
five-seed campaign spans **512.574–518.621** (mean 515.682), with exact replay.
The CPU-SA independent-search baseline is 335,044,976.675435 and is
time-limited, not converged. No partner-impact claim is made.

## 6. Limitations

1. The internal TSP path does not scale to the large TSPLIB tail.
2. Large-QAP has only a mixed SciPy FAQ independent baseline; it does not establish state-of-the-art performance.
3. The QAP converged mean is pulled by a heavy tail; median alone is insufficient.
4. The applied case is public-data, not partner-endorsed operational impact.
5. Population/hybrid search is implemented but not the source of the strongest
   benchmark results.
6. Patience is a plateau rule, not global optimality.
7. LKH is optional and external; it must not be presented as part of the
   Apache-licensed package.

## 7. Conclusion

Fresh Solutions makes the application of known metaheuristic principles
reproducible through a stable adapter boundary, exact replay, convergence
records, and public benchmark evidence. It is useful today for small and medium
QAP/TSP work and for building applied cases. It is not yet a universal
large-instance solver, and the paper should say so.
