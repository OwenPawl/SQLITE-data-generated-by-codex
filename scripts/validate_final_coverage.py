#!/usr/bin/env python3
import hashlib
import json
import os
import re
import sqlite3
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXPECTED_DATABASE_SHA256 = "6d81e93772304ff00df64a975546c56795d53ce980c0b95f977eac091350fb5a"


def load_json(relative: str):
    return json.loads((ROOT / relative).read_text())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_jsonl(relative: str):
    with (ROOT / relative).open() as handle:
        for line_number, line in enumerate(handle, 1):
            if line.strip():
                yield line_number, json.loads(line)


def main() -> int:
    checks = []
    failures = []

    def check(name: str, passed: bool, observed=None, expected=None) -> None:
        record = {"name": name, "passed": bool(passed)}
        if observed is not None:
            record["observed"] = observed
        if expected is not None:
            record["expected"] = expected
        checks.append(record)
        if not passed:
            failures.append(record)

    metadata = load_json("coverage/metadata.json")
    decode_summary = load_json("decoded/decode_summary.json")
    observed = load_json("coverage/native_observed_coverage.json")
    defaults = load_json("decoded/native_message_defaults_summary.json")
    raw_summary = load_json("decoded/raw_identifier_field_summary.json")
    identifier = load_json("decoded/identifier_semantic_verification.json")
    link = load_json("decoded/link_runtime_comparison.json")
    model_flags = load_json("decoded/native_model_flag_comparison.json")
    runtime_flags = load_json("decoded/flag_runtime_probe.json")
    report = load_json("reports/toolkit_protobuf_decoding_report.json")
    snapshot_manifest = load_json("evidence/startup/input_snapshot_manifest.json")
    source_drift = load_json("coverage/source_drift_comparison.json")

    database = ROOT / "inputs/raw/Tools-active.sqlite"
    database_hash = sha256(database)
    database_mode = oct(os.stat(database).st_mode & 0o777)
    check("database hash", database_hash == EXPECTED_DATABASE_SHA256,
          database_hash, EXPECTED_DATABASE_SHA256)
    check("database snapshot mode", database_mode == "0o444", database_mode, "0o444")
    check("snapshot manifest content matches", snapshot_manifest["all_content_matches"] is True)
    check("snapshot manifest read only", snapshot_manifest["snapshot_read_only"] is True)
    for key, record in snapshot_manifest["records"].items():
        snapshot = ROOT / record["snapshot"]["path"]
        check(f"snapshot exists: {key}", snapshot.is_file())
        check(f"snapshot hash: {key}", sha256(snapshot) == record["snapshot"]["sha256"])
        check(f"snapshot mode: {key}", oct(os.stat(snapshot).st_mode & 0o777) == "0o444")

    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    user_version = connection.execute("PRAGMA user_version").fetchone()[0]
    connection.close()
    check("SQLite integrity", integrity == "ok", integrity, "ok")
    check("SQLite user version", user_version == 78, user_version, 78)

    refresh_database = ROOT / "inputs/refresh_20260721T102100Z/Tools-active.sqlite"
    refresh_hash = sha256(refresh_database)
    refresh_mode = oct(os.stat(refresh_database).st_mode & 0o777)
    active_database = Path(os.path.realpath(
        "/Users/owenpawling/Library/Shortcuts/ToolKit/Tools-active"
    ))
    active_hash = sha256(active_database)
    check("refresh snapshot hash", refresh_hash == source_drift["new_sha256"],
          refresh_hash, source_drift["new_sha256"])
    check("refresh snapshot mode", refresh_mode == "0o444", refresh_mode, "0o444")
    check("current active source hash", active_hash == source_drift["new_sha256"],
          active_hash, source_drift["new_sha256"])
    check("source drift table coverage", source_drift["table_count"] == 36,
          source_drift["table_count"], 36)
    check("source drift logical equivalence", source_drift["changed_table_count"] == 0
          and not source_drift["old_only_tables"] and not source_drift["new_only_tables"])
    check("source physical drift byte count", source_drift["physical_difference_count"] == 2,
          source_drift["physical_difference_count"], 2)
    check("source physical drift offsets", [row["offset"] for row in source_drift["physical_differences"]]
          == [27, 95], [row["offset"] for row in source_drift["physical_differences"]], [27, 95])
    header = source_drift["sqlite_header"]
    check("source SQLite counters", header["new_change_counter"]
          == header["new_version_valid_for"] == header["old_change_counter"] + 1
          == header["old_version_valid_for"] + 1)

    unique_ids = set()
    unique_count = 0
    unique_errors = 0
    unique_unknowns = 0
    unique_roundtrip_mismatches = 0
    canonical_mismatches = 0
    for _, row in iter_jsonl("decoded/native_unique_messages.jsonl"):
        unique_count += 1
        unique_ids.add(row["decode_id"])
        unique_errors += row["error"] is not None
        result = row.get("result") or {}
        unique_unknowns += bool(result.get("unknownFieldsHex"))
        unique_roundtrip_mismatches += row.get("round_trip_equal") is not True
        canonical_mismatches += result.get("canonicalBinaryHex") != row.get("input_hex")
    check("unique native messages", unique_count == 12986, unique_count, 12986)
    check("unique decode IDs", len(unique_ids) == unique_count, len(unique_ids), unique_count)
    check("native decode errors", unique_errors == 0, unique_errors, 0)
    check("native unknown fields", unique_unknowns == 0, unique_unknowns, 0)
    check("native round trips", unique_roundtrip_mismatches == 0,
          unique_roundtrip_mismatches, 0)
    check("native canonical bytes", canonical_mismatches == 0, canonical_mismatches, 0)

    status_counts = Counter()
    instance_count = 0
    reference_count = 0
    bad_references = 0
    instance_native_errors = 0
    instance_unknowns = 0
    for _, row in iter_jsonl("decoded/blob_instances.jsonl"):
        instance_count += 1
        status_counts[row["decode_status"]] += 1
        ids = row.get("decode_ids", [])
        reference_count += len(ids)
        bad_references += sum(decode_id not in unique_ids for decode_id in ids)
        instance_native_errors += row.get("native_error_count", 0)
        instance_unknowns += row.get("native_unknown_field_count", 0)
    check("blob instance ledger", instance_count == 87795, instance_count, 87795)
    check("decoded blob instances", status_counts["decoded"] == 87255,
          status_counts["decoded"], 87255)
    check("raw bytes blob instances", status_counts["accounted_raw_bytes_field"] == 540,
          status_counts["accounted_raw_bytes_field"], 540)
    check("only final blob statuses", set(status_counts) == {"decoded", "accounted_raw_bytes_field"},
          sorted(status_counts), ["accounted_raw_bytes_field", "decoded"])
    check("native decode references", reference_count == 33730, reference_count, 33730)
    check("all decode references resolve", bad_references == 0, bad_references, 0)
    check("instance native errors", instance_native_errors == 0, instance_native_errors, 0)
    check("instance unknown fields", instance_unknowns == 0, instance_unknowns, 0)

    raw_rows = 0
    raw_failures = 0
    for _, row in iter_jsonl("decoded/raw_identifier_field_verification.jsonl"):
        raw_rows += 1
        raw_failures += row["error"] is not None or not all(row["checks"].values())
    check("flattened bytes wrapper rows", raw_rows == 540, raw_rows, 540)
    check("flattened bytes native wrapper verification", raw_failures == 0, raw_failures, 0)
    check("flattened bytes summary", raw_summary["all_native_decodes_succeeded"] is True)

    summary = observed["summary"]
    expected_schema_counts = {
        "defined_message_count": 216,
        "defined_field_count": 868,
        "defined_oneof_group_count": 43,
        "defined_enum_count": 48,
        "observed_defined_field_count": 291,
        "observed_enum_field_count": 93,
        "unresolved_path_count": 0,
    }
    for key, expected in expected_schema_counts.items():
        check(f"schema coverage: {key}", summary[key] == expected, summary[key], expected)
    check("message presence ledger", len(observed["message_presence"]) == 216)
    check("field ledger", len(observed["fields"]) == 868)
    check("oneof ledger", len(observed["oneofs"]) == 43)
    check("report field semantics", len(report["field_ledger"]) == 868 and all(
        row.get("semantic_meaning") and row.get("evidence") for row in report["field_ledger"]
    ))
    check("report enums", len(report["enums"]) == 48)
    check("report enum semantics", all(
        enum.get("semantic_meaning")
        and enum.get("runtime_verification_status") == "live_name_map_and_enum_decoder_verified"
        and all(value.get("semantic_meaning") for value in enum["names"])
        for enum in report["enums"]
    ))

    default_rows = list(iter_jsonl("decoded/native_message_defaults.jsonl"))
    default_failures = sum(
        row["json"] != "{}" or row["canonicalBinaryHex"] != "" or row["unknownFieldsHex"] != ""
        for _, row in default_rows
    )
    check("default message rows", len(default_rows) == 216, len(default_rows), 216)
    check("default encodings", default_failures == 0, default_failures, 0)
    check("default summary", defaults["message_count"] == 216 and not defaults["nonempty_json"]
          and not defaults["nonempty_unknown"] and not defaults["nonempty_canonical"])

    combinations = {(row["family"], row["rawValue"]): row for row in runtime_flags["combinations"]}
    observed_flag_values = 0
    observed_unknown_bits = 0
    for domain in report["flags"]:
        for value in domain["values"]:
            if value["value"] is None:
                continue
            observed_flag_values += 1
            combo = combinations.get((domain["family"], value["value"]))
            if combo is None or combo["members"] != value["members"]:
                observed_unknown_bits += 1
            observed_unknown_bits += value["unknown_bits"] != 0
        observed_unknown_bits += domain["unknown_observed_bits"] != 0
    check("runtime flag combination matrix", len(combinations) == 290, len(combinations), 290)
    check("observed flag domains", len(report["flags"]) == 6, len(report["flags"]), 6)
    check("observed flag values resolved", observed_unknown_bits == 0,
          observed_unknown_bits, 0)
    for key in ("toolFlagMismatches", "parameterFlagMismatches",
                "hiddenPartitionMismatches", "missingNativeTools", "nativeOnlyTools",
                "missingNativeParameters", "nativeOnlyParameters"):
        check(f"native model flags: {key}", not model_flags[key], len(model_flags[key]), 0)
    check("native model tool count", model_flags["nativeToolCount"] == model_flags["storedToolCount"] == 2400)
    check("native model parameter count", model_flags["nativeParameterCount"] == model_flags["storedParameterCount"] == 7535)
    check("native model type count", model_flags["nativeTypeCount"] == model_flags["storedTypeCount"] == 3428)
    check("native entity runtime flags", model_flags["entityRuntimeFlagValuesMatch"] is True)

    launch_services = identifier["launchServicesPersistentIdentifier"]
    check("LaunchServices identifier rows", launch_services["rows"] == 451)
    check("LaunchServices native reconstruction", launch_services["reconstructedFromStoredIdentifier"] == 451)
    check("LaunchServices bundle identity", launch_services["reconstructedBundleIdentifierMatches"] == 451)
    check("LaunchServices byte mismatches", not launch_services["mismatches"])
    check("Link identifier exact matches", link["databaseRows"] == link["runtimeRegistrations"]
          == link["exactMatches"] == 89 and not link["mismatches"]
          and not link["missingAtRuntime"] and not link["runtimeOnly"])

    check("decode summary count", decode_summary["planned_instance_count"]
          == decode_summary["inventory_instance_count"] == instance_count)
    check("metadata blob count", metadata["blob_instance_count"] == instance_count)
    check("report completion", report["status"] == "complete"
          and report["coverage"]["complete"] is True
          and report["coverage"]["accounted_blob_instances"] == instance_count
          and report["coverage"]["latest_source_logically_equivalent"] is True
          and report["coverage"]["latest_source_database_sha256"] == refresh_hash)

    log_requirements = {
        "logs/lldb-verify-native-schema.log": [r"hit count = 1", r"ToolKit.framework", r"InternalSwiftProtobuf.framework"],
        "logs/lldb-verify-native-defaults.log": [r"Process .* exited with status = 0", r"hit count = 216"],
        "logs/lldb-verify-flags.log": [r"Process .* exited with status = 0", r"ToolKit.framework"],
        "logs/lldb-verify-native-model-flags.log": [r"hit count = 2400", r"hit count = 7535", r"hit count = 936"],
        "logs/lldb-verify-launchservices-identifiers.log": [r"hit count = 451", r"LaunchServices"],
        "logs/lldb-capture-link-registrations-shortcuts.log": [r"\(id\) 0x0000000000000059", r"Process .* detached"],
    }
    for relative, patterns in log_requirements.items():
        text = (ROOT / relative).read_text(errors="replace")
        check(f"runtime log evidence: {relative}", all(re.search(pattern, text) for pattern in patterns))

    result = {
        "schema_version": "toolkit_final_validation.v1",
        "status": "passed" if not failures else "failed",
        "check_count": len(checks),
        "failure_count": len(failures),
        "checks": checks,
        "failures": failures,
        "totals": {
            "blob_instances": instance_count,
            "decoded_blob_instances": status_counts["decoded"],
            "raw_bytes_field_instances": status_counts["accounted_raw_bytes_field"],
            "unique_native_messages": unique_count,
            "native_decode_references": reference_count,
            "observed_flag_values": observed_flag_values,
        },
    }
    output = ROOT / "evidence/final_validation.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: result[key] for key in ("status", "check_count", "failure_count", "totals")},
                     indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
