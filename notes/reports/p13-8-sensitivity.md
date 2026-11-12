# P13.8 sensitivity and statistical analysis

Status: partial; no target-weight sensitivity yet
Date: 2026-11-09
Issue: #89

## Completed

- QAP 50k vs 100k patience: 50k was not convergence-stable; two seeds improved at 100k. Final
  evidence uses 100k and ten seeds.
- BLS 5-seed vs 10-seed: mean gap 0.116% vs 0.096% over the 20-instance panel; conclusions stable.
- TSP 2,000-kick/200-patience vs 10,000-kick/1,000-patience: the short panel was not converged on
  `ch150`; the deep panel reaches all 20 optima.
- TSP 20-instance breadth panel: 95/100 patience, five `brazil58` cap hits at the known optimum,
  94/100 optima, mean 0.004%, worst 0.185%.
- BLS vs tabu paired difference: mean -0.158 points, bootstrap 95% CI -0.222 to -0.094; BLS lower on
  57 of 64 non-tied seed-level pairs. The instances are not independent, so this is descriptive.

- TSA24 target-variant screen: five published target files, 1,000 SA iterations, same seed/start.
  Objectives range from $1.714\times10^9$ to 1,010. This is a target-sensitivity screen, **not** a
  converged comparison; the main 100k campaign is only for `evenflow_tsa24`.
- No matched wall-clock sensitivity for BLS vs tabu.

The screen is evidence that target construction dominates the objective scale, not a ranking of
targets. A full-budget target sensitivity remains future work.
