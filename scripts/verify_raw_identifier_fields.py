#!/usr/bin/env python3
"""Round-trip flattened identifier bytes through their native State messages."""

from __future__ import annotations

import base64
import hashlib
import json
import sqlite3
import subprocess
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parents[1]
DB_PATH = RUN_DIR / "inputs/raw/Tools-active.sqlite"
DECODER_PATH = RUN_DIR / "runtime/toolkit_native_decoder"
OUTPUT_PATH = RUN_DIR / "decoded/raw_identifier_field_verification.jsonl"
SUMMARY_PATH = RUN_DIR / "decoded/raw_identifier_field_summary.json"
BATCH_PATH = RUN_DIR / "runtime/raw_identifier_batch.ndjson"

FAMILIES = (
    {
        "table": "LaunchServicesState",
        "key_column": "bundleId",
        "bytes_column": "persistentIdentifier",
        "schema": "ToolKitProtoLaunchServicesSnapshot.State",
        "json_key": "bundleId",
        "json_bytes": "persistentIdentifier",
    },
    {
        "table": "LinkState",
        "key_column": "containerId",
        "bytes_column": "installIdentifier",
        "schema": "ToolKitProtoLinkSnapshot.State",
        "json_key": "containerId",
        "json_bytes": "installIdentifier",
    },
)


def varint(value: int) -> bytes:
    output = bytearray()
    while value >= 0x80:
        output.append((value & 0x7F) | 0x80)
        value >>= 7
    output.append(value)
    return bytes(output)


def length_delimited(number: int, value: bytes) -> bytes:
    return varint((number << 3) | 2) + varint(len(value)) + value


def run_batch(requests: list[dict[str, str]]) -> dict[str, dict[str, Any]]:
    process = subprocess.run(
        [str(DECODER_PATH), "batch"],
        input="".join(json.dumps(item, sort_keys=True) + "\n" for item in requests),
        text=True,
        capture_output=True,
        check=False,
    )
    if process.returncode:
        raise RuntimeError(process.stderr.strip())
    return {
        response["id"]: response
        for response in map(json.loads, process.stdout.splitlines())
    }


def main() -> None:
    connection = sqlite3.connect(f"file:{DB_PATH}?mode=ro&immutable=1", uri=True)
    connection.execute("PRAGMA query_only=ON")
    sources: dict[str, dict[str, Any]] = {}
    requests = []
    for family in FAMILIES:
        query = (
            f'SELECT rowid, "{family["key_column"]}", '
            f'"{family["bytes_column"]}" FROM "{family["table"]}" ORDER BY rowid'
        )
        for rowid, key, raw_value in connection.execute(query):
            raw = bytes(raw_value)
            wrapped = length_delimited(1, key.encode()) + length_delimited(2, raw)
            request_id = f'{family["table"]}:rowid={rowid}'
            sources[request_id] = {
                **family,
                "rowid": rowid,
                "key": key,
                "raw_hex": raw.hex(),
                "raw_sha256": hashlib.sha256(raw).hexdigest(),
                "wrapped_hex": wrapped.hex(),
            }
            requests.append(
                {"id": request_id, "type": family["schema"], "hex": wrapped.hex()}
            )
    connection.close()

    BATCH_PATH.write_text(
        "".join(json.dumps(item, sort_keys=True) + "\n" for item in requests)
    )

    responses = run_batch(requests)
    counts = {family["table"]: 0 for family in FAMILIES}
    failures = []
    with OUTPUT_PATH.open("w") as stream:
        for request_id in sorted(sources):
            source = sources[request_id]
            response = responses[request_id]
            result = response.get("result")
            decoded = json.loads(result["json"]) if result else None
            expected = {
                source["json_key"]: source["key"],
                source["json_bytes"]: base64.b64encode(
                    bytes.fromhex(source["raw_hex"])
                ).decode(),
            }
            checks = {
                "native_decode_succeeded": result is not None and not response.get("error"),
                "decoded_json_equal": decoded == expected,
                "unknown_fields_empty": bool(result) and not result["unknownFieldsHex"],
                "wrapped_round_trip_equal": bool(result)
                and result["canonicalBinaryHex"].lower() == source["wrapped_hex"],
            }
            if not all(checks.values()):
                failures.append({"id": request_id, "checks": checks, "response": response})
            counts[source["table"]] += 1
            stream.write(
                json.dumps(
                    {
                        **source,
                        "decoded_json": decoded,
                        "checks": checks,
                        "error": response.get("error"),
                    },
                    sort_keys=True,
                )
                + "\n"
            )

    summary = {
        "row_count": len(sources),
        "family_counts": counts,
        "failure_count": len(failures),
        "all_native_decodes_succeeded": not failures,
        "interpretation": (
            "Each database BLOB is a raw bytes field flattened from the named "
            "ToolKit snapshot State message; it is not a standalone protobuf message."
        ),
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
