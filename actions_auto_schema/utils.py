"""Utility helpers for schema discovery."""
from __future__ import annotations

import json
import plistlib
from typing import Any, Dict, Iterable


def _get_first(obj: Dict[str, Any], keys: Iterable[str]) -> Any:
    """Return the first value found in ``obj`` for the provided key variants."""
    lowered = {k.lower(): v for k, v in obj.items()}
    for key in keys:
        if key.lower() in lowered:
            return lowered[key.lower()]
    return None


def load_plist_data(data: Any) -> Any:
    """Safely parse plist ``data`` from SQLite blobs or text."""
    if data is None:
        return None
    if isinstance(data, memoryview):
        data = data.tobytes()
    if isinstance(data, bytes):
        try:
            return plistlib.loads(data)
        except Exception:
            try:
                return plistlib.loads(data, fmt=plistlib.FMT_BINARY)
            except Exception:
                return None
    if isinstance(data, str):
        try:
            return plistlib.loads(data.encode())
        except Exception:
            return None
    return None


def infer_parameter_type_from_definition(defn: Dict[str, Any]) -> str:
    """Map a parameter definition into a friendly type string."""
    cls = defn.get("Class") or defn.get("ParameterClass") or ""
    cls = str(cls)
    class_map = {
        "WFTextInputParameter": "string",
        "WFStringParameter": "string",
        "WFNumberParameter": "number",
        "WFSliderParameter": "number",
        "WFBooleanParameter": "boolean",
        "WFDictionaryParameter": "dictionary",
        "WFArrayParameter": "list",
        "WFContentArrayParameter": "content-item",
        "WFContentItemParameter": "content-item",
        "WFDateFieldParameter": "date",
        "WFURLParameter": "string",
        "WFEnumerationParameter": "enum",
        "WFExpandingParameter": "dictionary",
        "WFVariableFieldParameter": "token-only",
        "WFRichTextParameter": "rich-text",
    }
    if cls in class_map:
        return class_map[cls]

    # Fallback to validation hints.
    if defn.get("MultiValue"):
        return "list"
    if "Items" in defn:
        return "list"
    return "unknown"


def map_type_id_to_type(type_id: str) -> str:
    """Map a Shortcuts ``typeId`` into a normalized parameter type."""
    mapping = {
        "string": "string",
        "number": "number",
        "integer": "number",
        "boolean": "boolean",
        "array": "list",
        "dictionary": "dictionary",
        "date": "date",
        "time": "date",
        "file": "file",
        "image": "content-item",
        "content": "content-item",
    }
    if type_id is None:
        return "unknown"
    type_id = type_id.lower()
    for key, value in mapping.items():
        if type_id == key or type_id.endswith(f".{key}"):
            return value
    return "unknown"


def infer_value_type(value: Any) -> str:
    """Infer parameter type from a workflow JSON value."""
    if value is None:
        return "unknown"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "list"
    if isinstance(value, dict):
        serialization = value.get("WFSerializationType")
        if serialization:
            if "File" in serialization:
                return "file"
            if "Date" in serialization:
                return "date"
            if "URL" in serialization:
                return "string"
            return "token-only"
        # Dictionaries often represent parameter collections
        return "dictionary"
    return "unknown"


def merge_dicts(base: Dict[str, Any], extra: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries without mutating inputs."""
    merged = {**base}
    for key, value in extra.items():
        if key not in merged:
            merged[key] = value
    return merged


def ensure_serializable(obj: Any) -> Any:
    """Ensure the object can be JSON serialized."""
    try:
        json.dumps(obj)
        return obj
    except TypeError:
        if isinstance(obj, bytes):
            return obj.decode(errors="ignore")
        if isinstance(obj, memoryview):
            return obj.tobytes().decode(errors="ignore")
        if isinstance(obj, dict):
            return {k: ensure_serializable(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [ensure_serializable(v) for v in obj]
    return str(obj)
