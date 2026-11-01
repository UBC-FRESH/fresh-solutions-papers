# Benchmark adapter contract

Status: P2 design contract
Date: 2026-11-01
Related: `compiled-state-architecture.md`, `benchmark-record-schema.md`,
`fresh-solutions/notes/design/architecture.md`

## Purpose

A benchmark result is only comparable if the problem, instance, objective, feasibility rule, and
schedule are explicit. The adapter is the boundary between the published problem and the solver.

## Required adapter surface

### Instance identity

- `instance_id`: stable identifier.
- `source`: citation, DOI, URL.
- `availability`: `public`, `reconstructable`, `abstract-only`, or `unusable`.
- `license`: data/code licence, or `null`.
- `provenance`: how the instance was obtained or reconstructed.

### Decision representation

- `variable_count`: number of discrete decision variables.
- `option_count(variable)`: number of options.
- `option_at(variable, option)`: option value for display/serialization.
- `initial_assignment()`: complete starting assignment.
- `assignment_from_schedule(path)`: parse a published or solver schedule.
- `schedule_from_assignment(assignment)`: write the canonical schedule CSV.

### Evaluation

- `evaluate(assignment)`: exact objective and hard feasibility.
- `evaluate_batch(assignments)`: exact batch path, or a documented fallback.
- `target_cells()`: target-cell index used by the sparse table.
- `objective_terms(assignment)`: per-target residual penalties for the evidence record.

### State and moves

- `initial_state()`: resident exact state.
- `apply(state, change)`: apply one reversible change.
- `undo(state, change)`: restore it exactly.
- `propose(state, rng)`: propose one valid move.
- `resident_state_hash(state)`: hash for state round-trip tests.

### Replay

- `replay(schedule)`: exact evaluation from serialized schedule.
- `feasible(assignment)`: hard-rule check.
- `schedule_sha256(path)`: canonical hash.

## Mapping to Fresh Solutions

`fresh_solutions.contracts.ProblemAdapter` is the solver-facing subset. The benchmark adapter adds
provenance, schedule serialization, and target residuals. A generic benchmark runner must not require
the solver to know about a paper.

## Evidence rules

A valid benchmark record must have:

- an adapter name/version;
- an instance availability status;
- an objective and feasibility definition;
- a schedule path and SHA-256;
- timing decomposed into model build, cache load, time-to-first-feasible, time-to-best, and wall;
- exact replay true;
- per-target residuals, not only a scalar objective.

## Adapter acceptance tests

1. `assignment_from_schedule(schedule_from_assignment(a)) == a`.
2. `undo(apply(state, change), change)` restores the exact state hash.
3. `evaluate_batch([a])[0] == evaluate(a)` or the fallback is explicit.
4. A record generated from the adapter validates against the benchmark schema.
5. Feasibility is checked separately from weighted target residuals.

## Open decisions

- Whether schedule serialization is CSV or a canonical JSON array.
- Whether target residuals are returned by the adapter or recomputed by the harness.
- How the harness represents a schedule whose chains are absent from the candidate list.
