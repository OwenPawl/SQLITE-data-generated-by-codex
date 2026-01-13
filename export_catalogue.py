import argparse
import base64
import datetime as dt
import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Tuple

Row = Mapping[str, Any]


def table_exists(conn: sqlite3.Connection, table: str) -> bool:
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,)
    )
    return cursor.fetchone() is not None


def get_table_columns(conn: sqlite3.Connection, table: str) -> List[Tuple[str, str]]:
    cursor = conn.execute(f"PRAGMA table_info({table});")
    return [(row[1], row[2]) for row in cursor.fetchall()]


def encode_blob(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (bytes, bytearray, memoryview)):
        return base64.b64encode(bytes(value)).decode("ascii")
    return value


def load_table(conn: sqlite3.Connection, table: str) -> List[Dict[str, Any]]:
    columns = get_table_columns(conn, table)
    blob_columns = {name for name, col_type in columns if "BLOB" in col_type.upper()}
    cursor = conn.execute(f"SELECT * FROM {table}")
    rows: List[Dict[str, Any]] = []
    for row in cursor.fetchall():
        entry: Dict[str, Any] = {}
        for idx, (name, _) in enumerate(columns):
            value = row[idx]
            if name in blob_columns:
                value = encode_blob(value)
            entry[name] = value
        rows.append(entry)
    return rows


def group_by(rows: Iterable[Row], key_fn) -> MutableMapping[Any, List[Row]]:
    grouped: MutableMapping[Any, List[Row]] = {}
    for row in rows:
        key = key_fn(row)
        grouped.setdefault(key, []).append(row)
    return grouped


def attach_sample_phrases(samples: List[Dict[str, Any]], phrases: List[Dict[str, Any]]) -> None:
    phrase_map = group_by(phrases, lambda row: row["invocationId"])
    for sample in samples:
        sample["phrases"] = phrase_map.get(sample.get("rowId"), [])


def attach_parameters(
    tools: List[Dict[str, Any]],
    parameters: List[Dict[str, Any]],
    parameter_localizations: List[Dict[str, Any]],
    parameter_types: Optional[List[Dict[str, Any]]],
    owner_key: str = "toolId",
) -> None:
    params_by_tool = group_by(parameters, lambda row: row[owner_key])
    param_locs_by_key = group_by(
        parameter_localizations, lambda row: (row[owner_key], row["key"])
    )
    type_by_key: Dict[Tuple[Any, Any], Dict[str, Any]] = {}
    if parameter_types:
        for row in parameter_types:
            type_by_key[(row[owner_key], row["key"])] = row

    for tool in tools:
        tool_params = params_by_tool.get(tool.get("rowId"), [])
        for param in tool_params:
            param_key = (param.get(owner_key), param.get("key"))
            param["localizations"] = param_locs_by_key.get(param_key, [])
            if type_by_key:
                override = type_by_key.get(param_key)
                if override:
                    param["typeOverride"] = override
        tool["parameters"] = sorted(
            tool_params, key=lambda p: p.get("sortOrder", 0)
        )


def attach_localizations(
    entities: List[Dict[str, Any]],
    localizations: List[Dict[str, Any]],
    key: str,
) -> None:
    loc_by_id = group_by(localizations, lambda row: row[key])
    for entity in entities:
        entity["localizations"] = loc_by_id.get(entity.get("rowId"), [])


def attach_simple_group(
    entities: List[Dict[str, Any]],
    rows: List[Dict[str, Any]],
    key: str,
    label: str,
) -> None:
    grouped = group_by(rows, lambda row: row[key])
    for entity in entities:
        entity[label] = grouped.get(entity.get("rowId"), [])


def index_containers(
    metadata: List[Dict[str, Any]],
    localizations: List[Dict[str, Any]],
    synonyms: List[Dict[str, Any]],
) -> Dict[Any, Dict[str, Any]]:
    loc_by_id = group_by(localizations, lambda row: row["containerId"])
    syn_by_id = group_by(synonyms, lambda row: row["containerId"])

    indexed: Dict[Any, Dict[str, Any]] = {}
    for row in metadata:
        container_id = row.get("rowId")
        indexed[container_id] = {
            **row,
            "localizations": loc_by_id.get(container_id, []),
            "synonyms": syn_by_id.get(container_id, []),
        }

    return indexed


def resolve_container(index: Mapping[Any, Dict[str, Any]], key: Any) -> Optional[Dict[str, Any]]:
    if key is None:
        return None
    return index.get(key) or index.get(str(key))


def build_catalogue(conn: sqlite3.Connection) -> Dict[str, Any]:
    catalogue: Dict[str, Any] = {
        "generatedAt": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }

    tools = load_table(conn, "Tools")
    tool_localizations = load_table(conn, "ToolLocalizations")
    parameters = load_table(conn, "Parameters")
    parameter_localizations = load_table(conn, "ParameterLocalizations")
    parameter_types = load_table(conn, "ToolParameterTypes") if table_exists(conn, "ToolParameterTypes") else None
    output_types = load_table(conn, "ToolOutputTypes")
    search_keywords = load_table(conn, "SearchKeywords")
    sample_invocations = load_table(conn, "SampleInvocation")
    sample_phrases = load_table(conn, "SampleInvocationPhrase")

    attach_localizations(tools, tool_localizations, "toolId")
    attach_parameters(tools, parameters, parameter_localizations, parameter_types)
    attach_simple_group(tools, output_types, "toolId", "outputTypes")
    attach_simple_group(tools, search_keywords, "toolId", "searchKeywords")
    attach_sample_phrases(sample_invocations, sample_phrases)
    sample_by_tool = group_by(sample_invocations, lambda row: row["toolId"])
    for tool in tools:
        tool["sampleInvocations"] = sample_by_tool.get(tool.get("rowId"), [])

    catalogue["tools"] = sorted(tools, key=lambda t: t.get("id", ""))

    if table_exists(conn, "Triggers"):
        triggers = load_table(conn, "Triggers")
        trigger_localizations = load_table(conn, "TriggerLocalizations")
        trigger_parameters = load_table(conn, "TriggerParameters")
        trigger_parameter_localizations = load_table(conn, "TriggerParameterLocalizations")
        trigger_output_types = load_table(conn, "TriggerOutputTypes")

        attach_localizations(triggers, trigger_localizations, "triggerId")
        attach_parameters(
            triggers,
            trigger_parameters,
            trigger_parameter_localizations,
            parameter_types=None,
            owner_key="triggerId",
        )
        attach_simple_group(
            triggers, trigger_output_types, "triggerId", "outputTypes"
        )
        catalogue["triggers"] = sorted(triggers, key=lambda trg: trg.get("id", ""))

    container_metadata = load_table(conn, "ContainerMetadata")
    container_localizations = load_table(conn, "ContainerMetadataLocalizations")
    container_synonyms = load_table(conn, "ContainerMetadataSynonyms")
    container_index = index_containers(
        container_metadata, container_localizations, container_synonyms
    )
    additional_attribution = load_table(conn, "AdditionalToolAttributionContainers")

    additional_by_tool = group_by(additional_attribution, lambda row: row["toolId"])
    for tool in tools:
        tool["sourceContainer"] = resolve_container(
            container_index, tool.get("sourceContainerId")
        )
        tool["attributionContainer"] = resolve_container(
            container_index, tool.get("attributionContainerId")
        )
        extra = []
        for entry in additional_by_tool.get(tool.get("rowId"), []):
            container = resolve_container(container_index, entry.get("containerId"))
            if container:
                extra.append(container)
        tool["additionalAttributionContainers"] = extra

    catalogue["containers"] = {
        "metadata": container_metadata,
        "localizations": container_localizations,
        "synonyms": container_synonyms,
        "additionalAttribution": additional_attribution,
    }

    catalogue["types"] = {
        "types": load_table(conn, "Types"),
        "display": load_table(conn, "TypeDisplayRepresentations"),
        "coercions": load_table(conn, "TypeCoercions"),
        "utTypeCoercions": load_table(conn, "UTTypeCoercions"),
        "entityProperties": load_table(conn, "EntityProperties"),
        "entityPropertyLocalizations": load_table(
            conn, "EntityPropertyLocalizations"
        ),
        "enumerationCases": load_table(conn, "EnumerationCases"),
        "systemTypeProtocols": load_table(conn, "SystemTypeProtocols"),
    }

    catalogue["metadata"] = {
        "launchServicesState": load_table(conn, "LaunchServicesState"),
        "metadata": load_table(conn, "Metadata"),
        "linkState": load_table(conn, "LinkState"),
        "linkActionIdentifiers": load_table(conn, "LinkActionIdentifiers"),
        "systemToolProtocols": load_table(conn, "SystemToolProtocols"),
        "categories": load_table(conn, "Categories"),
    }

    return catalogue


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export a complete Shortcuts-style catalogue from the SQLite snapshots."
    )
    parser.add_argument(
        "--database",
        required=True,
        help="Path to the SQLite database (e.g., raw.sqlite or 'Tools-prod 2.sqlite').",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to the JSON file that will receive the full catalogue.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Write indented JSON for easier inspection (slightly slower and larger).",
    )

    args = parser.parse_args()

    db_path = Path(args.database)
    if not db_path.exists():
        raise SystemExit(f"Database not found: {db_path}")

    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        catalogue = build_catalogue(conn)
        catalogue["sourceDatabase"] = db_path.name
        output_path = Path(args.output)
        output_path.write_text(
            json.dumps(catalogue, indent=2 if args.pretty else None),
            encoding="utf-8",
        )
    finally:
        conn.close()


if __name__ == "__main__":
    main()
