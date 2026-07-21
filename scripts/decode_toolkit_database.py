#!/usr/bin/env python3
"""Decode every populated BLOB instance using the live ToolKit protobuf runtime."""

from __future__ import annotations

import hashlib
import json
import sqlite3
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


RUN_DIR = Path(__file__).resolve().parents[1]
DB_PATH = RUN_DIR / "inputs/raw/Tools-active.sqlite"
INVENTORY_PATH = RUN_DIR / "coverage/blob_instances.jsonl"
DECODER_PATH = RUN_DIR / "runtime/toolkit_native_decoder"
OUTPUT_DIR = RUN_DIR / "decoded"


DIRECT_SCHEMAS = {
    ("EntityProperties", "typeInstance"): "ToolKitProtoTypeInstance",
    ("Parameters", "typeInstance"): "ToolKitProtoTypeInstance",
    ("TriggerParameters", "typeInstance"): "ToolKitProtoTypeInstance",
    ("Tools", "outputTypeInstance"): "ToolKitProtoTypeInstance",
    ("Triggers", "outputTypeInstance"): "ToolKitProtoTypeInstance",
    ("SystemToolProtocols", "protocol"): "ToolKitProtoSystemToolProtocol",
    ("SystemTypeProtocols", "protocol"): "ToolKitProtoSystemTypeProtocol",
    (
        "Tools",
        "customIcon",
    ): "ToolKitProtoToolDefinition.Version1.ToolIcon",
    ("TypeCoercions", "coercionDefinition"): "ToolKitProtoCoercionDefinition",
    ("Types", "id"): "ToolKitProtoTypeIdentifier",
}

REPEATED_MESSAGE_SCHEMAS = {
    (
        "Parameters",
        "relationships",
    ): "ToolKitProtoToolDefinition.Version1.Parameter.Relationship",
    (
        "TriggerParameters",
        "relationships",
    ): "ToolKitProtoToolDefinition.Version1.Parameter.Relationship",
    (
        "PredicateTemplates",
        "comparison",
    ): "ToolKitProtoComparisonPredicate.Template",
    ("Tools", "requirements"): "ToolKitProtoRuntimeRequirement",
    ("Triggers", "requirements"): "ToolKitProtoRuntimeRequirement",
    ("Types", "runtimeRequirements"): "ToolKitProtoRuntimeRequirement",
}

REPEATED_STRING_SCHEMAS = {
    ("EnumerationCases", "synonyms"),
    ("TypeDisplayRepresentations", "synonyms"),
}

RAW_IDENTIFIER_FIELDS = {
    ("LaunchServicesState", "persistentIdentifier"): {
        "containing_schema": "ToolKitProtoLaunchServicesSnapshot.State",
        "field_number": 2,
        "field_name": "persistentIdentifier",
    },
    ("LinkState", "installIdentifier"): {
        "containing_schema": "ToolKitProtoLinkSnapshot.State",
        "field_number": 2,
        "field_name": "installIdentifier",
    },
}


class WireError(ValueError):
    pass


@dataclass(frozen=True)
class WireField:
    number: int
    wire_type: int
    raw: bytes
    payload: bytes | None


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_varint(data: bytes, offset: int) -> tuple[int, int]:
    value = 0
    shift = 0
    start = offset
    while offset < len(data) and shift < 70:
        byte = data[offset]
        offset += 1
        value |= (byte & 0x7F) << shift
        if not byte & 0x80:
            if offset - start > 1 and byte == 0:
                raise WireError("non-canonical varint")
            return value, offset
        shift += 7
    raise WireError("truncated or oversized varint")


def parse_wire(data: bytes) -> list[WireField]:
    fields: list[WireField] = []
    offset = 0
    while offset < len(data):
        start = offset
        key, offset = read_varint(data, offset)
        number = key >> 3
        wire_type = key & 7
        if number == 0:
            raise WireError("field number zero")
        payload = None
        if wire_type == 0:
            _, offset = read_varint(data, offset)
        elif wire_type == 1:
            offset += 8
        elif wire_type == 2:
            length, offset = read_varint(data, offset)
            end = offset + length
            if end > len(data):
                raise WireError("truncated length-delimited field")
            payload = data[offset:end]
            offset = end
        elif wire_type == 5:
            offset += 4
        else:
            raise WireError(f"unsupported wire type {wire_type}")
        if offset > len(data):
            raise WireError("truncated fixed-width field")
        fields.append(WireField(number, wire_type, data[start:offset], payload))
    return fields


def repeated_field_one_payloads(data: bytes) -> tuple[list[bytes], list[dict[str, Any]]]:
    payloads = []
    unknown = []
    for field in parse_wire(data):
        if field.number == 1 and field.wire_type == 2 and field.payload is not None:
            payloads.append(field.payload)
        else:
            unknown.append(
                {
                    "field_number": field.number,
                    "wire_type": field.wire_type,
                    "raw_hex": field.raw.hex(),
                }
            )
    return payloads, unknown


def decode_synonym_item(data: bytes) -> dict[str, Any]:
    fields = parse_wire(data)
    values = []
    unknown = []
    for field in fields:
        if field.number == 1 and field.wire_type == 2 and field.payload is not None:
            try:
                values.append(field.payload.decode("utf-8"))
            except UnicodeDecodeError as error:
                unknown.append(
                    {
                        "field_number": 1,
                        "wire_type": 2,
                        "raw_hex": field.raw.hex(),
                        "error": str(error),
                    }
                )
        else:
            unknown.append(
                {
                    "field_number": field.number,
                    "wire_type": field.wire_type,
                    "raw_hex": field.raw.hex(),
                }
            )
    return {"strings": values, "unknown_fields": unknown}


def load_inventory() -> list[dict[str, Any]]:
    with INVENTORY_PATH.open() as stream:
        return [json.loads(line) for line in stream]


def fetch_blob(connection: sqlite3.Connection, record: dict[str, Any]) -> bytes:
    table = record["table"]
    column = record["column"]
    allowed = set(DIRECT_SCHEMAS) | set(REPEATED_MESSAGE_SCHEMAS)
    allowed |= REPEATED_STRING_SCHEMAS | set(RAW_IDENTIFIER_FIELDS)
    if (table, column) not in allowed:
        raise KeyError(f"unmapped populated BLOB column {table}.{column}")
    row = connection.execute(
        f'SELECT "{column}" FROM "{table}" WHERE rowid = ?',
        (record["rowid"],),
    ).fetchone()
    if row is None or row[0] is None:
        raise KeyError(f"missing BLOB for {record['instance_id']}")
    return bytes(row[0])


def chunks(values: list[dict[str, str]], size: int) -> Iterable[list[dict[str, str]]]:
    for offset in range(0, len(values), size):
        yield values[offset : offset + size]


def run_native_decoder(requests: list[dict[str, str]]) -> dict[str, dict[str, Any]]:
    results: dict[str, dict[str, Any]] = {}
    for batch in chunks(requests, 500):
        input_text = "".join(json.dumps(request, sort_keys=True) + "\n" for request in batch)
        process = subprocess.run(
            [str(DECODER_PATH), "batch"],
            input=input_text,
            text=True,
            capture_output=True,
            check=False,
        )
        if process.returncode != 0:
            raise RuntimeError(
                f"native decoder exited {process.returncode}: {process.stderr.strip()}"
            )
        for line in process.stdout.splitlines():
            response = json.loads(line)
            results[response["id"]] = response
    missing = {request["id"] for request in requests} - set(results)
    if missing:
        raise RuntimeError(f"native decoder omitted {len(missing)} responses")
    return results


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    inventory = load_inventory()
    connection = sqlite3.connect(
        f"file:{DB_PATH}?mode=ro&immutable=1",
        uri=True,
    )
    connection.execute("PRAGMA query_only=ON")

    unique_inputs: dict[str, dict[str, Any]] = {}
    instance_plans: list[dict[str, Any]] = []
    counters = Counter()

    for record in inventory:
        key = (record["table"], record["column"])
        data = fetch_blob(connection, record)
        if sha256(data) != record["sha256"]:
            raise RuntimeError(f"inventory hash mismatch for {record['instance_id']}")
        plan: dict[str, Any] = {
            "instance_id": record["instance_id"],
            "table": record["table"],
            "column": record["column"],
            "rowid": record["rowid"],
            "primary_key": record["primary_key"],
            "blob_sha256": record["sha256"],
            "blob_length": len(data),
            "inventory_classification": record["classification"],
        }

        if key in DIRECT_SCHEMAS:
            schema = DIRECT_SCHEMAS[key]
            decode_id = f"{schema}:{record['sha256']}"
            unique_inputs.setdefault(
                decode_id,
                {"id": decode_id, "type": schema, "hex": data.hex()},
            )
            plan.update({"storage_kind": "direct_message", "decode_ids": [decode_id]})
        elif key in REPEATED_MESSAGE_SCHEMAS:
            schema = REPEATED_MESSAGE_SCHEMAS[key]
            payloads, envelope_unknown = repeated_field_one_payloads(data)
            decode_ids = []
            for payload in payloads:
                digest = sha256(payload)
                decode_id = f"{schema}:{digest}"
                unique_inputs.setdefault(
                    decode_id,
                    {"id": decode_id, "type": schema, "hex": payload.hex()},
                )
                decode_ids.append(decode_id)
            plan.update(
                {
                    "storage_kind": "repeated_message_envelope",
                    "element_schema": schema,
                    "decode_ids": decode_ids,
                    "envelope_unknown_fields": envelope_unknown,
                }
            )
        elif key in REPEATED_STRING_SCHEMAS:
            payloads, envelope_unknown = repeated_field_one_payloads(data)
            items = [decode_synonym_item(payload) for payload in payloads]
            plan.update(
                {
                    "storage_kind": "repeated_string_envelope",
                    "items": items,
                    "envelope_unknown_fields": envelope_unknown,
                }
            )
        elif key in RAW_IDENTIFIER_FIELDS:
            plan.update(
                {
                    "storage_kind": "raw_protobuf_bytes_field",
                    **RAW_IDENTIFIER_FIELDS[key],
                    "raw_hex": data.hex(),
                    "decode_status": "accounted_raw_bytes_field",
                }
            )
        else:
            raise KeyError(f"unmapped populated BLOB column {key[0]}.{key[1]}")

        counters[(key, plan["storage_kind"])] += 1
        instance_plans.append(plan)

    native_results = run_native_decoder(list(unique_inputs.values()))
    unique_output = OUTPUT_DIR / "native_unique_messages.jsonl"
    with unique_output.open("w") as stream:
        for decode_id in sorted(native_results):
            response = native_results[decode_id]
            source = unique_inputs[decode_id]
            result = response.get("result")
            output = {
                "decode_id": decode_id,
                "schema": source["type"],
                "input_sha256": decode_id.rsplit(":", 1)[1],
                "input_length": len(bytes.fromhex(source["hex"])),
                "input_hex": source["hex"],
                "error": response.get("error"),
                "result": result,
            }
            if result is not None:
                output["decoded_json"] = json.loads(result["json"])
                output["round_trip_equal"] = (
                    result["canonicalBinaryHex"].lower() == source["hex"].lower()
                )
            stream.write(json.dumps(output, sort_keys=True) + "\n")

    instance_output = OUTPUT_DIR / "blob_instances.jsonl"
    with instance_output.open("w") as stream:
        for plan in instance_plans:
            decode_ids = plan.get("decode_ids", [])
            if decode_ids:
                plan["native_results"] = [native_results[item] for item in decode_ids]
                errors = [
                    item.get("error")
                    for item in plan["native_results"]
                    if item.get("error")
                ]
                unknown = [
                    item["result"]["unknownFieldsHex"]
                    for item in plan["native_results"]
                    if item.get("result") and item["result"]["unknownFieldsHex"]
                ]
                plan["decode_status"] = "decoded" if not errors else "error"
                plan["native_error_count"] = len(errors)
                plan["native_unknown_field_count"] = len(unknown)
            elif plan["storage_kind"] == "repeated_string_envelope":
                item_unknown = sum(len(item["unknown_fields"]) for item in plan["items"])
                plan["decode_status"] = "decoded" if not item_unknown else "partial"
                plan["native_error_count"] = 0
                plan["native_unknown_field_count"] = item_unknown
            elif plan["storage_kind"] == "repeated_message_envelope":
                plan["native_results"] = []
                plan["decode_status"] = "decoded"
                plan["native_error_count"] = 0
                plan["native_unknown_field_count"] = 0
            stream.write(json.dumps(plan, sort_keys=True) + "\n")

    schema_counts: dict[str, Any] = {}
    for (key, storage_kind), count in sorted(counters.items()):
        family = f"{key[0]}.{key[1]}"
        schema_counts[family] = {
            "table": key[0],
            "column": key[1],
            "storage_kind": storage_kind,
            "instance_count": count,
            "direct_schema": DIRECT_SCHEMAS.get(key),
            "element_schema": REPEATED_MESSAGE_SCHEMAS.get(key),
        }

    native_error_count = sum(1 for value in native_results.values() if value.get("error"))
    native_unknown_count = sum(
        1
        for value in native_results.values()
        if value.get("result") and value["result"]["unknownFieldsHex"]
    )
    summary = {
        "database_sha256": sha256(DB_PATH.read_bytes()),
        "inventory_instance_count": len(inventory),
        "planned_instance_count": len(instance_plans),
        "unique_native_decode_count": len(native_results),
        "native_error_count": native_error_count,
        "native_unknown_field_result_count": native_unknown_count,
        "schema_families": schema_counts,
    }
    write_json(OUTPUT_DIR / "decode_summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
