# P16: Opportunity hardening of the submission drafts

Date: 2026-11-18
Status: queued
Targets: Paper 1 SoftwareX; Paper 2 JORS Issues in Research Software.

## Objective

Increase impact, clarity, reuse, and application relevance without inventing new evidence.
These are opportunity additions, not correctness fixes.

## Queue

### P16.1 — Paper 1: policy context and application visibility (highest priority)

1. Add the 70M/AAC context: 70M m3 per 10-year period = 7.0M m3/year; 2025 AAC = 6,917,231 m3/year;
   realized 51.21–52.49M per 10-year = 5.12–5.25M m3/year, roughly 24–26% below the 2025 AAC.
   Source: TSA24 artifact target comment and records. No outside claim.
2. Add a realized-level figure: per-seed min/max/mean level versus 70M aspiration and 2025 AAC.
   Use existing `target_penalties` fields; no new simulation.
3. Add a compact "audit and scenario" use case: replay a submitted schedule, compare targets, inspect
   assignments, teach model/accounting/search separation.
4. Move the five-seed and evaluation-path tables to a SoftwareX supplement; keep a scaling summary in
   the main text. This protects the 4,000-word cap and page budget.
5. Reframe the abstract opening around the planning/audit problem before the implementation.
6. Add a short "to adapt WS4" list: compiler, candidate index, effect rows, target file, validator.

Acceptance:
- Main text ≤4,000 counted words including content tables; supplement contains moved tables.
- New figure uses only existing records; target/AAC values match artifact.
- SoftwareX build compiles; no new unsupported environmental or adoption claim.
- Page target: main ≤11 pages; supplement ≤3 pages.

### P16.2 — Paper 2: reporting protocol and reuse (highest priority)

1. Add a compact "minimum replayable heuristic result" checklist in the main text: instance/source,
   adapter/commit, seed, budget, stopping rule, stop reason, assignment, exact replay, CPU/hardware,
   code/data release.
2. Add a "harness changed the conclusion" sentence: the replayable BLS comparison made the tabu
   reference's weakness visible.
3. Add a "protocol drift" lesson: mixed-depth TSP and `brazil58` cap hits show why per-run configuration
   must be recorded.
4. Add a "when to use this harness" decision table to the supplement.
5. Add a minimal adapter skeleton and a sample evidence record to the supplement.
6. Add a three-command quickstart to the main text or supplement.
7. Keep the main text within 3,000–4,000 words; no new experiments.

Acceptance:
- Main text remains ≤4,000 words; supplement additions are clearly labelled.
- Checklist and decision table are actionable and consistent with the existing schema.
- No new state-of-the-art or portability claim.
- Page target: main ≤8 pages; supplement ≤4 pages.

### P16.3 — Release, verification, and final gate

1. Rebuild Paper 1 main + supplement, Paper 2 main + supplement.
2. Re-run clean-clone Paper 2 replay and Paper 1 public-layout replay.
3. Refresh manifests, release notes, and target release tags.
4. One final opportunity-focused review of both drafts.
5. Final PI approval before submission.

## Non-goals

- No new benchmark campaigns.
- No new claims of adoption, state of the art, or third-party portability.
- No DOI/container action without credentials/tools.
