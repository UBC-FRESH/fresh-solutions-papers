# WS4 TSA24 100k-generation GPU-GA record

Scaled accelerated run on the full 208,255-block TSA24 landscape.

- Solver: WS4 GPU-GA, population 64, **100,000 generations**, seed 7
- Objective: **517.8619818205188**
- Exact CPU replay: **517.8619818205188**
- Search: 856.10 s; wall: 941.51 s; max RSS: 8,260 MB
- Schedules: identical across repeated runs
- 1,000-generation record: 8,588,725.370498
- 10,000-generation record: 76,540.740733
- CPU-SA 100k/30min baseline: 335,044,976.675435

Replay:

```bash
PYTHONPATH="$WS4_ROOT" python evidence/ws4-tsa24-gpu-ga-100000-r7/replay.py
```
