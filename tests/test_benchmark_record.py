"""Tests for the benchmark-record schema and hash gate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from check_benchmark_record import main, validate_record


def _record(tmp_path: Path, *, exact_replay: bool = True, bad_hash: bool = False) -> Path:
    """Write a minimal valid record and return its path."""
    schedule = tmp_path / "schedule.csv"
    schedule.write_text("block_id,treatment,offset\n1,CC,0\n", encoding="utf-8")
    digest = hashlib.sha256(schedule.read_bytes()).hexdigest()
    record = {
        "schema_version": "1.0.0",
        "record_id": "test-1",
        "source": {"citation": "Test", "doi": None, "url": None},
        "instance": {
            "id": "test",
            "availability": "public",
            "license": "MIT",
            "variables": 1,
            "periods": 1,
            "options": 2,
        },
        "problem": {
            "objective": "minimize cost",
            "constraints": [],
            "feasibility": "one assignment",
        },
        "algorithm": {
            "name": "test",
            "version": "1",
            "config": {},
            "deterministic": True,
        },
        "run": {
            "seed": 1,
            "hardware": "test",
            "software": "test",
            "time_to_first_feasible_s": 0.0,
            "time_to_best_s": 0.0,
            "wall_s": 0.0,
            "memory_mb": 0.0,
        },
        "result": {
            "objective": 0.0,
            "feasible": True,
            "schedule_sha256": "0" * 64 if bad_hash else digest,
            "schedule_path": schedule.name,
            "exact_replay": exact_replay,
            "target_penalties": {},
        },
    }
    path = tmp_path / "record.json"
    path.write_text(json.dumps(record), encoding="utf-8")
    return path


def test_valid_record_and_schedule_hash(tmp_path: Path) -> None:
    """A matching schedule hash and exact replay pass the gate."""
    record = validate_record(_record(tmp_path))
    assert record["record_id"] == "test-1"


def test_schedule_root_is_honoured(tmp_path: Path) -> None:
    """A relative schedule path can be resolved from a separate root."""
    record_path = _record(tmp_path)
    assert validate_record(record_path, schedule_root=tmp_path)["instance"]["id"] == "test"


def test_false_replay_is_rejected(tmp_path: Path) -> None:
    """A record that did not replay exactly cannot be evidence."""
    with pytest.raises(ValueError, match="exact_replay=false"):
        validate_record(_record(tmp_path, exact_replay=False))


def test_hash_mismatch_is_rejected(tmp_path: Path) -> None:
    """A schedule whose bytes do not match the recorded hash fails."""
    with pytest.raises(ValueError, match="hash"):
        validate_record(_record(tmp_path, bad_hash=True))


def test_missing_schedule_is_rejected(tmp_path: Path) -> None:
    """A record whose schedule path is absent fails."""
    path = _record(tmp_path)
    (tmp_path / "schedule.csv").unlink()
    with pytest.raises(ValueError, match="does not exist"):
        validate_record(path)


def test_cli_success_and_failure(tmp_path: Path) -> None:
    """The command-line entry point reports valid and invalid records."""
    valid = _record(tmp_path)
    assert main([str(valid)]) == 0
    invalid = _record(tmp_path, exact_replay=False)
    assert main([str(invalid)]) == 1
