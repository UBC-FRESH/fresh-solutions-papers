# Container and clean replay notes

The evidence is designed for a Linux container with Python 3.12 and the packages in
`requirements-dev.txt`. The public TSA24 artifact and the pinned Fresh Solutions solver are external
inputs, not vendored here.

Minimal replay after the external inputs are mounted:

```bash
export WS4_ROOT=/path/to/ws4
export TSA24_ROOT=/path/to/femic-tsa24-instance
export QAPLIB_ROOT=/path/to/QAPLIB
export TSPLIB_ROOT=/path/to/tsplib
python3 paper2/check_evidence.py
python3 paper2/replay_framework_use.py
python3 paper2/replay_tsp_convergence.py
```

A full container recipe is not yet claimed. The missing pieces are the exact base image digest, the
solver submodule checkout, and the TSA24 artifact mount point.
