# Paper 1 evidence artifact v0.1.0

Date: 2026-11-01

This is the first frozen Paper 1 evidence artifact. It is an internal research release, not a claim of a
solver win.

## Contents

- Paper draft: `paper/paper1-draft.md`
- Evidence table: `paper/tables/evidence.md`
- Benchmark records: `evidence/*/record.json`
- Serialized schedules and replay scripts alongside each record
- Benchmark schema: `schemas/benchmark-record.schema.json`
- Replay gate: `scripts/check_benchmark_record.py`
- Table generator: `scripts/build_evidence_tables.py`
- Artifact manifest: `paper/release/manifest.json`

## Evidence

| Record | Objective | Exact replay |
| --- | ---: | ---: |
| FHOPS tiny7 SA | 4,295.774752 | yes |
| FHOPS small21 SA | 15,508.884819999994 | yes |
| WS4 TSA24 GPU-GA | 8,588,725.370498415 | 8,588,725.370498514 |

## Verification

- Evidence records validate with schedule hashes and exact replay.
- Paper table regenerates from records.
- Tests and Sphinx build pass.
- Clean-checkout verification is recorded in the P5 close-out.

## Clean-checkout verification

A clean clone with submodules passed:

- 154 tests
- Sphinx `-W`
- workflow validator: 0 errors
- all three evidence records valid
- evidence table regenerated
- submodule pinned to `58695d350fa5998a0e069e96e669cd3fa6870a9b`

Log: `paper/release/clean-checkout.log`

## Known gaps

1. No matched optimized landscape baseline.
2. TSA24 is a local reconstructable fixture, not a public benchmark.
3. Time-to-first-feasible is not separately instrumented.
4. FHOPS is operational planning, not a direct architecture peer.
5. Reference metadata needs final verification.
6. Paper text has not had external peer review.

## Do not claim

Do not describe this artifact as a controlled speed or quality win over published landscape solvers.
