# Paper 2 framework-use results

Status: final QAP and TSP evidence complete
Date: 2026-11-03
Issue: #76

## QAP comparison

Protocol: `notes/reports/paper2-framework-use-protocol.md`.

- Ten seeds per instance.
- 100,000-iteration patience, 1,000,000-iteration cap.
- Forty worker processes.
- Framework path: `ResidentAssignment` apply/evaluate plus the delta-matrix scan.
- Standalone path: private-array delta-matrix scan.
- Production path: `run_qap_tabu` accelerated path.
- Execution order alternated by seed (20 baseline-first, 20 framework-first).

All **40/40** runs stopped on `patience`, all **40/40** framework objectives matched the standalone
and production objectives exactly, and all **40/40** incumbents replayed exactly through the adapter.

| Instance | Mean gap | Median gap | Worst gap | Mean iterations | CPU ratio | Wall ratio |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| tai12a | 0.000% | 0.000% | 0.000% | 100,186 | 1.327 | 1.319 |
| tai20a | 0.030% | 0.000% | 0.304% | 147,748 | 1.170 | 1.155 |
| tai25a | 0.077% | 0.000% | 0.402% | 175,611 | 1.181 | 1.135 |
| tai30a | 0.245% | 0.391% | 0.491% | 161,046 | 1.279 | 1.282 |

Overall CPU overhead: **1.239×** (95% bootstrap CI **1.168–1.310**). Overall wall overhead:
**1.231×** (95% CI **1.163–1.300**).

The 50k-patience run was not convergence-stable. On three seeds per instance, 100k patience improved
`tai20a` seed 1 by 2,140 objective units and `tai25a` seed 2 by 8,042 units. All 12 sensitivity runs
stopped on patience. The final evidence therefore uses 100k patience and ten seeds.

## Budget comparison

| Instance | Fixed 10k mean | 100k-patience mean | Optima in 10 seeds |
| --- | ---: | ---: | ---: |
| tai12a | 0.000% | 0.000% | 10/10 |
| tai20a | 0.403% | 0.030% | 9/10 |
| tai25a | 0.786% | 0.077% | 8/10 |
| tai30a | 0.792% | 0.245% | 4/10 |

The comparison is descriptive: the runs use different stopping rules and seed counts. It supports the
statement that the old fixed-budget table is not a per-run convergence table.

## TSP

The final campaign uses 10,000 kicks with 1,000-kick patience, five seeds:

| Instance | Runs | Mean gap | Worst gap | Plateau-stopped | Mean wall |
| --- | ---: | ---: | ---: | ---: | ---: |
| berlin52 | 5 | 0.000% | 0.000% | 5/5 | 754.3 s |
| kroA100 | 5 | 0.000% | 0.000% | 5/5 | 605.0 s |
| kroB100 | 5 | 0.000% | 0.000% | 5/5 | 688.4 s |
| ch150 | 5 | 0.000% | 0.000% | 5/5 | 603.9 s |

All 20/20 incumbents replay exactly.

The 2,000-kick/200-patience check reached 19/20 optima and a 0.077% worst gap on `ch150`. The
20-kick pilot reached the optimum on three of four instances (15/20 runs) and a 0.383% mean gap on `ch150`. Neither is the convergence table.

The TSP resident-state check replays the 20 existing ILK incumbents exactly. It is a contract check,
not the TSP convergence campaign above.

## Current claim boundary

Allowed:

- The framework-managed QAP path reproduces the standalone trajectory exactly on this panel.
- State management costs about 1.24× CPU time on this panel.
- The 100k QAP and 10k TSP campaigns are plateau-stopped, exact-replay evidence.
- The old fixed-budget QAP table and the 20-kick TSP table are not convergence evidence.

Not allowed:

- Global optimality.
- State-of-the-art QAP/TSP performance.
- A generic-engine search claim.
- A tag, release, or submission without maintainer approval.
