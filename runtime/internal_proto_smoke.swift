import Foundation
import InternalSwiftProtobuf

do {
    let message = try Google_Protobuf_Empty(serializedBytes: Data())
    print("proto=\(Google_Protobuf_Empty.protoMessageName)")
    print("json=\(try message.jsonString())")
    print("unknown=\(message.unknownFields.data.count)")
} catch {
    fputs("error=\(error)\n", stderr)
    exit(1)
}
