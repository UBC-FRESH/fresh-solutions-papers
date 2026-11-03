#!/usr/bin/env bash
set -euo pipefail
: "${WS4_ROOT:?set WS4_ROOT to the pinned ws4 checkout}"
: "${TSA24_ROOT:?set TSA24_ROOT to the public TSA24 artifact}"
for record in evidence/*/record.json; do
  python3 scripts/check_benchmark_record.py --replay "$record"
done
