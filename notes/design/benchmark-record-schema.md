# Benchmark record schema

Status: frozen for P1
Date: 2026-11-01
Schema: `schemas/benchmark-record.schema.json`

## Rule

No benchmark claim is reported unless there is a record that a third party can replay. A record carries
the problem, the instance, the objective, the algorithm, the run environment, timing, and an exact
verification result.

## Required fields

- `source`: citation, DOI, URL.
- `instance`: identifier, availability status, license, variables, periods, options.
- `problem`: objective, constraints, feasibility definition.
- `algorithm`: name, version, config, deterministic flag.
- `run`: seed, hardware, software, time to first feasible, time to best, wall time, memory.
- `result`: objective, feasibility, schedule hash/path, exact replay flag, per-target residuals.

## Availability vocabulary

- `public`: data/code and license permit direct use.
- `reconstructable`: enough detail to rebuild, but not the original instance.
- `abstract-only`: no usable instance or objective details.
- `unusable`: no defensible comparison.

## Comparison protocol

1. Reproduce or reconstruct the objective and constraints first.
2. Report model-build, cache-load, time-to-first-feasible, time-to-best, and steady-state separately.
3. Use equal feasibility tolerances and account definitions.
4. Do not compare a heuristic to a MIP optimum without the gap and time limit.
5. Replay the reported schedule exactly and publish its hash.

## Timing vocabulary

- **time to first feasible**: first schedule satisfying the hard rules.
- **time to best**: first arrival at the reported objective.
- **wall**: process wall clock, including setup.
- **search**: optimizer loop only.
- **cache load**: table/candidate/state load.
- **preprocessing**: model construction before search.

This distinction is mandatory because the architecture's cache and launch costs are part of the
production story, not an implementation detail.
