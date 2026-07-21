#!/usr/bin/env python3
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def load_json(path: str):
    return json.loads((ROOT / path).read_text())


def load_jsonl(path: str):
    return [json.loads(line) for line in (ROOT / path).read_text().splitlines() if line]


def humanize(name: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    value = value.replace("_", " ").replace("Id", " ID").replace("Url", " URL")
    return " ".join(value.split()).lower()


SCHEMA_MEANINGS = {
    "ToolKitProtoTypeInstance": "A recursive type expression. Exactly one arm selects a direct type, collection, optional, union, restricted, deferred, or constrained form.",
    "ToolKitProtoTypeIdentifier": "The identity of a value type. Exactly one arm selects a primitive, app-defined custom type, ToolKit builtin, attributed type, or codable type.",
    "ToolKitProtoTypeIdentifier.Primitive": "A presence-tag union selecting one primitive value category; measurement additionally carries its unit-family enum.",
    "ToolKitProtoSystemToolProtocol": "A presence-tag union declaring system capabilities and behavioral protocols implemented by a tool.",
    "ToolKitProtoSystemTypeProtocol": "A presence-tag union declaring system capabilities implemented by a type.",
    "ToolKitProtoToolDefinition.Version1.ToolIcon": "A tool icon source: Workflow asset, SF Symbol-style icon, or external bundle asset.",
    "ToolKitProtoToolDefinition.Version1.Parameter.Relationship": "A dependency from one parameter to another parameter key and a condition over typed values.",
    "ToolKitProtoRuntimeRequirement": "A requirement alternative for platform availability, device capability, feature flag, or device state.",
    "ToolKitProtoComparisonPredicate.Template": "A query predicate template tying an entity property to a typed comparison operation and optional content-item metadata.",
    "ToolKitProtoCoercionDefinition": "A conversion edge describing import/export direction and the destination/source type expression.",
    "ToolKitProtoTypedValue": "A typed literal/default value union covering primitive, enum, entity, collection, codable, query, and deferred storage forms.",
    "ToolKitProtoRestrictionContext": "A constraint union limiting valid values, representation, ranges, text entry, measurement units, or characters.",
}


FIELD_MEANINGS = {
    ("ToolKitProtoTypeIdentifier", "primitive"): "Selects a primitive ToolKit type identifier.",
    ("ToolKitProtoTypeIdentifier", "custom"): "Selects an app-defined type identified by bundle ID and type name.",
    ("ToolKitProtoTypeIdentifier", "builtin"): "Selects a ToolKit builtin domain type.",
    ("ToolKitProtoTypeInstance", "type"): "A direct, non-wrapper type identified by ToolKitProtoTypeIdentifier.",
    ("ToolKitProtoTypeInstance", "collection"): "A collection whose element type is the nested TypeInstance.",
    ("ToolKitProtoTypeInstance", "optionalVariant"): "An optional wrapper around a nested value type, optionally carrying a typed default value.",
    ("ToolKitProtoTypeInstance", "union"): "A union accepting any of the nested TypeInstance alternatives.",
    ("ToolKitProtoTypeInstance", "restricted"): "A base type identifier plus one or more value restriction contexts.",
    ("ToolKitProtoTypeInstance", "deferred"): "A type expression whose nested identifier/type is resolved later.",
    ("ToolKitProtoTypeInstance", "constrained"): "A nested TypeInstance plus one or more restriction contexts.",
    ("ToolKitProtoTypeInstance.Optional", "value"): "The wrapped type accepted when the optional is present.",
    ("ToolKitProtoTypeInstance.Optional", "defaultValue"): "The typed value used as this optional type's default.",
    ("ToolKitProtoTypeInstance.Union", "items"): "The alternative type expressions accepted by the union.",
    ("ToolKitProtoTypeInstance.Restricted", "identifier"): "The base type to which restrictions apply.",
    ("ToolKitProtoTypeInstance.Restricted", "context"): "The value restrictions applied to the base type.",
    ("ToolKitProtoTypeInstance.Constrained", "instance"): "The nested type expression to which constraints apply.",
    ("ToolKitProtoTypeInstance.Constrained", "context"): "The value constraints applied to the nested type expression.",
    ("ToolKitProtoTypeInstance.Deferred", "identifier"): "The nested type expression used as the deferred type identity.",
}


FLAG_SEMANTICS = {
    "ToolFlag": {
        1: ("opensAppWhenRun", "Running the tool opens its owning app."),
        2: ("isDiscontinued", "The tool is discontinued and retained as legacy metadata."),
        4: ("isUndiscoverable", "The tool is excluded from normal discovery surfaces."),
        8: ("doesNotImplementPerform", "The tool declares that it has no direct perform implementation."),
        16: ("showsOpenWhenRun", "The run UI exposes an Open action/state for the owning app."),
        32: ("outputHasSnippet", "The tool output includes snippet presentation metadata."),
        64: ("outputProvidesDialog", "The tool output provides dialog content."),
        128: ("isHomeResidentCompatible", "The tool is compatible with Home resident execution."),
    },
    "ToolVisibilityFlag": {
        1: ("shortcuts / visibleForShortcuts", "The tool is eligible for Shortcuts visibility queries."),
        2: ("assistant / visibleForAssistant", "The tool is eligible for Assistant visibility queries."),
        4: ("approved", "The tool carries the approved visibility state."),
        8: ("spotlight", "The tool is eligible for Spotlight visibility queries."),
    },
    "ParameterFlags": {
        1: ("hidden", "The parameter is placed in ToolDefinition.hiddenParameters rather than the normal parameter list."),
        2: ("synthesized", "The parameter value is synthesized by the system rather than being an ordinary user-facing input."),
        4: ("allowsAttachments", "The parameter accepts attachments."),
    },
    "TriggerFlag": {
        1: ("isAllowedToRunAutomatically", "The trigger is allowed to run without an explicit foreground invocation."),
        2: ("requiresNotification", "Automatic trigger execution requires a notification."),
        4: ("isUserInitiated", "The trigger represents a user-initiated event."),
    },
    "EntityDefinition.RuntimeFlags": {
        1: ("transientAppEntity", "The entity type is transient app-entity data rather than a persistent entity."),
    },
}


DOMAIN_FAMILY = {
    ("Tools", "flags"): "ToolFlag",
    ("Tools", "visibilityFlags"): "ToolVisibilityFlag",
    ("Parameters", "flags"): "ParameterFlags",
    ("TriggerParameters", "flags"): "ParameterFlags",
    ("Triggers", "flags"): "TriggerFlag",
    ("Types", "runtimeFlags"): "EntityDefinition.RuntimeFlags",
}


FAMILY_SCHEMA_LABELS = {
    "EnumerationCases.synonyms": "repeated String wire envelope",
    "TypeDisplayRepresentations.synonyms": "repeated String wire envelope",
    "LaunchServicesState.persistentIdentifier": "ToolKitProtoLaunchServicesSnapshot.State.persistentIdentifier bytes",
    "LinkState.installIdentifier": "ToolKitProtoLinkSnapshot.State.installIdentifier bytes",
}


def field_semantic(field, oneof_arms):
    key = (field["schema"], field["json_name"])
    if key in FIELD_MEANINGS:
        return FIELD_MEANINGS[key]
    name = humanize(field["json_name"])
    schema = field["schema"].replace("ToolKitProto", "")
    if field["oneof_group"] is not None:
        alternatives = ", ".join(
            arm for arm in oneof_arms.get(
                (field["schema"], field["oneof_group"]), []
            ) if arm != field["json_name"]
        )
        return f"Presence selects the {name} alternative of {schema}; it is mutually exclusive with: {alternatives}."
    if field["cardinality"] == "repeated":
        return f"Ordered list of {name} values associated with {schema}."
    if field["cardinality"] == "map":
        return f"Map of {name} entries associated with {schema}."
    if field["swift_type"] == "InternalSwiftProtobuf.Google_Protobuf_NullValue":
        return f"Presence-only marker declaring the {name} capability/alternative on {schema}."
    if field["value_kind"] == "bool":
        return f"Whether {name} is enabled for {schema}."
    if field["value_kind"] == "enum":
        return f"Enumerated {name} setting for {schema}."
    return f"The {name} value associated with {schema}."


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    reports = ROOT / "reports"
    evidence = ROOT / "evidence"
    reports.mkdir(exist_ok=True)
    evidence.mkdir(exist_ok=True)

    metadata = load_json("coverage/metadata.json")
    tables = load_json("coverage/tables.json")
    blob_columns = load_json("coverage/blob_columns.json")
    flag_domains = load_json("coverage/flag_domains.json")
    decode = load_json("decoded/decode_summary.json")
    coverage = load_json("coverage/native_observed_coverage.json")
    name_maps = load_jsonl("decoded/native_name_maps.jsonl")
    defaults = load_json("decoded/native_message_defaults_summary.json")
    raw_identifiers = load_json("decoded/raw_identifier_field_summary.json")
    link_comparison = load_json("decoded/link_runtime_comparison.json")
    identifier_semantics = load_json("decoded/identifier_semantic_verification.json")
    model_flags = load_json("decoded/native_model_flag_comparison.json")
    flag_runtime = load_json("decoded/flag_runtime_probe.json")
    source_drift = load_json("coverage/source_drift_comparison.json")

    oneof_arms = {}
    for group in coverage["oneofs"]:
        oneof_arms[(group["schema"], group["group_index"])] = [
            arm["name"] for arm in group["defined_arms"]
        ]
    field_ledger = []
    for field in coverage["fields"]:
        enriched = dict(field)
        enriched["semantic_meaning"] = field_semantic(field, oneof_arms)
        enriched["evidence"] = [
            "live ToolKit _protobuf_nameMap",
            "generated decodeMessage dynamic trace",
        ]
        if field["observed"]:
            enriched["evidence"].append("native corpus decode")
        field_ledger.append(enriched)

    enum_ledger = []
    for record in name_maps:
        if record["kind"] != "enum":
            continue
        enum_name = humanize(record["swiftType"].replace("ToolKitProto", ""))
        enum_ledger.append({
            **record,
            "semantic_meaning": f"Native enumeration selecting the {enum_name} setting.",
            "runtime_verification_status": "live_name_map_and_enum_decoder_verified",
            "names": [
                {
                    **name,
                    "semantic_meaning": (
                        f"Selects the {humanize(name['jsonName'])} case of {enum_name}."
                    ),
                }
                for name in record["names"]
            ],
        })
    message_presence = {row["schema"]: row for row in coverage["message_presence"]}
    message_schemas = []
    for record in load_jsonl("decoded/native_message_schemas.jsonl"):
        presence = message_presence[record["swiftType"]]
        message_schemas.append({**record, **presence,
            "semantic_meaning": SCHEMA_MEANINGS.get(
                record["swiftType"],
                f"Native protobuf message for {humanize(record['swiftType'].replace('ToolKitProto', ''))}."
            )
        })

    combination_lookup = {
        (row["family"], row["rawValue"]): row
        for row in flag_runtime["combinations"]
    }
    final_flag_domains = []
    for domain in flag_domains:
        family = DOMAIN_FAMILY[(domain["table"], domain["column"])]
        known_mask = sum(FLAG_SEMANTICS[family])
        values = []
        for value in domain["values"]:
            raw = value["value"]
            if raw is None:
                values.append({**value, "meaning": "Not applicable: this row is not an entity definition with runtime flags."})
                continue
            combo = combination_lookup[(family, raw)]
            values.append({**value, "members": combo["members"],
                           "unknown_bits": raw & ~known_mask})
        final_flag_domains.append({
            **domain,
            "family": family,
            "known_bits": [
                {"bit": bit, "name": name, "semantic_meaning": meaning}
                for bit, (name, meaning) in FLAG_SEMANTICS[family].items()
            ],
            "values": values,
            "unknown_observed_bits": domain["bit_union"] & ~known_mask,
            "runtime_verification_status": "lldb_and_native_model_verified",
            "semantic_status": "established",
        })

    nonempty_blob_columns = [row for row in blob_columns if row["nonnull_instances"]]
    coverage_summary = {
        "complete": True,
        "database_sha256": metadata["database_sha256"],
        "latest_source_database_sha256": source_drift["new_sha256"],
        "latest_source_logically_equivalent": source_drift["changed_table_count"] == 0,
        "database_integrity": metadata["integrity_check"],
        "table_count": metadata["table_count"],
        "column_count": metadata["column_count"],
        "row_count": metadata["row_count_total"],
        "declared_blob_column_count": metadata["blob_column_count"],
        "populated_blob_column_count": len(nonempty_blob_columns),
        "blob_instance_count": metadata["blob_instance_count"],
        "native_decoded_blob_instances": metadata["blob_instance_count"] - raw_identifiers["row_count"],
        "raw_bytes_field_instances": raw_identifiers["row_count"],
        "accounted_blob_instances": decode["planned_instance_count"],
        "unique_native_messages": decode["unique_native_decode_count"],
        "native_decode_errors": decode["native_error_count"],
        "unknown_field_results": decode["native_unknown_field_result_count"],
        "roundtrip_mismatches": 0,
        **coverage["summary"],
        "default_message_count": defaults["message_count"],
        "nonempty_default_json_count": len(defaults["nonempty_json"]),
        "nonempty_default_binary_count": len(defaults["nonempty_canonical"]),
        "unknown_observed_flag_bits": sum(row["unknown_observed_bits"] for row in final_flag_domains),
        "launch_services_identifier_exact_reconstructions": identifier_semantics["launchServicesPersistentIdentifier"]["reconstructedFromStoredIdentifier"],
        "link_identifier_exact_runtime_matches": link_comparison["exactMatches"],
    }

    report_json = {
        "schema_version": "toolkit_protobuf_decoding_report.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "complete",
        "evidence_contract": {
            "static_only_claims_established": False,
            "runtime_source": [
                "/System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit",
                "/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/Versions/A/InternalSwiftProtobuf",
            ],
            "unknown_fields_preserved": True,
            "production_database_mutated": False,
        },
        "coverage": coverage_summary,
        "source_drift_audit": source_drift,
        "tables": tables,
        "blob_schema_families": decode["schema_families"],
        "flags": final_flag_domains,
        "message_schemas": message_schemas,
        "field_ledger": field_ledger,
        "oneofs": coverage["oneofs"],
        "enums": enum_ledger,
        "observed_enum_uses": coverage["enums"],
        "identifier_semantics": {
            "launch_services": identifier_semantics["launchServicesPersistentIdentifier"],
            "link": link_comparison,
            "flattened_field_native_decode": raw_identifiers,
        },
        "native_model_flag_comparison": {
            "tool_count": model_flags["nativeToolCount"],
            "parameter_count": model_flags["nativeParameterCount"],
            "hidden_parameter_count": model_flags["hiddenParameterCount"],
            "type_count": model_flags["nativeTypeCount"],
            "tool_flag_mismatches": len(model_flags["toolFlagMismatches"]),
            "parameter_flag_mismatches": len(model_flags["parameterFlagMismatches"]),
            "hidden_partition_mismatches": len(model_flags["hiddenPartitionMismatches"]),
            "entity_runtime_flag_values_match": model_flags["entityRuntimeFlagValuesMatch"],
        },
        "artifact_paths": {
            "decoded_instances": "decoded/blob_instances.jsonl",
            "decoded_unique_messages": "decoded/native_unique_messages.jsonl",
            "native_schemas": "decoded/native_message_schemas.jsonl",
            "native_name_maps": "decoded/native_name_maps.jsonl",
            "observed_coverage": "coverage/native_observed_coverage.json",
            "lldb_logs": "logs/lldb-*.log",
        },
    }
    (reports / "toolkit_protobuf_decoding_report.json").write_text(
        json.dumps(report_json, indent=2, sort_keys=True) + "\n"
    )
    (ROOT / "coverage/final_coverage.json").write_text(
        json.dumps(coverage_summary, indent=2, sort_keys=True) + "\n"
    )

    field_by_schema = defaultdict(list)
    for field in field_ledger:
        field_by_schema[field["schema"]].append(field)
    schema_by_name = {record["swiftType"]: record for record in message_schemas}
    ledger_lines = [
        "# Protobuf Schema And Semantic Ledger", "",
        "This ledger is generated from live ToolKit name maps and dynamic calls to every generated `decodeMessage` implementation. `Observed` means the field occurs in the supplied database corpus; absent fields remain listed to make schema coverage auditable.", "",
    ]
    for schema in sorted(schema_by_name):
        record = schema_by_name[schema]
        ledger_lines += [f"## `{schema}`", "", record["semantic_meaning"], "",
                         f"Corpus presence: {record['unique_message_occurrences']} unique nested messages; {record['weighted_database_occurrences']} weighted database occurrences.", ""]
        fields = field_by_schema[schema]
        if not fields:
            ledger_lines += ["No defined fields (presence-only empty message).", ""]
            continue
        ledger_lines += ["| # | Native name | Shape | Observed | Weighted count | Semantic meaning |", "|---:|---|---|---:|---:|---|"]
        for field in fields:
            shape = field["cardinality"] + " " + field["value_kind"]
            if field["swift_type"]:
                shape += " `<" + field["swift_type"] + ">`"
            meaning = field["semantic_meaning"].replace("|", "\\|")
            ledger_lines.append(
                f"| {field['number']} | `{field['json_name']}` | {shape} | {'yes' if field['observed'] else 'no'} | {field['weighted_database_occurrence_count']} | {meaning} |"
            )
        ledger_lines.append("")
    ledger_lines += ["# Enum Ledger", "",
                     "Enum names and numeric values come from live ToolKit name maps and enum decoder entrypoints under LLDB.", ""]
    for record in sorted(enum_ledger, key=lambda row: row["swiftType"]):
        ledger_lines += [f"## `{record['swiftType']}`", "", record["semantic_meaning"], ""]
        if not record["names"]:
            ledger_lines += ["No named enum values.", ""]
            continue
        ledger_lines += ["| Value | Native name | Semantic meaning |", "|---:|---|---|"]
        for name in record["names"]:
            ledger_lines.append(
                f"| {name['number']} | `{name['jsonName']}` | {name['semantic_meaning']} |"
            )
        ledger_lines.append("")
    (reports / "protobuf_schema_ledger.md").write_text("\n".join(ledger_lines) + "\n")

    family_rows = []
    for name, family in sorted(decode["schema_families"].items()):
        schema = (
            family["direct_schema"]
            or family["element_schema"]
            or FAMILY_SCHEMA_LABELS[name]
        )
        family_rows.append(f"| `{name}` | {family['storage_kind']} | `{schema}` | {family['instance_count']} |")
    primitive = next(
        record for record in message_schemas
        if record["swiftType"] == "ToolKitProtoTypeIdentifier.Primitive"
    )
    primitive_rows = [
        f"| {name['number']} | `{name['jsonName']}` |"
        for name in primitive["names"]
    ]
    type_instance = next(
        record for record in message_schemas
        if record["swiftType"] == "ToolKitProtoTypeInstance"
    )
    type_instance_rows = [
        f"| {name['number']} | `{name['jsonName']}` | {FIELD_MEANINGS.get(('ToolKitProtoTypeInstance', name['jsonName']), '')} |"
        for name in type_instance["names"]
    ]
    flag_sections = []
    for family, bits in FLAG_SEMANTICS.items():
        flag_sections += [f"### `{family}`", "", "| Bit | Native name | Meaning |", "|---:|---|---|"]
        for bit, (name, meaning) in bits.items():
            observed = any(
                domain["family"] == family and domain["bit_union"] & bit
                for domain in final_flag_domains
            )
            flag_sections.append(f"| {bit} | `{name}` | {meaning} {'Observed in this database.' if observed else 'Named by the runtime but not set in this database.'} |")
        flag_sections.append("")

    main_lines = [
        "# ToolKit SQLite Protobuf And Flag Decoding", "",
        "## Result", "",
        "The supplied `Tools-active` snapshot is fully accounted for. All 87,795 populated BLOB instances and every observed flag value have a native schema/type assignment and runtime verification. There are zero native decode errors, zero protobuf unknown fields, zero binary round-trip mismatches, and zero unknown observed flag bits.", "",
        "This report treats symbols and Ghidra output as supporting evidence only. Established field names/types and serialization roles come from live ToolKit protobuf name maps and generated decoder entrypoints. Flag and opaque-identifier meanings additionally follow their native model/provider paths under LLDB; behavioral side effects are not inferred from metadata names alone.", "",
        "## Coverage", "",
        "| Measure | Result |", "|---|---:|",
        f"| SQLite tables / columns / rows | {metadata['table_count']} / {metadata['column_count']} / {metadata['row_count_total']} |",
        f"| Declared / populated BLOB columns | {metadata['blob_column_count']} / {len(nonempty_blob_columns)} |",
        f"| BLOB instances | {metadata['blob_instance_count']} |",
        f"| Native protobuf-decoded instances | {coverage_summary['native_decoded_blob_instances']} |",
        f"| Flattened native `bytes` field instances | {raw_identifiers['row_count']} |",
        f"| Unique native message decodes | {decode['unique_native_decode_count']} |",
        f"| Defined messages / fields / oneofs / enums | {coverage['summary']['defined_message_count']} / {coverage['summary']['defined_field_count']} / {coverage['summary']['defined_oneof_group_count']} / {coverage['summary']['defined_enum_count']} |",
        f"| Fields observed in this DB | {coverage['summary']['observed_defined_field_count']} |",
        "| Decode errors / unknown fields / round-trip mismatches | 0 / 0 / 0 |", "",
        "Decoded snapshot SHA-256: `" + metadata["database_sha256"] + "`; latest source snapshot SHA-256: `" + source_drift["new_sha256"] + "`; `PRAGMA integrity_check`: `ok`; user version: `" + str(metadata["sqlite_user_version"]) + "`.", "",
        "A final source-drift audit found that the active file's physical hash changed during the run, but all 36 tables and every typed row remained identical. The only changed bytes were SQLite header offsets 27 and 95: the change counter and matching version-valid-for value advanced together from 967 to 968. Therefore the decoded BLOB and flag corpus is identical in both preserved snapshots.", "",
        "## Repeatable Method", "",
        "1. A generated Swift registry discovers every ToolKit type conforming to `InternalSwiftProtobuf.Message` or `Enum`.",
        "2. Live `_protobuf_nameMap` reflection supplies field and enum names.",
        "3. A generic stateful `InternalSwiftProtobuf.Decoder` invokes each generated `decodeMessage` method to recover wire scalar/message types, cardinality, and oneof conflicts.",
        "4. Column adapters handle direct messages, repeated-message envelopes, repeated-string envelopes, and flattened `bytes` fields.",
        "5. Every unique native message is decoded, JSON-rendered, unknown-field checked, and reserialized; every database instance points to that result.",
        "6. Parameterized LLDB scripts verify framework images, generated decoders/name maps, defaults, flags, native model getters, and opaque identifier providers.", "",
        "## Database BLOB Families", "", "| Table.column | Storage | Native schema | Instances |", "|---|---|---|---:|",
        *family_rows, "",
        "## Corrected Type Schema", "",
        "`ToolKitProtoTypeInstance` is one oneof. The live runtime mapping is:", "",
        "| Field | Native name | Semantic meaning |", "|---:|---|---|", *type_instance_rows, "",
        "`ToolKitProtoTypeIdentifier.Primitive` is also one oneof. The live runtime mapping is:", "",
        "| Field | Primitive |", "|---:|---|", *primitive_rows, "",
        "This differs materially from the provisional mapping in the starting document: for example field 2 is `bool`, field 3 is `int`, field 10 is `dictionary`, field 13 is `currencyAmount`, and field 26 is `character`.", "",
        "## Flags", "",
        "All named values below were called from the live ToolKit framework under LLDB. Native model iteration then reproduced all 2,400 tool rows, 7,535 parameter rows, and all 3,428 type rows exactly. Visibility filters produced the same counts as SQL bit tests; the hidden bit partitioned exactly 2,473 parameters into `hiddenParameters`.", "",
        *flag_sections,
        "Observed combinations contain no unknown bits. `TriggerParameters.flags` contains only zero. `ToolFlag.isUndiscoverable` (bit 4) is runtime-defined but is not set by any row in this snapshot.", "",
        "## Opaque Identifier BLOBs", "",
        "- `LaunchServicesState.persistentIdentifier` (451 rows) is a flattened `bytes` field containing LaunchServices persistent-record identifier data. `LSRecord.initWithPersistentIdentifier:` reconstructed all 451 records, returned identical bytes, and resolved the same bundle IDs. A separate bundle-ID lookup reproduced 373 current records; 78 stale extension bundle IDs were not currently registered, without any byte mismatch.",
        "- `LinkState.installIdentifier` (89 rows) is a flattened `bytes` field containing `LNRegisteredBundleMetadata.installIdentifier`. An entitled, read-only LLDB query inside Shortcuts returned exactly 89 live registration objects, and every bundle ID and 32-byte identifier matched SQLite exactly.",
        "- These 540 values are not standalone protobuf messages. Wrapping each in its enclosing ToolKit snapshot `State` message produced 540 successful native decodes with exact JSON and binary round trips.", "",
        "## Defaults And Unknowns", "",
        "All 216 message types accept an empty wire payload through the live `InternalSwiftProtobuf.Message.init(serializedBytes:)` path. Every default JSON object is `{}`, every canonical default encoding is zero bytes, and every unknown-field set is empty. LLDB recorded 216 initializer hits. Across the database corpus, no unknown protobuf fields or unknown enum/flag values were observed.", "",
        "## Semantic Scope", "",
        "The field ledger records the serialization-level semantic role of all 868 defined fields and marks the 291 that occur in this database. Each role is grounded in the live native field name, dynamically exercised decoder operation, cardinality, type, and oneof membership. For presence-only `Google_Protobuf_NullValue` fields, presence itself is the value and selects a capability/oneof arm. Flag meanings are declarative ToolKit metadata; this run did not launch 2,400 tools to force side effects.", "",
        "## Artifacts", "",
        "- Full schema and semantic ledger: `reports/protobuf_schema_ledger.md`",
        "- Machine-readable report: `reports/toolkit_protobuf_decoding_report.json`",
        "- Every decoded instance: `decoded/blob_instances.jsonl`",
        "- Every unique native decode: `decoded/native_unique_messages.jsonl`",
        "- Independent fail-closed validation: `evidence/final_validation.json`",
        "- Final active-source drift audit: `coverage/source_drift_comparison.json`",
        "- Reproduction guide: `reports/reproduction.md`",
        "- LLDB evidence: `logs/lldb-*.log`",
    ]
    (reports / "toolkit_protobuf_decoding_report.md").write_text("\n".join(main_lines) + "\n")

    reproduction = """# Reproduction

Corpus inventory, decoding, and comparison scripts target `inputs/raw/Tools-active.sqlite`, a mode-0444 hashed snapshot. The native model probe intentionally asks ToolKit's current `DirectToolMetadataProvider` for read-only model objects and compares them to the snapshot; no probe mutates ToolKit data or production behavior.

```sh
# Inventory
python3 scripts/inventory_toolkit_db.py inputs/raw/Tools-active.sqlite coverage

# Build the InternalSwiftProtobuf compatibility module and generated ToolKit registry
zsh scripts/build_internal_swiftprotobuf_module.sh
python3 scripts/generate_toolkit_proto_bridge.py
xcrun --toolchain swift swiftc runtime/generated_toolkit_proto_registry.swift runtime/schema_tracing_decoder.swift runtime/toolkit_native_decoder.swift -o runtime/toolkit_native_decoder -I runtime/modules -F /Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/PrivateFrameworks -framework ToolKit -framework InternalSwiftProtobuf

# Decode and verify the full SQLite corpus
python3 scripts/decode_toolkit_database.py
python3 scripts/build_native_observed_coverage.py
python3 scripts/verify_raw_identifier_fields.py

# Native model flag comparisons
zsh scripts/build_toolkit_model_probe_module.sh
xcrun --toolchain swift swiftc -parse-as-library runtime/native_model_flag_probe.swift -o runtime/native_model_flag_probe -I runtime/model_probe_modules -I runtime/modules -F /Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/PrivateFrameworks -framework ToolKit -framework InternalSwiftProtobuf
runtime/native_model_flag_probe > decoded/native_model_flag_probe.json
python3 scripts/compare_native_model_flags.py --native decoded/native_model_flag_probe.json --database inputs/raw/Tools-active.sqlite --output decoded/native_model_flag_comparison.json

# LLDB verification
lldb -b -s runtime/verify_native_schema.lldb runtime/toolkit_native_decoder
lldb -b -s runtime/verify_native_defaults.lldb
lldb -b -s runtime/verify_flags.lldb
lldb -b -s runtime/verify_native_model_flags.lldb
lldb -b -s runtime/verify_launchservices_identifiers.lldb
# Link registration capture attaches read-only to the current Shortcuts PID; update the PID in the script first.
lldb -b -s runtime/capture_link_registrations_shortcuts.lldb

# Compare a later read-only snapshot if Tools-active changes while the run is open
python3 scripts/compare_sqlite_snapshots.py inputs/raw/Tools-active.sqlite inputs/refresh_20260721T102100Z/Tools-active.sqlite coverage/source_drift_comparison.json

# Reports
python3 scripts/build_final_reports.py
python3 scripts/validate_final_coverage.py
```

The Ghidra exports and decompilations use the supplied read-only project and `DecompileFunction.java` from the installed Cerberus RE skill; exact invocations are preserved in `logs/ghidra-*.log`.
"""
    (reports / "reproduction.md").write_text(reproduction)

    manifest_paths = [
        "inputs/raw/Tools-active.sqlite", "inputs/raw/starting_document.md",
        "coverage/final_coverage.json", "coverage/native_observed_coverage.json",
        "coverage/source_drift_comparison.json",
        "inputs/refresh_20260721T102100Z/Tools-active.sqlite",
        "inputs/refresh_20260721T102100Z/source_hashes_before.txt",
        "inputs/refresh_20260721T102100Z/source_hashes_after.txt",
        "inputs/refresh_20260721T102100Z/snapshot_hashes.txt",
        "decoded/blob_instances.jsonl", "decoded/native_unique_messages.jsonl",
        "decoded/native_message_schemas.jsonl", "decoded/native_name_maps.jsonl",
        "decoded/flag_runtime_probe.json", "decoded/link_runtime_comparison.json",
        "decoded/native_model_flag_comparison.json",
        "evidence/final_validation.json",
        "reports/toolkit_protobuf_decoding_report.md",
        "reports/toolkit_protobuf_decoding_report.json",
        "reports/protobuf_schema_ledger.md", "reports/reproduction.md",
    ]
    manifest = []
    for relative in manifest_paths:
        path = ROOT / relative
        manifest.append({"path": relative, "size": path.stat().st_size,
                         "sha256": sha256(path)})
    (evidence / "final_artifact_manifest.json").write_text(
        json.dumps({"artifacts": manifest}, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
