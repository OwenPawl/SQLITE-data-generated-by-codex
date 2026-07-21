import Foundation
import ToolKit

struct NativeParameterFlagRow: Codable {
    let key: String
    let flags: Int
    let collection: String
}

struct NativeToolFlagRow: Codable {
    let id: String
    let flags: Int
    let visibilityFlags: Int
    let parameters: [NativeParameterFlagRow]
}

struct NativeTriggerFlagRow: Codable {
    let id: String
    let flags: Int
    let parameters: [NativeParameterFlagRow]
}

struct VisibilityCount: Codable {
    let name: String
    let rawValue: Int
    let count: Int
    let filterDescription: String
}

struct NativeModelFlagOutput: Codable {
    let toolCount: Int
    let triggerCount: Int
    let typeCount: Int
    let entityRuntimeFlagValues: [Int]
    let visibilityCounts: [VisibilityCount]
    let tools: [NativeToolFlagRow]
    let triggers: [NativeTriggerFlagRow]
}

@main
struct NativeModelFlagProbe {
    static func main() throws {
        let provider = try DirectToolMetadataProvider()
        let locale = Locale(identifier: "en_US")

        var toolQuery = ToolDefinitionQuery.all()
        toolQuery.visibility = .any
        let nativeTools = try provider.tools(matching: toolQuery, locale: locale, scope: .all)
        var tools: [NativeToolFlagRow] = []
        for tool in nativeTools {
            let parameters = tool.parameters.map {
                NativeParameterFlagRow(key: $0.key, flags: $0.flags.rawValue, collection: "parameters")
            } + tool.hiddenParameters.map {
                NativeParameterFlagRow(key: $0.key, flags: $0.flags.rawValue, collection: "hiddenParameters")
            }
            tools.append(NativeToolFlagRow(
                id: tool.id,
                flags: tool.flags.rawValue,
                visibilityFlags: tool.visibilityFlags.rawValue,
                parameters: parameters.sorted { ($0.key, $0.collection) < ($1.key, $1.collection) }
            ))
        }

        let namedVisibility: [(String, ToolVisibilityFlag)] = [
            ("shortcuts", .shortcuts),
            ("assistant", .assistant),
            ("approved", .approved),
            ("spotlight", .spotlight),
        ]
        let visibilityCounts = try namedVisibility.map { name, flag in
            var query = ToolDefinitionQuery.all()
            query.visibility = .is(flag)
            return VisibilityCount(
                name: name,
                rawValue: flag.rawValue,
                count: try provider.tools(matching: query, locale: locale, scope: .all).count,
                filterDescription: query.visibility.debugDescription
            )
        }

        let triggers: [NativeTriggerFlagRow] = []
        let nativeTypes = try provider.types(
            matching: TypeDefinitionQuery.all(), locale: locale, scope: .all
        )
        let entityRuntimeFlagValues = nativeTypes.compactMap { definition -> Int? in
            guard case .entity(let entity) = definition else { return nil }
            return entity.runtimeFlags.rawValue
        }

        let output = NativeModelFlagOutput(
            toolCount: tools.count,
            triggerCount: triggers.count,
            typeCount: nativeTypes.count,
            entityRuntimeFlagValues: entityRuntimeFlagValues.sorted(),
            visibilityCounts: visibilityCounts,
            tools: tools.sorted { $0.id < $1.id },
            triggers: triggers.sorted { $0.id < $1.id }
        )
        let encoder = JSONEncoder()
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys, .withoutEscapingSlashes]
        print(String(decoding: try encoder.encode(output), as: UTF8.self))
    }
}
