# Two-paper programme

Status: planning
Date: 2026-11-01

## Thesis

The transferable contribution is a **compiled spatial optimisation architecture**, not a claim that one
solver is universally faster:

1. compile the model into a stable sparse representation;
2. maintain exact resident accounting state and compact candidate/effect indexes;
3. run exact local CPU moves and batched GPU population evaluation;
4. express objectives as weighted goal programming with inspectable aspirations;
5. replay every elite schedule against the exact evaluator.

GPU throughput is the visible effect. The architecture is the claimed cause.

## Paper 1: compiled spatial optimisation

Working title: **Compiled spatial optimisation: GPU-accelerated hybrid metaheuristics for landscape
harvest scheduling**.

### Contributions

- The architecture pattern and its data contracts.
- Exact resident state plus batched GPU effect evaluation.
- Hybrid global/local search with exact replay.
- A benchmark programme that reproduces or reconstructs published spatially explicit harvest-scheduling
  results.
- A reproducible evidence schema: instance, objective, feasible schedule, hardware, seed, time to first
  feasible, time to best, and exact replay.

### Benchmark lanes

- **Historical heuristic anchors:** Lockwood and Moore (1993); Boston and Bettinger (2002); Bettinger et
  al. (2002); Bachmatiuk et al. (2015); McDill et al. (2002); Dong et al. (2015).
- **Exact/upper-bound lane:** Goycoolea et al. (2005) and related area-restriction exact models.
- **Reproducible stack lane:** FHOPS, if its paper, code, license, and instance versions are usable.
- **Conservation/prioritisation lane:** Martin Conservation Decisions Lab, Carwardine et al. (2015),
  Gopalakrishna et al. (2024), Marxan, Zonation. These are transfer tests unless the problem is a true
  temporal harvest-scheduling analogue.

### Fairness rules

- Reproduce the published objective and constraints before claiming a win.
- Report model build, cache load, time to first feasible, time to best, and steady-state separately.
- Use equal objectives, feasibility tolerances, and account definitions.
- Never compare a heuristic to a MIP optimum without the gap and time limit.
- Every reported schedule must replay exactly.

## Paper 2: Fresh Solutions

Working title: **Fresh Solutions: a compiled-state hybrid metaheuristic engine for hard combinatorial
optimisation**.

The second paper tests whether the architecture transfers. `fresh-solutions` supplies the generic
adapter API; the papers project supplies evidence and writing.

### Adapter boundary

- decision variables and discrete domains;
- compact candidate/option representation;
- exact and batched objective evaluation;
- feasibility and repair rules;
- neighbourhood/move operators;
- optional graph/spatial structure.

### Benchmark lanes

- quadratic assignment;
- graph colouring;
- job-shop scheduling;
- vehicle routing;
- set covering/facility location;
- SAT/MaxSAT;
- selected MIPLIB instances where a heuristic comparison is meaningful.

## Publication strategy

1. Architecture paper first, with forestry benchmark evidence.
2. General solver paper second, after the adapter API and benchmark suite stabilise.
3. Keep instances, configs, seeds, schedules, and logs public and replayable.

## Honest risks

- Historical instances may not exist and reconstructions may not be comparable.
- Hardware generations can manufacture wall-clock wins; report time-to-quality and provenance.
- Effect-table geometry is not stable under model changes; cache invalidation is production work.
- Dense global coupling may not benefit from the architecture.
- Weighted goal programming is not a feasibility proof; report every target residual.
- A fast objective on an infeasible schedule is not a result.

## Immediate tasks

1. Freeze the benchmark record schema before collecting results.
2. Verify the Lockwood and Moore citation and instance availability.
3. Find the FHOPS paper, repository, license, and instance version.
4. Build the literature/availability matrix in `notes/reference/benchmark-corpus.md`.
5. Keep TSA24 even-flow tuning as a case study until its target set is frozen and replayed.
