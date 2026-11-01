# P4 close-out: Paper 1 writing and verification

Status: complete
Date: 2026-11-01
Issue: #19

## Result

P4 produced the first evidence-constrained Paper 1 draft and the evidence-table generator.

Deliverables:

- `notes/design/paper1-thesis.md` — frozen thesis, contributions, permissible claims, limitations.
- `scripts/build_evidence_tables.py` + tests — table generation from records.
- `paper/tables/evidence.md` — generated table for the three records.
- `paper/paper1-draft.md` — abstract, architecture, evidence contract, results, limitations, conclusion.
- `paper/README.md` — reproduction commands.
- `notes/design/paper1-archive.md` — archive/reproduction procedure and gaps.
- `notes/reports/p4-review.md` — claim audit and internal review.

## Claim status

- Architecture is exact/replayable on TSA24. **Supported.**
- TSA24 GPU run improves on initial seed by about 200×. **Supported, with seed-is-not-control caveat.**
- FHOPS baselines are public/replayable. **Supported.**
- FHOPS is a direct architecture peer. **Rejected.**
- 1,000 generations converged even flow. **Not claimed.**
- Architecture beats published solvers. **Not claimed.**

## Verification

- 154 tests passed; coverage 99.5%.
- Sphinx `-W`: pass.
- Workflow validator: 0 errors.
- Three benchmark records validate with exact replay.
- Evidence table regenerates from records.

## Limits

- No matched optimized landscape baseline.
- TSA24 is a local reconstructable fixture.
- Time-to-first-feasible was not separately instrumented.
- Reference metadata needs final verification.
- No external peer review.

## Recommendation

Close P4. P5 should freeze the artifact, containerize the run environment, verify from a clean checkout,
and only then consider submission or a public release.
