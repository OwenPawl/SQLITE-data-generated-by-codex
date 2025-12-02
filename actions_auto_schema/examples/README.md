# Action Schema Auto-Discovery Examples

Use the package to build a canonical schema catalogue combining SQLite tools databases and sample Shortcut JSON files.

```python
from actions_auto_schema import (
    infer_schema_from_db,
    infer_schema_from_shortcut_json,
    load_shortcut_json,
    load_tools_db,
    merge_schemas,
    normalize_schema,
    save_schema,
)

# Load SQLite snapshots
raw_db = load_tools_db("raw.sqlite")
prod_db = load_tools_db("Tools-prod 2.sqlite")

# Discover from both DBs
raw_schema = infer_schema_from_db(raw_db)
prod_schema = infer_schema_from_db(prod_db)

# Load sample shortcuts (JSON or .zip with JSON files)
sample_workflows = load_shortcut_json("Example shortcuts.zip")
shortcut_schema = infer_schema_from_shortcut_json(sample_workflows)

# Merge and normalize
combined = {**raw_schema, **prod_schema}
combined = merge_schemas(combined, shortcut_schema)
normalized = normalize_schema(combined)

# Save to disk
save_schema(normalized, "schema.json")
```
