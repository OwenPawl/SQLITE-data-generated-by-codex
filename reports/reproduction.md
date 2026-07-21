# Reproduction

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
