#!/bin/zsh
set -euo pipefail

root=${0:A:h:h}
output="$root/runtime/model_probe_modules/ToolKit.swiftmodule"
mkdir -p "$output"
cp "$root/runtime/modules/ToolKit.swiftmodule/arm64-apple-macos.swiftinterface" \
   "$output/arm64-apple-macos.swiftinterface"
cat "$root/runtime/toolkit_model_probe_overlay.swiftinterface" >> \
    "$output/arm64-apple-macos.swiftinterface"
