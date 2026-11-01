# P10.4 close-out: serious-budget policy

Status: complete
Date: 2026-11-01
Issue: #35

## Recommendation

Close P10.4. The policy is written and has been applied to the QAP competitive campaign. TSP and
Paper 1 remain internal until their matched baselines are complete.

## Policy artifact

`notes/reports/serious-budget-policy.md`

The policy requires:

- a pinned release/commit;
- public instance provenance and known optimum/best-known value;
- at least five seeds;
- a stated budget and stopping reason;
- exact replay;
- a budget-doubling check with a 0.10-percentage-point material-improvement threshold;
- the smallest certified budget, not a lucky larger run.

## Applied evidence

QAP robust tabu, Fresh Solutions v0.4.0:

| Instance | Certified budget | Mean gap | Replay |
| --- | ---: | ---: | --- |
| tai12a | 10,000 | 0.000% | exact |
| tai20a | 10,000 | 0.403% | exact |
| tai25a | 20,000 | 0.685% | exact |
| tai30a | 40,000 | 0.407% | exact |

Larger-budget checks are recorded in `paper2/evidence/qap-tabu-*-stability-summary.json`.

## Deviations and limits

- TSP converged runs use a patience rule but are not yet publication evidence because no matched
  baseline exists.
- Paper 1 still lacks a matched optimized landscape baseline; the seed-only comparison remains
  disallowed.
- One doubling is a minimum stopping rule, not a proof that no later improvement is possible.
- The policy does not require wall-clock parity across solvers; comparisons must state it.

## Next

P10.5 supplies the matched landscape baseline. P10.3 remains open for a stronger TSP neighborhood.
