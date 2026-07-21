#!/usr/bin/env python3

import argparse
import hashlib
import json
import math
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


MAX_FIELD_NUMBER = (1 << 29) - 1


def quote_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def read_varint(data: bytes, offset: int) -> tuple[int, int, bytes]:
    start = offset
    value = 0
    for index in range(10):
        if offset >= len(data):
            raise ValueError("truncated varint")
        byte = data[offset]
        offset += 1
        value |= (byte & 0x7F) << (index * 7)
        if not byte & 0x80:
            return value, offset, data[start:offset]
    raise ValueError("varint exceeds 10 bytes")


def is_printable_utf8(data: bytes) -> bool:
    if not data or b"\x00" in data:
        return False
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return False
    return all(character.isprintable() or character in "\r\n\t" for character in text)


def recognized_binary_kind(data: bytes) -> str | None:
    signatures = (
        (b"bplist00", "binary_plist"),
        (b"\x89PNG\r\n\x1a\n", "png"),
        (b"\xff\xd8\xff", "jpeg"),
        (b"GIF87a", "gif"),
        (b"GIF89a", "gif"),
        (b"RIFF", "riff"),
        (b"PK\x03\x04", "zip"),
    )
    for prefix, name in signatures:
        if data.startswith(prefix):
            return name
    return None


def parse_wire(data: bytes, depth: int = 0, max_depth: int = 8) -> dict:
    offset = 0
    fields = []
    canonical = True
    while offset < len(data):
        field_start = offset
        key, offset, key_bytes = read_varint(data, offset)
        field_number = key >> 3
        wire_type = key & 7
        if field_number == 0 or field_number > MAX_FIELD_NUMBER:
            raise ValueError(f"invalid field number {field_number}")
        if wire_type not in (0, 1, 2, 5):
            raise ValueError(f"unsupported wire type {wire_type}")
        minimum_key_size = max(1, math.ceil(key.bit_length() / 7))
        canonical &= len(key_bytes) == minimum_key_size
        field = {
            "field_number": field_number,
            "wire_type": wire_type,
            "offset": field_start,
            "key_hex": key_bytes.hex(),
        }
        if wire_type == 0:
            value, offset, raw_value = read_varint(data, offset)
            minimum_size = max(1, math.ceil(value.bit_length() / 7))
            canonical &= len(raw_value) == minimum_size
            field.update({"value": value, "raw_value_hex": raw_value.hex()})
        elif wire_type == 1:
            end = offset + 8
            if end > len(data):
                raise ValueError("truncated fixed64")
            field["raw_value_hex"] = data[offset:end].hex()
            offset = end
        elif wire_type == 5:
            end = offset + 4
            if end > len(data):
                raise ValueError("truncated fixed32")
            field["raw_value_hex"] = data[offset:end].hex()
            offset = end
        else:
            length, offset, raw_length = read_varint(data, offset)
            minimum_size = max(1, math.ceil(length.bit_length() / 7))
            canonical &= len(raw_length) == minimum_size
            end = offset + length
            if end > len(data):
                raise ValueError("truncated length-delimited value")
            payload = data[offset:end]
            field.update(
                {
                    "length": length,
                    "raw_length_hex": raw_length.hex(),
                    "payload_sha256": hashlib.sha256(payload).hexdigest(),
                    "payload_prefix_hex": payload[:32].hex(),
                }
            )
            binary_kind = recognized_binary_kind(payload)
            if binary_kind:
                field["payload_kind"] = binary_kind
            elif is_printable_utf8(payload):
                field["payload_kind"] = "utf8"
                field["utf8"] = payload.decode("utf-8")
            elif payload and depth < max_depth:
                try:
                    nested = parse_wire(payload, depth + 1, max_depth)
                except ValueError:
                    field["payload_kind"] = "bytes"
                else:
                    field["payload_kind"] = "message_candidate"
                    field["nested"] = nested
            elif not payload:
                field["payload_kind"] = "empty"
            else:
                field["payload_kind"] = "bytes"
            offset = end
        field["end_offset"] = offset
        fields.append(field)
        if len(fields) > 100000:
            raise ValueError("field count limit exceeded")
    if not fields:
        raise ValueError("empty payload is schema-ambiguous")
    return {"canonical_varints": canonical, "fields": fields}


def nested_shape(field: dict) -> str:
    base = f"{field['field_number']}:{field['wire_type']}"
    if field["wire_type"] != 2:
        return base
    kind = field.get("payload_kind", "bytes")
    if kind == "message_candidate":
        return f"{base}<{'/'.join(nested_shape(item) for item in field['nested']['fields'])}>"
    return f"{base}<{kind}>"


def classify_blob(data: bytes) -> tuple[str, dict | None, str | None, str | None]:
    if not data:
        return "empty", None, None, None
    binary_kind = recognized_binary_kind(data)
    if binary_kind:
        return binary_kind, None, None, None
    if is_printable_utf8(data):
        return "utf8", None, None, None
    try:
        wire = parse_wire(data)
    except ValueError as error:
        return "opaque", None, None, str(error)
    shape = "/".join(nested_shape(field) for field in wire["fields"])
    return "protobuf_wire_candidate", wire, shape, None


def json_value(value):
    if isinstance(value, bytes):
        return {"blob_sha256": hashlib.sha256(value).hexdigest(), "length": len(value)}
    return value


def table_has_rowid(connection: sqlite3.Connection, table: str) -> bool:
    try:
        connection.execute(f"SELECT rowid FROM {quote_identifier(table)} LIMIT 0")
        return True
    except sqlite3.DatabaseError:
        return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    uri = f"file:{args.database.resolve()}?mode=ro&immutable=1"
    connection = sqlite3.connect(uri, uri=True)
    connection.execute("PRAGMA query_only=ON")
    connection.row_factory = sqlite3.Row

    schema_rows = connection.execute(
        "SELECT type, name, tbl_name, sql FROM sqlite_schema "
        "ORDER BY CASE type WHEN 'table' THEN 0 WHEN 'index' THEN 1 ELSE 2 END, name"
    ).fetchall()
    schema = [dict(row) for row in schema_rows]
    tables = [
        row["name"]
        for row in schema_rows
        if row["type"] == "table" and row["name"] != "sqlite_schema"
    ]

    table_records = []
    scalar_domains = []
    flag_domains = []
    blob_instances_path = args.output_dir / "blob_instances.jsonl"
    blob_column_stats = defaultdict(
        lambda: {
            "nonnull_instances": 0,
            "total_bytes": 0,
            "hashes": Counter(),
            "classifications": Counter(),
            "wire_shapes": Counter(),
        }
    )
    wire_families = defaultdict(
        lambda: {"instances": 0, "hashes": Counter(), "columns": Counter()}
    )

    with blob_instances_path.open("w") as blob_output:
        for table in tables:
            quoted_table = quote_identifier(table)
            column_rows = connection.execute(f"PRAGMA table_xinfo({quoted_table})").fetchall()
            columns = [dict(row) for row in column_rows]
            row_count = connection.execute(f"SELECT COUNT(*) FROM {quoted_table}").fetchone()[0]
            has_rowid = table_has_rowid(connection, table)
            pk_columns = [
                item["name"]
                for item in sorted(columns, key=lambda item: item["pk"])
                if item["pk"]
            ]
            column_records = []
            blob_columns = []
            for column in columns:
                name = column["name"]
                quoted_column = quote_identifier(name)
                aggregate = connection.execute(
                    f"SELECT COUNT({quoted_column}), COUNT(DISTINCT {quoted_column}) "
                    f"FROM {quoted_table}"
                ).fetchone()
                type_rows = connection.execute(
                    f"SELECT typeof({quoted_column}) AS storage_type, COUNT(*) AS count "
                    f"FROM {quoted_table} GROUP BY typeof({quoted_column}) ORDER BY storage_type"
                ).fetchall()
                storage_types = {row["storage_type"]: row["count"] for row in type_rows}
                record = {
                    **column,
                    "nonnull_count": aggregate[0],
                    "null_count": row_count - aggregate[0],
                    "distinct_count": aggregate[1],
                    "storage_types": storage_types,
                }
                column_records.append(record)
                declared_type = (column["type"] or "").upper()
                if "BLOB" in declared_type or storage_types.get("blob", 0):
                    blob_columns.append(name)
                normalized_name = name.lower()
                is_integer_domain = "INT" in declared_type or (
                    set(storage_types).issubset({"integer", "null"})
                    and storage_types.get("integer", 0)
                )
                if is_integer_domain:
                    values = connection.execute(
                        f"SELECT {quoted_column} AS value, COUNT(*) AS count "
                        f"FROM {quoted_table} GROUP BY {quoted_column} ORDER BY {quoted_column}"
                    ).fetchall()
                    domain = {
                        "table": table,
                        "column": name,
                        "values": [
                            {"value": row["value"], "count": row["count"]} for row in values
                        ],
                    }
                    scalar_domains.append(domain)
                    if "flag" in normalized_name:
                        nonnegative_values = [
                            row["value"]
                            for row in values
                            if isinstance(row["value"], int) and row["value"] >= 0
                        ]
                        bit_union = 0
                        for value in nonnegative_values:
                            bit_union |= value
                        flag_domains.append(
                            {
                                **domain,
                                "bit_union": bit_union,
                                "present_bit_values": [
                                    1 << bit
                                    for bit in range(bit_union.bit_length())
                                    if bit_union & (1 << bit)
                                ],
                                "semantic_status": "unverified",
                                "runtime_verification_status": "not_started",
                            }
                        )
                elif aggregate[1] <= 64 and not storage_types.get("blob", 0):
                    values = connection.execute(
                        f"SELECT {quoted_column} AS value, COUNT(*) AS count "
                        f"FROM {quoted_table} GROUP BY {quoted_column} ORDER BY {quoted_column}"
                    ).fetchall()
                    scalar_domains.append(
                        {
                            "table": table,
                            "column": name,
                            "values": [
                                {"value": json_value(row["value"]), "count": row["count"]}
                                for row in values
                            ],
                        }
                    )

            table_records.append(
                {
                    "table": table,
                    "row_count": row_count,
                    "has_rowid": has_rowid,
                    "primary_key_columns": pk_columns,
                    "columns": column_records,
                    "blob_columns": blob_columns,
                }
            )

            for blob_column in blob_columns:
                key = f"{table}.{blob_column}"
                blob_column_stats[key]
                identity_columns = pk_columns or []
                select_parts = ["rowid"] if has_rowid else []
                select_parts.extend(quote_identifier(name) for name in identity_columns)
                select_parts.append(quote_identifier(blob_column))
                query = (
                    f"SELECT {', '.join(select_parts)} FROM {quoted_table} "
                    f"WHERE typeof({quote_identifier(blob_column)}) = 'blob'"
                )
                for row in connection.execute(query):
                    index = 0
                    rowid = row[index] if has_rowid else None
                    index += int(has_rowid)
                    identity = {}
                    for name in identity_columns:
                        identity[name] = json_value(row[index])
                        index += 1
                    data = row[index]
                    digest = hashlib.sha256(data).hexdigest()
                    classification, wire, shape, parse_error = classify_blob(data)
                    stats = blob_column_stats[key]
                    stats["nonnull_instances"] += 1
                    stats["total_bytes"] += len(data)
                    stats["hashes"][digest] += 1
                    stats["classifications"][classification] += 1
                    if shape:
                        stats["wire_shapes"][shape] += 1
                        family = wire_families[shape]
                        family["instances"] += 1
                        family["hashes"][digest] += 1
                        family["columns"][key] += 1
                    instance = {
                        "instance_id": f"{table}:{blob_column}:rowid={rowid}",
                        "table": table,
                        "column": blob_column,
                        "rowid": rowid,
                        "primary_key": identity,
                        "length": len(data),
                        "sha256": digest,
                        "prefix_hex": data[:64].hex(),
                        "classification": classification,
                        "wire_shape": shape,
                        "wire": wire,
                        "parse_error": parse_error,
                        "schema_family": None,
                        "decode_status": "not_started",
                        "runtime_verification_status": "not_started",
                    }
                    blob_output.write(json.dumps(instance, sort_keys=True) + "\n")

    blob_columns = []
    for key, stats in sorted(blob_column_stats.items()):
        table, column = key.split(".", 1)
        blob_columns.append(
            {
                "table": table,
                "column": column,
                "nonnull_instances": stats["nonnull_instances"],
                "unique_blob_count": len(stats["hashes"]),
                "total_bytes": stats["total_bytes"],
                "classifications": dict(sorted(stats["classifications"].items())),
                "wire_shapes": dict(sorted(stats["wire_shapes"].items())),
                "decode_status": "not_started",
                "runtime_verification_status": "not_started",
            }
        )

    wire_family_records = []
    for index, (shape, stats) in enumerate(
        sorted(wire_families.items(), key=lambda item: (-item[1]["instances"], item[0])),
        start=1,
    ):
        wire_family_records.append(
            {
                "wire_family_id": f"wire-{index:04d}",
                "shape": shape,
                "instances": stats["instances"],
                "unique_blob_count": len(stats["hashes"]),
                "columns": dict(sorted(stats["columns"].items())),
                "schema_family": None,
                "decode_status": "not_started",
                "runtime_verification_status": "not_started",
            }
        )

    metadata = {
        "schema_version": "toolkit_coverage_ledger.v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "database_path": str(args.database),
        "database_sha256": hashlib.sha256(args.database.read_bytes()).hexdigest(),
        "sqlite_user_version": connection.execute("PRAGMA user_version").fetchone()[0],
        "integrity_check": connection.execute("PRAGMA integrity_check").fetchone()[0],
        "table_count": len(tables),
        "column_count": sum(len(table["columns"]) for table in table_records),
        "row_count_total": sum(table["row_count"] for table in table_records),
        "blob_column_count": len(blob_columns),
        "blob_instance_count": sum(item["nonnull_instances"] for item in blob_columns),
        "unique_blob_hash_count": len(
            {
                digest
                for stats in blob_column_stats.values()
                for digest in stats["hashes"]
            }
        ),
        "protobuf_wire_candidate_count": sum(
            item["classifications"].get("protobuf_wire_candidate", 0)
            for item in blob_columns
        ),
        "wire_shape_count": len(wire_family_records),
        "flag_domain_count": len(flag_domains),
        "coverage_status": "inventory_complete_decode_not_started",
    }

    outputs = {
        "metadata.json": metadata,
        "sqlite_schema.json": schema,
        "tables.json": table_records,
        "scalar_domains.json": scalar_domains,
        "flag_domains.json": flag_domains,
        "blob_columns.json": blob_columns,
        "wire_families.json": wire_family_records,
    }
    for name, value in outputs.items():
        (args.output_dir / name).write_text(
            json.dumps(value, indent=2, sort_keys=True) + "\n"
        )
    connection.close()


if __name__ == "__main__":
    main()
