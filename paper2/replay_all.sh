#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 paper2/check_evidence.py
python3 paper2/replay_framework_use.py
python3 paper2/replay_tsp_convergence.py
