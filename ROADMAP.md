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
| P3 Paper 1 benchmark evidence | #10 | `feature/p3-paper1-evidence` | complete |
| P4 Paper 1 writing and verification | #19 | `feature/p4-paper1-writing` | complete |
| P5 Release and reproducibility | #21 | `feature/p5-release` | complete |
| P6 Paper 2 evidence and operation | #23 | `feature/p6-paper2-evidence` | complete |
| P7 Paper 2 writing and evidence | #25 | `feature/p7-paper2-writing` | complete |
| P8 Paper 2 multi-seed campaign | #27 | `feature/p8-multiseed` | complete |
| P9 Converged Paper 2 campaign | #29 | `feature/p9-converged` | complete |
| P10 Competitive benchmark programme | #31 | `feature/p10-competitive-benchmark` | active |

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
Status: complete

Goal: produce the forestry evidence: reproduced baselines, hybrid runs, and exact schedules.

- [x] P3.1 Select and document the first reproducible benchmark target
- [x] P3.2 Implement the benchmark-record validator and replay gate
- [x] P3.3 Record the first benchmark evidence or documented stop
- [x] P3.4 Record hardware and software provenance for every run
- [x] P3.5 Implement or reject the WS4/FHOPS comparison adapter
- [x] P3.6 Run the next public benchmark evidence pass
- [x] P3.7 Record the first WS4 architecture benchmark

Acceptance criteria:

- Every reported result has a schedule that replays exactly.
- Comparisons use equal objectives and feasible schedules.

## Phase 4: Paper 1 writing and verification

Parent issue: #19
Branch: `feature/p4-paper1-writing`
Status: complete

Goal: turn the evidence into a defensible architecture paper.

- [x] P4.1 Freeze the paper-1 thesis and contribution list
- [x] P4.2 Build the benchmark tables and figures from evidence files
- [x] P4.3 Write and review the paper draft
- [x] P4.4 Archive the artifact and reproduce it from a clean checkout

Acceptance criteria:

- Every claim points to a benchmark record.
- The benchmark wins are presented as evidence, not as the thesis.

## Phase 5: Release and reproducibility

Parent issue: #21
Branch: `feature/p5-release`
Status: complete

Goal: freeze and verify the Paper 1 evidence artifact, then publish the release.

- [x] P5.1 Write release notes and known gaps
- [x] P5.2 Verify from a clean checkout
- [x] P5.3 Build and publish the benchmark artifact

Acceptance criteria:

- The evidence release is tagged and verified from a clean checkout.
- Every published record passes the replay gate.

## Phase 6: Paper 2 evidence and operation

Parent issue: #23
Branch: `feature/p6-paper2-evidence`
Status: complete

Goal: produce the first public-library Paper 2 evidence and set the maintenance cadence.

- [x] P6.1 Pin tai12a and berlin52 with provenance
- [x] P6.2 Run public QAP/TSP evidence
- [x] P6.3 Record optimality gaps and replay
- [x] P6.4 Set maintenance cadence

Acceptance criteria:

- Public QAP/TSP assignments replay exactly.
- Gaps to known optima are recorded without leadership claims.

## Phase 7: Paper 2 writing and evidence

Parent issue: #25
Branch: `feature/p7-paper2-writing`
Status: complete

Goal: expand Paper 2 public evidence and write the first transfer-paper draft.

- [x] P7.1 Add two larger public instances
- [x] P7.2 Refresh four-instance evidence
- [x] P7.3 Write Paper 2 draft
- [x] P7.4 Archive and verify

## Phase 8: Paper 2 multi-seed campaign

Parent issue: #27
Branch: `feature/p8-multiseed`
Status: complete

Goal: replace single-seed evidence with a multi-instance, multi-seed distribution.

- [x] P8.1 Add four larger public instances
- [x] P8.2 Run five seeds per instance
- [x] P8.3 Record distribution and exact replay
- [x] P8.4 Update Paper 2 draft

## Phase 9: Converged Paper 2 campaign

Parent issue: #29
Branch: `feature/p9-converged`
Status: complete

Goal: replace pilot Paper 2 evidence with convergence-controlled multi-seed results.

- [x] P9.1 Run convergence-controlled campaign
- [x] P9.2 Record stop evidence and distributions
- [x] P9.3 Replay all assignments
- [x] P9.4 Update Paper 2 draft and close pilot table

## Phase 10: Competitive benchmark programme

Parent issue: #31
Branch: `feature/p10-competitive-benchmark`
Status: active

Goal: move from architecture/smoke evidence to competitive, converged, independently baselined applied OR results under the required workflow.

- [x] P10.1 Workflow conformance audit (#32)
- [x] P10.2 QAP competitive neighborhood (#33)
- [ ] P10.3 TSP 3-opt/Lin–Kernighan evaluation (#34) — deferred; Or-opt only
- [x] P10.4 Serious-budget convergence protocol (#35)
- [x] P10.5 Matched landscape baseline (#36)
- [ ] P10.6 Applied case selection (#37) — active; permission pending
- [ ] P10.7 Competitive evidence and closeout (#38)

Acceptance criteria:

- Every task is a linked child issue with closeout evidence.
- Benchmark results are converged, multi-seed, independently baselined, and replayable.
- Paper/software claims are limited to what the evidence supports.
