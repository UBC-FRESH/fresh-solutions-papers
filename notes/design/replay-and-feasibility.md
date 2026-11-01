# Exact replay and feasibility checks

Status: P2 design contract
Date: 2026-11-01
Related: `benchmark-record-schema.md`, `benchmark-adapter-contract.md`

## Rule

A benchmark result exists only when its schedule replays exactly. `exact_replay: true` is a gate; a
record with `false` is evidence of a problem, not a result.

## Replay procedure

1. Parse the record against `schemas/benchmark-record.schema.json`.
2. Resolve the instance and adapter by name/version.
3. Load the schedule from `result.schedule_path`.
4. Check the schedule file SHA-256 against `result.schedule_sha256`.
5. Validate every block/variable exists and every treatment/offset is valid for the instance.
6. Re-evaluate with the exact evaluator.
7. Compare objective and per-target residuals with the record.
8. Check hard feasibility independently from weighted residuals.
9. Check timing provenance and required metadata.

## Tolerances

- Objective comparison: absolute `1e-6` or relative `1e-9`, whichever is tighter for the problem, and
  recorded in the record.
- Per-target residuals: same tolerance as the objective.
- Hard feasibility: **no tolerance**. A violated opening, adjacency, or other hard rule fails the replay.
- Floating-point totals must be compared as floats, not formatted strings.

## Feasibility versus goal performance

Weighted goal programming does not make every target a hard constraint. Replay must distinguish:

- **hard feasibility**: opening size, green-up, adjacency, locked assignments, legal treatment;
- **goal residuals**: aspiration shortfall/excess, flow-band penalty, stock penalty.

A schedule can be feasible and still have large target residuals. A schedule can have zero residuals and
still violate a hard rule. The record must report both.

## Failure handling

- A missing schedule file fails replay.
- A hash mismatch fails replay.
- A different objective definition fails the benchmark; it is not “close enough.”
- A different feasibility rule is a different instance.
- A reconstructed instance is labelled as reconstructed; it is not inserted into the original paper's
  row without that label.

## Harness requirements

The benchmark harness must emit:

- exact evaluator version and commit;
- solver version and commit;
- adapter version;
- dataset fingerprint;
- config hash;
- seed;
- schedule path and SHA-256;
- time decomposition;
- per-target residuals;
- replay status.

The harness must not write `exact_replay: true` from a cached scalar alone. It must replay the serialized
schedule through the exact evaluator.
