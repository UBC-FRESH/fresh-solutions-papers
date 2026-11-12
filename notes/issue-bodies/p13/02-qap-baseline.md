# P13.2: Independent QAP baseline

Parent: #81

## Why

SciPy FAQ is a weak baseline and a reviewer will say so.

## Work

- [ ] Implement or port a published-style QAP baseline: Breakout Local Search or Ro-TS.
- [ ] Run it on the 20-instance expanded panel with the same seeds, budget, and stopping rule.
- [ ] Record full distribution, wall/CPU time, and exact replay.
- [ ] Add a fair comparison table, including cases where the baseline wins.
- [ ] Update the claim boundary.

## Acceptance

- Baseline code, runner, evidence, replay, and table are committed.
- The baseline is not a straw man and is not described as state-of-the-art without support.
- The comparison uses one statistic per claim.
