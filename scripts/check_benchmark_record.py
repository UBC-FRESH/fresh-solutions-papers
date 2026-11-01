#!/usr/bin/env python3
"""Validate a benchmark record and its exact-replay schedule hash."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, cast

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "benchmark-record.schema.json"


def sha256_file(path: Path) -> str:
    """Return the SHA-256 digest of one file.

    Parameters
    ----------
    path : Path
        File to hash.

    Returns
    -------
    str
        Lowercase hexadecimal digest.
    """
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_schema(path: Path = DEFAULT_SCHEMA) -> dict[str, Any]:
    """Load the benchmark-record JSON schema.

    Parameters
    ----------
    path : Path, optional
        Schema path. Defaults to the repository schema.

    Returns
    -------
    dict of str to object
        Parsed schema.
    """
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def resolve_schedule(record_path: Path, schedule_path: str, root: Path | None) -> Path:
    """Resolve a recorded schedule path relative to the record or a root.

    Parameters
    ----------
    record_path : Path
        Benchmark record path.
    schedule_path : str
        Path stored in the record.
    root : Path or None
        Optional schedule root.

    Returns
    -------
    Path
        Resolved schedule path.
    """
    path = Path(schedule_path)
    if path.is_absolute():
        return path
    return (root if root is not None else record_path.parent) / path


def validate_record(
    record_path: Path,
    *,
    schedule_root: Path | None = None,
    schema_path: Path = DEFAULT_SCHEMA,
) -> dict[str, Any]:
    """Validate one record against the schema and replay hash gate.

    Parameters
    ----------
    record_path : Path
        Record JSON path.
    schedule_root : Path or None, optional
        Root for relative schedule paths.
    schema_path : Path, optional
        JSON schema path.

    Returns
    -------
    dict of str to object
        Validated record.

    Raises
    ------
    ValueError
        When the schema, replay flag, schedule, or hash is invalid.
    """
    payload = cast(dict[str, Any], json.loads(record_path.read_text(encoding="utf-8")))
    try:
        jsonschema.validate(payload, load_schema(schema_path))
    except jsonschema.ValidationError as error:
        raise ValueError(f"record does not match schema: {error.message}") from error
    result = payload["result"]
    if not result["exact_replay"]:
        raise ValueError("record reports exact_replay=false; it is not evidence")
    schedule = resolve_schedule(record_path, str(result["schedule_path"]), schedule_root)
    if not schedule.is_file():
        raise ValueError(f"schedule does not exist: {schedule}")
    digest = sha256_file(schedule)
    if digest != result["schedule_sha256"]:
        raise ValueError("schedule hash does not match result.schedule_sha256")
    return payload


def main(argv: list[str] | None = None) -> int:
    """Validate a benchmark record from the command line.

    Parameters
    ----------
    argv : list of str or None, optional
        Arguments. None reads ``sys.argv``.

    Returns
    -------
    int
        Zero when the record and schedule hash are valid.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path, help="Benchmark record JSON")
    parser.add_argument("--schedule-root", type=Path, default=None)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args(argv)
    try:
        record = validate_record(
            args.record,
            schedule_root=args.schedule_root,
            schema_path=args.schema,
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"INVALID: {error}")
        return 1
    print(f"VALID: {record['record_id']} ({record['instance']['id']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
