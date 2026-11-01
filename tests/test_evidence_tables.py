"""Tests for the evidence-table generator."""

from __future__ import annotations

import json
from pathlib import Path

from build_evidence_tables import load_records, main, markdown_table


def _record(root: Path, name: str, objective: float) -> None:
    """Write a minimal record directory."""
    root.mkdir(parents=True, exist_ok=True)
    directory = root / name
    directory.mkdir()
    record = {
        "schema_version": "1.0.0",
        "record_id": name,
        "instance": {"id": "instance"},
        "algorithm": {"name": "solver", "version": "1"},
        "run": {"wall_s": 1.0, "time_to_best_s": 0.5},
        "result": {"objective": objective, "exact_replay": True},
    }
    (directory / "record.json").write_text(json.dumps(record), encoding="utf-8")


def test_records_are_sorted_and_rendered(tmp_path: Path) -> None:
    """Records load in stable order and render every evidence column."""
    _record(tmp_path, "b-record", 2.0)
    _record(tmp_path, "a-record", 1.0)
    records = load_records(tmp_path)
    assert [record["record_id"] for record in records] == ["a-record", "b-record"]
    table = markdown_table(records)
    assert "a-record" in table
    assert "1.000000" in table
    assert "| True |" in table


def test_cli_writes_the_table(tmp_path: Path) -> None:
    """The command writes a Markdown table to the requested path."""
    _record(tmp_path / "evidence", "record", 1.0)
    output = tmp_path / "table.md"
    assert main(["--evidence", str(tmp_path / "evidence"), "--out", str(output)]) == 0
    assert output.read_text(encoding="utf-8").startswith("| Record |")
