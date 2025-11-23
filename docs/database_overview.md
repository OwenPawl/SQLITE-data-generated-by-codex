# Database overview

This repository contains two SQLite snapshots of Apple's automation metadata. Both databases store definitions for tools (Shortcuts actions, intents, and triggers), their parameters, types, and localizations. They share a common core schema but capture different snapshots and auxiliary tables. The notes below walk through table roles so you can understand how each snapshot could be used to rebuild or introspect the Shortcuts catalogue.

## `raw.sqlite`

**Table inventory**

```
AdditionalToolAttributionContainers
Categories
ContainerMetadata
ContainerMetadataLocalizations
ContainerMetadataSynonyms
EntityProperties
EntityPropertyLocalizations
EnumerationCases
LaunchServicesState
LinkActionIdentifiers
LinkState
Metadata
ParameterLocalizations
Parameters
PredicateTemplates
SampleInvocation
SampleInvocationPhrase
SearchKeywords
SystemToolProtocols
SystemTypeProtocols
ToolLocalizations
ToolOutputTypes
Tools
TypeCoercions
TypeDisplayRepresentations
Types
UTTypeCoercions
```

**Snapshot details**

- 1,890 tools, 2,687 types, and 5,752 parameters.
- Example tools include bundled Shortcuts actions such as `is.workflow.actions.comment`, `is.workflow.actions.calculateexpression`, and system intents like `com.apple.UniversalAccess.UASettingsShortcuts.UAToggleStickyKeysIntent`.
- Metadata keys capture Launch Services database versions and a version UUID.

**How the schema drives Shortcuts-like tooling**

- **Tool definitions:** `Tools` holds one row per action/intent (primary identifier in `id`). `flags`, `visibilityFlags`, and `requirements` encode eligibility (e.g., device requirements, entitlement gates) while `outputTypeInstance` serializes the default output type. `sourceContainerId` and `attributionContainerId` link to container metadata that describe the owning app/bundle. `authenticationPolicy` and `deprecationReplacementId` flag sensitive actions and replacements.
- **Input modeling:** `Parameters` ties input slots to each tool via `toolId`, ordering them with `sortOrder`, linking to type metadata through `typeId`, and recording parameter-level constraints in `relationships` and `flags` (e.g., whether multiple values are allowed). `ParameterLocalizations` supplies user-facing names, summaries, and footers keyed by parameter `key` + `toolId`. The `typeInstance` BLOB stores the serialized Swift value specification for the parameter and is complemented by `typeId` for quick joins to `Types`.
- **Type system:** `Types`, `TypeDisplayRepresentations`, and `TypeCoercions`/`UTTypeCoercions` collectively describe accepted data classes, coercion paths, and how to present them. `ToolOutputTypes` expresses which types a tool emits, while `EntityProperties` and `EnumerationCases` refine complex types with property accessors or enum options. `TypeCoercions` rows often include a `toId`/`fromId` pair for legal conversions that an editor can auto-apply.
- **User-facing strings:** `ToolLocalizations`, `ContainerMetadataLocalizations`, `SearchKeywords`, and `SampleInvocationPhrase`/`SampleInvocation` provide UI labels, search indexing terms, and sample phrases that inform Shortcuts search and the “Add Action” browser.
- **Linkage to system state:** `LinkActionIdentifiers`, `LinkState`, and `SystemToolProtocols`/`SystemTypeProtocols` connect actions to Launch Services identifiers, enabling OS lookups to map a bundle or XPC domain to the correct tool definitions.
- **Additional metadata:** `ContainerMetadata`, `ContainerMetadataSynonyms`, and `AdditionalToolAttributionContainers` capture app or extension identifiers that own the tools, allowing attribution in the editor and permission prompts.

## `Tools-prod 2.sqlite`

**Table inventory**

```
AdditionalToolAttributionContainers
Categories
ContainerMetadata
ContainerMetadataLocalizations
ContainerMetadataSynonyms
EntityProperties
EntityPropertyLocalizations
EnumerationCases
LaunchServicesState
LinkActionIdentifiers
LinkState
Metadata
ParameterLocalizations
Parameters
PredicateTemplates
SampleInvocation
SampleInvocationPhrase
SearchKeywords
SystemToolProtocols
SystemTypeProtocols
ToolLocalizations
ToolOutputTypes
ToolParameterTypes
Tools
TriggerLocalizations
TriggerOutputTypes
TriggerParameterLocalizations
TriggerParameters
Triggers
TypeCoercions
TypeDisplayRepresentations
Types
UTTypeCoercions
```

**Snapshot details**

- 1,121 tools, 1,652 types, and 3,380 parameters.
- Example tools skew toward app intent entries such as `com.apple.reminders.CreateGroupAppIntent`, `com.apple.mobilecal.OpenCalendarEditorIntent`, and deep links like `com.apple.Preferences.OpenCameraSettingsDeepLinks`.
- Metadata includes Launch Services versioning plus an `OSVersion` entry (`23B86`).

**How the schema drives Shortcuts-like tooling**

- **Shared tool backbone:** `Tools`, `Parameters`, `Types`, `ToolLocalizations`, and related localization/type tables mirror `raw.sqlite`, so the same join strategies retrieve tool catalog data. The smaller counts suggest a curated, production-focused subset of tools. `authenticationPolicy` and `deprecationReplacementId` columns remain available to gate or replace actions.
- **Trigger pipeline:** `Triggers` parallels `Tools` for background-trigger definitions (e.g., focus changes, time, location). `TriggerParameters`, `TriggerParameterLocalizations`, and `TriggerOutputTypes` mirror the tool parameter/output pattern, giving you enough metadata to render trigger configuration UI and validate values. `TriggerLocalizations` supplies display names and summaries.
- **Richer parameter typing:** `ToolParameterTypes` supplements `Parameters` by attaching a `typeId` keyed by `toolId` + parameter `key`, clarifying situations where the serialized `typeInstance` alone is ambiguous. Use it to tighten editor validation or to infer parameter value shapes when generating APIs.
- **Trigger serialization:** `Triggers` stores the trigger `id`, `flags`, `requirements`, and `outputTypeInstance` (serialized Swift value for emitted content). Each trigger parameter row carries `typeInstance`, `typeId`, `flags`, and `relationships` like tools do, so validation and UI scaffolding can reuse the same code paths.

## How the two snapshots compare

- **Scope and size:** `raw.sqlite` is the larger capture, with roughly 70% more tools and a denser parameter/type catalog than `Tools-prod 2.sqlite`.
- **Schema differences:** `Tools-prod 2.sqlite` adds trigger-specific tables (`Triggers` and related localization/output/parameter tables) and `ToolParameterTypes`, suggesting a focus on app-intent triggers and richer parameter typing. `raw.sqlite` omits these trigger tables but retains the core tool/type/parameter schema.
- **Content focus:** The `raw.sqlite` sample rows show classic Shortcuts actions (e.g., Comment, Calculate Expression), whereas `Tools-prod 2.sqlite` samples center on app intents and deep links, indicating it may be a curated, production-ready subset.
- **Metadata:** Both track Launch Services sequence numbers and UUIDs; only `Tools-prod 2.sqlite` records the OS build string, hinting at a more recent or platform-specific export.

## Key columns and how to read them

- **Identity fields:** `Tools.id` and `Triggers.id` are the canonical identifiers that tie together parameters, output types, and localizations. Foreign keys in parameter/typing tables (`toolId`/`triggerId`) reference them.
- **Ordering:** `Parameters.sortOrder` and `TriggerParameters.sortOrder` define the user-facing order of inputs. Sort by this column before rendering parameter lists.
- **Eligibility and visibility:** `flags`, `visibilityFlags`, and `requirements` columns (on both tools and triggers) encode gating. They are BLOBs/integers that align with internal bitfields; treat non-zero requirements as conditions to check (e.g., OS version, device capability).
- **Serialization blobs:** `typeInstance` and `outputTypeInstance` store binary protobuf payloads describing Swift types and default values. Pair them with `typeId` joins to `Types`/`ToolParameterTypes` to avoid having to deserialize when only the high-level type is needed.
- **Localization keys:** `ParameterLocalizations` and `ToolLocalizations` index rows by (`toolId`, `key`, `languageCode`, `regionCode`). Use both language and region to pick the most specific string available, falling back to language-only entries when region-specific rows are absent.

## Example queries for reconstruction

- Fetch a tool with its parameters, types, and localizations (ordered as the UI would show):

  ```sql
  SELECT t.id, t.toolType, p.key, p.sortOrder, p.flags, tp.typeId AS parameterTypeId,
         tl.title, pl.name AS paramName, pl.summary AS paramSummary
  FROM Tools t
  JOIN Parameters p ON p.toolId = t.rowId
  LEFT JOIN ToolParameterTypes tp ON tp.toolId = t.rowId AND tp.key = p.key
  LEFT JOIN ToolLocalizations tl ON tl.toolId = t.rowId AND tl.languageCode = 'en'
  LEFT JOIN ParameterLocalizations pl ON pl.toolId = t.rowId AND pl.key = p.key AND pl.languageCode = 'en'
  WHERE t.id = 'is.workflow.actions.calculateexpression'
  ORDER BY p.sortOrder;
  ```

- Fetch a trigger and its configuration surface (production snapshot only):

  ```sql
  SELECT trg.id, trg.flags, tp.key, tp.sortOrder, tpl.name AS paramName, tp.typeId
  FROM Triggers trg
  JOIN TriggerParameters tp ON tp.triggerId = trg.rowId
  LEFT JOIN TriggerParameterLocalizations tpl ON tpl.triggerId = trg.rowId AND tpl.key = tp.key AND tpl.languageCode = 'en'
  WHERE trg.id LIKE 'com.apple.%'
  ORDER BY trg.id, tp.sortOrder;
  ```

These patterns surface how presentation strings, ordering, and type enforcement combine so you can rebuild the Shortcuts catalog programmatically.

## Reconstructing shortcuts and triggers from the data

The tables collectively encode everything needed to surface actions/triggers, validate inputs, and assemble a shortcut graph:

1. **Enumerate tools/triggers:** Read `Tools` (and `Triggers` in the production snapshot) to list available building blocks. Use `flags`, `visibilityFlags`, and `requirements` to filter out unsupported entries for a given device profile.
2. **Attach presentation:** Join against `ToolLocalizations`, `TriggerLocalizations`, and `ContainerMetadataLocalizations` using `toolId`/`triggerId` and `sourceContainerId` to render titles, subtitles, categories, and search keywords.
3. **Bind parameters:** For each tool/trigger, query `Parameters` or `TriggerParameters` ordered by `sortOrder`. Pair them with `ParameterLocalizations`/`TriggerParameterLocalizations` for labels and with `Types`/`ToolParameterTypes` for type validation. `relationships` and `flags` define cardinality or dependency rules that the editor must enforce.
4. **Validate and coerce values:** Use `TypeCoercions` and `UTTypeCoercions` to determine allowed conversions. `TypeDisplayRepresentations` guides how to show example values or pickers. `EnumerationCases` and `EntityProperties` reveal discrete options and object fields for complex parameter types.
5. **Compute outputs:** `ToolOutputTypes` or `TriggerOutputTypes` describe what each block emits, allowing downstream step validation and type checking when chaining actions. `outputTypeInstance` on `Tools`/`Triggers` stores the serialized default output payload.
6. **Contextual metadata:** `LaunchServicesState`, `Metadata`, and `Link*` tables help map runtime identifiers (bundle IDs, activity types, URL schemes) back to tools. This is useful for rendering correct icons, enabling handoff from other apps, or syncing with OS registries.

Following these steps lets you reconstruct a Shortcuts-like catalogue, render configuration UIs, and ensure parameter values align with each action’s expectations.

## Working with the databases

Use the built-in `sqlite3` CLI to explore each snapshot:

- List tables: `sqlite3 raw.sqlite ".tables"` or `sqlite3 'Tools-prod 2.sqlite' ".tables"`
- Inspect schema: `sqlite3 raw.sqlite "PRAGMA table_info(Tools);"`
- Count entities: `sqlite3 raw.sqlite "SELECT count(*) FROM Tools;"`
- Peek at sample rows: `sqlite3 'Tools-prod 2.sqlite' "SELECT id, toolType FROM Tools LIMIT 5;"`

The core relationships align across both files: `Tools` defines each action/intent, `Parameters` declares inputs tied to a `toolId`, `Types` and `ToolOutputTypes` describe value shapes, and localization tables attach human-facing strings. Trigger-specific tables in `Tools-prod 2.sqlite` mirror that pattern for trigger records.
