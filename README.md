# ToolKit SQLite Protobuf Decoding

This repository contains the complete evidence and tooling from the focused
reverse-engineering run over macOS Shortcuts `Tools-active` database version
78.

## Results

- 87,795 populated BLOB instances accounted for.
- 87,255 instances decoded through native ToolKit/InternalSwiftProtobuf.
- 540 flattened native `bytes` fields reconstructed and verified.
- 12,986 unique native messages with zero decode errors, unknown fields, or
  binary round-trip mismatches.
- 216 messages, 868 fields, 43 oneofs, 48 enums, and 262 enum values mapped.
- Six flag domains verified against live ToolKit models with no unknown bits.
- Final source-drift and coverage validator passed 90 of 90 checks.

Start with:

- [Concise report](reports/toolkit_protobuf_decoding_report.md)
- [Complete schema and semantic ledger](reports/protobuf_schema_ledger.md)
- [Machine-readable report](reports/toolkit_protobuf_decoding_report.json)
- [Reproduction guide](reports/reproduction.md)
- [Final validation](evidence/final_validation.json)
- [Artifact hash manifest](evidence/final_artifact_manifest.json)

Large databases, exhaustive instance ledgers, and ToolKit static exports use
Git LFS. Run `git lfs pull` after cloning.

The upstream SwiftProtobuf source checkout used to build the compatibility
module is pinned in [reference/README.md](reference/README.md); generated
interfaces and runtime artifacts are included here.
