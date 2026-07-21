import Foundation
import InternalSwiftProtobuf
import ToolKit

guard CommandLine.arguments.count == 2 else {
    fputs("usage: toolkit_typeinstance_smoke HEX\n", stderr)
    exit(64)
}

let hex = CommandLine.arguments[1]
guard hex.count.isMultiple(of: 2) else {
    fputs("hex must have an even length\n", stderr)
    exit(64)
}

var data = Data(capacity: hex.count / 2)
var index = hex.startIndex
while index < hex.endIndex {
    let next = hex.index(index, offsetBy: 2)
    guard let byte = UInt8(hex[index..<next], radix: 16) else {
        fputs("invalid hex\n", stderr)
        exit(64)
    }
    data.append(byte)
    index = next
}

func hexString<C: Collection>(_ bytes: C) -> String where C.Element == UInt8 {
    bytes.map { String(format: "%02x", $0) }.joined()
}

do {
    let message = try ToolKitProtoTypeInstance(serializedBytes: data)
    let roundTrip = try message.serializedData(partial: true)
    print("proto=\(ToolKitProtoTypeInstance.protoMessageName)")
    print("json=\(try message.jsonString())")
    print("unknown=\(hexString(message.unknownFields.data))")
    print("roundtrip=\(hexString(roundTrip))")
} catch {
    fputs("error=\(error)\n", stderr)
    exit(1)
}
