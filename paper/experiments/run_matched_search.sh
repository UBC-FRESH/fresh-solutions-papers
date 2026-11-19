#!/usr/bin/env bash
# Reproduce the TSA24 matched CPU/CUDA search rows in Table 3.
# Requires WS4-GPU at $WS4_GPU_ROOT and the public TSA24 artifact paths.
set -euo pipefail
: "${WS4_GPU_ROOT:?set WS4_GPU_ROOT}"
: "${TSA24_ROOT:?set TSA24_ROOT}"
DATASET="${TSA24_ROOT}/build/compiled"
TARGETS="${TSA24_ROOT}/config/ws4/targets/evenflow_tsa24.yaml"
SEED="${TSA24_ROOT}/runtime/seed_oldest_first_tsa24.csv"
TABLE="${TSA24_ROOT}/runtime/gpu-effects/effects-lean.pt"
CACHE="${TSA24_ROOT}/runtime/gpu-cache"
for device in cpu cuda; do
  for generations in 1 10 100; do
    out="/tmp/tsa24-match-${device}-${generations}"
    rm -rf "${out}"
    PYTHONPATH="${WS4_GPU_ROOT}" python3 -c 'from ws4.cli import app; app()' gpu-run \
      --dataset "${DATASET}" --targets "${TARGETS}" --seed-schedule "${SEED}" \
      --table "${TABLE}" --cache-dir "${CACHE}" --out-dir "${out}" \
      --seeds 7 --population 64 --generations "${generations}" --device "${device}"
  done
done
