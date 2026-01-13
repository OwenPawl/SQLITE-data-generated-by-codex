# SQLITE-data-generated-by-codex

This repository bundles two SQLite databases that catalog automation tools (Shortcuts-style actions, intents, triggers, and related metadata). Use them as reference snapshots for inspecting tool definitions, parameters, and type information.

## Contents

- `raw.sqlite` – Larger snapshot with classic Shortcuts actions and intents.
- `Tools-prod 2.sqlite` – Production-focused snapshot that includes trigger tables and app-intent entries.

See [`docs/database_overview.md`](docs/database_overview.md) for schema inventories, record counts, and tips on exploring each file with `sqlite3`.

## Export a full catalogue

Generate a complete JSON catalogue for either snapshot (including tools, parameters, types, triggers, and localizations) with the included exporter.

### Prerequisites

- Python 3.9+ (no third-party dependencies; only the standard library is used).

### Steps

1) Choose the database file to export (`raw.sqlite` or `Tools-prod 2.sqlite`).
2) Run the exporter from the repository root, pointing `--database` at the chosen file and `--output` at the destination JSON:

```bash
python export_catalogue.py --database raw.sqlite --output raw_catalogue.json --pretty
python export_catalogue.py --database 'Tools-prod 2.sqlite' --output tools_prod_catalogue.json
```

`--pretty` is optional and writes indented JSON for easier manual inspection.

### Notes

- The output bundles every table relevant to actions/shortcuts, including trigger metadata when present.
- Binary columns (e.g., `typeInstance`, `outputTypeInstance`, `requirements`) are base64-encoded so the full payload is preserved in JSON.
- Each tool entry also includes resolved container metadata (source/attribution and any extra attribution containers) with localized names and synonyms merged in.
