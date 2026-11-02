# TSA24 public benchmark artifact

Status: published
Date: 2026-11-02
Release: https://github.com/UBC-FRESH/femic-tsa24-instance/releases/tag/ws4-tsa24-evenflow-v1

## Contents

- Frozen WS4 compiled dataset (`compiled/`, 12 Parquet tables).
- Even-flow target (`evenflow_tsa24.yaml`).
- Initial feasible schedule (`seed_oldest_first_tsa24.csv`).
- README and SHA-256 manifest.
- Compressed artifact size: 4.5 MB.

## Provenance

The artifact is derived from the public UBC-FRESH TSA24 instance and public BC
VRI 2025, FADM boundaries, and SiteProd data. Source data retains BC government
licences; the artifact is a derived benchmark bundle, not a redistribution of the
raw source layers.

## Boundary

- The GPU effect table and caches are not included because of size; rebuild them
  with WS4 GPU tooling.
- This makes the benchmark artifact public. It does not create an independent
  model baseline.
- The paper can now say “public frozen artifact,” not “local reconstructable
  fixture.”
