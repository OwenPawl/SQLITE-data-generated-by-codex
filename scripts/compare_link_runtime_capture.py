#!/usr/bin/env python3
import argparse
import base64
import json
import sqlite3
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--captured-output", type=Path, required=True)
    parser.add_argument("--summary-output", type=Path, required=True)
    args = parser.parse_args()

    captured = None
    for line in args.log.read_text().splitlines():
        if line.startswith('[{"bundleIdentifier"'):
            captured = json.loads(line)
    if captured is None:
        raise RuntimeError("no registration JSON found in LLDB log")

    args.captured_output.write_text(
        json.dumps(captured, indent=2, sort_keys=True) + "\n"
    )
    runtime = {
        row["bundleIdentifier"]: base64.b64decode(row["installIdentifierBase64"])
        for row in captured
    }
    if len(runtime) != len(captured):
        raise RuntimeError("duplicate runtime bundle identifiers")

    uri = f"file:{args.database.resolve()}?mode=ro&immutable=1"
    with sqlite3.connect(uri, uri=True) as database:
        stored = dict(database.execute(
            "SELECT containerId, installIdentifier FROM LinkState"
        ))

    mismatches = [
        {
            "bundleIdentifier": bundle,
            "storedHex": stored[bundle].hex(),
            "runtimeHex": runtime[bundle].hex(),
        }
        for bundle in sorted(stored.keys() & runtime.keys())
        if stored[bundle] != runtime[bundle]
    ]
    summary = {
        "databaseRows": len(stored),
        "runtimeRegistrations": len(runtime),
        "exactMatches": sum(
            stored[bundle] == runtime[bundle]
            for bundle in stored.keys() & runtime.keys()
        ),
        "missingAtRuntime": sorted(stored.keys() - runtime.keys()),
        "runtimeOnly": sorted(runtime.keys() - stored.keys()),
        "mismatches": mismatches,
    }
    args.summary_output.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
