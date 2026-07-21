# ToolKit SQLite Protobuf And Flag Decoding

## Result

The supplied `Tools-active` snapshot is fully accounted for. All 87,795 populated BLOB instances and every observed flag value have a native schema/type assignment and runtime verification. There are zero native decode errors, zero protobuf unknown fields, zero binary round-trip mismatches, and zero unknown observed flag bits.

This report treats symbols and Ghidra output as supporting evidence only. Established field names/types and serialization roles come from live ToolKit protobuf name maps and generated decoder entrypoints. Flag and opaque-identifier meanings additionally follow their native model/provider paths under LLDB; behavioral side effects are not inferred from metadata names alone.

## Coverage

| Measure | Result |
|---|---:|
| SQLite tables / columns / rows | 36 / 170 / 156984 |
| Declared / populated BLOB columns | 34 / 20 |
| BLOB instances | 87795 |
| Native protobuf-decoded instances | 87255 |
| Flattened native `bytes` field instances | 540 |
| Unique native message decodes | 12986 |
| Defined messages / fields / oneofs / enums | 216 / 868 / 43 / 48 |
| Fields observed in this DB | 291 |
| Decode errors / unknown fields / round-trip mismatches | 0 / 0 / 0 |

Decoded snapshot SHA-256: `6d81e93772304ff00df64a975546c56795d53ce980c0b95f977eac091350fb5a`; latest source snapshot SHA-256: `817be7a669f5189e57f31fa83157d4adb640b127460c690792b5225288708c6b`; `PRAGMA integrity_check`: `ok`; user version: `78`.

A final source-drift audit found that the active file's physical hash changed during the run, but all 36 tables and every typed row remained identical. The only changed bytes were SQLite header offsets 27 and 95: the change counter and matching version-valid-for value advanced together from 967 to 968. Therefore the decoded BLOB and flag corpus is identical in both preserved snapshots.

## Repeatable Method

1. A generated Swift registry discovers every ToolKit type conforming to `InternalSwiftProtobuf.Message` or `Enum`.
2. Live `_protobuf_nameMap` reflection supplies field and enum names.
3. A generic stateful `InternalSwiftProtobuf.Decoder` invokes each generated `decodeMessage` method to recover wire scalar/message types, cardinality, and oneof conflicts.
4. Column adapters handle direct messages, repeated-message envelopes, repeated-string envelopes, and flattened `bytes` fields.
5. Every unique native message is decoded, JSON-rendered, unknown-field checked, and reserialized; every database instance points to that result.
6. Parameterized LLDB scripts verify framework images, generated decoders/name maps, defaults, flags, native model getters, and opaque identifier providers.

## Database BLOB Families

| Table.column | Storage | Native schema | Instances |
|---|---|---|---:|
| `EntityProperties.typeInstance` | direct_message | `ToolKitProtoTypeInstance` | 2794 |
| `EnumerationCases.synonyms` | repeated_string_envelope | `repeated String wire envelope` | 38540 |
| `LaunchServicesState.persistentIdentifier` | raw_protobuf_bytes_field | `ToolKitProtoLaunchServicesSnapshot.State.persistentIdentifier bytes` | 451 |
| `LinkState.installIdentifier` | raw_protobuf_bytes_field | `ToolKitProtoLinkSnapshot.State.installIdentifier bytes` | 89 |
| `Parameters.relationships` | repeated_message_envelope | `ToolKitProtoToolDefinition.Version1.Parameter.Relationship` | 7535 |
| `Parameters.typeInstance` | direct_message | `ToolKitProtoTypeInstance` | 7535 |
| `PredicateTemplates.comparison` | repeated_message_envelope | `ToolKitProtoComparisonPredicate.Template` | 411 |
| `SystemToolProtocols.protocol` | direct_message | `ToolKitProtoSystemToolProtocol` | 4793 |
| `SystemTypeProtocols.protocol` | direct_message | `ToolKitProtoSystemTypeProtocol` | 1351 |
| `Tools.customIcon` | direct_message | `ToolKitProtoToolDefinition.Version1.ToolIcon` | 264 |
| `Tools.outputTypeInstance` | direct_message | `ToolKitProtoTypeInstance` | 2400 |
| `Tools.requirements` | repeated_message_envelope | `ToolKitProtoRuntimeRequirement` | 2400 |
| `TriggerParameters.relationships` | repeated_message_envelope | `ToolKitProtoToolDefinition.Version1.Parameter.Relationship` | 65 |
| `TriggerParameters.typeInstance` | direct_message | `ToolKitProtoTypeInstance` | 65 |
| `Triggers.outputTypeInstance` | direct_message | `ToolKitProtoTypeInstance` | 42 |
| `Triggers.requirements` | repeated_message_envelope | `ToolKitProtoRuntimeRequirement` | 42 |
| `TypeCoercions.coercionDefinition` | direct_message | `ToolKitProtoCoercionDefinition` | 746 |
| `TypeDisplayRepresentations.synonyms` | repeated_string_envelope | `repeated String wire envelope` | 11876 |
| `Types.id` | direct_message | `ToolKitProtoTypeIdentifier` | 3428 |
| `Types.runtimeRequirements` | repeated_message_envelope | `ToolKitProtoRuntimeRequirement` | 2968 |

## Corrected Type Schema

`ToolKitProtoTypeInstance` is one oneof. The live runtime mapping is:

| Field | Native name | Semantic meaning |
|---:|---|---|
| 1 | `type` | A direct, non-wrapper type identified by ToolKitProtoTypeIdentifier. |
| 2 | `collection` | A collection whose element type is the nested TypeInstance. |
| 3 | `optionalVariant` | An optional wrapper around a nested value type, optionally carrying a typed default value. |
| 4 | `union` | A union accepting any of the nested TypeInstance alternatives. |
| 5 | `restricted` | A base type identifier plus one or more value restriction contexts. |
| 6 | `deferred` | A type expression whose nested identifier/type is resolved later. |
| 7 | `constrained` | A nested TypeInstance plus one or more restriction contexts. |

`ToolKitProtoTypeIdentifier.Primitive` is also one oneof. The live runtime mapping is:

| Field | Primitive |
|---:|---|
| 1 | `noneP` |
| 2 | `bool` |
| 3 | `int` |
| 4 | `number` |
| 5 | `decimal` |
| 6 | `string` |
| 7 | `date` |
| 8 | `dateComponents` |
| 9 | `url` |
| 10 | `dictionary` |
| 11 | `attributedString` |
| 12 | `measurement` |
| 13 | `currencyAmount` |
| 14 | `paymentMethod` |
| 15 | `placemark` |
| 16 | `person` |
| 17 | `file` |
| 18 | `app` |
| 19 | `searchableItem` |
| 20 | `intentsFile` |
| 21 | `shortcut` |
| 22 | `recurrenceRule` |
| 23 | `dateInterval` |
| 24 | `personNameComponents` |
| 25 | `duration` |
| 26 | `character` |

This differs materially from the provisional mapping in the starting document: for example field 2 is `bool`, field 3 is `int`, field 10 is `dictionary`, field 13 is `currencyAmount`, and field 26 is `character`.

## Flags

All named values below were called from the live ToolKit framework under LLDB. Native model iteration then reproduced all 2,400 tool rows, 7,535 parameter rows, and all 3,428 type rows exactly. Visibility filters produced the same counts as SQL bit tests; the hidden bit partitioned exactly 2,473 parameters into `hiddenParameters`.

### `ToolFlag`

| Bit | Native name | Meaning |
|---:|---|---|
| 1 | `opensAppWhenRun` | Running the tool opens its owning app. Observed in this database. |
| 2 | `isDiscontinued` | The tool is discontinued and retained as legacy metadata. Observed in this database. |
| 4 | `isUndiscoverable` | The tool is excluded from normal discovery surfaces. Named by the runtime but not set in this database. |
| 8 | `doesNotImplementPerform` | The tool declares that it has no direct perform implementation. Observed in this database. |
| 16 | `showsOpenWhenRun` | The run UI exposes an Open action/state for the owning app. Observed in this database. |
| 32 | `outputHasSnippet` | The tool output includes snippet presentation metadata. Observed in this database. |
| 64 | `outputProvidesDialog` | The tool output provides dialog content. Observed in this database. |
| 128 | `isHomeResidentCompatible` | The tool is compatible with Home resident execution. Observed in this database. |

### `ToolVisibilityFlag`

| Bit | Native name | Meaning |
|---:|---|---|
| 1 | `shortcuts / visibleForShortcuts` | The tool is eligible for Shortcuts visibility queries. Observed in this database. |
| 2 | `assistant / visibleForAssistant` | The tool is eligible for Assistant visibility queries. Observed in this database. |
| 4 | `approved` | The tool carries the approved visibility state. Observed in this database. |
| 8 | `spotlight` | The tool is eligible for Spotlight visibility queries. Observed in this database. |

### `ParameterFlags`

| Bit | Native name | Meaning |
|---:|---|---|
| 1 | `hidden` | The parameter is placed in ToolDefinition.hiddenParameters rather than the normal parameter list. Observed in this database. |
| 2 | `synthesized` | The parameter value is synthesized by the system rather than being an ordinary user-facing input. Observed in this database. |
| 4 | `allowsAttachments` | The parameter accepts attachments. Observed in this database. |

### `TriggerFlag`

| Bit | Native name | Meaning |
|---:|---|---|
| 1 | `isAllowedToRunAutomatically` | The trigger is allowed to run without an explicit foreground invocation. Observed in this database. |
| 2 | `requiresNotification` | Automatic trigger execution requires a notification. Observed in this database. |
| 4 | `isUserInitiated` | The trigger represents a user-initiated event. Observed in this database. |

### `EntityDefinition.RuntimeFlags`

| Bit | Native name | Meaning |
|---:|---|---|
| 1 | `transientAppEntity` | The entity type is transient app-entity data rather than a persistent entity. Observed in this database. |

Observed combinations contain no unknown bits. `TriggerParameters.flags` contains only zero. `ToolFlag.isUndiscoverable` (bit 4) is runtime-defined but is not set by any row in this snapshot.

## Opaque Identifier BLOBs

- `LaunchServicesState.persistentIdentifier` (451 rows) is a flattened `bytes` field containing LaunchServices persistent-record identifier data. `LSRecord.initWithPersistentIdentifier:` reconstructed all 451 records, returned identical bytes, and resolved the same bundle IDs. A separate bundle-ID lookup reproduced 373 current records; 78 stale extension bundle IDs were not currently registered, without any byte mismatch.
- `LinkState.installIdentifier` (89 rows) is a flattened `bytes` field containing `LNRegisteredBundleMetadata.installIdentifier`. An entitled, read-only LLDB query inside Shortcuts returned exactly 89 live registration objects, and every bundle ID and 32-byte identifier matched SQLite exactly.
- These 540 values are not standalone protobuf messages. Wrapping each in its enclosing ToolKit snapshot `State` message produced 540 successful native decodes with exact JSON and binary round trips.

## Defaults And Unknowns

All 216 message types accept an empty wire payload through the live `InternalSwiftProtobuf.Message.init(serializedBytes:)` path. Every default JSON object is `{}`, every canonical default encoding is zero bytes, and every unknown-field set is empty. LLDB recorded 216 initializer hits. Across the database corpus, no unknown protobuf fields or unknown enum/flag values were observed.

## Semantic Scope

The field ledger records the serialization-level semantic role of all 868 defined fields and marks the 291 that occur in this database. Each role is grounded in the live native field name, dynamically exercised decoder operation, cardinality, type, and oneof membership. For presence-only `Google_Protobuf_NullValue` fields, presence itself is the value and selects a capability/oneof arm. Flag meanings are declarative ToolKit metadata; this run did not launch 2,400 tools to force side effects.

## Artifacts

- Full schema and semantic ledger: `reports/protobuf_schema_ledger.md`
- Machine-readable report: `reports/toolkit_protobuf_decoding_report.json`
- Every decoded instance: `decoded/blob_instances.jsonl`
- Every unique native decode: `decoded/native_unique_messages.jsonl`
- Independent fail-closed validation: `evidence/final_validation.json`
- Final active-source drift audit: `coverage/source_drift_comparison.json`
- Reproduction guide: `reports/reproduction.md`
- LLDB evidence: `logs/lldb-*.log`
