import Foundation
import ToolKit

struct NamedFlag: Codable {
    let family: String
    let name: String
    let rawValue: Int
    let description: String?
}

struct FlagCombination: Codable {
    let family: String
    let rawValue: Int
    let description: String?
    let members: [String]
    let unknownBits: Int
}

struct FlagProbeOutput: Codable {
    let namedFlags: [NamedFlag]
    let combinations: [FlagCombination]
}

@main
struct FlagProbe {
    static func main() throws {
        let namedFlags = [
            NamedFlag(family: "ToolFlag", name: "opensAppWhenRun", rawValue: ToolFlag.opensAppWhenRun.rawValue, description: ToolFlag.opensAppWhenRun.description),
            NamedFlag(family: "ToolFlag", name: "isDiscontinued", rawValue: ToolFlag.isDiscontinued.rawValue, description: ToolFlag.isDiscontinued.description),
            NamedFlag(family: "ToolFlag", name: "isUndiscoverable", rawValue: ToolFlag.isUndiscoverable.rawValue, description: ToolFlag.isUndiscoverable.description),
            NamedFlag(family: "ToolFlag", name: "doesNotImplementPerform", rawValue: ToolFlag.doesNotImplementPerform.rawValue, description: ToolFlag.doesNotImplementPerform.description),
            NamedFlag(family: "ToolFlag", name: "showsOpenWhenRun", rawValue: ToolFlag.showsOpenWhenRun.rawValue, description: ToolFlag.showsOpenWhenRun.description),
            NamedFlag(family: "ToolFlag", name: "outputHasSnippet", rawValue: ToolFlag.outputHasSnippet.rawValue, description: ToolFlag.outputHasSnippet.description),
            NamedFlag(family: "ToolFlag", name: "outputProvidesDialog", rawValue: ToolFlag.outputProvidesDialog.rawValue, description: ToolFlag.outputProvidesDialog.description),
            NamedFlag(family: "ToolFlag", name: "isHomeResidentCompatible", rawValue: ToolFlag.isHomeResidentCompatible.rawValue, description: ToolFlag.isHomeResidentCompatible.description),
            NamedFlag(family: "ToolVisibilityFlag", name: "shortcuts", rawValue: ToolVisibilityFlag.shortcuts.rawValue, description: ToolVisibilityFlag.shortcuts.description),
            NamedFlag(family: "ToolVisibilityFlag", name: "assistant", rawValue: ToolVisibilityFlag.assistant.rawValue, description: ToolVisibilityFlag.assistant.description),
            NamedFlag(family: "ToolVisibilityFlag", name: "visibleForShortcuts", rawValue: ToolVisibilityFlag.visibleForShortcuts.rawValue, description: ToolVisibilityFlag.visibleForShortcuts.description),
            NamedFlag(family: "ToolVisibilityFlag", name: "visibleForAssistant", rawValue: ToolVisibilityFlag.visibleForAssistant.rawValue, description: ToolVisibilityFlag.visibleForAssistant.description),
            NamedFlag(family: "ToolVisibilityFlag", name: "approved", rawValue: ToolVisibilityFlag.approved.rawValue, description: ToolVisibilityFlag.approved.description),
            NamedFlag(family: "ToolVisibilityFlag", name: "spotlight", rawValue: ToolVisibilityFlag.spotlight.rawValue, description: ToolVisibilityFlag.spotlight.description),
            NamedFlag(family: "ParameterFlags", name: "hidden", rawValue: ParameterDefinition.ParameterFlags.hidden.rawValue, description: ParameterDefinition.ParameterFlags.hidden.description),
            NamedFlag(family: "ParameterFlags", name: "synthesized", rawValue: ParameterDefinition.ParameterFlags.synthesized.rawValue, description: ParameterDefinition.ParameterFlags.synthesized.description),
            NamedFlag(family: "ParameterFlags", name: "allowsAttachments", rawValue: ParameterDefinition.ParameterFlags.allowsAttachments.rawValue, description: ParameterDefinition.ParameterFlags.allowsAttachments.description),
            NamedFlag(family: "TriggerFlag", name: "isAllowedToRunAutomatically", rawValue: TriggerFlag.isAllowedToRunAutomatically.rawValue, description: TriggerFlag.isAllowedToRunAutomatically.description),
            NamedFlag(family: "TriggerFlag", name: "requiresNotification", rawValue: TriggerFlag.requiresNotification.rawValue, description: TriggerFlag.requiresNotification.description),
            NamedFlag(family: "TriggerFlag", name: "isUserInitiated", rawValue: TriggerFlag.isUserInitiated.rawValue, description: TriggerFlag.isUserInitiated.description),
            NamedFlag(family: "EntityDefinition.RuntimeFlags", name: "transientAppEntity", rawValue: EntityDefinition.RuntimeFlags.transientAppEntity.rawValue, description: nil),
        ]

        let toolNames: [(String, ToolFlag)] = [
            ("opensAppWhenRun", .opensAppWhenRun),
            ("isDiscontinued", .isDiscontinued),
            ("isUndiscoverable", .isUndiscoverable),
            ("doesNotImplementPerform", .doesNotImplementPerform),
            ("showsOpenWhenRun", .showsOpenWhenRun),
            ("outputHasSnippet", .outputHasSnippet),
            ("outputProvidesDialog", .outputProvidesDialog),
            ("isHomeResidentCompatible", .isHomeResidentCompatible),
        ]
        let visibilityNames: [(String, ToolVisibilityFlag)] = [
            ("shortcuts", .shortcuts), ("assistant", .assistant),
            ("approved", .approved), ("spotlight", .spotlight),
        ]
        let parameterNames: [(String, ParameterDefinition.ParameterFlags)] = [
            ("hidden", .hidden), ("synthesized", .synthesized),
            ("allowsAttachments", .allowsAttachments),
        ]
        let triggerNames: [(String, TriggerFlag)] = [
            ("isAllowedToRunAutomatically", .isAllowedToRunAutomatically),
            ("requiresNotification", .requiresNotification),
            ("isUserInitiated", .isUserInitiated),
        ]

        let toolCombinations = (0...255).map { rawValue in
            let value = ToolFlag(rawValue: rawValue)
            return FlagCombination(
                family: "ToolFlag", rawValue: rawValue, description: value.description,
                members: toolNames.compactMap { value.contains($0.1) ? $0.0 : nil },
                unknownBits: rawValue & ~toolNames.reduce(0) { $0 | $1.1.rawValue }
            )
        }
        let visibilityCombinations = (0...15).map { rawValue in
            let value = ToolVisibilityFlag(rawValue: rawValue)
            return FlagCombination(
                family: "ToolVisibilityFlag", rawValue: rawValue, description: value.description,
                members: visibilityNames.compactMap { value.contains($0.1) ? $0.0 : nil },
                unknownBits: rawValue & ~visibilityNames.reduce(0) { $0 | $1.1.rawValue }
            )
        }
        let parameterCombinations = (0...7).map { rawValue in
            let value = ParameterDefinition.ParameterFlags(rawValue: rawValue)
            return FlagCombination(
                family: "ParameterFlags", rawValue: rawValue, description: value.description,
                members: parameterNames.compactMap { value.contains($0.1) ? $0.0 : nil },
                unknownBits: rawValue & ~parameterNames.reduce(0) { $0 | $1.1.rawValue }
            )
        }
        let triggerCombinations = (0...7).map { rawValue in
            let value = TriggerFlag(rawValue: rawValue)
            return FlagCombination(
                family: "TriggerFlag", rawValue: rawValue, description: value.description,
                members: triggerNames.compactMap { value.contains($0.1) ? $0.0 : nil },
                unknownBits: rawValue & ~triggerNames.reduce(0) { $0 | $1.1.rawValue }
            )
        }
        let runtimeCombinations = (0...1).map { rawValue in
            let value = EntityDefinition.RuntimeFlags(rawValue: rawValue)
            return FlagCombination(
                family: "EntityDefinition.RuntimeFlags", rawValue: rawValue, description: nil,
                members: value.contains(.transientAppEntity) ? ["transientAppEntity"] : [],
                unknownBits: rawValue & ~EntityDefinition.RuntimeFlags.transientAppEntity.rawValue
            )
        }
        let combinations = toolCombinations + visibilityCombinations +
            parameterCombinations + triggerCombinations + runtimeCombinations

        let encoder = JSONEncoder()
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys, .withoutEscapingSlashes]
        print(String(decoding: try encoder.encode(FlagProbeOutput(namedFlags: namedFlags, combinations: combinations)), as: UTF8.self))
    }
}
