# Container and clean replay notes

The evidence is designed for a Linux container with Python 3.12 and the packages in
`requirements-dev.txt`. The public TSA24 artifact and the pinned Fresh Solutions solver are external
inputs, not vendored here.

Minimal replay after the external inputs are mounted:

```bash
export WS4_ROOT=/path/to/ws4
export TSA24_ROOT=/path/to/extracted-tsa24-evenflow-v1
export QAPLIB_ROOT=/path/to/QAPLIB
export TSPLIB_ROOT=/path/to/tsplib
python3 paper2/check_evidence.py
python3 paper2/replay_framework_use.py
python3 paper2/replay_tsp_convergence.py
```

The base image is pinned to a digest and the solver checkout is pinned to `4583ad3`; the remaining
release item is a tested container run with the TSA24 release tarball mounted.
