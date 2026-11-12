#!/usr/bin/env python3
"""Rerun the GEO TSPLIB broad-panel records after the parser fix."""

from __future__ import annotations

import gzip
import json
import multiprocessing
import os
import re
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

os.environ.setdefault("TSPLIB_ROOT", "benchmarks/tsplib")
ROOT = Path(__file__).resolve().parent

sys.path.insert(0, str(ROOT))
from run_broad_converged import run_tsp, tsp_optima  # noqa: E402

GEO = (
    "ali535",
    "burma14",
    "gr137",
    "gr202",
    "gr229",
    "gr431",
    "gr666",
    "gr96",
    "ulysses16",
    "ulysses22",
)
BROAD = ROOT / "evidence" / "broad-converged.json.gz"
TSP_ROOT = Path(os.environ["TSPLIB_ROOT"])


def main() -> int:
    """Rerun GEO instances and merge them into the broad evidence."""
    known = tsp_optima()
    tasks = []
    for name in GEO:
        if name not in known:
            continue
        text = (TSP_ROOT / f"{name}.tsp").read_text(errors="ignore")
        match = re.search(r"DIMENSION\s*:\s*(\d+)", text)
        size = int(match.group(1)) if match else 0
        tasks.extend((name, size, known[name], seed) for seed in range(1, 6))
    records = []
    with ProcessPoolExecutor(
        max_workers=min(40, os.cpu_count() or 1),
        mp_context=multiprocessing.get_context("spawn"),
    ) as executor:
        futures = {executor.submit(run_tsp, task): task for task in tasks}
        for index, future in enumerate(as_completed(futures), 1):
            records.append(future.result())
            if index % 10 == 0 or index == len(tasks):
                print(f"completed {index}/{len(tasks)}", flush=True)
    with gzip.open(BROAD, "rt", encoding="utf-8") as handle:
        all_records = json.load(handle)
    all_records = [
        record
        for record in all_records
        if not (record.get("family") == "tsp" and record.get("instance") in GEO)
    ]
    all_records.extend(records)
    all_records.sort(
        key=lambda record: (
            str(record.get("family")),
            str(record.get("instance")),
            record.get("seed", 0),
        )
    )
    with gzip.open(BROAD, "wt", encoding="utf-8") as handle:
        json.dump(all_records, handle)
    print(f"merged {len(records)} GEO records into {len(all_records)} broad records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
