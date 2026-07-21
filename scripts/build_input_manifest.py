#!/usr/bin/env python3

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def file_record(path: Path) -> dict:
    stat = path.stat()
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return {
        "path": str(path),
        "size": stat.st_size,
        "mode": oct(stat.st_mode & 0o7777),
        "mtime_ns": stat.st_mtime_ns,
        "sha256": digest.hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-document", type=Path, required=True)
    parser.add_argument("--source-active", type=Path, required=True)
    parser.add_argument("--snapshot-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    active_lstat = args.source_active.lstat()
    database = args.source_active.resolve(strict=True)
    source_paths = {
        "starting_document": args.source_document,
        "database": database,
        "database_shm": Path(f"{database}-shm"),
        "database_wal": Path(f"{database}-wal"),
        "database_lock": Path(f"{database}.lock"),
    }
    snapshot_paths = {
        "starting_document": args.snapshot_dir / "starting_document.md",
        "database": args.snapshot_dir / "Tools-active.sqlite",
        "database_shm": args.snapshot_dir / "Tools-active.sqlite-shm",
        "database_wal": args.snapshot_dir / "Tools-active.sqlite-wal",
        "database_lock": args.snapshot_dir / "Tools-active.sqlite.lock",
    }

    records = {}
    for name, source_path in source_paths.items():
        snapshot_path = snapshot_paths[name]
        source = file_record(source_path)
        snapshot = file_record(snapshot_path)
        records[name] = {
            "source": source,
            "snapshot": snapshot,
            "content_match": source["sha256"] == snapshot["sha256"],
            "size_match": source["size"] == snapshot["size"],
        }

    manifest = {
        "schema_version": "toolkit_input_snapshot.v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_active": {
            "path": str(args.source_active),
            "is_symlink": args.source_active.is_symlink(),
            "symlink_target": os.readlink(args.source_active),
            "lstat_size": active_lstat.st_size,
            "lstat_mtime_ns": active_lstat.st_mtime_ns,
            "resolved_path": str(database),
        },
        "records": records,
        "all_content_matches": all(item["content_match"] for item in records.values()),
        "snapshot_read_only": all(
            (item["snapshot"]["mode"] == "0o444") for item in records.values()
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
