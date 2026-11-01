# P10.7 close-out: competitive evidence and stop recommendation

Status: task complete; phase PR queued
Date: 2026-11-01
Issue: #38
Parent: #31
Branch: `feature/p10-competitive-benchmark`

## Recommendation

Queue the P10 PR for maintainer review. Do **not** publish either paper yet, and do **not** convert the
QAP result into a solver-leadership claim.

Phase disposition: **partial evidence, documented limits**. P10.3 is complete with a
quality-at-additional-cost caveat. P10.6 is complete as a public-data applied case.

## Evidence freeze

| Area | Result | Status |
| --- | --- | --- |
| QAP certified tabu | tai12a 0.000%, tai20a 0.403%, tai25a 0.685%, tai30a 0.407% | 20/20 exact |
| QAP independent baseline | SciPy FAQ 9.026%, 4.642%, 4.474%, 2.289% | 20/20 exact; not budget-matched |
| Paper 1 landscape baseline | 10× same-engine: 76,540.740733 | exact; not independent |
| TSP neighborhood | Iterated LK: 0.000/0.000/0.000/0.383% mean gap; 20/20 exact | P10.3 complete; extra-budget caveat |
| Applied case | TSA24/Prince George, UBC-FRESH public instance | complete; public-data case |

## Acceptance

- Every claim maps to a replayable record: **met** for QAP and Paper 1 tables.
- Workflow compliance and gate evidence: **met** for the queued PR.
- Report recommends next phase or stop: **met** (stop publication; resolve permission/TSP separately).

## Gate evidence

- `python3 -m pytest -q`: **154 passed**, 99.53% coverage (95% gate).
- `python3 scripts/check_workflow.py`: **0 errors**, 3 recommended-file warnings.
- Four benchmark records: **VALID**.
- QAP certified records: **20/20 exact**; SciPy baseline: **20/20 exact**.
- LK records: **20/20 exact**.
- Evidence table regenerated: `paper/tables/evidence.md`.
- Sphinx/docs and workflow validator run on the phase branch.
- **CI correction:** the first PR run failed on `ruff format` for `paper2/replay_qap_tabu.py` and a
  missing `types-jsonschema` stub in the CI environment. Both are fixed; the rerun is the gate of record.

## Workflow compliance

- Parent #31; child issues #32–#38.
- Phase branch `feature/p10-competitive-benchmark`.
- P10.1/P10.2/P10.3/P10.4/P10.5/P10.6/P10.7 complete.
- No direct `main` commits for P10 work.
- No new tag or release in P10.

## Deviations and blockers

1. **TSP uses additional LK budget.** Iterated LK improves materially, but the comparison is not an equal-budget ablation.
2. **Paper 1 baseline is same-engine.** It is a budget-scaling baseline, not an independent solver.
3. **Applied case is public-data, not partner-endorsed.** TSA24 is a UBC-FRESH public instance built
   from public BC data; the repository lacks an explicit LICENSE file, which is an attribution gap.
4. **Earlier workflow deviations remain disclosed** in `notes/reports/workflow-conformance-audit.md`.

## Claim boundary

- Paper 1: **not submission-ready**; same-engine scaling evidence only.
- Paper 2: internal engineering evidence; not publication-grade.
- QAP: competitive tabu result with a certified budget and a time-quality baseline; not state of the art.
- TSP: iterated LK improves materially; no state-of-the-art or equal-budget claim.
- Applied impact: public-data case only; no partner-impact claim.

## Next

1. Maintainer review of this phase PR.
2. Add explicit licence/attribution metadata to the public TSA24 instance.
3. Approve the LK release/merge path and decide whether to expand the TSP campaign.
4. Keep both papers internal until the remaining gates pass.
