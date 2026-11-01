# P10.7 close-out: competitive evidence and stop recommendation

Status: task complete; phase PR queued
Date: 2026-11-01
Issue: #38
Parent: #31
Branch: `feature/p10-competitive-benchmark`

## Recommendation

Queue the P10 PR for maintainer review. Do **not** publish either paper yet, and do **not** convert the
QAP result into a solver-leadership claim.

Phase disposition: **partial evidence, documented blockers**. P10.6 remains permission-blocked, and
P10.3 is deferred.

## Evidence freeze

| Area | Result | Status |
| --- | --- | --- |
| QAP certified tabu | tai12a 0.000%, tai20a 0.403%, tai25a 0.685%, tai30a 0.407% | 20/20 exact |
| QAP independent baseline | SciPy FAQ 9.026%, 4.642%, 4.474%, 2.289% | 20/20 exact; not budget-matched |
| Paper 1 landscape baseline | 10× same-engine: 76,540.740733 | exact; not independent |
| TSP neighborhood | Or-opt only, ~3.7–8.2% mean gap | P10.3 deferred; 3-opt negative |
| Applied case | TSA24/Prince George selected | permission unresolved |

## Acceptance

- Every claim maps to a replayable record: **met** for QAP and Paper 1 tables.
- Workflow compliance and gate evidence: **met** for the queued PR.
- Report recommends next phase or stop: **met** (stop publication; resolve permission/TSP separately).

## Gate evidence

- `python3 -m pytest -q`: **154 passed**, 99.53% coverage (95% gate).
- `python3 scripts/check_workflow.py`: **0 errors**, 3 recommended-file warnings.
- Four benchmark records: **VALID**.
- QAP certified records: **20/20 exact**; SciPy baseline: **20/20 exact**.
- Evidence table regenerated: `paper/tables/evidence.md`.
- Sphinx/docs and workflow validator run on the phase branch.

## Workflow compliance

- Parent #31; child issues #32–#38.
- Phase branch `feature/p10-competitive-benchmark`.
- P10.1/P10.2/P10.4/P10.5/P10.7 complete; P10.3 deferred; P10.6 active and blocked.
- No direct `main` commits for P10 work.
- No new tag or release in P10.

## Deviations and blockers

1. **TSP is not competitive.** Randomized 3-opt did not improve Or-opt; LK is not implemented.
2. **Paper 1 baseline is same-engine.** It is a budget-scaling baseline, not an independent solver.
3. **Applied-case permission is missing.** TSA24 is a real TSA decision problem, but the local fixture
   has no established publication licence or partner permission.
4. **Earlier workflow deviations remain disclosed** in `notes/reports/workflow-conformance-audit.md`.

## Claim boundary

- Paper 1: **not submission-ready**; same-engine scaling evidence only.
- Paper 2: internal engineering evidence; not publication-grade.
- QAP: competitive tabu result with a certified budget and a time-quality baseline; not state of the art.
- TSP: Or-opt only; no 3-opt/LK claim.
- Applied impact: none claimed until P10.6 permission and case evidence are complete.

## Next

1. Maintainer review of this phase PR.
2. Resolve TSA24 licence/permission or replace the fixture.
3. Decide whether TSP Lin–Kernighan deserves a dedicated phase.
4. Keep both papers internal until the remaining gates pass.
