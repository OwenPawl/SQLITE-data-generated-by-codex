import Foundation
import InternalSwiftProtobuf

struct NativeFieldSchema: Codable {
    let number: Int
    let cardinality: String
    let valueKind: String
    let swiftType: String?
}

struct SchemaTracingDecoder: InternalSwiftProtobuf.Decoder {
    private let fieldNumbers: [Int]
    private var nextIndex = 0
    private(set) var currentFieldNumber = 0
    private(set) var fields: [NativeFieldSchema] = []
    private(set) var conflictCount = 0

    init(fieldNumbers: [Int]) {
        self.fieldNumbers = fieldNumbers
    }

    mutating func handleConflictingOneOf() throws {
        conflictCount += 1
    }

    mutating func nextFieldNumber() throws -> Int? {
        guard nextIndex < fieldNumbers.count else { return nil }
        currentFieldNumber = fieldNumbers[nextIndex]
        nextIndex += 1
        return currentFieldNumber
    }

    private mutating func record(
        _ cardinality: String,
        _ valueKind: String,
        _ swiftType: String? = nil
    ) {
        fields.append(NativeFieldSchema(
            number: currentFieldNumber,
            cardinality: cardinality,
            valueKind: valueKind,
            swiftType: swiftType
        ))
    }

    mutating func decodeSingularFloatField(value: inout Float) throws { record("singular", "float"); value = 1 }
    mutating func decodeSingularFloatField(value: inout Float?) throws { record("singular_presence", "float"); value = 1 }
    mutating func decodeRepeatedFloatField(value: inout [Float]) throws { record("repeated", "float"); value.append(1) }
    mutating func decodeSingularDoubleField(value: inout Double) throws { record("singular", "double"); value = 1 }
    mutating func decodeSingularDoubleField(value: inout Double?) throws { record("singular_presence", "double"); value = 1 }
    mutating func decodeRepeatedDoubleField(value: inout [Double]) throws { record("repeated", "double"); value.append(1) }
    mutating func decodeSingularInt32Field(value: inout Int32) throws { record("singular", "int32"); value = 1 }
    mutating func decodeSingularInt32Field(value: inout Int32?) throws { record("singular_presence", "int32"); value = 1 }
    mutating func decodeRepeatedInt32Field(value: inout [Int32]) throws { record("repeated", "int32"); value.append(1) }
    mutating func decodeSingularInt64Field(value: inout Int64) throws { record("singular", "int64"); value = 1 }
    mutating func decodeSingularInt64Field(value: inout Int64?) throws { record("singular_presence", "int64"); value = 1 }
    mutating func decodeRepeatedInt64Field(value: inout [Int64]) throws { record("repeated", "int64"); value.append(1) }
    mutating func decodeSingularUInt32Field(value: inout UInt32) throws { record("singular", "uint32"); value = 1 }
    mutating func decodeSingularUInt32Field(value: inout UInt32?) throws { record("singular_presence", "uint32"); value = 1 }
    mutating func decodeRepeatedUInt32Field(value: inout [UInt32]) throws { record("repeated", "uint32"); value.append(1) }
    mutating func decodeSingularUInt64Field(value: inout UInt64) throws { record("singular", "uint64"); value = 1 }
    mutating func decodeSingularUInt64Field(value: inout UInt64?) throws { record("singular_presence", "uint64"); value = 1 }
    mutating func decodeRepeatedUInt64Field(value: inout [UInt64]) throws { record("repeated", "uint64"); value.append(1) }
    mutating func decodeSingularSInt32Field(value: inout Int32) throws { record("singular", "sint32"); value = 1 }
    mutating func decodeSingularSInt32Field(value: inout Int32?) throws { record("singular_presence", "sint32"); value = 1 }
    mutating func decodeRepeatedSInt32Field(value: inout [Int32]) throws { record("repeated", "sint32"); value.append(1) }
    mutating func decodeSingularSInt64Field(value: inout Int64) throws { record("singular", "sint64"); value = 1 }
    mutating func decodeSingularSInt64Field(value: inout Int64?) throws { record("singular_presence", "sint64"); value = 1 }
    mutating func decodeRepeatedSInt64Field(value: inout [Int64]) throws { record("repeated", "sint64"); value.append(1) }
    mutating func decodeSingularFixed32Field(value: inout UInt32) throws { record("singular", "fixed32"); value = 1 }
    mutating func decodeSingularFixed32Field(value: inout UInt32?) throws { record("singular_presence", "fixed32"); value = 1 }
    mutating func decodeRepeatedFixed32Field(value: inout [UInt32]) throws { record("repeated", "fixed32"); value.append(1) }
    mutating func decodeSingularFixed64Field(value: inout UInt64) throws { record("singular", "fixed64"); value = 1 }
    mutating func decodeSingularFixed64Field(value: inout UInt64?) throws { record("singular_presence", "fixed64"); value = 1 }
    mutating func decodeRepeatedFixed64Field(value: inout [UInt64]) throws { record("repeated", "fixed64"); value.append(1) }
    mutating func decodeSingularSFixed32Field(value: inout Int32) throws { record("singular", "sfixed32"); value = 1 }
    mutating func decodeSingularSFixed32Field(value: inout Int32?) throws { record("singular_presence", "sfixed32"); value = 1 }
    mutating func decodeRepeatedSFixed32Field(value: inout [Int32]) throws { record("repeated", "sfixed32"); value.append(1) }
    mutating func decodeSingularSFixed64Field(value: inout Int64) throws { record("singular", "sfixed64"); value = 1 }
    mutating func decodeSingularSFixed64Field(value: inout Int64?) throws { record("singular_presence", "sfixed64"); value = 1 }
    mutating func decodeRepeatedSFixed64Field(value: inout [Int64]) throws { record("repeated", "sfixed64"); value.append(1) }
    mutating func decodeSingularBoolField(value: inout Bool) throws { record("singular", "bool"); value = true }
    mutating func decodeSingularBoolField(value: inout Bool?) throws { record("singular_presence", "bool"); value = true }
    mutating func decodeRepeatedBoolField(value: inout [Bool]) throws { record("repeated", "bool"); value.append(true) }
    mutating func decodeSingularStringField(value: inout String) throws { record("singular", "string"); value = "x" }
    mutating func decodeSingularStringField(value: inout String?) throws { record("singular_presence", "string"); value = "x" }
    mutating func decodeRepeatedStringField(value: inout [String]) throws { record("repeated", "string"); value.append("x") }
    mutating func decodeSingularBytesField(value: inout Data) throws { record("singular", "bytes"); value = Data([1]) }
    mutating func decodeSingularBytesField(value: inout Data?) throws { record("singular_presence", "bytes"); value = Data([1]) }
    mutating func decodeRepeatedBytesField(value: inout [Data]) throws { record("repeated", "bytes"); value.append(Data([1])) }

    mutating func decodeSingularEnumField<E: InternalSwiftProtobuf.Enum>(value: inout E) throws where E.RawValue == Int {
        record("singular", "enum", String(reflecting: E.self)); value = E()
    }
    mutating func decodeSingularEnumField<E: InternalSwiftProtobuf.Enum>(value: inout E?) throws where E.RawValue == Int {
        record("singular_presence", "enum", String(reflecting: E.self)); value = E()
    }
    mutating func decodeRepeatedEnumField<E: InternalSwiftProtobuf.Enum>(value: inout [E]) throws where E.RawValue == Int {
        record("repeated", "enum", String(reflecting: E.self)); value.append(E())
    }
    mutating func decodeSingularMessageField<M: InternalSwiftProtobuf.Message>(value: inout M?) throws {
        record("singular_presence", "message", String(reflecting: M.self)); value = M()
    }
    mutating func decodeRepeatedMessageField<M: InternalSwiftProtobuf.Message>(value: inout [M]) throws {
        record("repeated", "message", String(reflecting: M.self)); value.append(M())
    }
    mutating func decodeSingularGroupField<G: InternalSwiftProtobuf.Message>(value: inout G?) throws {
        record("singular_presence", "group", String(reflecting: G.self)); value = G()
    }
    mutating func decodeRepeatedGroupField<G: InternalSwiftProtobuf.Message>(value: inout [G]) throws {
        record("repeated", "group", String(reflecting: G.self)); value.append(G())
    }
    mutating func decodeMapField<KeyType, ValueType: InternalSwiftProtobuf.MapValueType>(
        fieldType: InternalSwiftProtobuf._ProtobufMap<KeyType, ValueType>.Type,
        value: inout InternalSwiftProtobuf._ProtobufMap<KeyType, ValueType>.BaseType
    ) throws {
        record("map", "scalar", "\(String(reflecting: KeyType.self))->\(String(reflecting: ValueType.self))")
    }
    mutating func decodeMapField<KeyType, ValueType>(
        fieldType: InternalSwiftProtobuf._ProtobufEnumMap<KeyType, ValueType>.Type,
        value: inout InternalSwiftProtobuf._ProtobufEnumMap<KeyType, ValueType>.BaseType
    ) throws where ValueType.RawValue == Int {
        record("map", "enum", "\(String(reflecting: KeyType.self))->\(String(reflecting: ValueType.self))")
    }
    mutating func decodeMapField<KeyType, ValueType>(
        fieldType: InternalSwiftProtobuf._ProtobufMessageMap<KeyType, ValueType>.Type,
        value: inout InternalSwiftProtobuf._ProtobufMessageMap<KeyType, ValueType>.BaseType
    ) throws {
        record("map", "message", "\(String(reflecting: KeyType.self))->\(String(reflecting: ValueType.self))")
    }
    mutating func decodeExtensionField(
        values: inout InternalSwiftProtobuf.ExtensionFieldValueSet,
        messageType: any InternalSwiftProtobuf.Message.Type,
        fieldNumber: Int
    ) throws {
        record("extension", "message", String(reflecting: messageType))
    }
}

func traceSchema<M: InternalSwiftProtobuf.Message>(
    _ type: M.Type,
    fieldNumbers: [Int]
) -> [NativeFieldSchema] {
    fieldNumbers.compactMap { number in
        var message = M()
        var decoder = SchemaTracingDecoder(fieldNumbers: [number])
        try? message.decodeMessage(decoder: &decoder)
        return decoder.fields.first
    }
}

func traceOneofGroups<M: InternalSwiftProtobuf.Message>(
    _ type: M.Type,
    fieldNumbers: [Int]
) -> [[Int]] {
    var parent = Dictionary(uniqueKeysWithValues: fieldNumbers.map { ($0, $0) })
    func root(_ value: Int) -> Int {
        var value = value
        while parent[value] != value { value = parent[value]! }
        return value
    }
    for firstIndex in fieldNumbers.indices {
        for secondIndex in fieldNumbers.index(after: firstIndex)..<fieldNumbers.endIndex {
            let pair = [fieldNumbers[firstIndex], fieldNumbers[secondIndex]]
            var message = M()
            var decoder = SchemaTracingDecoder(fieldNumbers: pair)
            try? message.decodeMessage(decoder: &decoder)
            if decoder.conflictCount > 0 {
                parent[root(pair[1])] = root(pair[0])
            }
        }
    }
    let groups = Dictionary(grouping: fieldNumbers, by: root)
    return groups.values.filter { $0.count > 1 }.map { $0.sorted() }
        .sorted { $0[0] < $1[0] }
}
