"""Shortcut JSON parsing utilities."""
from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import Any, Dict, Iterable, List

from .utils import infer_value_type


def load_shortcut_json(path: str) -> List[Dict[str, Any]]:
    """Load Shortcut JSON workflows from a file or zip archive."""
    file_path = Path(path)
    workflows: List[Dict[str, Any]] = []

    if file_path.suffix.lower() == ".zip":
        with zipfile.ZipFile(file_path, "r") as zf:
            for name in zf.namelist():
                if name.lower().endswith(".json"):
                    with zf.open(name) as handle:
                        workflows.append(json.loads(handle.read().decode()))
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                workflows.extend(data)
            else:
                workflows.append(data)
    return workflows


def _collect_workflow_actions(workflow: Dict[str, Any]) -> Iterable[Dict[str, Any]]:
    actions = workflow.get("WFWorkflowActions") or workflow.get("actions")
    if isinstance(actions, list):
        for action in actions:
            if isinstance(action, dict):
                yield action


def _infer_parameter_entry(value: Any) -> Dict[str, Any]:
    param_type = infer_value_type(value)
    allowed_tokens = None
    aggrandizements_allowed = False

    if isinstance(value, dict):
        serialization = value.get("WFSerializationType")
        if serialization:
            allowed_tokens = [serialization]
            aggrandizements_allowed = bool(value.get("Aggrandizements"))
        if "WFTextTokenString" in value:
            allowed_tokens = ["WFTextTokenString"]
            aggrandizements_allowed = True
    return {
        "type": param_type,
        "required": False,
        "default": None,
        "allowed_tokens": allowed_tokens,
        "aggrandizements_allowed": aggrandizements_allowed,
        "unknown": param_type == "unknown",
    }


def infer_schema_from_shortcut_json(json_data: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Infer schemas by inspecting real workflow JSON payloads."""
    schema: Dict[str, Dict[str, Any]] = {}
    for workflow in json_data:
        for action in _collect_workflow_actions(workflow):
            identifier = action.get("WFWorkflowActionIdentifier") or action.get("identifier")
            parameters = action.get("WFWorkflowActionParameters", {}) or {}
            if not identifier:
                continue

            param_schema: Dict[str, Dict[str, Any]] = {}
            special_fields = []
            for key, value in parameters.items():
                param_schema[key] = _infer_parameter_entry(value)
                if key in {"UUID", "GroupingIdentifier", "WFControlFlowMode"}:
                    special_fields.append(key)

            supports_block = bool(special_fields) or identifier.startswith("is.workflow.actions.conditional")
            output_name = action.get("OutputName") or parameters.get("OutputName")

            schema_entry = schema.setdefault(
                identifier,
                {
                    "id": identifier,
                    "title": identifier,
                    "description": None,
                    "parameters": {},
                    "supports_block": supports_block,
                    "special_fields": special_fields,
                    "required_capabilities": None,
                    "allowed_input_classes": None,
                    "produced_output_classes": None,
                    "output_name": output_name,
                    "variable_class": None,
                    "takes_input": True,
                    "produces_output": output_name is not None,
                },
            )

            # Merge parameter observations.
            for key, param in param_schema.items():
                existing = schema_entry["parameters"].get(key, {})
                merged = {**param, **{k: v for k, v in existing.items() if v is not None}}
                schema_entry["parameters"][key] = merged
            if output_name:
                schema_entry["output_name"] = schema_entry.get("output_name") or output_name
            if special_fields:
                schema_entry["special_fields"] = list(set(schema_entry.get("special_fields", [])) | set(special_fields))
                schema_entry["supports_block"] = True
    return schema
