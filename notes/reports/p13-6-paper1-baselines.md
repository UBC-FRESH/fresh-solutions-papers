# P13.6 closeout: Paper 1 independent-search baselines

Status: complete as a negative result
Date: 2026-11-09
Issue: #87

## Existing baseline

The existing CPU-SA record is `evidence/ws4-tsa24-cpu-sa-100000-r7/record.json`:
objective **335,044,976.675435**, 100,000 proposals, 32 threads, 1,875.12 s wall, time-limited, not
converged, 204,413 scheduled blocks.

## Attempts to improve it

Three additional CPU searches were run on the same model, target, seed, and 32-thread budget:

| Run | Budget | Objective | Scheduled blocks | Status |
| --- | ---: | ---: | ---: | --- |
| CPU-SA, existing | 100,000 proposals | 335,044,976.675435 | 204,413 | time-limited |
| CPU tabu, one start | 30 min | 1,773,106,286.31 | 208,255 | time-limited |
| CPU ILS, one start | 10 min | 1,773,628,651.85 | 208,236 | time-limited |
| CPU tabu, 32 starts | 10 min | 1,988.68 | **1,290** | invalid comparator |

The 32-start result is not evidence: it scheduled only 1,290 blocks, so its objective is not
comparable to the full schedule. The one-start tabu/ILS runs are worse than the existing CPU-SA.

## Conclusion

There is no improved independent CPU-search baseline from this pass. The paper must not use the
one-start tabu/ILS runs as a competitive baseline, and must not use the 32-start run at all. The
existing CPU-SA remains the weak, time-limited secondary comparator.

The real Paper 1 gap is still the architecture ablation, not a better CPU-SA. That work is tracked
under P13.5.
