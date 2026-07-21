#!/usr/bin/env python3
"""Generate module-only ToolKit declarations and a native decoder registry."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
METADATA_PATH = RUN_DIR / "static/ghidra/ToolKit/swift_metadata.json"
INTERFACE_PATH = (
    RUN_DIR
    / "runtime/modules/ToolKit.swiftmodule/arm64-apple-macos.swiftinterface"
)
REGISTRY_PATH = RUN_DIR / "runtime/generated_toolkit_proto_registry.swift"
MESSAGE_CONFORMANCE_SUFFIX = " : InternalSwiftProtobuf.Message in ToolKit"
NAME_MAP_CONFORMANCE_SUFFIX = (
    " : InternalSwiftProtobuf._ProtoNameProviding in ToolKit"
)


@dataclass
class Node:
    name: str
    is_message: bool = False
    is_enum: bool = False
    children: dict[str, "Node"] = field(default_factory=dict)


def load_message_names() -> list[str]:
    metadata = json.loads(METADATA_PATH.read_text())
    names = set()
    for conformance in metadata["protocol_conformances"]:
        if not conformance.endswith(MESSAGE_CONFORMANCE_SUFFIX):
            continue
        qualified = conformance[: -len(MESSAGE_CONFORMANCE_SUFFIX)]
        if not qualified.startswith("ToolKit."):
            continue
        names.add(qualified.removeprefix("ToolKit."))
    return sorted(names)


def load_enum_names(message_names: list[str]) -> list[str]:
    metadata = json.loads(METADATA_PATH.read_text())
    message_set = set(message_names)
    names = set()
    for conformance in metadata["protocol_conformances"]:
        if not conformance.endswith(NAME_MAP_CONFORMANCE_SUFFIX):
            continue
        qualified = conformance[: -len(NAME_MAP_CONFORMANCE_SUFFIX)]
        if not qualified.startswith("ToolKit."):
            continue
        name = qualified.removeprefix("ToolKit.")
        if name not in message_set:
            names.add(name)
    return sorted(names)


def build_tree(message_names: list[str], enum_names: list[str]) -> Node:
    root = Node("ToolKit")
    for qualified_name in message_names:
        node = root
        for component in qualified_name.split("."):
            node = node.children.setdefault(component, Node(component))
        node.is_message = True
    for qualified_name in enum_names:
        node = root
        for component in qualified_name.split("."):
            node = node.children.setdefault(component, Node(component))
        node.is_enum = True
    return root


def emit_node(node: Node, indent: str = "") -> list[str]:
    if node.is_enum:
        lines = [
            f"{indent}public enum {node.name} : InternalSwiftProtobuf.Enum, InternalSwiftProtobuf._ProtoNameProviding {{",
            f"{indent}  public init()",
            f"{indent}  public init?(rawValue: Swift.Int)",
            f"{indent}  public var rawValue: Swift.Int {{ get }}",
            f"{indent}  public static let _protobuf_nameMap: InternalSwiftProtobuf._NameMap",
        ]
    else:
        conformance = (
            " : InternalSwiftProtobuf.Message, InternalSwiftProtobuf._ProtoNameProviding"
            if node.is_message
            else ""
        )
        lines = [f"{indent}public struct {node.name}{conformance} {{"]
    if node.is_message:
        lines.extend(
            [
                f"{indent}  public init()",
                f"{indent}  public static let protoMessageName: Swift.String",
                f"{indent}  public static let _protobuf_nameMap: InternalSwiftProtobuf._NameMap",
                f"{indent}  public var unknownFields: InternalSwiftProtobuf.UnknownStorage",
                f"{indent}  public mutating func decodeMessage<D>(decoder: inout D) throws where D : InternalSwiftProtobuf.Decoder",
                f"{indent}  public func traverse<V>(visitor: inout V) throws where V : InternalSwiftProtobuf.Visitor",
            ]
        )
    for child in node.children.values():
        lines.extend(emit_node(child, indent + "  "))
    lines.append(f"{indent}}}")
    return lines


def generate_interface(message_names: list[str], enum_names: list[str]) -> str:
    root = build_tree(message_names, enum_names)
    lines = [
        "// swift-interface-format-version: 1.0",
        "// swift-compiler-version: Apple Swift version 6.4 (swiftlang-6.4.0.25.4 clang-2100.3.25.1)",
        "// swift-module-flags: -target arm64-apple-macosx27.0 -enable-objc-interop -enable-library-evolution -language-mode 6 -module-name ToolKit",
        "import Foundation",
        "import InternalSwiftProtobuf",
        "import Swift",
        "",
    ]
    for node in root.children.values():
        lines.extend(emit_node(node))
    lines.extend(
        [
            "public struct ToolFlag : Swift.OptionSet, Swift.CustomStringConvertible {",
            "  public let rawValue: Swift.Int",
            "  public init(rawValue: Swift.Int)",
            "  public static var opensAppWhenRun: ToolKit.ToolFlag { get }",
            "  public static var isDiscontinued: ToolKit.ToolFlag { get }",
            "  public static var isUndiscoverable: ToolKit.ToolFlag { get }",
            "  public static var doesNotImplementPerform: ToolKit.ToolFlag { get }",
            "  public static var showsOpenWhenRun: ToolKit.ToolFlag { get }",
            "  public static var outputHasSnippet: ToolKit.ToolFlag { get }",
            "  public static var outputProvidesDialog: ToolKit.ToolFlag { get }",
            "  public static var isHomeResidentCompatible: ToolKit.ToolFlag { get }",
            "  public var allFlags: [ToolKit.ToolFlag] { get }",
            "  public var description: Swift.String { get }",
            "}",
            "public struct ToolVisibilityFlag : Swift.OptionSet, Swift.CustomStringConvertible {",
            "  public let rawValue: Swift.Int",
            "  public init(rawValue: Swift.Int)",
            "  public static var shortcuts: ToolKit.ToolVisibilityFlag { get }",
            "  public static var assistant: ToolKit.ToolVisibilityFlag { get }",
            "  public static var visibleForShortcuts: ToolKit.ToolVisibilityFlag { get }",
            "  public static var visibleForAssistant: ToolKit.ToolVisibilityFlag { get }",
            "  public static var approved: ToolKit.ToolVisibilityFlag { get }",
            "  public static var spotlight: ToolKit.ToolVisibilityFlag { get }",
            "  public static var allCases: [ToolKit.ToolVisibilityFlag] { get }",
            "  public var description: Swift.String { get }",
            "}",
            "public struct TriggerFlag : Swift.OptionSet, Swift.CustomStringConvertible {",
            "  public let rawValue: Swift.Int",
            "  public init(rawValue: Swift.Int)",
            "  public static var isAllowedToRunAutomatically: ToolKit.TriggerFlag { get }",
            "  public static var requiresNotification: ToolKit.TriggerFlag { get }",
            "  public static var isUserInitiated: ToolKit.TriggerFlag { get }",
            "  public static var allFlags: [ToolKit.TriggerFlag] { get }",
            "  public var description: Swift.String { get }",
            "}",
            "public struct ParameterDefinition {",
            "  public struct ParameterFlags : Swift.OptionSet {",
            "    public let rawValue: Swift.Int",
            "    public init(rawValue: Swift.Int)",
            "    public static var hidden: ToolKit.ParameterDefinition.ParameterFlags { get }",
            "    public static var synthesized: ToolKit.ParameterDefinition.ParameterFlags { get }",
            "    public static var allowsAttachments: ToolKit.ParameterDefinition.ParameterFlags { get }",
            "    public static var all: [ToolKit.ParameterDefinition.ParameterFlags] { get set }",
            "    public var description: Swift.String { get }",
            "  }",
            "}",
            "public struct EntityDefinition {",
            "  public struct RuntimeFlags : Swift.OptionSet {",
            "    public let rawValue: Swift.Int",
            "    public init(rawValue: Swift.Int)",
            "    public static var transientAppEntity: ToolKit.EntityDefinition.RuntimeFlags { get }",
            "  }",
            "}",
        ]
    )
    lines.append("")
    return "\n".join(lines)


def generate_registry(message_names: list[str], enum_names: list[str]) -> str:
    message_entries = "\n".join(
        f'    NativeMessageType("{name}", ToolKit.{name}.self),'
        for name in message_names
    )
    enum_entries = "\n".join(
        f'    NativeEnumType("{name}", ToolKit.{name}.self),'
        for name in enum_names
    )
    return f"""// Generated by scripts/generate_toolkit_proto_bridge.py.
import Foundation
import InternalSwiftProtobuf
import ToolKit

struct NativeDecodeResult: Codable {{
    let swiftType: String
    let protoMessageName: String
    let json: String
    let unknownFieldsHex: String
    let canonicalBinaryHex: String
}}

struct NativeProtoName: Codable {{
    let number: Int
    let protoName: String
    let jsonName: String?
}}

func reflectedOptionalDescription(_ value: Any) -> String? {{
    let mirror = Mirror(reflecting: value)
    guard mirror.displayStyle == .optional else {{
        return String(describing: value)
    }}
    guard let wrapped = mirror.children.first?.value else {{ return nil }}
    return String(describing: wrapped)
}}

func nativeNames<T: InternalSwiftProtobuf._ProtoNameProviding>(
    _ type: T.Type
) -> [NativeProtoName] {{
    let mapMirror = Mirror(reflecting: T._protobuf_nameMap)
    guard let numberMap = mapMirror.children.first(where: {{
        $0.label == "numberToNameMap"
    }})?.value else {{ return [] }}

    return Mirror(reflecting: numberMap).children.compactMap {{ entry in
        let pair = Array(Mirror(reflecting: entry.value).children)
        guard pair.count == 2, let number = pair[0].value as? Int else {{
            return nil
        }}
        let fields = Dictionary(uniqueKeysWithValues:
            Mirror(reflecting: pair[1].value).children.compactMap {{ child in
                child.label.map {{ ($0, child.value) }}
            }}
        )
        guard let proto = fields["proto"] else {{ return nil }}
        return NativeProtoName(
            number: number,
            protoName: String(describing: proto),
            jsonName: fields["json"].flatMap(reflectedOptionalDescription)
        )
    }}.sorted {{ $0.number < $1.number }}
}}

struct NativeMessageType {{
    let swiftType: String
    let decode: (Data) throws -> NativeDecodeResult
    let names: () -> [NativeProtoName]
    let fields: () -> [NativeFieldSchema]
    let oneofGroups: () -> [[Int]]

    init<M: InternalSwiftProtobuf.Message & InternalSwiftProtobuf._ProtoNameProviding>(
        _ swiftType: String,
        _ type: M.Type
    ) {{
        self.swiftType = swiftType
        self.names = {{ nativeNames(M.self) }}
        self.fields = {{
            traceSchema(M.self, fieldNumbers: nativeNames(M.self).map(\\.number))
        }}
        self.oneofGroups = {{
            traceOneofGroups(
                M.self,
                fieldNumbers: nativeNames(M.self).map(\\.number)
            )
        }}
        self.decode = {{ data in
            let message = try M(serializedBytes: data)
            return NativeDecodeResult(
                swiftType: swiftType,
                protoMessageName: M.protoMessageName,
                json: try message.jsonString(),
                unknownFieldsHex: message.unknownFields.data.hexString,
                canonicalBinaryHex: try message.serializedData(partial: true).hexString
            )
        }}
    }}
}}

struct NativeEnumType {{
    let swiftType: String
    let names: () -> [NativeProtoName]

    init<E: InternalSwiftProtobuf.Enum & InternalSwiftProtobuf._ProtoNameProviding>(
        _ swiftType: String,
        _ type: E.Type
    ) {{
        self.swiftType = swiftType
        self.names = {{ nativeNames(E.self) }}
    }}
}}

let nativeMessageTypes: [NativeMessageType] = [
{message_entries}
]

let nativeEnumTypes: [NativeEnumType] = [
{enum_entries}
]
"""


def main() -> None:
    message_names = load_message_names()
    enum_names = load_enum_names(message_names)
    INTERFACE_PATH.parent.mkdir(parents=True, exist_ok=True)
    INTERFACE_PATH.write_text(generate_interface(message_names, enum_names))
    REGISTRY_PATH.write_text(generate_registry(message_names, enum_names))
    print(
        f"generated {len(message_names)} message declarations and "
        f"{len(enum_names)} enum declarations"
    )
    print(INTERFACE_PATH)
    print(REGISTRY_PATH)


if __name__ == "__main__":
    main()
