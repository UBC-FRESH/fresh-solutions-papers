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

### P6 close-out

- Pinned QAPLIB tai12a and TSPLIB berlin52 with provenance.
- Ran Fresh Solutions v0.1.0 hybrid; recorded 11.997% QAP gap and 128.268% TSP gap.
- Both assignments replay exactly; maintenance cadence recorded.
- P6 is complete; the result is transfer evidence, not a leadership claim.

### P6 v0.2.0 evidence refresh

- Synced the submodule to fresh-solutions v0.2.0.
- Refreshed public evidence with population 32 / 50 generations / 3,000 local iterations.
- tai12a: 241,016 (7.397% gap); berlin52: 9,033 (19.769% gap).
- Replay passes for both assignments.

### P7 close-out

- Added tai20a and kroA100 public instances.
- Refreshed four-instance Paper 2 evidence and wrote the first transfer-paper draft.
- All four assignments replay exactly.
- P7 is complete; no leadership claim is made.

### P8 close-out

- Added tai25a, tai30a, kroB100, ch150.
- Recorded five-seed distributions for eight public instances; 40/40 assignments replay exactly.
- Updated Paper 2 draft and evidence.
- QAP mean gaps 5.2–8.9%; TSP mean gaps 10.2–56.3%; ch150 is the weak case.

### P9 close-out

- Replaced pilot Paper 2 evidence with 40 converged runs.
- All 40 stopped on patience and replay exactly.
- TSP Or-opt: mean gaps 3.696–8.229%; QAP swap lane: 5.249–8.897%.
- Updated draft and README to report converged results.

### P10.2/P10.4 QAP tabu and serious budget

- Pinned `fresh-solutions` v0.4.0.
- Added QAP tabu runner, replay check, and budget ladder.
- Certified QAP means: tai12a 0.000%, tai20a 0.403%, tai25a 0.685%, tai30a 0.407%.
- Added the serious-budget policy; 20/20 certified assignments replay exactly.

### P10.5 same-engine landscape baseline

- Added `ws4-tsa24-gpu-ga-10000-r7` record: 10,000 generations, objective 76,540.740733.
- Exact replay and duplicate schedule hash verified.
- Paper 1 now reports a same-engine scaling baseline, not an independent solver baseline.

### P10.3 TSP decision

- Randomized 3-opt retained as a negative result; not adopted.
- TSP remains Or-opt-only at roughly 3.7–8.2% mean gap.
- P10.3 marked deferred, not complete; no LK claim.

### P10.6 applied case selection

- Selected TSA24/Prince George even-flow harvest scheduling as the candidate case.
- Defined decision metrics, same-engine baseline, and provenance.
- Blocked on data licence/partner publication permission; no applied-impact claim.

### P10.7 competitive close-out

- Froze QAP, Paper 1 scaling, TSP, and applied-case status.
- Verified four benchmark records and 40/40 QAP/baseline replays.
- Queued the phase PR; publication blocked on P10.6 permission and TSP limits.

### P10.7 CI correction

- Formatted `paper2/replay_qap_tabu.py`.
- Added `types-jsonschema` to the CI dev requirements.
- Disclosed the first failed PR run; rerun is the gate of record.

### P10.3 Lin–Kernighan evidence

- Pinned solver LK commit `24dc60c`.
- Added five-seed LK campaign from converged Or-opt tours.
- Three instances reach the known optimum; ch150 mean gap 0.383%; 20/20 exact replays.
- P10.3 complete with an extra-budget caveat.

### P10.6 correct TSA24 provenance

- Confirmed TSA24 is a UBC-FRESH-owned public instance at github.com/UBC-FRESH/femic-tsa24-instance.
- Confirmed public BC data sources and public Arbutus storage.
- Removed the erroneous external-permission blocker; retained the no-partner-endorsement and
  no-independent-baseline limits.

### P10 LK kicks ablation

- Added LK-only, ILK-5, and ILK-20 five-seed ablation.
- LK-only means 0.780–2.580%; ILK-20 means 0.000–0.383%.
- All 60 ablation tours replay exactly.

### Broad QAP/TSP panel pilot

- Added a 212-instance, 1,085-run pilot over TSPLIB/QAPLIB at solver v0.5.1.
- Small/medium results are strong; large TSP and large QAP tails are weak and disclosed.
- Evidence: `paper2/evidence/broad-suite-v051.json.gz` and summary.
