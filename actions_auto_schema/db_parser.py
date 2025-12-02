"""SQLite database parsing for Shortcut actions."""
from __future__ import annotations

import sqlite3
from typing import Any, Dict, List

from .utils import (
    _get_first,
    ensure_serializable,
    infer_parameter_type_from_definition,
    load_plist_data,
    map_type_id_to_type,
)


def load_tools_db(path: str) -> Dict[str, List[Dict[str, Any]]]:
    """Load all tables from a Shortcuts tools SQLite database.

    The function automatically loads the Tools tables and any localization
    tables when present. Binary columns are preserved as-is so downstream
    inference can parse plist payloads.
    """
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cur.fetchall()]

    data: Dict[str, List[Dict[str, Any]]] = {}
    for table in tables:
        cur.execute(f"SELECT * FROM {table}")
        rows = []
        for row in cur.fetchall():
            row_dict = {k: ensure_serializable(row[k]) for k in row.keys()}
            rows.append(row_dict)
        data[table] = rows
    return data


def _extract_parameter_schema(param_definitions: Any) -> Dict[str, Dict[str, Any]]:
    parameters: Dict[str, Dict[str, Any]] = {}
    if isinstance(param_definitions, dict):
        iterable = param_definitions.items()
    elif isinstance(param_definitions, list):
        iterable = []
        for entry in param_definitions:
            if isinstance(entry, dict) and "Key" in entry:
                iterable.append((entry.get("Key"), entry))
    else:
        return parameters

    for key, definition in iterable:
        if not key:
            continue
        param_type = infer_parameter_type_from_definition(definition)
        parameters[key] = {
            "type": param_type,
            "required": bool(definition.get("Required")),
            "default": definition.get("DefaultValue"),
            "allowed_tokens": definition.get("AllowedVariableTypes"),
            "allowed_item_classes": definition.get("AllowedValueTypes") or definition.get("AllowedContentItemClasses"),
            "aggrandizements_allowed": bool(definition.get("SupportsVariableInjection", True)),
            "unknown": param_type == "unknown",
        }
    return parameters


def infer_schema_from_db(db_data: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Dict[str, Any]]:
    """Infer action schemas from the SQLite database payload."""
    tools = db_data.get("Tools", []) or db_data.get("tools", [])
    parameters = db_data.get("Parameters", [])
    param_localizations = db_data.get("ParameterLocalizations", [])
    localizations = db_data.get("ToolLocalizations", []) or db_data.get("toollocalizations", [])
    tool_outputs = db_data.get("ToolOutputTypes", [])

    tool_loc_map = {loc.get("toolId"): loc for loc in localizations}
    param_loc_map = {(loc.get("toolId"), loc.get("key")): loc for loc in param_localizations}

    output_map: Dict[int, List[str]] = {}
    for row in tool_outputs:
        output_map.setdefault(row.get("toolId"), []).append(row.get("typeIdentifier"))

    params_by_tool: Dict[int, List[Dict[str, Any]]] = {}
    for param in parameters:
        params_by_tool.setdefault(param.get("toolId"), []).append(param)

    schema: Dict[str, Dict[str, Any]] = {}
    for row in tools:
        tool_row_id = row.get("rowId") or row.get("ROWID")
        identifier = row.get("id") or _get_first(row, ["WFWorkflowActionIdentifier", "identifier", "Name"])
        if not identifier:
            continue

        localization = tool_loc_map.get(tool_row_id, {})
        title = localization.get("name") or _get_first(row, ["WFDisplayName", "displayName", "Name", "title"]) or identifier
        description = localization.get("descriptionSummary") or localization.get("description")

        # Build parameters from the normalized Parameters table first.
        param_entries = params_by_tool.get(tool_row_id, [])
        parameters_schema: Dict[str, Dict[str, Any]] = {}
        for param in param_entries:
            key = param.get("key")
            if not key:
                continue
            type_id = param.get("typeId")
            param_type = map_type_id_to_type(type_id)
            param_schema = {
                "type": param_type,
                "required": bool(param.get("flags", 0) & 0x1),
                "default": None,
                "allowed_tokens": None,
                "allowed_item_classes": None,
                "aggrandizements_allowed": True,
                "unknown": param_type == "unknown",
            }
            loc = param_loc_map.get((tool_row_id, key), {})
            if loc:
                param_schema["title"] = loc.get("name")
                if loc.get("description"):
                    param_schema["description"] = loc.get("description")
            parameters_schema[key] = param_schema

        # Fallback to embedded parameter definitions when present.
        raw_param_definitions = _get_first(
            row,
            [
                "WFParameterDefinitions",
                "parameterDefinitions",
                "Parameters",
                "WFWorkflowActionParameters",
            ],
        )
        param_definitions = load_plist_data(raw_param_definitions) or raw_param_definitions
        if param_definitions:
            fallback_parameters = _extract_parameter_schema(param_definitions)
            for key, value in fallback_parameters.items():
                if key not in parameters_schema:
                    parameters_schema[key] = value

        special_fields = [key for key in parameters_schema.keys() if key in {"UUID", "GroupingIdentifier", "WFControlFlowMode"}]
        supports_block = bool(special_fields)
        output_classes = output_map.get(tool_row_id)

        schema[identifier] = {
            "id": identifier,
            "title": title,
            "description": description,
            "parameters": parameters_schema,
            "supports_block": supports_block,
            "special_fields": special_fields,
            "required_capabilities": row.get("requirements"),
            "allowed_input_classes": None,
            "produced_output_classes": output_classes,
            "output_name": localization.get("outputResultName"),
            "variable_class": row.get("outputTypeInstance"),
            "takes_input": True,
            "produces_output": bool(output_classes),
        }
    return schema
