# Paper 2 convergence audit

Status: correction to P8 pilot evidence
Date: 2026-11-01

## Finding

The P8 five-seed table used 10,000 local iterations. A budget check shows that this is not a
convergence budget.

### tai12a

| Local iterations | Objective | Gap |
| ---: | ---: | ---: |
| 10,000 | 241,016 | 7.397% |
| 50,000 | 241,016 | 7.397% |
| 100,000 | 241,016 | 7.397% |
| 250,000 | 241,016 | 7.397% |

The search is converged to a **local optimum** under the current swap neighborhood. More of the same
search does not close the gap.

### ch150

| Local iterations | Objective | Gap |
| ---: | ---: | ---: |
| 10,000 | 10,550 | 61.612% |
| 50,000 | 7,556 | 15.748% |
| 100,000 | 7,323 | 12.178% |
| 250,000 | 7,323 | 12.178% |

The 10k point is severely under-converged. The search appears to plateau around 100k under the current
2-opt neighborhood, at a 12.178% gap.

## Consequence

The P8 five-seed table must be labelled **pilot / under-converged**, not a final benchmark result. It
does not establish solver quality and cannot support a leadership or “close to optimum” claim.

The safe claims are:

- the adapters and replay contract work;
- all 40 assignments replay exactly;
- the engine reaches local optima within the tested budgets;
- QAP/TSP quality is limited by neighborhood design, not accounting.

Unsafe claims:

- “within 7.4% of optimum” as a converged result;
- “within 19.8%” for TSP;
- any comparison to published heuristic performance.

## Required next step

For every reported instance:

1. define a convergence rule (no improvement over a fixed evaluation budget, or stable objective across
   repeated restarts);
2. run at least three independent seeds to that rule;
3. report the budget used;
4. add stronger neighborhoods where the plateau is unacceptable (QAP robust tabu / TSP Or-opt or 3-opt);
5. only then populate a final results table.

## Resolution

The P9 converged campaign replaces the pilot table. All 40 runs stopped on patience and replay exactly;
see `paper2/evidence/converged-summary.json`.
