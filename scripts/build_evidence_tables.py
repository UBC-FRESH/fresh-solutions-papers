#!/usr/bin/env python3
"""Build Markdown evidence tables from replayable benchmark records."""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any, cast


def load_records(evidence_root: Path) -> list[dict[str, Any]]:
    """Load every ``record.json`` below an evidence root.

    Parameters
    ----------
    evidence_root : Path
        Directory containing one subdirectory per evidence record.

    Returns
    -------
    list of dict
        Records sorted by record id.
    """
    records: list[dict[str, Any]] = []
    for path in sorted(evidence_root.glob("*/record.json")):
        records.append(cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8"))))
    return sorted(records, key=lambda record: str(record["record_id"]))


def _cell(value: object) -> str:
    """Render one table cell."""
    return str(value).replace("|", "\\|")


def markdown_table(records: Iterable[dict[str, Any]]) -> str:
    """Render records as a Markdown table.

    Parameters
    ----------
    records : iterable of dict
        Benchmark records.

    Returns
    -------
    str
        Markdown table.
    """
    lines = [
        "| Record | Instance | Algorithm | Objective | Replay | Wall s | Best s (est.) |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for record in records:
        result = record["result"]
        run = record["run"]
        algorithm = record["algorithm"]
        lines.append(
            "| "
            + " | ".join(
                [
                    _cell(record["record_id"]),
                    _cell(record["instance"]["id"]),
                    _cell(f"{algorithm['name']} {algorithm['version']}"),
                    f"{float(result['objective']):.6f}",
                    str(bool(result["exact_replay"])),
                    f"{float(run['wall_s']):.3f}",
                    f"{float(run['time_to_best_s']):.3f}",
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    """Write the evidence table.

    Parameters
    ----------
    argv : list of str or None, optional
        Arguments. None reads ``sys.argv``.

    Returns
    -------
    int
        Zero on success.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, default=Path("evidence"))
    parser.add_argument("--out", type=Path, default=Path("paper/tables/evidence.md"))
    args = parser.parse_args(argv)
    records = load_records(args.evidence)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(markdown_table(records), encoding="utf-8")
    print(f"wrote {args.out} ({len(records)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
