#!/usr/bin/env bash
set -euo pipefail
: "${TSA24_ROOT:?set TSA24_ROOT to the public TSA24 artifact}"
for record in evidence/*/record.json; do
  python3 scripts/check_benchmark_record.py "$record"
done
