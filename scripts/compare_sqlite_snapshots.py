#!/usr/bin/env python3
import argparse
import hashlib
import json
import sqlite3
import struct
from collections import Counter
from pathlib import Path


def quote(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def connect(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(f"file:{path.resolve()}?mode=ro&immutable=1", uri=True)
    connection.row_factory = sqlite3.Row
    return connection


def encode_value(value) -> bytes:
    if value is None:
        return b"n"
    if isinstance(value, int):
        return b"i" + str(value).encode("ascii") + b";"
    if isinstance(value, float):
        return b"f" + struct.pack(">d", value)
    if isinstance(value, str):
        data = value.encode("utf-8")
        return b"s" + len(data).to_bytes(8, "big") + data
    if isinstance(value, bytes):
        return b"b" + len(value).to_bytes(8, "big") + value
    raise TypeError(type(value))


def encode_row(row, columns) -> bytes:
    return b"".join(encode_value(row[column]) for column in columns)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_value(value):
    if isinstance(value, bytes):
        return {"blob_length": len(value), "sha256": digest(value)}
    return value


def table_names(connection: sqlite3.Connection):
    return [
        row[0] for row in connection.execute(
            "SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name"
        )
    ]


def table_info(connection: sqlite3.Connection, table: str):
    return list(connection.execute(f"PRAGMA table_info({quote(table)})"))


def rows(connection: sqlite3.Connection, table: str):
    return list(connection.execute(f"SELECT * FROM {quote(table)}"))


def compare_table(old_connection, new_connection, table: str):
    old_info = table_info(old_connection, table)
    new_info = table_info(new_connection, table)
    old_schema = [(row["name"], row["type"], row["notnull"], row["dflt_value"], row["pk"]) for row in old_info]
    new_schema = [(row["name"], row["type"], row["notnull"], row["dflt_value"], row["pk"]) for row in new_info]
    result = {
        "table": table,
        "schema_equal": old_schema == new_schema,
        "old_row_count": 0,
        "new_row_count": 0,
        "added_row_count": 0,
        "removed_row_count": 0,
        "changed_row_count": 0,
        "changed_column_counts": {},
        "changes": [],
    }
    if old_schema != new_schema:
        result["old_schema"] = old_schema
        result["new_schema"] = new_schema
        return result

    columns = [row["name"] for row in old_info]
    primary_key = [
        row["name"] for row in sorted(old_info, key=lambda item: item["pk"])
        if row["pk"]
    ]
    old_rows = rows(old_connection, table)
    new_rows = rows(new_connection, table)
    result["old_row_count"] = len(old_rows)
    result["new_row_count"] = len(new_rows)

    if not primary_key:
        old_counter = Counter(digest(encode_row(row, columns)) for row in old_rows)
        new_counter = Counter(digest(encode_row(row, columns)) for row in new_rows)
        removed = old_counter - new_counter
        added = new_counter - old_counter
        result["removed_row_count"] = sum(removed.values())
        result["added_row_count"] = sum(added.values())
        result["unchanged"] = not removed and not added
        if removed or added:
            result["changes"] = [{
                "key": None,
                "removed_row_hash_counts": dict(removed),
                "added_row_hash_counts": dict(added),
            }]
        return result

    def key_for(row):
        return tuple(row[column] for column in primary_key)

    old_by_key = {key_for(row): row for row in old_rows}
    new_by_key = {key_for(row): row for row in new_rows}
    old_keys = set(old_by_key)
    new_keys = set(new_by_key)
    result["primary_key"] = primary_key
    result["removed_row_count"] = len(old_keys - new_keys)
    result["added_row_count"] = len(new_keys - old_keys)
    changed_columns = Counter()
    changes = []
    for key in sorted(old_keys | new_keys, key=repr):
        if key not in new_by_key:
            changes.append({"kind": "removed", "key": [json_value(value) for value in key]})
            continue
        if key not in old_by_key:
            changes.append({"kind": "added", "key": [json_value(value) for value in key]})
            continue
        old_row = old_by_key[key]
        new_row = new_by_key[key]
        fields = []
        for column in columns:
            if encode_value(old_row[column]) == encode_value(new_row[column]):
                continue
            changed_columns[column] += 1
            fields.append({
                "column": column,
                "old": json_value(old_row[column]),
                "new": json_value(new_row[column]),
            })
        if fields:
            changes.append({
                "kind": "changed",
                "key": [json_value(value) for value in key],
                "fields": fields,
            })
    result["changed_row_count"] = sum(change["kind"] == "changed" for change in changes)
    result["changed_column_counts"] = dict(sorted(changed_columns.items()))
    result["changes"] = changes
    result["unchanged"] = not changes
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("old", type=Path)
    parser.add_argument("new", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    old_connection = connect(args.old)
    new_connection = connect(args.new)
    old_tables = table_names(old_connection)
    new_tables = table_names(new_connection)
    common_tables = sorted(set(old_tables) & set(new_tables))
    comparisons = [compare_table(old_connection, new_connection, table) for table in common_tables]
    old_connection.close()
    new_connection.close()

    changed = [record for record in comparisons if not record.get("unchanged", False)]
    old_bytes = args.old.read_bytes()
    new_bytes = args.new.read_bytes()
    physical_differences = [
        {"offset": offset, "old": old_value, "new": new_value}
        for offset, (old_value, new_value) in enumerate(zip(old_bytes, new_bytes))
        if old_value != new_value
    ]
    if len(old_bytes) != len(new_bytes):
        physical_differences.append({
            "offset": min(len(old_bytes), len(new_bytes)),
            "old_remaining_bytes": max(0, len(old_bytes) - len(new_bytes)),
            "new_remaining_bytes": max(0, len(new_bytes) - len(old_bytes)),
        })
    result = {
        "schema_version": "sqlite_snapshot_comparison.v1",
        "old_path": str(args.old),
        "new_path": str(args.new),
        "old_sha256": digest(old_bytes),
        "new_sha256": digest(new_bytes),
        "old_size": len(old_bytes),
        "new_size": len(new_bytes),
        "physical_difference_count": len(physical_differences),
        "physical_differences": physical_differences[:64],
        "sqlite_header": {
            "old_change_counter": int.from_bytes(old_bytes[24:28], "big"),
            "new_change_counter": int.from_bytes(new_bytes[24:28], "big"),
            "old_version_valid_for": int.from_bytes(old_bytes[92:96], "big"),
            "new_version_valid_for": int.from_bytes(new_bytes[92:96], "big"),
        },
        "old_only_tables": sorted(set(old_tables) - set(new_tables)),
        "new_only_tables": sorted(set(new_tables) - set(old_tables)),
        "table_count": len(common_tables),
        "changed_table_count": len(changed),
        "changed_tables": changed,
        "all_tables": comparisons,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "old_sha256": result["old_sha256"],
        "new_sha256": result["new_sha256"],
        "table_count": result["table_count"],
        "changed_table_count": result["changed_table_count"],
        "physical_difference_count": result["physical_difference_count"],
        "sqlite_header": result["sqlite_header"],
        "changed_tables": [
            {
                "table": record["table"],
                "added": record["added_row_count"],
                "removed": record["removed_row_count"],
                "changed": record["changed_row_count"],
                "columns": record["changed_column_counts"],
            }
            for record in changed
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
