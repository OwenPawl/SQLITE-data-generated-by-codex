import Foundation

extension Collection where Element == UInt8 {
    var hexString: String {
        map { String(format: "%02x", $0) }.joined()
    }
}

enum CLIError: Error, CustomStringConvertible {
    case usage
    case invalidHex
    case unknownType(String)

    var description: String {
        switch self {
        case .usage:
            return "usage: toolkit_native_decoder list | describe TYPE | describe-all | schema TYPE | schema-all | defaults-all | decode TYPE HEX | scan HEX | batch"
        case .invalidHex:
            return "invalid hex input"
        case .unknownType(let name):
            return "unknown message type: \(name)"
        }
    }
}

struct BatchRequest: Decodable {
    let id: String
    let type: String
    let hex: String
}

struct BatchResponse: Encodable {
    let id: String
    let result: NativeDecodeResult?
    let error: String?
}

struct NativeSchemaDescription: Encodable {
    let kind: String
    let swiftType: String
    let names: [NativeProtoName]
    let fields: [NativeFieldSchema]?
    let oneofGroups: [[Int]]?
}

func dataFromHex(_ hex: String) throws -> Data {
    guard hex.count.isMultiple(of: 2) else { throw CLIError.invalidHex }
    var data = Data(capacity: hex.count / 2)
    var index = hex.startIndex
    while index < hex.endIndex {
        let next = hex.index(index, offsetBy: 2)
        guard let byte = UInt8(hex[index..<next], radix: 16) else {
            throw CLIError.invalidHex
        }
        data.append(byte)
        index = next
    }
    return data
}

func emitJSON<T: Encodable>(_ value: T) throws {
    let encoder = JSONEncoder()
    encoder.outputFormatting = [.sortedKeys, .withoutEscapingSlashes]
    FileHandle.standardOutput.write(try encoder.encode(value))
    FileHandle.standardOutput.write(Data([0x0a]))
}

@main
struct NativeDecoderCLI {
    static func main() {
        do {
            try run()
        } catch {
            fputs("error: \(error)\n", stderr)
            exit(1)
        }
    }

    static func run() throws {
        let arguments = Array(CommandLine.arguments.dropFirst())
        guard let command = arguments.first else { throw CLIError.usage }
        switch command {
        case "list" where arguments.count == 1:
            for messageType in nativeMessageTypes {
                print("message\t\(messageType.swiftType)")
            }
            for enumType in nativeEnumTypes {
                print("enum\t\(enumType.swiftType)")
            }
        case "describe" where arguments.count == 2:
            if let messageType = nativeMessageTypes.first(where: {
                $0.swiftType == arguments[1]
            }) {
                try emitJSON(NativeSchemaDescription(
                    kind: "message",
                    swiftType: messageType.swiftType,
                    names: messageType.names(),
                    fields: nil,
                    oneofGroups: nil
                ))
            } else if let enumType = nativeEnumTypes.first(where: {
                $0.swiftType == arguments[1]
            }) {
                try emitJSON(NativeSchemaDescription(
                    kind: "enum",
                    swiftType: enumType.swiftType,
                    names: enumType.names(),
                    fields: nil,
                    oneofGroups: nil
                ))
            } else {
                throw CLIError.unknownType(arguments[1])
            }
        case "describe-all" where arguments.count == 1:
            for messageType in nativeMessageTypes {
                try emitJSON(NativeSchemaDescription(
                    kind: "message",
                    swiftType: messageType.swiftType,
                    names: messageType.names(),
                    fields: nil,
                    oneofGroups: nil
                ))
            }
            for enumType in nativeEnumTypes {
                try emitJSON(NativeSchemaDescription(
                    kind: "enum",
                    swiftType: enumType.swiftType,
                    names: enumType.names(),
                    fields: nil,
                    oneofGroups: nil
                ))
            }
        case "schema" where arguments.count == 2:
            guard let messageType = nativeMessageTypes.first(where: {
                $0.swiftType == arguments[1]
            }) else { throw CLIError.unknownType(arguments[1]) }
            try emitJSON(NativeSchemaDescription(
                kind: "message",
                swiftType: messageType.swiftType,
                names: messageType.names(),
                fields: messageType.fields(),
                oneofGroups: messageType.oneofGroups()
            ))
        case "schema-all" where arguments.count == 1:
            for messageType in nativeMessageTypes {
                try emitJSON(NativeSchemaDescription(
                    kind: "message",
                    swiftType: messageType.swiftType,
                    names: messageType.names(),
                    fields: messageType.fields(),
                    oneofGroups: messageType.oneofGroups()
                ))
            }
        case "defaults-all" where arguments.count == 1:
            for messageType in nativeMessageTypes {
                try emitJSON(messageType.decode(Data()))
            }
        case "decode" where arguments.count == 3:
            guard let messageType = nativeMessageTypes.first(where: {
                $0.swiftType == arguments[1]
            }) else {
                throw CLIError.unknownType(arguments[1])
            }
            try emitJSON(messageType.decode(try dataFromHex(arguments[2])))
        case "scan" where arguments.count == 2:
            let data = try dataFromHex(arguments[1])
            for messageType in nativeMessageTypes {
                if let result = try? messageType.decode(data) {
                    try emitJSON(result)
                }
            }
        case "batch" where arguments.count == 1:
            let decoder = JSONDecoder()
            while let line = readLine() {
                let request = try decoder.decode(BatchRequest.self, from: Data(line.utf8))
                guard let messageType = nativeMessageTypes.first(where: {
                    $0.swiftType == request.type
                }) else {
                    try emitJSON(BatchResponse(
                        id: request.id,
                        result: nil,
                        error: CLIError.unknownType(request.type).description
                    ))
                    continue
                }
                do {
                    let result = try messageType.decode(try dataFromHex(request.hex))
                    try emitJSON(BatchResponse(id: request.id, result: result, error: nil))
                } catch {
                    try emitJSON(BatchResponse(
                        id: request.id,
                        result: nil,
                        error: String(describing: error)
                    ))
                }
            }
        default:
            throw CLIError.usage
        }
    }
}
