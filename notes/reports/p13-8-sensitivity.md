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

## Not completed

- Target-weight and level-aspiration sensitivity for TSA24.
- Seed-count sensitivity for the full tabu panel (only 5 seeds; framework panel has 10 on four
  instances).
- Matched wall-clock sensitivity for BLS vs tabu.

No claim of full statistical generality is made.
