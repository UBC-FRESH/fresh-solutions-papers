# Compiled spatial optimisation: exact resident state and GPU population search for landscape harvest scheduling

Status: **WORKING MANUSCRIPT — sections 1–2 drafted; evidence sections pending**
Date: 2026-11-03

## Abstract

Spatially explicit forest planning models are difficult not because the objective is exotic, but
because the model, the exact accounting state, and the search move are usually rebuilt together. This
paper describes a compiled-state architecture that separates four concerns: a stable compiled model,
compact candidate and sparse effect indexes, exact resident accounting, and batched GPU population
search paired with exact CPU refinement. We evaluate the architecture on a public frozen TSA24
landscape with 208,255 operable blocks. A 1,000-generation GPU search reduces the weighted penalty
from 1,722,144,291.336651 to 8,588,725.370498 in 9.381 s of search time; a 100,000-generation,
five-seed campaign reaches 512.574–518.621 (mean 515.682) with exact CPU replay. The target uses
deliberately unattainable harvest-level aspirations to pull the solution toward the maximum even-flow
level; the final level is approximately 51.3–52.4M m³ per 10-year period against a 70M aspiration.
The frozen dataset, target, seed, and replay contract are public. We do not claim an independent model
comparison or a state-of-the-art landscape result; the contribution is the architecture and its
reproducibility contract.

## 1 Introduction

Forest planning models combine long planning horizons, spatially explicit treatment choices, and
objectives that mix timber production with ecological and operational constraints. At the scale of a
timber supply area, the decision is not a single harvest level but a schedule: which blocks receive
which treatments, in which periods, under which spatial and temporal rules. The combinatorial state is
large, the feasible set is structured, and the objective is usually a weighted compromise among
targets. The resulting models are hard for exact methods and expensive for generic heuristics.

A recurring engineering problem sits underneath the optimisation problem. A compiled forest model
contains blocks, fragments, strata, tracks, treatments, transitions, growth curves, products, and
accounting rules. A search move changes one small part of that model, but the implementation often
recomputes or reconstructs a much larger state to evaluate it. The model, the accounting state, and
the move are therefore rebuilt together. This coupling makes experiments slow, makes replay fragile,
and makes it difficult to separate the effect of a search method from the effect of an implementation
detail.

This paper asks a narrower question than “which metaheuristic is best for forest planning?” It asks
whether a compiled-state architecture can make a large landscape search exact, replayable, and fast
enough to support controlled experiments. The architecture has five layers:

1. a compiled model;
2. a compact candidate index;
3. a sparse effect table over target cells;
4. exact resident accounting state;
5. a hybrid search loop that combines batched GPU population search with exact CPU refinement.

The first two layers make the model cheap to query. The sparse table makes an evaluation proportional
to the cells a move touches rather than to the whole schedule. The resident state makes the objective
authoritative and reversible. The hybrid loop uses the GPU for breadth and the CPU for exact
accounting and local refinement.

We evaluate the architecture on a frozen TSA24/Prince George even-flow instance. The instance has
208,255 operable blocks out of 458,708 compiled blocks and a 20-period horizon. The target is a
weighted goal-programming construction: a dominant even-flow target defines the shape, while
deliberately unattainable harvest-level aspirations provide a persistent pull toward more volume.
The realized level is an outcome, not a declared feasible floor. This construction is intentional;
the 70M m³ per-period aspiration is not a hard constraint and the reported residual is not evidence
that the model is infeasible.

The paper makes three contributions:

- a compiled-state architecture that separates model, accounting, and search;
- an exact replay contract for a large landscape instance, including a public frozen artifact;
- a measured scaling record from 1,000 to 100,000 GPU generations, with five-seed evidence at the
  largest budget.

It does not make a competitive landscape claim. The CPU simulated-annealing comparison reported here
is a weak, untuned secondary comparator, and no independent harvest-scheduling model is available on
the same instance. Those limits are part of the result, not a footnote.

## 2 Related work

### 2.1 Spatial harvest scheduling

Spatial harvest scheduling has a long history in forest operations research. Lockwood and Moore
(1993) formulated harvest scheduling with spatial constraints and applied simulated annealing to a
problem in which adjacency and opening-size restrictions make the feasible set non-trivial. Their
work established a template that remains recognizable: represent a schedule as a set of treatment
decisions, define a penalty or objective over the resulting landscape, and use a stochastic search to
move between feasible or penalized states.

Boston and Bettinger (2002) compared tabu search and a genetic algorithm on spatial harvest
scheduling problems. Their comparison is important here because it treats the search method as an
experimental factor rather than as an implementation detail. Bettinger et al. (2002) extended the
comparison to eight heuristic planning techniques on three wildlife planning problems of increasing
difficulty. Together, these studies show that the choice of neighbourhood, the representation of the
schedule, and the handling of spatial constraints can matter as much as the name of the metaheuristic.

The present paper is not a replacement for those comparisons. It addresses the layer beneath them:
how the model state and objective are maintained while a search runs. The architecture is designed to
make that layer explicit, exact, and replayable, so that future comparisons can vary the search method
without rebuilding the model and accounting machinery.

### 2.2 Exact state and neighbourhood search

Metaheuristic implementations often trade exactness for speed. A move is evaluated by an approximate
delta, a cached value, or a full re-simulation; each choice changes what the search is actually
optimising. For forest planning, this is a material issue because the objective is a weighted
goal-programming penalty over multiple accounts and periods. An approximate evaluator can make a
schedule look better than it is, and a full re-simulation can make a controlled experiment
impractically slow.

The architecture described here keeps the exact objective as the authority. A move is priced by the
cells it changes, but the resident state is updated with the same accounting rules used by the full
evaluator. The search can therefore use a fast delta without giving up the exactness of the reported
incumbent. This is closest in spirit to the exact incremental evaluation used in move-based local
search, but it is applied to a compiled landscape model rather than to a generic permutation problem.

### 2.3 Reproducibility and software infrastructure

Reproducibility in applied optimisation is usually discussed at the level of random seeds and
reported objective values. That is necessary but not sufficient. A result also depends on the
compiled model, the candidate order, the effect table, the treatment definitions, the objective
weights, the hardware, and the replay procedure. If those are not part of the artifact, a reader
cannot tell whether a difference comes from the algorithm or from the data pipeline.

This paper treats the evidence record as part of the architecture. Each reported schedule is stored
with its objective, seed, configuration, hardware, and a hash. An exact replay loads the schedule
through the same model and evaluator, rather than trusting the search process that produced it. The
frozen TSA24 artifact and its rebuild recipe are published so that the GPU result is not a local
demonstration that cannot be inspected.

The related work on reproducible optimisation software is broad, and this paper does not attempt a
general survey. Its narrower claim is that an exact resident state plus an explicit artifact can make
a large landscape experiment auditable even when the search itself is stochastic.

## 3 Problem and model

This section will define the TSA24 instance, the block/treatment schedule, the even-flow and
level-aspiration targets, and the weighted goal-programming objective. It will state explicitly that
the 70M level target is an aspiration rather than a hard floor, and will document the public artifact
and its license.

## 4 Architecture

This section will describe the compiled model, candidate index, sparse effect table, resident exact
state, hybrid GPU/CPU search, and the replay contract.

## 5 Experimental design

This section will define the hardware, seeds, budgets, stopping rules, baselines, and metrics. The
CPU-SA baseline will be labelled as an untuned secondary comparator, not a controlled performance
proof.

## 6 Results

This section will report the 1k/10k/100k scaling curve, the five-seed 100k distribution, the
flow/level residual decomposition, the realized harvest profile, and the architecture ablation. It
will not describe the 517.86 penalty as “near zero.”

## 7 Discussion

This section will separate what the architecture makes possible from what the current evidence does
not establish: independent model performance, operational impact, and global optimality.

## 8 Limitations and conclusion

The TSA24 instance is a public frozen artifact, but there is no independent model baseline. The
100,000-generation result is a maximum even-flow compromise, not a proof of the exact maximum. The
CPU-SA comparator is weak and time-limited. The architecture is the contribution; the competitive
landscape claim remains open.

## References

Bettinger, P., Graetz, D., Sessions, J., et al. (2002). Eight heuristic planning techniques applied
to three increasingly difficult wildlife planning problems. *Silva Fennica* 36.
https://doi.org/10.14214/sf.545

Boston, K., and Bettinger, P. (2002). Combining tabu search and genetic algorithm heuristic techniques
to solve spatial harvest scheduling problems. *Forest Science* 48(1), 35–46.
https://doi.org/10.1093/forestscience/48.1.35

Lockwood, C., and Moore, T. (1993). Harvest scheduling with spatial constraints: a simulated
annealing approach. *Canadian Journal of Forest Research* 23, 468–478.
https://doi.org/10.1139/x93-065
