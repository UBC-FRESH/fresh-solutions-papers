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

### P3.5/P3.6

- Rejected a direct FHOPS/WS4 adapter as a problem-contract mismatch; FHOPS remains a public baseline and reproducibility stack.
- Recorded FHOPS small21 SA baseline: objective 15508.884819999994, exact replay, hard violations 0.
- Added `evidence/fhops-small21-sa-200-r42/`.
- P3.7 remains open for the first WS4 architecture benchmark.

### P3 close-out

- Recorded three replayable records: FHOPS tiny7, FHOPS small21, and WS4 TSA24 GPU-GA.
- WS4 TSA24 GPU objective 8,588,725.370498415; exact replay 8,588,725.370498514; initial seed 1,722,144,291.336651.
- Added the TSA24 schedule, record, seed-baseline evidence, and replay script.
- Direct FHOPS/WS4 comparison rejected as a contract mismatch.
- P3 is complete; P4 remains planned.

### P4 close-out

- Froze the Paper 1 thesis and contribution list.
- Added evidence-table generation, Paper 1 draft, reproduction procedure, and claim audit.
- Draft explicitly labels the TSA24 seed comparison as non-controlled and withholds unsupported claims.
- P4 is complete; P5 remains planned for artifact freeze, clean-checkout verification, and release.

### P5 close-out

- Froze Paper 1 evidence release `paper1-evidence-v0.1.0`.
- Added release notes, manifest, clean-checkout log, and close-out report.
- Clean clone: 154 tests, Sphinx -W, workflow validator 0 errors, all records valid.
- P5 is complete; P6 remains planned for maintenance and Paper 2.
