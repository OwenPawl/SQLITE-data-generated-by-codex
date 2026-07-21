#!/usr/bin/env python3
import argparse
import json
import sqlite3
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--native", type=Path, required=True)
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    native_document = json.loads(args.native.read_text())
    native_tools = {row["id"]: row for row in native_document["tools"]}
    native_parameters = {
        (tool["id"], parameter["key"]): parameter
        for tool in native_document["tools"]
        for parameter in tool["parameters"]
    }

    uri = f"file:{args.database.resolve()}?mode=ro&immutable=1"
    with sqlite3.connect(uri, uri=True) as database:
        database.row_factory = sqlite3.Row
        stored_tools = {
            row["id"]: dict(row)
            for row in database.execute(
                "SELECT id, flags, visibilityFlags FROM Tools"
            )
        }
        stored_parameters = {
            (row["toolIdentifier"], row["key"]): dict(row)
            for row in database.execute(
                "SELECT Tools.id AS toolIdentifier, Parameters.key, Parameters.flags "
                "FROM Parameters JOIN Tools ON Tools.rowId = Parameters.toolId"
            )
        }
        stored_type_count = database.execute("SELECT count(*) FROM Types").fetchone()[0]
        stored_entity_runtime_flags = [
            row[0] for row in database.execute(
                "SELECT runtimeFlags FROM Types WHERE kind = 2 ORDER BY runtimeFlags"
            )
        ]

    tool_mismatches = []
    for identifier in sorted(stored_tools.keys() & native_tools.keys()):
        stored = stored_tools[identifier]
        native = native_tools[identifier]
        if (stored["flags"], stored["visibilityFlags"]) != (
            native["flags"], native["visibilityFlags"]
        ):
            tool_mismatches.append({
                "id": identifier,
                "stored": stored,
                "native": {
                    "flags": native["flags"],
                    "visibilityFlags": native["visibilityFlags"],
                },
            })

    parameter_mismatches = []
    hidden_partition_mismatches = []
    for key in sorted(stored_parameters.keys() & native_parameters.keys()):
        stored = stored_parameters[key]
        native = native_parameters[key]
        if stored["flags"] != native["flags"]:
            parameter_mismatches.append({
                "toolIdentifier": key[0], "key": key[1],
                "storedFlags": stored["flags"], "nativeFlags": native["flags"],
            })
        expected_collection = (
            "hiddenParameters" if stored["flags"] & 1 else "parameters"
        )
        if native["collection"] != expected_collection:
            hidden_partition_mismatches.append({
                "toolIdentifier": key[0], "key": key[1],
                "flags": stored["flags"],
                "nativeCollection": native["collection"],
            })

    summary = {
        "storedToolCount": len(stored_tools),
        "nativeToolCount": len(native_tools),
        "missingNativeTools": sorted(stored_tools.keys() - native_tools.keys()),
        "nativeOnlyTools": sorted(native_tools.keys() - stored_tools.keys()),
        "toolFlagMismatches": tool_mismatches,
        "storedParameterCount": len(stored_parameters),
        "nativeParameterCount": len(native_parameters),
        "missingNativeParameters": [list(key) for key in sorted(stored_parameters.keys() - native_parameters.keys())],
        "nativeOnlyParameters": [list(key) for key in sorted(native_parameters.keys() - stored_parameters.keys())],
        "parameterFlagMismatches": parameter_mismatches,
        "hiddenPartitionMismatches": hidden_partition_mismatches,
        "hiddenParameterCount": sum(row["flags"] & 1 != 0 for row in stored_parameters.values()),
        "storedTypeCount": stored_type_count,
        "nativeTypeCount": native_document["typeCount"],
        "typeCountMatches": stored_type_count == native_document["typeCount"],
        "storedEntityRuntimeFlagValues": stored_entity_runtime_flags,
        "nativeEntityRuntimeFlagValues": native_document["entityRuntimeFlagValues"],
        "entityRuntimeFlagValuesMatch": (
            stored_entity_runtime_flags == native_document["entityRuntimeFlagValues"]
        ),
    }
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
