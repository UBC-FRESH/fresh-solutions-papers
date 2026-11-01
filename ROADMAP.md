# Fresh Solutions Papers Roadmap

This roadmap is the plan of record and issue tracker map for Fresh Solutions Papers. Keep it in step
with the GitHub issues, `CHANGE_LOG.md`, and `notes/`. `scripts/check_workflow.py` parses the phase
headers, status lines, and checkboxes below, so keep their format.

The programme produces two papers:

1. **Compiled spatial optimisation** — architecture, GPU hybrid metaheuristics, and reproduced
   forestry benchmarks.
2. **Fresh Solutions** — a general hybrid metaheuristic engine tested outside forestry.

Every phase starts as `planned` with `Parent issue: TBD`. Activate a phase only after its parent issue
exists and the maintainer approves it.

## Issue Tracker Map

| Phase | Parent issue | Branch | Status |
| --- | --- | --- | --- |
| P0 Bootstrap | #1 | `feature/p0-bootstrap` | complete |
| P1 Scope, literature, and benchmark corpus | #2 | `feature/p1-scope-literature` | complete |
| P2 Architecture and benchmark contracts | #8 | `feature/p2-architecture-contracts` | complete |
| P3 Paper 1 benchmark evidence | #10 | `feature/p3-paper1-evidence` | active |
| P4 Paper 1 writing and verification | TBD | `feature/p4-paper1-writing` | planned |
| P5 Fresh Solutions and Paper 2 evidence | TBD | `feature/p5-fresh-solutions` | planned |
| P6 Release, reproducibility, and operation | TBD | `feature/p6-release` | planned |

## Lifecycle Map

| Stage | Phases | Exit criteria |
| --- | --- | --- |
| Scope and design | P0, P1, P2 | Thesis, scope, benchmark corpus, and contracts are recorded |
| Evidence | P3, P5 | Every benchmark claim has a replayable instance, config, seed, and schedule |
| Writing and verify | P4 | Claims are tied to evidence and the paper draft is reviewable |
| Release and operate | P6 | Artifacts are tagged, archived, and reproducible from a clean checkout |
| Retire | P6 | Final record and archive notice |

## Conventions

- A phase is `P<n>`. A task is `P<n>.<m>`. A subtask is a checklist item inside the task's issue body.
  Three levels at most.
- Status values are `planned`, `active`, `pr-open`, `complete`, and `deferred`.
- A phase becomes `complete` only after its pull request merges to `main` and its parent issue closes.
- Every benchmark claim names the instance, objective, hardware, software version, seed, and exact
  verification result.

## Phase 0: Bootstrap

Parent issue: #1
Branch: `feature/p0-bootstrap`
Status: complete

Goal: adapt the seed to the paper programme, add `fresh-solutions` as a submodule, and make the first
pull request reviewable.

- [x] P0.1 Adapt `AGENTS.md`, `README.md`, `LICENSE`, and the roadmap to this programme
- [x] P0.2 Add `fresh-solutions` as a git submodule
- [x] P0.3 Confirm the validator and the docs build pass

Acceptance criteria:

- The repository identifies the two papers and the submodule.
- `python scripts/check_workflow.py` reports zero errors.
- `sphinx-build -b html docs _build/html -W` passes.

## Phase 1: Scope, literature, and benchmark corpus

Parent issue: #2
Branch: `feature/p1-scope-literature`
Status: complete

Goal: define the research questions and build a reproducible benchmark corpus, not a list of
aspirational citations.

- [x] P1.1 Verify the Lockwood and Moore (1993) citation and locate or reconstruct an instance
- [x] P1.2 Build the spatially explicit harvest-scheduling benchmark matrix
- [x] P1.3 Build the conservation-planning and general combinatorial benchmark matrix
- [x] P1.4 Define the benchmark record schema (problem, objective, hardware, time-to-quality, replay)

Acceptance criteria:

- Every benchmark has an availability status: public data, reconstructable, abstract-only, or
  unusable.
- The comparison protocol is recorded before results are collected.

## Phase 2: Architecture and benchmark contracts

Parent issue: #8
Branch: `feature/p2-architecture-contracts`
Status: complete

Goal: state the architecture claim and define the interfaces that make benchmark reproduction
auditable.

- [x] P2.1 Write the compiled-state architecture and hybrid search design note
- [x] P2.2 Define the benchmark adapter and evidence schema
- [x] P2.3 Define exact replay and feasibility checks

Acceptance criteria:

- The architecture note separates the claimed contribution from the benchmark effects.
- A benchmark record can be replayed without reading the paper prose.

## Phase 3: Paper 1 benchmark evidence

Parent issue: #10
Branch: `feature/p3-paper1-evidence`
Status: active

Goal: produce the forestry evidence: reproduced baselines, hybrid runs, and exact schedules.

- [x] P3.1 Select and document the first reproducible benchmark target
- [x] P3.2 Implement the benchmark-record validator and replay gate
- [x] P3.3 Record the first benchmark evidence or documented stop
- [x] P3.4 Record hardware and software provenance for every run
- [ ] P3.5 Implement or reject the WS4/FHOPS comparison adapter
- [ ] P3.6 Run the next public benchmark evidence pass

Acceptance criteria:

- Every reported result has a schedule that replays exactly.
- Comparisons use equal objectives and feasible schedules.

## Phase 4: Paper 1 writing and verification

Parent issue: TBD
Branch: `feature/p4-paper1-writing`
Status: planned

Goal: turn the evidence into a defensible architecture paper.

- [ ] P4.1 Freeze the paper-1 thesis and contribution list
- [ ] P4.2 Build the benchmark tables and figures from evidence files
- [ ] P4.3 Write and review the paper draft
- [ ] P4.4 Archive the artifact and reproduce it from a clean checkout

Acceptance criteria:

- Every claim points to a benchmark record.
- The benchmark wins are presented as evidence, not as the thesis.

## Phase 5: Fresh Solutions and Paper 2 evidence

Parent issue: TBD
Branch: `feature/p5-fresh-solutions`
Status: planned

Goal: extract the generic engine and test whether the architecture transfers.

- [ ] P5.1 Freeze the `fresh-solutions` adapter API
- [ ] P5.2 Implement the non-forestry adapters
- [ ] P5.3 Run the public combinatorial benchmark suite
- [ ] P5.4 Write the Paper 2 evidence table

Acceptance criteria:

- The generic engine has at least three non-forestry adapters.
- Every Paper 2 claim has a reproducible benchmark record.

## Phase 6: Release, reproducibility, and operation

Parent issue: TBD
Branch: `feature/p6-release`
Status: planned

Goal: publish the artifacts and keep the programme maintainable.

- [ ] P6.1 Tag the paper artifacts and publish the benchmark archive
- [ ] P6.2 Verify from a clean checkout
- [ ] P6.3 Set the review cadence and archive the final evidence

Acceptance criteria:

- Both repositories have release tags and archival records.
- A clean checkout reproduces the published evidence.
