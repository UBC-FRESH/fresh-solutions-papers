# Paper 1 CPU-SA baseline

Status: independent-search baseline; time-limited, not converged
Date: 2026-11-02
Record: `evidence/ws4-tsa24-cpu-sa-100000-r7/record.json`

## Result

- Algorithm: WS4 CPU simulated annealing (`ws4@f23d450`), 32 threads.
- Model/target: frozen TSA24 even-flow.
- Budget: 100,000 iterations, 30-minute cap.
- Objective: **335,044,976.675435**.
- Exact replay: **335,044,976.675435**.
- Wall: 1,875.12 s; memory: 8,969 MB.
- Stop: time limit reached; **not converged**.

## Comparison

| Record | Objective | Wall |
| --- | ---: | ---: |
| CPU-SA 100k | 335,044,976.675 | 1,875 s |
| GPU-GA 1,000 | 8,588,725.370 | 23.13 s |
| GPU-GA 10,000 | 76,540.740733 | 157.34 s |

CPU-SA is an independent search on the same model, not an independent model. It is not
equal-time, and it is not converged. It is a defensible baseline, but not a controlled
proof of universal GPU superiority.

## Boundary

- Do not call this an optimized/converged landscape baseline.
- Do not compare it to FHOPS; FHOPS is a different operational problem.
- The next step is a converged independent baseline or a public landscape instance.
