#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 paper2/check_evidence.py
python3 paper2/replay_framework_use.py
python3 paper2/replay_tsp_convergence.py
python3 paper2/replay_qap_expanded.py
python3 paper2/replay_tsp_expanded.py
python3 paper2/replay_qap_bls.py
python3 paper2/replay_generic_tabu.py
