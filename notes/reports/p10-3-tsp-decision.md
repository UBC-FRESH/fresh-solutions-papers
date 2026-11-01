# P10.3 decision: stop at Or-opt for this phase

Status: **deferred — acceptance not met**
Date: 2026-11-01
Issue: #34

## Decision

Do **not** adopt randomized 3-opt. Stop the TSP neighbourhood work at the existing Or-opt/2-opt path
for P10. Implementing Lin–Kernighan is a separate task, not a checkbox to claim here.

## Why

- Or-opt with the convergence protocol yields five-seed mean gaps of roughly 3.7–8.2% on the four
  TSPLIB instances.
- Randomized 3-opt, started from the converged Or-opt incumbent, produced no improvement on
  `berlin52`, `kroA100`, or `ch150`; it was not adopted.
- No candidate-list 3-opt or Lin–Kernighan implementation exists in Fresh Solutions.
- P10.3's acceptance requires a material improvement over the 3.7–8.2% range; that has not happened.

## Evidence

- `paper2/evidence/converged-summary.json` — Or-opt/patience campaign.
- `fresh-solutions/notes/reports/heuristic-progression.md` — negative 3-opt result.
- Fresh Solutions v0.4.0 contains `tsp_three_opt.py` as experimental; it is not the default.

## Consequences

- Paper 2 must describe TSP as Or-opt-only and must not claim 3-opt/LK competitiveness.
- P10 cannot claim a completed competitive TSP result.
- If TSP competitiveness becomes a requirement, open a dedicated phase with:
  1. candidate-list construction;
  2. a proper 3-opt or LK implementation;
  3. equal-budget comparisons against Or-opt and an independent baseline;
  4. exact replay and convergence checks.

## Recommendation

Close P10.3 as deferred, not complete. Continue with the applied case and close-out with this limitation
visible.
