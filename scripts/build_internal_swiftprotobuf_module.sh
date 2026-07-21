#!/bin/zsh
set -euo pipefail

run_dir=${0:A:h:h}
source_dir="$run_dir/reference/swift-protobuf/Sources/SwiftProtobuf"
output_dir="$run_dir/runtime/modules/InternalSwiftProtobuf.swiftmodule"
sdk=$(xcrun --toolchain swift --sdk macosx --show-sdk-path)

mkdir -p "$output_dir"
sources=("$source_dir"/*.swift)

xcrun --toolchain swift swiftc \
  -parse-as-library \
  -emit-module \
  -emit-module-path "$output_dir/arm64-apple-macos.swiftmodule" \
  -emit-module-interface-path "$output_dir/arm64-apple-macos.swiftinterface" \
  -enable-library-evolution \
  -swift-version 6 \
  -package-name swift-protobuf \
  -module-name InternalSwiftProtobuf \
  -target arm64-apple-macosx27.0 \
  -sdk "$sdk" \
  "${sources[@]}"

shasum -a 256 "$output_dir"/*
