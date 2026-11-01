# P9 close-out: converged Paper 2 campaign

Status: complete
Date: 2026-11-01
Issue: #29

## Result

The pilot Paper 2 table is replaced by a convergence-controlled, eight-instance, five-seed campaign.

All 40 runs stopped on patience and all 40 assignments replay exactly.

Config: Fresh Solutions v0.3.0, population 32, generations 50, 10,000 local iterations per round,
patience 3 rounds, max 30 rounds / 500,000 evaluations.

| Instance | Mean gap | Median gap | Worst gap | Mean evaluations |
| --- | ---: | ---: | ---: | ---: |
| tai12a | 8.897% | 8.039% | 11.616% | 31,635 |
| tai20a | 7.185% | 7.102% | 9.394% | 37,636 |
| tai25a | 5.249% | 5.980% | 6.174% | 41,636 |
| tai30a | 5.679% | 5.937% | 6.678% | 41,636 |
| berlin52 | 6.433% | 5.754% | 11.522% | 71,639 |
| kroA100 | 7.323% | 7.293% | 13.847% | 105,642 |
| kroB100 | 3.696% | 2.823% | 7.272% | 105,642 |
| ch150 | 8.229% | 8.517% | 10.463% | 171,649 |

## Interpretation

TSP Or-opt plus the convergence protocol materially improved the TSP lane. QAP remains swap-limited;
tai12a is a local optimum. This is converged transfer evidence, not a leadership claim.

## Verification

- 40/40 replay exact.
- Sphinx `-W`, tests, and workflow validator pass.
