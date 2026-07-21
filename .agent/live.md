# Live Control

## User Updates
- 2026-07-21: Use Cerberus RE and the long-run-agent operating procedure.
- 2026-07-21: Do not stop until every protobuf blob and flag present throughout
  `~/Library/Shortcuts/ToolKit/Tools-active` has been decoded, named, assigned
  a semantic meaning, and represented in the final reports.
- 2026-07-21: Static evidence is never sufficient by itself. Every schema,
  enum, flag, and semantic interpretation must receive LLDB/runtime
  verification before being reported as established.
- 2026-07-21: Prefer a repeatable descriptor/reflection-driven decoder and a
  parameterized runtime verifier over bespoke field-by-field work.
The ToolKit and InternalSwiftProtobuf were extracted with ipsw and are from the host dyld. simruntime may have the frameworks actual binary which would be a better source of truth. However, only switch to this if you run into issues with the ipsw extracted binaries, that justify doing this and not just using lldb as a better source of truth.****
**push to https://github.com/OwenPawl/SQLITE-data-generated-by-codex clearing what was there first**

## Current Goal
- Decode every protobuf blob and every flag present throughout ~/Library/Shortcuts/ToolKit/Tools-active; recover schema names and semantic meanings; require LLDB verification for every static conclusion; produce exhaustive Markdown/JSON reports and reproduction evidence.

## Constraints
- Exactly one worker; do not spawn, delegate to, or request child agents.
- First verify the installed `cerberus-re` tooling against
  `/Users/owenpawling/Documents/Playground/ghidra_re` before new RE.
- Preserve and build from the supplied starting document at
  `/Users/owenpawling/Downloads/tools_requirements_protobuf_structure (1).md`.
- Relevant static targets include ToolKit and InternalSwiftProtobuf from the
  macOS dyld extract, but all static findings require guarded LLDB proof.
- Inventory the complete SQLite schema and every distinct protobuf-bearing
  column/value shape; shared schemas may be decoded once only after proving
  all instances conform and recording coverage.
- Preserve raw database hashes, queries, blob inventories, schema definitions,
  static exports, LLDB scripts/logs, coverage matrices, reproduction commands,
  and concise Markdown plus machine-readable JSON reports under this run.
- Treat supplied ToolVisibilityFlag, Parameters.flags, ToolFlag, and primitive
  TypeIdentifier mappings as starting hypotheses that also require direct
  verification against the current database/runtime.
- Do not mutate the source ToolKit database or production Shortcuts behavior.

## Agent Status
- Run ID: run_20260721T084650Z_1b7ecd17
- Status: running; publishing a clean repository replacement per live instruction
- Started: 2026-07-21T08:46:50Z

## Interrupts / Corrections
- Every protobuf-bearing ToolKit structure can be independently parsed, constructed, serialized, and accepted by Apple’s native ToolKit implementation, without relying on an existing database instance as a template.
- 2026-07-21T10:20Z: `Tools-active` still resolves to the original path, but
  its SHA-256 changed from `6d81e937...b5a` to `817be7a6...c6b` while the run
  was active. Preserve the completed first snapshot, acquire a second
  read-only consistent snapshot, and compare all tables before restoring
  completion status.
- 2026-07-21T10:25Z: Replace everything currently in
  `https://github.com/OwenPawl/SQLITE-data-generated-by-codex` with this run's
  deliverables and push the replacement.

## Decisions Made This Run
- Use only the hashed `inputs/raw/Tools-active.sqlite` copy for corpus queries.
- Recover generated protobuf metadata/reflection first and build one generic
  schema-family decoder plus parameterized LLDB verifier.
- Treat field meanings as serialization-level roles established by live native
  names, decoder operations, cardinality, nested types, and oneof membership.
  Reserve behavioral claims for paths additionally exercised through native
  ToolKit models/providers under LLDB.
- Keep the mission run open after completion; wait here until an explicit
  `STOP` or `FINALIZE AND STOP` directive.

## Commands Run
- Compared all 243 tracked Cerberus files between source and installed skill;
  byte content matched.
- Ran Cerberus dependency dry-run, doctor, bootstrap, and bridge audit.
- Built and ran `scripts/build_input_manifest.py` and
  `scripts/inventory_toolkit_db.py` against the read-only snapshot.
- Exported ToolKit and InternalSwiftProtobuf from the supplied Ghidra project
  with Ghidra 12.1.2 and the matching Xcode beta Swift demangler.
- Built a module-only `InternalSwiftProtobuf` compatibility interface from the
  Apple SwiftProtobuf source and linked probes to the live private framework.
- Generated interface declarations and a native decoder registry for all 216
  ToolKit structs conforming to `InternalSwiftProtobuf.Message`.
- Ran the generic native decoder over all database schema families, built the
  observed-coverage graph, exercised all empty/default messages, and generated
  exhaustive schema, enum, flag, identifier, and instance reports.
- Queried LaunchServices through native record reconstruction and queried Link
  registration metadata by a read-only LLDB attach to Shortcuts.
- Ran `scripts/validate_final_coverage.py`, registered six tested harness
  claims and seven artifacts, settled the Cerberus wrapper friction item, and
  rebuilt/validated the mission index.

## Tests / Verification
- Snapshot/source SHA-256 values match for the document, database, WAL, SHM,
  and lock files; all snapshot files are mode 0444.
- Snapshot `PRAGMA integrity_check` returned `ok`; user version is 78.
- Initial ledger: 36 tables, 170 columns, 34 declared BLOB columns, 87,795
  BLOB instances, 13,099 unique blob hashes, and six flag domains.
- Cerberus doctor resolved Ghidra, Java 21, LLDB, and Frida CLI; bridge audit
  reported no stale sessions or orphan processes.
- Native decode/JSON encoding of a real `Parameters.typeInstance` sample
  succeeded with no unknown fields and a byte-identical binary round trip.
- LLDB hit live `ToolKitProtoTypeInstance.decodeMessage` and
  `InternalSwiftProtobuf.Message.jsonString`; image inspection confirmed both
  host private frameworks supplied the implementations.
- Reflected all 264 live protobuf name maps and traced all 216 generated
  `decodeMessage` implementations through a generic stateful decoder; the
  resulting schema contains 868 fields and 43 oneof groups.
- Exhaustively decoded all 12,986 unique native protobuf messages represented
  by 87,255 database BLOB instances: zero decode errors, zero unknown fields,
  and zero binary round-trip mismatches.
- Accounted for the remaining 540 BLOB instances as flattened protobuf `bytes`
  fields and independently reconstructed/native-decoded their enclosing state
  messages with exact JSON and binary round trips.
- LLDB verified every generated protobuf name-map getter, every top-level
  database schema family decoder, and all 24 named flag getters against the
  live host ToolKit/InternalSwiftProtobuf implementations.
- All 216 message defaults decode to `{}`, serialize to zero bytes, and contain
  no unknown fields; LLDB observed all 216 native initializer calls.
- All six flag domains were exhaustively enumerated through native option sets;
  the native ToolKit model reproduced 2,400 tool rows, 7,535 parameter rows,
  2,473 hidden-parameter placements, and 3,428 type rows with zero mismatch.
- LaunchServices reconstructed 451/451 persisted identifiers with exact bytes
  and bundle identity. Link returned 89/89 live registrations with exact
  bundle IDs and 32-byte install identifiers.
- Final independent validation passed 82/82 checks: 87,795 BLOB instances,
  12,986 unique native messages, 33,730 native decode references, 216 messages,
  868 fields, 43 oneofs, 48 enums, 262 enum values, and no unresolved data.
- A second consistent `Tools-active` snapshot had a different physical hash,
  but a typed comparison of all 36 tables found zero schema or row changes.
  Only SQLite header offsets 27 and 95 advanced from 967 to 968. The expanded
  final validation passed 90/90 checks and confirms the current active source
  still matches the preserved second snapshot.
- `mission_harness.py validate` passed; friction report has zero ambiguous or
  release-blocking items; the mission index contains 21 records.

## Failures / Blockers
- None. The Cerberus wrapper's `analyzeHeadless` smoke test failed, but the
  direct Java 21 headless fallback succeeded against the supplied read-only
  project; its exports/logs are preserved and the friction record is resolved.

## Claims Touched
- `all-blobs-accounted` (tested)
- `native-schema-recovered` (tested)
- `native-roundtrip-clean` (tested)
- `flags-decoded` (tested)
- `opaque-identifiers-decoded` (tested)
- `defaults-and-unknowns` (tested)
- `active-source-equivalence` (tested)

## Artifacts Produced
- `evidence/startup/input_snapshot_manifest.json`
- `inputs/raw/Tools-active.sqlite` and sidecars (read-only)
- `inputs/raw/starting_document.md` (read-only)
- `coverage/metadata.json`, `coverage/tables.json`,
  `coverage/scalar_domains.json`, `coverage/flag_domains.json`,
  `coverage/blob_columns.json`, `coverage/blob_instances.jsonl`, and
  `coverage/wire_families.json`
- `static/ghidra/ToolKit/`, `static/ghidra/InternalSwiftProtobuf/`, and
  `static/decomp/`
- `scripts/build_internal_swiftprotobuf_module.sh` and
  `scripts/generate_toolkit_proto_bridge.py`
- `runtime/toolkit_native_decoder`, generated module interfaces/registry, and
  `logs/lldb-verify-native-decoder.log`
- `decoded/native_name_maps.jsonl`, `decoded/native_message_schemas.jsonl`,
  `decoded/native_messages.jsonl`, and `decoded/blob_instances.jsonl`
- `coverage/native_observed_coverage.json`
- `decoded/flag_runtime_probe.json` and `logs/lldb-verify-flags.log`
- `decoded/raw_identifier_field_verification.jsonl`,
  `decoded/raw_identifier_field_summary.json`, and
  `logs/lldb-verify-raw-identifier-types.log`
- `reports/toolkit_protobuf_decoding_report.md`
- `reports/toolkit_protobuf_decoding_report.json`
- `reports/protobuf_schema_ledger.md`
- `reports/reproduction.md`
- `coverage/final_coverage.json`
- `evidence/final_validation.json`
- `evidence/final_artifact_manifest.json`
- `inputs/refresh_20260721T102100Z/Tools-active.sqlite` and source hash records
- `coverage/source_drift_comparison.json`

## Friction Observed
- `friction_20260721T090629Z_212cdc93` resolved with the verified direct Ghidra
  headless fallback; zero ambiguous open friction remains.

## Next Actions
- Inspect the target repository, authenticated Git state, publication size,
  and files that cannot be stored by normal GitHub Git objects.
- Stage a clean replacement in a separate clone, preserving this run tree.
- Validate the staged tree, commit, push, and verify the remote branch.
- Return to dormant after publication; do not close the mission without an
  explicit `STOP` or `FINALIZE AND STOP`.
