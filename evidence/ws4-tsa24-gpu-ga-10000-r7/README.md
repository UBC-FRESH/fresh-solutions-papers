# WS4 TSA24 10k-generation scaling baseline

Same-engine scaling baseline for `ws4-tsa24-gpu-ga-1000-r7`, not an independent solver.

- Instance: TSA24 compiled landscape, even-flow target file
- Solver: WS4 GPU-GA, population 64, **10,000 generations**, seed 7
- Objective: **76,540.74073269201**
- 1,000-generation record: 8,588,725.370498415
- Exact CPU replay: **76,540.74073269201**
- Search: 89.78 s; wall: 157.34 s; max RSS: 8,256 MB
- Schedule SHA-256: `cd430e634b35b320ee404ba75fecb739afa2f585daaee041af97ff6172a914b8`
- Two independent runs produced the identical schedule hash.

Replay:

```bash
PYTHONPATH=/srv/shared-data/gep/ws4/ws4 python evidence/ws4-tsa24-gpu-ga-10000-r7/replay.py
```

The comparison is a same-engine budget scaling, not an independent algorithm baseline.
