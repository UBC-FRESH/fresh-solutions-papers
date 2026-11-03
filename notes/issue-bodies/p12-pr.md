# P12.1: framework-use and TSP convergence evidence

## Summary

- Adds a ten-seed QAP framework-use comparison between a private-array delta path and a path whose
  incumbent is managed by `ResidentAssignment`.
- Final QAP protocol: 100,000-iteration patience, 1,000,000 cap. All 40 runs stopped on patience,
  all objectives matched, and all incumbents replayed exactly.
- Adds a convergence-controlled TSP campaign: five seeds, 10,000 kicks, 1,000-kick patience. All
  20 runs stopped on patience, reached the known optimum, and replayed exactly.
- Expands Paper 2 to 18 pages and 8,000 source words.
- Adds replay, sensitivity, and table-generation scripts plus evidence manifest entries.

## Evidence

- `paper2/evidence/framework-use.json`
- `paper2/evidence/framework-use-analysis.json`
- `paper2/evidence/framework-use-sensitivity.json`
- `paper2/evidence/tsp-convergence-10k.json`
- `paper2/evidence/tsp-convergence-2k.json`

## Checks

`python scripts/dashboard.py`: all gates green.

## Claim boundary

- No state-of-the-art claim.
- No global optimality claim.
- No generic-engine search claim.
- No tag, release, or submission action.
