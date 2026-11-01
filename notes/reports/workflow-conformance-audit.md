# Workflow conformance audit

Status: P10.1 complete
Date: 2026-11-01
Scope: `fresh-solutions-papers` and `fresh-solutions`
Reference: `ubc-fresh-dev-workflow` / `AGENTS.md` and `docs/reference/phase-closeout.rst`

## Compliant

- Repositories were created from the UBC-FRESH seed.
- The validator, per-commit dashboard, roadmap, changelog, docs, and branch/PR flow exist.
- P1 and P3 in the papers project used linked child issues.
- P1 in the solver project used linked child issues.
- Every phase has a parent issue, branch record, close-out report, and squash-merged PR except where listed below.
- P10 is the first phase created after this audit: parent #31 and linked child issues #32–#38.

## Deviations

| # | Deviation | Evidence | Cause | Remedy |
| --- | --- | --- | --- | --- |
| D1 | Parent tasks were inline checklists, not child issues, in P4–P9 papers and P2–P7 solver. | Issue lists: papers parent issues #19/#21/#23/#25/#27/#29; solver #7/#9/#11/#13/#15/#17. | Phases were activated in a hurry; parent checklist used as a shortcut. | P10 uses linked child issues #32–#38. All future phases must create child issues before work. |
| D2 | Direct commits to `main` outside phase PRs. | Papers `1e7938b`, `bdd57d8`, `ecaefc3`, `e63458c`, `0b2208b`; solver `58695d3`. | Release/evidence housekeeping was treated as exempt. | No direct main commits. Any post-merge correction needs a new bounded issue and PR. |
| D3 | Close-out reports did not use the required nine-section template: header, recommendation, objectives/acceptance, workflow compliance, gate evidence, CI evidence, deviations, next phase, decision. | `notes/reports/p*-closeout.md`; most reports omit CI/workflow/deviation sections. | Reports written to summarize results, not to satisfy the review template. | Future close-outs use the template verbatim; a report missing a section is incomplete. |
| D4 | Tags/releases were created after “go” but without an explicit approval line naming each tag command in a close-out. | `paper1-evidence-v0.1.0`; solver `v0.1.0`, `v0.2.0`, `v0.3.0`. | Approval gates were not written into the release reports. | No tag/release without a named approval item. Historical tags remain declared. |
| D5 | Paper drafts were produced before evidence gates passed. | Paper 2 draft moved to `notes/reports/paper2-smoke-notes.md` and marked DO NOT SUBMIT; Paper 1 marked NOT SUBMISSION-READY. | Mistook smoke tests for paper evidence. | No paper prose until P10.5/P10.7 evidence and Paper 1 matched baseline pass. |
| D6 | P9 added after P8 close-out without a P8 recommendation and approval line. | ROADMAP history and issue #29. | Ad hoc continuation. | Future phase activation comes from an approved close-out recommendation or direct maintainer instruction. |

## Forward rules

1. Parent issue exists before phase branch.
2. Child issue exists before task work.
3. One phase branch, one PR, `Part of #<parent>`.
4. Every commit starts with the task ID and dashboard green.
5. Close-out report uses the nine required sections.
6. No tag/release/settings/external action without an explicit named approval.
7. No paper/software claim without a replayable, converged, independently baselined result.
8. Post-merge corrections require a new issue and PR; never edit `main` directly.

## Historical limits

Closed-phase deviations cannot be erased without rewriting history. They are disclosed here and are not
to be repeated. The P10 process is the remediation boundary.

## Verification

- Issue/PR audit performed with `gh issue list` and `gh pr list` on both repositories.
- `python scripts/check_workflow.py` passes on the P10 branch.
