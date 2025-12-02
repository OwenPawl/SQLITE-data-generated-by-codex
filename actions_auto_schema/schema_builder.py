"""Schema merging and normalization logic."""
from __future__ import annotations

import json
from typing import Any, Dict

from .utils import ensure_serializable, merge_dicts


DEFAULT_FIELDS = {
    "title": None,
    "description": None,
    "parameters": {},
    "supports_block": False,
    "special_fields": [],
    "required_capabilities": None,
    "allowed_input_classes": None,
    "produced_output_classes": None,
    "output_name": None,
    "variable_class": None,
    "takes_input": True,
    "produces_output": False,
}


def merge_schemas(db_schema: Dict[str, Dict[str, Any]], json_schema: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Merge database-derived schemas with JSON-observed schemas."""
    merged: Dict[str, Dict[str, Any]] = {**db_schema}
    for action_id, json_entry in json_schema.items():
        if action_id not in merged:
            merged[action_id] = json_entry
            continue
        base_entry = merged[action_id]
        merged_entry = merge_dicts(json_entry, base_entry)

        # Merge parameters deeply.
        parameters: Dict[str, Dict[str, Any]] = {}
        for param_key in set(base_entry.get("parameters", {}).keys()) | set(json_entry.get("parameters", {}).keys()):
            db_param = base_entry.get("parameters", {}).get(param_key, {})
            json_param = json_entry.get("parameters", {}).get(param_key, {})
            combined = merge_dicts(db_param, json_param)
            # Prefer explicit flags from JSON for aggrandizements
            if "aggrandizements_allowed" in json_param:
                combined["aggrandizements_allowed"] = json_param["aggrandizements_allowed"]
            parameters[param_key] = combined
        merged_entry["parameters"] = parameters

        merged[action_id] = merged_entry
    return merged


def normalize_schema(schema: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Normalize schema entries and fill default fields."""
    normalized: Dict[str, Dict[str, Any]] = {}
    for action_id, entry in schema.items():
        normalized_entry = {"id": action_id}
        for key, default in DEFAULT_FIELDS.items():
            normalized_entry[key] = entry.get(key, default)
        normalized_entry["parameters"] = {}
        for param_key, param_value in entry.get("parameters", {}).items():
            normalized_entry["parameters"][param_key] = {
                "type": param_value.get("type", "unknown"),
                "required": bool(param_value.get("required", False)),
                "default": param_value.get("default"),
                "allowed_tokens": param_value.get("allowed_tokens"),
                "allowed_item_classes": param_value.get("allowed_item_classes"),
                "aggrandizements_allowed": bool(param_value.get("aggrandizements_allowed", False)),
                "unknown": bool(param_value.get("unknown", False)),
            }
        normalized[action_id] = normalized_entry
    return normalized


def save_schema(schema: Dict[str, Dict[str, Any]], path: str) -> None:
    """Persist the normalized schema to disk."""
    serializable = {k: ensure_serializable(v) for k, v in schema.items()}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)
