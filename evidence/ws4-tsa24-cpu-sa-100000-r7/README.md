# WS4 TSA24 CPU simulated-annealing baseline

Independent-search baseline on the frozen TSA24 model.

- Solver: WS4 CPU simulated annealing (`ws4@f23d450`)
- Budget: 100,000 iterations, 30-minute limit
- Objective: **335,044,976.675435**
- Stop: time limit reached; **not converged**
- Exact CPU replay: **335,044,976.675435**
- GPU-GA 1,000-generation record: 8,588,725.370498
- GPU-GA 10,000-generation record: 76,540.740733

This is an independent search on the same WS4 model and target, not an
independent model or an equal-time comparison. It is a baseline, not a claim
that CPU-SA is competitive.

Replay:

```bash
PYTHONPATH=/srv/shared-data/gep/ws4/ws4 python evidence/ws4-tsa24-cpu-sa-100000-r7/replay.py
```
