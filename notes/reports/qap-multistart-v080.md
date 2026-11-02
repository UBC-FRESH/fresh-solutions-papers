# Large-QAP multi-start tabu — patience-converged

Status: converged under the declared patience rule
Date: 2026-11-02
Solver: Fresh Solutions branch `v0.8.0` (delta-matrix tabu)

## Protocol

- Four QAPLIB instances with `n > 100`: `esc128`, `tai150b`, `tai256c`, `tho150`.
- Five random starts per instance.
- Robust tabu with delta-matrix updates, 10,000-iteration patience.
- **No time cap.** Every run stopped on patience.
- Exact replay through the Fresh Solutions QAP adapter.

## Results

| Instance | Best gap | Mean gap | Patience stops |
| --- | ---: | ---: | ---: |
| esc128 | **0.000%** | 1.250% | 5/5 |
| tai150b | **2.008%** | 2.976% | 5/5 |
| tai256c | **0.350%** | 0.413% | 5/5 |
| tho150 | **0.166%** | 0.507% | 5/5 |

All **20/20** assignments replay exactly. The campaign completed in 8m39s wall
with 20 runs across 8 workers. The previous identity-start runs were cap hits;
these are true patience stops.

## Interpretation

Multi-start plus the O(n²) delta-matrix update changed the large-QAP result from
cap-limited to converged under the declared patience. `tai256c` is still the
weakest large instance at 0.350% best gap; that is a real remaining gap, not a
timeout artifact.

## Boundary

- Robust tabu remains the heuristic; multi-start is a portfolio.
- Patience is a plateau rule, not a proof of global optimality.
- No independent QAP solver baseline is included here.

## Independent baseline

SciPy FAQ (`quadratic_assignment`, `maxiter=10000`, SciPy 1.18.1) is an
independent external baseline on the same four large instances. It is fast but
mixed in quality:

| Instance | SciPy FAQ mean gap | Fresh tabu best gap |
| --- | ---: | ---: |
| esc128 | 12.500% | 0.000% |
| tai150b | 1.861% | 2.008% |
| tai256c | 120.481% | 0.350% |
| tho150 | 1.523% | 0.166% |

SciPy wins on `tai150b` and `tho150`; Fresh tabu wins decisively on `esc128`
and `tai256c`. This is a mixed time-quality result, not a universal dominance
claim. All 20 SciPy assignments replay exactly.
