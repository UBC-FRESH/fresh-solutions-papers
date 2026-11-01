# P4 self-review

Status: internal review
Date: 2026-11-01

## Claim audit

| Claim | Evidence | Verdict |
|---|---|---|
| Architecture separates compiled model, candidate/effect indexes, state, and search. | `notes/design/compiled-state-architecture.md` | supported as design |
| TSA24 GPU run is exact and replayable. | `evidence/ws4-tsa24-gpu-ga-1000-r7/` | supported |
| TSA24 run improves on the initial seed by about 200×. | record and seed baseline output | supported, but seed is not an optimized control |
| FHOPS baselines are public and replayable. | two evidence records | supported |
| FHOPS is a direct architecture peer. | — | rejected |
| 1,000 generations converged the even-flow solution. | — | not claimed |
| The architecture is faster than published solvers. | — | not claimed |

## Review notes

- Abstract and conclusion state the limits.
- The seed comparison is labelled as a starting-point comparison, not a benchmark win.
- FHOPS is separated as operational planning, not landscape scheduling.
- The paper needs a matched optimized baseline before submission.
- Reference metadata still needs full verification.

## Recommendation

The draft is reviewable as an internal architecture draft. Do not submit until the matched-baseline gap
and reference verification are closed.
