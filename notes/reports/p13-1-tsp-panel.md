# P13.1 closeout: expanded TSP panel

Status: complete
Date: 2026-11-09
Issue: #82

## Result

- 20 TSPLIB instances, five seeds, 100 runs.
- 10,000-kick cap, 1,000-kick patience.
- 95/100 runs stopped on patience.
- 5/100 runs on `brazil58` reached the known optimum but hit the 3,600-second wall-clock cap;
  they are reported as cap hits, not convergence.
- 94/100 runs reached the known optimum.
- Overall mean gap 0.004%, median 0%, worst 0.185%.
- 100/100 incumbents replay exactly.

## Runtime fix

- The original depth-4 LK pass on `d198` exploded inside `_tour_from_edges`; one kick exceeded 300 s.
- The runner now uses adaptive depth: 4 for n<100, 3 for 100<=n<150, 2 for n>=150.
- Per-seed checkpointing stores each completed run.
- `gr137` was removed: it is a GEO instance and the distance path produced an objective below the
  published optimum. Replaced by the EUC_2D `pr152`. This is a data/parser boundary, not a solver win.

## Evidence

- `paper2/evidence/tsp-expanded-10k.json`
- `paper2/evidence/tsp-expanded-10k-summary.json`
- `paper2/run_tsp_expanded.py`
- `paper2/check_evidence.py`

## Claim boundary

The expanded panel is a breadth check, not the four-instance deep panel. The five `brazil58` cap hits
are in the denominator. No “all 100 converged” claim is made.
