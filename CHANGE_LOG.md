# Change Log

Newest entries last. Each milestone gets a dated entry that matches the roadmap status and the GitHub issue comments.

## 2026-11-01

- Created Fresh Solutions Papers from the UBC-FRESH dev workflow seed. The agent contract, roadmap, docs skeleton, and validator came from the seed. Every phase is planned, and no parent issues exist yet.

### P0 Bootstrap

- Created the repository from the UBC-FRESH seed and adapted the README/roadmap to the two-paper programme.
- Added `fresh-solutions` as a submodule pinned to the public solver repository.
- Added the programme design note and first benchmark-corpus matrix.
- Tests, docs, and the workflow validator pass. P0 issue #1 closed; P1 issue #2 activated.

### P1 Scope, literature, and benchmark corpus

- P1 started. The first literature pass is recorded in `notes/reference/benchmark-corpus.md`.
- Next: verify Lockwood and Moore (1993), FHOPS, and the remaining benchmark availability statuses.

### P1 close-out

- Completed the benchmark availability matrix and frozen the replay schema.
- Verified the Lockwood and Moore (1993) DOI; original instance remains unlocated and is classified as reconstructable candidate.
- Identified FHOPS as the primary public reproducibility anchor.
- 138 tests, Sphinx `-W`, JSON schema parse, and workflow validator pass.
- P1 is complete; P2 remains planned.

### P2 close-out

- Froze the compiled-state architecture, benchmark adapter contract, and exact replay/feasibility rules.
- Recorded cache identity and invalidation rules, including the distinction between pricing changes and table rebuilds.
- P2 is complete; P3 remains planned.

### P3 progress

- Selected FHOPS as the first public target; Lockwood remains reconstructable and deferred.
- Implemented the benchmark-record validator with schema, exact-replay, and schedule-hash gates.
- Added the first replay-harness tests and API documentation.
- P3 remains active: no benchmark result is claimed yet.

### P3 first evidence

- Recorded the first replayable public baseline: FHOPS tiny7 SA, 200 iterations, seed 42.
- Objective 4295.774752; exact replay 4295.774752; hard violations 0.
- Added `evidence/fhops-tiny7-sa-200-r42/` with schedule, record, hash, and replay script.
- Validator accepted the record: exact-replay gate and SHA-256 hash pass.
- P3 remains active; P3.5/P3.6 are the next comparison tasks.
