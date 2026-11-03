# WS4 TSA24 GPU-GA benchmark

First WS4 architecture benchmark record.

- Instance: TSA24 compiled landscape, current even-flow target file
- Solver: WS4 GPU-GA, population 64, 1,000 generations, seed 7
- GPU objective: **8588725.370498415**
- Exact CPU replay: **8588725.370498514**
- Schedule: `schedule.csv`
- Schedule SHA-256: verified in `record.json`
- Search elapsed: **9.381 s**
- Wall: **23.13 s**
- Blocks: 208,255
- Initial seed objective: **1,722,144,291.336651**
- Improvement from seed: about **200×** in objective (not a controlled baseline)

Target details: even flow ±1%, weight 10,000; harvest levels priority 1, weight 100,
`normalization: auto`, minimum 70,000,000 per period.

This is an architecture benchmark, not a FHOPS comparison. The TSA24 instance is a local
reconstructable fixture, not a public dataset.

Replay:

```bash
PYTHONPATH="$WS4_GPU_ROOT" python evidence/ws4-tsa24-gpu-ga-1000-r7/replay.py
```
