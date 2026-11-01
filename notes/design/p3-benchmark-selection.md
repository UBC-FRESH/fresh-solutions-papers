# P3 first benchmark selection

Status: decision
Date: 2026-11-01

## Decision

The first executable public comparison target is **FHOPS**, not Lockwood and Moore (1993).

## Why

- Lockwood and Moore is bibliographically verified (`10.1139/x93-065`), but its original instance has not
  been located. It remains a **reconstructable candidate**, not a usable public benchmark.
- FHOPS is public, MIT-licensed, has a documented benchmark/scenario harness, and is maintained in the
  UBC-FRESH organisation. It is a defensible reproducibility anchor.
- FHOPS is an operational harvest-planning stack, not a full landscape spatial harvest-scheduling model.
  The comparison must therefore state exactly which problem is being reproduced. It is not a like-for-like
  replacement for Lockwood until a spatial landscape adapter exists.

## Required before the first run

1. Pin the FHOPS commit/tag and install environment.
2. Identify the scenario ladder and objective/constraints.
3. Define the adapter or mapping to the Paper 1 benchmark schema.
4. Capture hardware/software provenance.
5. Produce a schema-valid record with an exact schedule hash and replay result.

## Deferred

Lockwood reconstruction remains P3 work only after the paper text/instance details are recovered. Do not
label a reconstructed instance as the original benchmark.
