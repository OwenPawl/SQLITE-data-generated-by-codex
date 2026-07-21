#!/usr/bin/env python3
"""Join native protobuf schemas to decoded database instances."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parents[1]
SCHEMAS_PATH = RUN_DIR / "decoded/native_message_schemas.jsonl"
NAMES_PATH = RUN_DIR / "decoded/native_name_maps.jsonl"
MESSAGES_PATH = RUN_DIR / "decoded/native_unique_messages.jsonl"
INSTANCES_PATH = RUN_DIR / "decoded/blob_instances.jsonl"
OUTPUT_PATH = RUN_DIR / "coverage/native_observed_coverage.json"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def normalize_type(name: str | None) -> str | None:
    if name is None:
        return None
    for prefix in ("ToolKit.", "InternalSwiftProtobuf."):
        if name.startswith(prefix):
            return name.removeprefix(prefix)
    return name


def scalar_key(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def main() -> None:
    schemas = {item["swiftType"]: item for item in load_jsonl(SCHEMAS_PATH)}
    name_maps = load_jsonl(NAMES_PATH)
    enums = {
        item["swiftType"]: item for item in name_maps if item["kind"] == "enum"
    }

    fields_by_schema: dict[str, dict[str, dict[str, Any]]] = {}
    oneof_by_schema: dict[str, dict[int, int]] = {}
    for schema_name, schema in schemas.items():
        by_number = {field["number"]: field for field in schema["fields"]}
        fields_by_schema[schema_name] = {
            name["jsonName"]: {**name, **by_number[name["number"]]}
            for name in schema["names"]
        }
        oneof_by_schema[schema_name] = {
            number: group_index
            for group_index, group in enumerate(schema["oneofGroups"])
            for number in group
        }

    instance_weights: Counter[str] = Counter()
    for instance in load_jsonl(INSTANCES_PATH):
        instance_weights.update(instance.get("decode_ids", []))

    field_occurrences: Counter[tuple[str, int]] = Counter()
    field_weighted_occurrences: Counter[tuple[str, int]] = Counter()
    field_roots: dict[tuple[str, int], set[str]] = defaultdict(set)
    field_weighted_roots: dict[tuple[str, int], Counter[str]] = defaultdict(Counter)
    scalar_values: dict[tuple[str, int], Counter[str]] = defaultdict(Counter)
    enum_values: dict[tuple[str, int], Counter[str]] = defaultdict(Counter)
    enum_weighted_values: dict[tuple[str, int], Counter[str]] = defaultdict(Counter)
    oneof_arms: dict[tuple[str, int], Counter[int]] = defaultdict(Counter)
    oneof_weighted_arms: dict[tuple[str, int], Counter[int]] = defaultdict(Counter)
    message_presence: Counter[str] = Counter()
    message_weighted_presence: Counter[str] = Counter()
    unresolved: Counter[tuple[str, str, str]] = Counter()

    def walk(
        schema_name: str,
        value: Any,
        root_id: str,
        weight: int,
        path: tuple[str, ...],
    ) -> None:
        schema_name = normalize_type(schema_name) or schema_name
        if not isinstance(value, dict):
            unresolved[(schema_name, ".".join(path), "message_not_object")] += 1
            return
        if schema_name not in fields_by_schema:
            unresolved[(schema_name, ".".join(path), "schema_not_in_registry")] += 1
            return

        message_presence[schema_name] += 1
        message_weighted_presence[schema_name] += weight
        field_map = fields_by_schema[schema_name]
        for json_name, field_value in value.items():
            field = field_map.get(json_name)
            field_path = path + (json_name,)
            if field is None:
                unresolved[(schema_name, ".".join(field_path), "field_not_in_name_map")] += 1
                continue

            field_key = (schema_name, field["number"])
            field_occurrences[field_key] += 1
            field_weighted_occurrences[field_key] += weight
            field_roots[field_key].add(root_id)
            field_weighted_roots[field_key][root_id] = weight

            group_index = oneof_by_schema[schema_name].get(field["number"])
            if group_index is not None:
                oneof_arms[(schema_name, group_index)][field["number"]] += 1
                oneof_weighted_arms[(schema_name, group_index)][field["number"]] += weight

            kind = field["valueKind"]
            cardinality = field["cardinality"]
            child_type = normalize_type(field.get("swiftType"))
            values = field_value if cardinality == "repeated" else [field_value]
            if cardinality == "map" and isinstance(field_value, dict):
                values = list(field_value.values())
                if child_type and "->" in child_type:
                    child_type = normalize_type(child_type.split("->", 1)[1])

            if kind in ("message", "group"):
                for child in values if isinstance(values, list) else []:
                    walk(child_type or "<unknown>", child, root_id, weight, field_path)
            elif kind == "enum":
                for enum_value in values if isinstance(values, list) else []:
                    rendered = scalar_key(enum_value)
                    enum_values[field_key][rendered] += 1
                    enum_weighted_values[field_key][rendered] += weight
            else:
                for scalar in values if isinstance(values, list) else []:
                    scalar_values[field_key][scalar_key(scalar)] += 1

    messages = load_jsonl(MESSAGES_PATH)
    for message in messages:
        if message["error"] is not None:
            continue
        root_id = message["decode_id"]
        walk(
            message["schema"],
            message["decoded_json"],
            root_id,
            instance_weights[root_id],
            (),
        )

    field_rows = []
    for schema_name, schema in sorted(schemas.items()):
        by_number = {name["number"]: name for name in schema["names"]}
        for field in schema["fields"]:
            key = (schema_name, field["number"])
            name = by_number[field["number"]]
            values = scalar_values[key]
            field_rows.append(
                {
                    "schema": schema_name,
                    "number": field["number"],
                    "proto_name": name["protoName"],
                    "json_name": name["jsonName"],
                    "cardinality": field["cardinality"],
                    "value_kind": field["valueKind"],
                    "swift_type": field.get("swiftType"),
                    "oneof_group": oneof_by_schema[schema_name].get(field["number"]),
                    "observed": field_occurrences[key] > 0,
                    "occurrence_count_in_unique_messages": field_occurrences[key],
                    "unique_root_message_count": len(field_roots[key]),
                    "weighted_database_occurrence_count": field_weighted_occurrences[key],
                    "weighted_database_root_count": sum(field_weighted_roots[key].values()),
                    "distinct_scalar_value_count": len(values),
                    "top_scalar_values": [
                        {"json_value": value, "count": count}
                        for value, count in values.most_common(25)
                    ],
                }
            )

    enum_rows = []
    for key, values in sorted(enum_values.items()):
        schema_name, number = key
        field = next(
            row for row in field_rows
            if row["schema"] == schema_name and row["number"] == number
        )
        enum_type = normalize_type(field["swift_type"])
        defined = {
            scalar_key(name["protoName"]): name["number"]
            for name in enums.get(enum_type or "", {}).get("names", [])
        }
        if enum_type == "Google_Protobuf_NullValue":
            defined = {"null": 0}
        enum_rows.append(
            {
                "schema": schema_name,
                "field_number": number,
                "field_name": field["json_name"],
                "enum_type": enum_type,
                "defined_values": [
                    {"raw_value": raw, "name": json.loads(name)}
                    for name, raw in sorted(defined.items(), key=lambda item: item[1])
                ],
                "observed_values": [
                    {
                        "json_value": json.loads(value),
                        "unique_message_occurrences": count,
                        "weighted_database_occurrences": enum_weighted_values[key][value],
                        "defined": value in defined,
                        "raw_value": defined.get(value),
                    }
                    for value, count in sorted(values.items())
                ],
            }
        )

    oneof_rows = []
    for schema_name, schema in sorted(schemas.items()):
        name_by_number = {name["number"]: name["jsonName"] for name in schema["names"]}
        for group_index, group in enumerate(schema["oneofGroups"]):
            counts = oneof_arms[(schema_name, group_index)]
            weighted = oneof_weighted_arms[(schema_name, group_index)]
            oneof_rows.append(
                {
                    "schema": schema_name,
                    "group_index": group_index,
                    "defined_arms": [
                        {"number": number, "name": name_by_number[number]}
                        for number in group
                    ],
                    "observed_arms": [
                        {
                            "number": number,
                            "name": name_by_number[number],
                            "unique_message_occurrences": counts[number],
                            "weighted_database_occurrences": weighted[number],
                        }
                        for number in group if counts[number]
                    ],
                }
            )

    output = {
        "summary": {
            "native_unique_message_count": len(messages),
            "native_decode_reference_count": sum(instance_weights.values()),
            "defined_message_count": len(schemas),
            "defined_enum_count": len(enums),
            "defined_field_count": len(field_rows),
            "observed_defined_field_count": sum(row["observed"] for row in field_rows),
            "defined_oneof_group_count": len(oneof_rows),
            "observed_enum_field_count": len(enum_rows),
            "unresolved_path_count": sum(unresolved.values()),
        },
        "message_presence": [
            {
                "schema": schema_name,
                "unique_message_occurrences": message_presence[schema_name],
                "weighted_database_occurrences": message_weighted_presence[schema_name],
            }
            for schema_name in sorted(schemas)
        ],
        "fields": field_rows,
        "enums": enum_rows,
        "oneofs": oneof_rows,
        "unresolved_paths": [
            {"schema": key[0], "path": key[1], "reason": key[2], "count": count}
            for key, count in sorted(unresolved.items())
        ],
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["summary"], indent=2, sort_keys=True))
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
