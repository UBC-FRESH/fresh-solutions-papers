# Maintenance and benchmark cadence

Status: P6.4
Date: 2026-11-01

## Cadence

- **Every release:** rerun `paper2/run_public_benchmarks.py`, regenerate `paper2/evidence/public.json`, and replay every assignment.
- **Every release:** rerun the paper1 evidence validator and table generator.
- **Quarterly:** review open adapters, dependency updates, and whether a benchmark instance has been
  superseded or withdrawn.
- **On adapter change:** record the prior and new objective, config, and seed; do not silently replace
  historical evidence.
- **On cache/model change:** invalidate the affected effect/state cache and record the reason.

## Non-negotiable gate

A benchmark claim without a replayable assignment, config, and source instance is not accepted.
