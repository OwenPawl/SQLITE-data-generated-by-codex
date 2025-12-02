"""Generate a canonical Shortcut action schema catalogue."""
from __future__ import annotations

import argparse
from pathlib import Path

from actions_auto_schema import (
    infer_schema_from_db,
    infer_schema_from_shortcut_json,
    load_shortcut_json,
    load_tools_db,
    merge_schemas,
    normalize_schema,
    save_schema,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--databases", nargs="*", default=[], help="Paths to Tools.sqlite snapshots")
    parser.add_argument("--shortcuts", nargs="*", default=[], help="Shortcut JSON files or zip archives")
    parser.add_argument("--output", default="schema.json", help="Destination JSON file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    combined_schema = {}

    for db_path in args.databases:
        if not Path(db_path).exists():
            continue
        db_data = load_tools_db(db_path)
        db_schema = infer_schema_from_db(db_data)
        combined_schema.update(db_schema)

    json_schema = {}
    for shortcut_path in args.shortcuts:
        if not Path(shortcut_path).exists():
            continue
        workflows = load_shortcut_json(shortcut_path)
        shortcut_schema = infer_schema_from_shortcut_json(workflows)
        json_schema.update(shortcut_schema)

    merged = merge_schemas(combined_schema, json_schema)
    normalized = normalize_schema(merged)
    save_schema(normalized, args.output)
    print(f"Saved schema catalogue to {args.output} with {len(normalized)} actions")


if __name__ == "__main__":
    main()
