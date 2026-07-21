# Protobuf Schema And Semantic Ledger

This ledger is generated from live ToolKit name maps and dynamic calls to every generated `decodeMessage` implementation. `Observed` means the field occurs in the supplied database corpus; absent fields remain listed to make schema coverage auditable.

## `ToolKitProtoAllPredicate`

Native protobuf message for all predicate.

Corpus presence: 216 unique nested messages; 218 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoAppDefinition`

Native protobuf message for app definition.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `id` | singular string | no | 0 | The id value associated with AppDefinition. |
| 2 | `name` | singular string | no | 0 | The name value associated with AppDefinition. |
| 3 | `bundleId` | singular string | no | 0 | The bundle id value associated with AppDefinition. |
| 4 | `bundleVersion` | singular string | no | 0 | The bundle version value associated with AppDefinition. |
| 5 | `teamId` | singular string | no | 0 | The team id value associated with AppDefinition. |
| 6 | `device` | singular_presence message `<ToolKit.ToolKitProtoAppDefinition.Device>` | no | 0 | The device value associated with AppDefinition. |
| 7 | `origin` | singular enum `<ToolKit.ToolKitProtoAppDefinition.Origin>` | no | 0 | Enumerated origin setting for AppDefinition. |
| 8 | `synonyms` | repeated string | no | 0 | Ordered list of synonyms values associated with AppDefinition. |

## `ToolKitProtoAppDefinition.Device`

Native protobuf message for app definition.device.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `local` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the local alternative of AppDefinition.Device; it is mutually exclusive with: remote. |
| 2 | `remote` | singular_presence string | no | 0 | Presence selects the remote alternative of AppDefinition.Device; it is mutually exclusive with: local. |

## `ToolKitProtoAssistantSchemaIdentifier`

Native protobuf message for assistant schema identifier.

Corpus presence: 300 unique nested messages; 395 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `kind` | singular string | yes | 395 | The kind value associated with AssistantSchemaIdentifier. |
| 2 | `version` | singular_presence message `<ToolKit.ToolKitProtoAssistantSchemaVersion>` | yes | 395 | The version value associated with AssistantSchemaIdentifier. |
| 3 | `domain` | singular string | yes | 395 | The domain value associated with AssistantSchemaIdentifier. |

## `ToolKitProtoAssistantSchemaVersion`

Native protobuf message for assistant schema version.

Corpus presence: 300 unique nested messages; 395 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `major` | singular uint64 | yes | 395 | The major value associated with AssistantSchemaVersion. |
| 2 | `minor` | singular uint64 | no | 0 | The minor value associated with AssistantSchemaVersion. |
| 3 | `patch` | singular uint64 | no | 0 | The patch value associated with AssistantSchemaVersion. |

## `ToolKitProtoAssistantToolSchemaDefinition`

Native protobuf message for assistant tool schema definition.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoAssistantSchemaIdentifier>` | no | 0 | The identifier value associated with AssistantToolSchemaDefinition. |
| 2 | `name` | singular string | no | 0 | The name value associated with AssistantToolSchemaDefinition. |
| 3 | `description` | singular_presence string | no | 0 | The description value associated with AssistantToolSchemaDefinition. |
| 4 | `parameters` | repeated message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter>` | no | 0 | Ordered list of parameters values associated with AssistantToolSchemaDefinition. |
| 5 | `sampleInvocations` | repeated message `<ToolKit.ToolKitProtoSampleInvocationDefinition>` | no | 0 | Ordered list of sample invocations values associated with AssistantToolSchemaDefinition. |
| 6 | `outputType` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | no | 0 | The output type value associated with AssistantToolSchemaDefinition. |

## `ToolKitProtoAssistantTypeSchemaDefinition`

Native protobuf message for assistant type schema definition.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `entity` | singular_presence message `<ToolKit.ToolKitProtoAssistantTypeSchemaDefinition.Entity>` | no | 0 | Presence selects the entity alternative of AssistantTypeSchemaDefinition; it is mutually exclusive with: enumeration. |
| 2 | `enumeration` | singular_presence message `<ToolKit.ToolKitProtoAssistantTypeSchemaDefinition.Enumeration>` | no | 0 | Presence selects the enumeration alternative of AssistantTypeSchemaDefinition; it is mutually exclusive with: entity. |

## `ToolKitProtoAssistantTypeSchemaDefinition.Entity`

Native protobuf message for assistant type schema definition.entity.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoAssistantSchemaIdentifier>` | no | 0 | The identifier value associated with AssistantTypeSchemaDefinition.Entity. |
| 2 | `properties` | repeated message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.Property>` | no | 0 | Ordered list of properties values associated with AssistantTypeSchemaDefinition.Entity. |
| 3 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoTypeDisplayRepresentation>` | no | 0 | The display representation value associated with AssistantTypeSchemaDefinition.Entity. |
| 4 | `authenticationPolicy` | singular_presence enum `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.AuthenticationPolicy>` | no | 0 | Enumerated authentication policy setting for AssistantTypeSchemaDefinition.Entity. |

## `ToolKitProtoAssistantTypeSchemaDefinition.Enumeration`

Native protobuf message for assistant type schema definition.enumeration.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoAssistantSchemaIdentifier>` | no | 0 | The identifier value associated with AssistantTypeSchemaDefinition.Enumeration. |
| 2 | `cases` | repeated message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Enumeration.Case>` | no | 0 | Ordered list of cases values associated with AssistantTypeSchemaDefinition.Enumeration. |
| 3 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoTypeDisplayRepresentation>` | no | 0 | The display representation value associated with AssistantTypeSchemaDefinition.Enumeration. |

## `ToolKitProtoChangeset`

Native protobuf message for changeset.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 3 | `full` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the full alternative of Changeset; it is mutually exclusive with: partial, noneVariant. |
| 4 | `partial` | singular_presence message `<ToolKit.ToolKitProtoChangeset.Partial>` | no | 0 | Presence selects the partial alternative of Changeset; it is mutually exclusive with: full, noneVariant. |
| 5 | `noneVariant` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the none variant alternative of Changeset; it is mutually exclusive with: full, partial. |

## `ToolKitProtoChangeset.Partial`

Native protobuf message for changeset.partial.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `updated` | repeated string | no | 0 | Ordered list of updated values associated with Changeset.Partial. |
| 2 | `removed` | repeated string | no | 0 | Ordered list of removed values associated with Changeset.Partial. |
| 3 | `provenance` | repeated message `<ToolKit.ToolKitProtoChangeset.Provenance>` | no | 0 | Ordered list of provenance values associated with Changeset.Partial. |

## `ToolKitProtoChangeset.Provenance`

Native protobuf message for changeset.provenance.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `LaunchServicesSnapshot` | singular_presence message `<ToolKit.ToolKitProtoLaunchServicesSnapshot>` | no | 0 | Presence selects the launch services snapshot alternative of Changeset.Provenance; it is mutually exclusive with: appIntentsDatabaseChanged, appProtectionChanged, cascadeSync. |
| 2 | `appIntentsDatabaseChanged` | singular_presence message `<ToolKit.ToolKitProtoLinkSnapshot>` | no | 0 | Presence selects the app intents database changed alternative of Changeset.Provenance; it is mutually exclusive with: LaunchServicesSnapshot, appProtectionChanged, cascadeSync. |
| 3 | `appProtectionChanged` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the app protection changed alternative of Changeset.Provenance; it is mutually exclusive with: LaunchServicesSnapshot, appIntentsDatabaseChanged, cascadeSync. |
| 4 | `cascadeSync` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the cascade sync alternative of Changeset.Provenance; it is mutually exclusive with: LaunchServicesSnapshot, appIntentsDatabaseChanged, appProtectionChanged. |

## `ToolKitProtoCoercionDefinition`

A conversion edge describing import/export direction and the destination/source type expression.

Corpus presence: 38 unique nested messages; 746 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `direction` | singular enum `<ToolKit.ToolKitProtoCoercionDefinition.CoercionDirection>` | yes | 735 | Enumerated direction setting for CoercionDefinition. |
| 2 | `typeInstance` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 746 | The type instance value associated with CoercionDefinition. |

## `ToolKitProtoComparisonPredicate`

Native protobuf message for comparison predicate.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `property` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.Property>` | no | 0 | The property value associated with ComparisonPredicate. |
| 2 | `comparison` | singular_presence message `<ToolKit.ToolKitProtoComparisonPredicate.Comparison>` | no | 0 | The comparison value associated with ComparisonPredicate. |
| 3 | `rawGroupId` | singular string | no | 0 | The raw group id value associated with ComparisonPredicate. |
| 4 | `contentItemClass` | singular_presence message `<ToolKit.ToolKitProtoContentItemClassDescriptor>` | no | 0 | The content item class value associated with ComparisonPredicate. |

## `ToolKitProtoComparisonPredicate.Comparison`

Native protobuf message for comparison predicate.comparison.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `notEqualTo` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the not equal to alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 2 | `equalTo` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the equal to alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 3 | `hasValue` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the has value alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 4 | `hasNoValue` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the has no value alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 5 | `greaterThan` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the greater than alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 6 | `greaterThanOrEqualTo` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the greater than or equal to alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 7 | `lessThan` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the less than alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 8 | `lessThanOrEqualTo` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the less than or equal to alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 9 | `contains` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the contains alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 10 | `notContains` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the not contains alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 11 | `beginsWith` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the begins with alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 12 | `endsWith` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the ends with alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, inTheNext, inTheLast, isToday, isBetween. |
| 13 | `inTheNext` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the in the next alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheLast, isToday, isBetween. |
| 14 | `inTheLast` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the in the last alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, isToday, isBetween. |
| 15 | `isToday` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the is today alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isBetween. |
| 16 | `isBetween` | singular_presence message `<ToolKit.ToolKitProtoComparisonPredicate.Comparison.Pair>` | no | 0 | Presence selects the is between alternative of ComparisonPredicate.Comparison; it is mutually exclusive with: notEqualTo, equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday. |

## `ToolKitProtoComparisonPredicate.Comparison.Pair`

Native protobuf message for comparison predicate.comparison.pair.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `first` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | The first value associated with ComparisonPredicate.Comparison.Pair. |
| 2 | `second` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | The second value associated with ComparisonPredicate.Comparison.Pair. |

## `ToolKitProtoComparisonPredicate.Comparison.Template`

Native protobuf message for comparison predicate.comparison.template.

Corpus presence: 3371 unique nested messages; 3440 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `equalTo` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 811 | Presence selects the equal to alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 2 | `notEqualTo` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 639 | Presence selects the not equal to alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 3 | `hasValue` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the has value alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 4 | `hasNoValue` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the has no value alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 5 | `greaterThan` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 186 | Presence selects the greater than alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 6 | `greaterThanOrEqualTo` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 67 | Presence selects the greater than or equal to alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 7 | `lessThan` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | no | 0 | Presence selects the less than alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 8 | `lessThanOrEqualTo` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 67 | Presence selects the less than or equal to alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 9 | `contains` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 501 | Presence selects the contains alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 10 | `notContains` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 233 | Presence selects the not contains alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, beginsWith, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 11 | `beginsWith` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 202 | Presence selects the begins with alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, endsWith, inTheNext, inTheLast, isToday, isBetween. |
| 12 | `endsWith` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 202 | Presence selects the ends with alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, inTheNext, inTheLast, isToday, isBetween. |
| 13 | `inTheNext` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 127 | Presence selects the in the next alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheLast, isToday, isBetween. |
| 14 | `inTheLast` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 135 | Presence selects the in the last alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, isToday, isBetween. |
| 15 | `isToday` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 135 | Presence selects the is today alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isBetween. |
| 16 | `isBetween` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 135 | Presence selects the is between alternative of ComparisonPredicate.Comparison.Template; it is mutually exclusive with: equalTo, notEqualTo, hasValue, hasNoValue, greaterThan, greaterThanOrEqualTo, lessThan, lessThanOrEqualTo, contains, notContains, beginsWith, endsWith, inTheNext, inTheLast, isToday. |

## `ToolKitProtoComparisonPredicate.Template`

A query predicate template tying an entity property to a typed comparison operation and optional content-item metadata.

Corpus presence: 3371 unique nested messages; 3440 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `property` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.Property>` | yes | 3440 | The property value associated with ComparisonPredicate.Template. |
| 2 | `comparisonTemplate` | singular_presence message `<ToolKit.ToolKitProtoComparisonPredicate.Comparison.Template>` | yes | 3440 | The comparison template value associated with ComparisonPredicate.Template. |
| 3 | `rawGroupId` | singular string | yes | 3440 | The raw group id value associated with ComparisonPredicate.Template. |
| 4 | `contentItemClass` | singular_presence message `<ToolKit.ToolKitProtoContentItemClassDescriptor>` | yes | 3440 | The content item class value associated with ComparisonPredicate.Template. |

## `ToolKitProtoCompoundPredicate`

Native protobuf message for compound predicate.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `operator` | singular enum `<ToolKit.ToolKitProtoCompoundPredicate.Operator>` | no | 0 | Enumerated operator setting for CompoundPredicate. |
| 2 | `operands` | repeated message `<ToolKit.ToolKitProtoComparisonPredicate>` | no | 0 | Ordered list of operands values associated with CompoundPredicate. |

## `ToolKitProtoContainerDefinition`

Native protobuf message for container definition.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 2 | `name` | singular string | no | 0 | The name value associated with ContainerDefinition. |
| 3 | `containerId` | singular string | no | 0 | The container id value associated with ContainerDefinition. |
| 4 | `bundleVersion` | singular_presence string | no | 0 | The bundle version value associated with ContainerDefinition. |
| 5 | `containerType` | singular enum `<ToolKit.ToolKitProtoContainerDefinition.TypeEnum>` | no | 0 | Enumerated container type setting for ContainerDefinition. |
| 6 | `teamId` | singular_presence string | no | 0 | The team id value associated with ContainerDefinition. |
| 7 | `device` | singular_presence message `<ToolKit.ToolKitProtoContainerDefinition.Device>` | no | 0 | The device value associated with ContainerDefinition. |
| 8 | `origin` | singular enum `<ToolKit.ToolKitProtoContainerDefinition.Origin>` | no | 0 | Enumerated origin setting for ContainerDefinition. |
| 9 | `synonyms` | repeated string | no | 0 | Ordered list of synonyms values associated with ContainerDefinition. |

## `ToolKitProtoContainerDefinition.Device`

Native protobuf message for container definition.device.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `local` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the local alternative of ContainerDefinition.Device; it is mutually exclusive with: remote. |
| 2 | `remote` | singular_presence string | no | 0 | Presence selects the remote alternative of ContainerDefinition.Device; it is mutually exclusive with: local. |

## `ToolKitProtoContentItemClassDescriptor`

Native protobuf message for content item class descriptor.

Corpus presence: 3385 unique nested messages; 3454 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `regularContentItemClass` | singular_presence string | yes | 508 | Presence selects the regular content item class alternative of ContentItemClassDescriptor; it is mutually exclusive with: linkEntityContentItemClass, linkEnumContentItemClass, linkCodableContentItemClass. |
| 2 | `linkEntityContentItemClass` | singular_presence message `<ToolKit.ToolKitProtoContentItemClassDescriptor.LinkEntityContentItemClass>` | yes | 2946 | Presence selects the link entity content item class alternative of ContentItemClassDescriptor; it is mutually exclusive with: regularContentItemClass, linkEnumContentItemClass, linkCodableContentItemClass. |
| 3 | `linkEnumContentItemClass` | singular_presence message `<ToolKit.ToolKitProtoContentItemClassDescriptor.LinkEnumContentItemClass>` | no | 0 | Presence selects the link enum content item class alternative of ContentItemClassDescriptor; it is mutually exclusive with: regularContentItemClass, linkEntityContentItemClass, linkCodableContentItemClass. |
| 4 | `linkCodableContentItemClass` | singular_presence message `<ToolKit.ToolKitProtoContentItemClassDescriptor.LinkCodableContentItemClass>` | no | 0 | Presence selects the link codable content item class alternative of ContentItemClassDescriptor; it is mutually exclusive with: regularContentItemClass, linkEntityContentItemClass, linkEnumContentItemClass. |

## `ToolKitProtoContentItemClassDescriptor.LinkCodableContentItemClass`

Native protobuf message for content item class descriptor.link codable content item class.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 2 | `identifier` | singular string | no | 0 | The identifier value associated with ContentItemClassDescriptor.LinkCodableContentItemClass. |

## `ToolKitProtoContentItemClassDescriptor.LinkEntityContentItemClass`

Native protobuf message for content item class descriptor.link entity content item class.

Corpus presence: 2904 unique nested messages; 2946 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 2 | `bundleIdentifier` | singular string | yes | 2946 | The bundle identifier value associated with ContentItemClassDescriptor.LinkEntityContentItemClass. |
| 3 | `identifier` | singular string | yes | 2946 | The identifier value associated with ContentItemClassDescriptor.LinkEntityContentItemClass. |

## `ToolKitProtoContentItemClassDescriptor.LinkEnumContentItemClass`

Native protobuf message for content item class descriptor.link enum content item class.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 2 | `bundleIdentifier` | singular string | no | 0 | The bundle identifier value associated with ContentItemClassDescriptor.LinkEnumContentItemClass. |
| 3 | `identifier` | singular string | no | 0 | The identifier value associated with ContentItemClassDescriptor.LinkEnumContentItemClass. |

## `ToolKitProtoDisplayRepresentation`

Native protobuf message for display representation.

Corpus presence: 1013 unique nested messages; 1072 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `title` | singular string | yes | 1072 | The title value associated with DisplayRepresentation. |
| 2 | `subtitle` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.Subtitle>` | yes | 1 | The subtitle value associated with DisplayRepresentation. |
| 3 | `altText` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.AltText>` | no | 0 | The alt text value associated with DisplayRepresentation. |
| 4 | `image` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.Image>` | yes | 3 | The image value associated with DisplayRepresentation. |
| 5 | `synonyms` | repeated string | no | 0 | Ordered list of synonyms values associated with DisplayRepresentation. |
| 6 | `snippetPluginModel` | singular_presence message `<ToolKit.ToolKitProtoPluginModelData>` | no | 0 | The snippet plugin model value associated with DisplayRepresentation. |

## `ToolKitProtoDisplayRepresentation.AltText`

Native protobuf message for display representation.alt text.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `lazy` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.Storage>` | no | 0 | Presence selects the lazy alternative of DisplayRepresentation.AltText; it is mutually exclusive with: static. |
| 2 | `static` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.AltText.Static>` | no | 0 | Presence selects the static alternative of DisplayRepresentation.AltText; it is mutually exclusive with: lazy. |

## `ToolKitProtoDisplayRepresentation.AltText.Static`

Native protobuf message for display representation.alt text.static.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `value` | singular string | no | 0 | The value value associated with DisplayRepresentation.AltText.Static. |

## `ToolKitProtoDisplayRepresentation.DisplayValue`

Native protobuf message for display representation.display value.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `type` | singular enum `<ToolKit.ToolKitProtoDisplayRepresentation.DisplayValue.DisplayValueEnum>` | no | 0 | Enumerated type setting for DisplayRepresentation.DisplayValue. |
| 2 | `lazy` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.Storage>` | no | 0 | Presence selects the lazy alternative of DisplayRepresentation.DisplayValue; it is mutually exclusive with: static. |
| 3 | `static` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.DisplayValue.Static>` | no | 0 | Presence selects the static alternative of DisplayRepresentation.DisplayValue; it is mutually exclusive with: lazy. |

## `ToolKitProtoDisplayRepresentation.DisplayValue.Static`

Native protobuf message for display representation.display value.static.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `value` | singular_presence message `<InternalSwiftProtobuf.Google_Protobuf_Any>` | no | 0 | The value value associated with DisplayRepresentation.DisplayValue.Static. |

## `ToolKitProtoDisplayRepresentation.Image`

Native protobuf message for display representation.image.

Corpus presence: 3 unique nested messages; 3 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `lazy` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.Storage>` | no | 0 | Presence selects the lazy alternative of DisplayRepresentation.Image; it is mutually exclusive with: static. |
| 2 | `static` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.Image.Static>` | yes | 3 | Presence selects the static alternative of DisplayRepresentation.Image; it is mutually exclusive with: lazy. |

## `ToolKitProtoDisplayRepresentation.Image.Static`

Native protobuf message for display representation.image.static.

Corpus presence: 3 unique nested messages; 3 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `data` | singular_presence bytes | no | 0 | Presence selects the data alternative of DisplayRepresentation.Image.Static; it is mutually exclusive with: symbol, file. |
| 2 | `symbol` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.Image.Static.Symbol>` | yes | 3 | Presence selects the symbol alternative of DisplayRepresentation.Image.Static; it is mutually exclusive with: data, file. |
| 3 | `file` | singular_presence string | no | 0 | Presence selects the file alternative of DisplayRepresentation.Image.Static; it is mutually exclusive with: data, symbol. |

## `ToolKitProtoDisplayRepresentation.Image.Static.Symbol`

Native protobuf message for display representation.image.static.symbol.

Corpus presence: 3 unique nested messages; 3 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `name` | singular string | yes | 3 | The name value associated with DisplayRepresentation.Image.Static.Symbol. |
| 2 | `tintColorData` | singular_presence bytes | yes | 1 | The tint color data value associated with DisplayRepresentation.Image.Static.Symbol. |
| 3 | `configurationData` | singular_presence bytes | no | 0 | The configuration data value associated with DisplayRepresentation.Image.Static.Symbol. |

## `ToolKitProtoDisplayRepresentation.Storage`

Native protobuf message for display representation.storage.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `data` | singular bytes | no | 0 | The data value associated with DisplayRepresentation.Storage. |

## `ToolKitProtoDisplayRepresentation.Subtitle`

Native protobuf message for display representation.subtitle.

Corpus presence: 1 unique nested messages; 1 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `lazy` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.Storage>` | no | 0 | Presence selects the lazy alternative of DisplayRepresentation.Subtitle; it is mutually exclusive with: static. |
| 2 | `static` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation.Subtitle.Static>` | yes | 1 | Presence selects the static alternative of DisplayRepresentation.Subtitle; it is mutually exclusive with: lazy. |

## `ToolKitProtoDisplayRepresentation.Subtitle.Static`

Native protobuf message for display representation.subtitle.static.

Corpus presence: 1 unique nested messages; 1 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `value` | singular string | yes | 1 | The value value associated with DisplayRepresentation.Subtitle.Static. |

## `ToolKitProtoEntityInstanceIdentifier`

Native protobuf message for entity instance identifier.

Corpus presence: 4 unique nested messages; 4 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `local` | singular_presence string | yes | 4 | Presence selects the local alternative of EntityInstanceIdentifier; it is mutually exclusive with: stable, paired. |
| 2 | `stable` | singular_presence string | no | 0 | Presence selects the stable alternative of EntityInstanceIdentifier; it is mutually exclusive with: local, paired. |
| 3 | `paired` | singular_presence message `<ToolKit.ToolKitProtoEntityInstanceIdentifier.SyncedIdentifier>` | no | 0 | Presence selects the paired alternative of EntityInstanceIdentifier; it is mutually exclusive with: local, stable. |

## `ToolKitProtoEntityInstanceIdentifier.SyncedIdentifier`

Native protobuf message for entity instance identifier.synced identifier.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `local` | singular string | no | 0 | The local value associated with EntityInstanceIdentifier.SyncedIdentifier. |
| 2 | `stable` | singular string | no | 0 | The stable value associated with EntityInstanceIdentifier.SyncedIdentifier. |

## `ToolKitProtoFlowToolSchemaIdentifier`

Native protobuf message for flow tool schema identifier.

Corpus presence: 44 unique nested messages; 48 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `kind` | singular string | yes | 48 | The kind value associated with FlowToolSchemaIdentifier. |
| 2 | `domain` | singular string | yes | 48 | The domain value associated with FlowToolSchemaIdentifier. |

## `ToolKitProtoIdSearchPredicate`

Native protobuf message for id search predicate.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular string | no | 0 | The identifier value associated with IdSearchPredicate. |
| 2 | `identifiers` | repeated string | no | 0 | Ordered list of identifiers values associated with IdSearchPredicate. |

## `ToolKitProtoIdSearchPredicate.Template`

Native protobuf message for id search predicate.template.

Corpus presence: 1520 unique nested messages; 1578 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoIndexingEvent`

Native protobuf message for indexing event.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `requestId` | singular string | no | 0 | The request id value associated with IndexingEvent. |
| 2 | `tool` | singular_presence string | no | 0 | Presence selects the tool alternative of IndexingEvent; it is mutually exclusive with: type. |
| 3 | `type` | singular_presence string | no | 0 | Presence selects the type alternative of IndexingEvent; it is mutually exclusive with: tool. |
| 5 | `success` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the success alternative of IndexingEvent; it is mutually exclusive with: failure. |
| 6 | `failure` | singular_presence string | no | 0 | Presence selects the failure alternative of IndexingEvent; it is mutually exclusive with: success. |

## `ToolKitProtoIndexingLogEntry`

Native protobuf message for indexing log entry.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `reason` | singular_presence message `<ToolKit.ToolKitProtoIndexingReason>` | no | 0 | Presence selects the reason alternative of IndexingLogEntry; it is mutually exclusive with: request, policyResolution, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 2 | `request` | singular_presence message `<ToolKit.ToolKitProtoIndexingRequest>` | no | 0 | Presence selects the request alternative of IndexingLogEntry; it is mutually exclusive with: reason, policyResolution, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 3 | `policyResolution` | singular_presence message `<ToolKit.ToolKitProtoIndexingPolicyResolution>` | no | 0 | Presence selects the policy resolution alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 4 | `indexingEvent` | singular_presence message `<ToolKit.ToolKitProtoIndexingEvent>` | no | 0 | Presence selects the indexing event alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, response, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 5 | `response` | singular_presence message `<ToolKit.ToolKitProtoIndexingResponse>` | no | 0 | Presence selects the response alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 6 | `walOperationStart` | singular_presence message `<ToolKit.ToolKitProtoWALOperationStart>` | no | 0 | Presence selects the wal operation start alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, response, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 7 | `walOperationEnd` | singular_presence message `<ToolKit.ToolKitProtoWALOperationEnd>` | no | 0 | Presence selects the wal operation end alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, response, walOperationStart, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 9 | `vacuumOperationStart` | singular_presence message `<ToolKit.ToolKitProtoVacuumOperationStart>` | no | 0 | Presence selects the vacuum operation start alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 10 | `vacuumOperationEnd` | singular_presence message `<ToolKit.ToolKitProtoVacuumOperationEnd>` | no | 0 | Presence selects the vacuum operation end alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationStart, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 11 | `indexingStep` | singular_presence message `<ToolKit.ToolKitProtoIndexingStep>` | no | 0 | Presence selects the indexing step alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, pushDonationStart, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 12 | `pushDonationStart` | singular_presence message `<ToolKit.ToolKitProtoPushDonationStart>` | no | 0 | Presence selects the push donation start alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationEnd, pullOperationStart, pullOperationEnd. |
| 13 | `pushDonationEnd` | singular_presence message `<ToolKit.ToolKitProtoPushDonationEnd>` | no | 0 | Presence selects the push donation end alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pullOperationStart, pullOperationEnd. |
| 14 | `pullOperationStart` | singular_presence message `<ToolKit.ToolKitProtoPullOperationStart>` | no | 0 | Presence selects the pull operation start alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationEnd. |
| 15 | `pullOperationEnd` | singular_presence message `<ToolKit.ToolKitProtoPullOperationEnd>` | no | 0 | Presence selects the pull operation end alternative of IndexingLogEntry; it is mutually exclusive with: reason, request, policyResolution, indexingEvent, response, walOperationStart, walOperationEnd, vacuumOperationStart, vacuumOperationEnd, indexingStep, pushDonationStart, pushDonationEnd, pullOperationStart. |

## `ToolKitProtoIndexingPolicyResolution`

Native protobuf message for indexing policy resolution.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `requestId` | singular string | no | 0 | The request id value associated with IndexingPolicyResolution. |
| 2 | `resolvedChangeset` | singular_presence message `<ToolKit.ToolKitProtoChangeset>` | no | 0 | The resolved changeset value associated with IndexingPolicyResolution. |
| 3 | `decisionMetadata` | repeated string | no | 0 | Ordered list of decision metadata values associated with IndexingPolicyResolution. |

## `ToolKitProtoIndexingReason`

Native protobuf message for indexing reason.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `id` | singular string | no | 0 | The id value associated with IndexingReason. |
| 2 | `requestedChangeset` | singular_presence message `<ToolKit.ToolKitProtoChangeset>` | no | 0 | The requested changeset value associated with IndexingReason. |
| 3 | `manual` | singular_presence bool | no | 0 | Presence selects the manual alternative of IndexingReason; it is mutually exclusive with: firstUnlock, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, testing, fastPass. |
| 4 | `firstUnlock` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the first unlock alternative of IndexingReason; it is mutually exclusive with: manual, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, testing, fastPass. |
| 5 | `schedulerBooted` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the scheduler booted alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, testing, fastPass. |
| 6 | `appProtectionStateChanged` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the app protection state changed alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, testing, fastPass. |
| 7 | `appIntentsDatabaseChanged` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the app intents database changed alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appProtectionStateChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, testing, fastPass. |
| 8 | `launchServicesDatabaseChanged` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the launch services database changed alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, testing, fastPass. |
| 9 | `languagesChanged` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the languages changed alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, testing, fastPass. |
| 10 | `siriLanguagesChanged` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the siri languages changed alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, testing, fastPass. |
| 11 | `shortcutsAppLaunched` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the shortcuts app launched alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, deferredFull, deferredDelta, testing, fastPass. |
| 12 | `deferredFull` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the deferred full alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredDelta, testing, fastPass. |
| 13 | `deferredDelta` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the deferred delta alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, testing, fastPass. |
| 14 | `testing` | singular_presence string | no | 0 | Presence selects the testing alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, fastPass. |
| 15 | `fastPass` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the fast pass alternative of IndexingReason; it is mutually exclusive with: manual, firstUnlock, schedulerBooted, appProtectionStateChanged, appIntentsDatabaseChanged, launchServicesDatabaseChanged, languagesChanged, siriLanguagesChanged, shortcutsAppLaunched, deferredFull, deferredDelta, testing. |

## `ToolKitProtoIndexingRequest`

Native protobuf message for indexing request.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `id` | singular string | no | 0 | The id value associated with IndexingRequest. |
| 2 | `reasonIds` | repeated string | no | 0 | Ordered list of reason ids values associated with IndexingRequest. |

## `ToolKitProtoIndexingResponse`

Native protobuf message for indexing response.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `requestId` | singular string | no | 0 | The request id value associated with IndexingResponse. |
| 2 | `updated` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the updated alternative of IndexingResponse; it is mutually exclusive with: skipped, failed. |
| 3 | `skipped` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the skipped alternative of IndexingResponse; it is mutually exclusive with: updated, failed. |
| 4 | `failed` | singular_presence string | no | 0 | Presence selects the failed alternative of IndexingResponse; it is mutually exclusive with: updated, skipped. |

## `ToolKitProtoIndexingStep`

Native protobuf message for indexing step.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `requestId` | singular string | no | 0 | The request id value associated with IndexingStep. |
| 2 | `eventId` | singular string | no | 0 | The event id value associated with IndexingStep. |
| 3 | `name` | singular string | no | 0 | The name value associated with IndexingStep. |
| 4 | `phase` | singular enum `<ToolKit.ToolKitProtoIndexingStep.Phase>` | no | 0 | Enumerated phase setting for IndexingStep. |
| 5 | `parentEventId` | singular_presence string | no | 0 | The parent event id value associated with IndexingStep. |

## `ToolKitProtoLaunchServicesSnapshot`

Native protobuf message for launch services snapshot.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `stateByBundleIdentifier` | map message `<InternalSwiftProtobuf.ProtobufString->ToolKit.ToolKitProtoLaunchServicesSnapshot.State>` | no | 0 | Map of state by bundle identifier entries associated with LaunchServicesSnapshot. |
| 2 | `version` | singular_presence message `<ToolKit.ToolKitProtoLaunchServicesSnapshot.Version>` | no | 0 | The version value associated with LaunchServicesSnapshot. |

## `ToolKitProtoLaunchServicesSnapshot.State`

Native protobuf message for launch services snapshot.state.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `bundleId` | singular string | no | 0 | The bundle id value associated with LaunchServicesSnapshot.State. |
| 2 | `persistentIdentifier` | singular bytes | no | 0 | The persistent identifier value associated with LaunchServicesSnapshot.State. |

## `ToolKitProtoLaunchServicesSnapshot.Version`

Native protobuf message for launch services snapshot.version.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `uuid` | singular string | no | 0 | The uuid value associated with LaunchServicesSnapshot.Version. |
| 2 | `sequenceNumber` | singular int64 | no | 0 | The sequence number value associated with LaunchServicesSnapshot.Version. |

## `ToolKitProtoLinkSnapshot`

Native protobuf message for link snapshot.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `stateByContainerIdentifier` | map message `<InternalSwiftProtobuf.ProtobufString->ToolKit.ToolKitProtoLinkSnapshot.State>` | no | 0 | Map of state by container identifier entries associated with LinkSnapshot. |

## `ToolKitProtoLinkSnapshot.State`

Native protobuf message for link snapshot.state.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `containerId` | singular string | no | 0 | The container id value associated with LinkSnapshot.State. |
| 2 | `installIdentifier` | singular bytes | no | 0 | The install identifier value associated with LinkSnapshot.State. |

## `ToolKitProtoModelRepresentation`

Native protobuf message for model representation.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `representations` | repeated message `<ToolKit.ToolKitProtoModelRepresentation.Representation>` | no | 0 | Ordered list of representations values associated with ModelRepresentation. |

## `ToolKitProtoModelRepresentation.Representation`

Native protobuf message for model representation.representation.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `level` | singular enum `<ToolKit.ToolKitProtoModelRepresentationLevel>` | no | 0 | Enumerated level setting for ModelRepresentation.Representation. |
| 2 | `components` | repeated message `<ToolKit.ToolKitProtoModelRepresentation.RepresentationComponent>` | no | 0 | Ordered list of components values associated with ModelRepresentation.Representation. |

## `ToolKitProtoModelRepresentation.RepresentationComponent`

Native protobuf message for model representation.representation component.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `propertyIdentifiers` | repeated string | no | 0 | Ordered list of property identifiers values associated with ModelRepresentation.RepresentationComponent. |
| 2 | `label` | singular_presence message `<ToolKit.ToolKitProtoModelRepresentation.RepresentationComponent.Label>` | no | 0 | The label value associated with ModelRepresentation.RepresentationComponent. |
| 3 | `text` | singular_presence message `<ToolKit.ToolKitProtoModelRepresentation.RepresentationComponent.TextValue>` | no | 0 | Presence selects the text alternative of ModelRepresentation.RepresentationComponent; it is mutually exclusive with: visual. |
| 4 | `visual` | singular_presence message `<ToolKit.ToolKitProtoModelRepresentation.RepresentationComponent.VisualValue>` | no | 0 | Presence selects the visual alternative of ModelRepresentation.RepresentationComponent; it is mutually exclusive with: text. |

## `ToolKitProtoModelRepresentation.RepresentationComponent.Label`

Native protobuf message for model representation.representation component.label.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `kind` | singular enum `<ToolKit.ToolKitProtoModelRepresentation.RepresentationComponent.Label.Kind>` | no | 0 | Enumerated kind setting for ModelRepresentation.RepresentationComponent.Label. |
| 2 | `customLabel` | singular_presence string | no | 0 | The custom label value associated with ModelRepresentation.RepresentationComponent.Label. |

## `ToolKitProtoModelRepresentation.RepresentationComponent.TextValue`

Native protobuf message for model representation.representation component.text value.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `properties` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the properties alternative of ModelRepresentation.RepresentationComponent.TextValue; it is mutually exclusive with: text. |
| 2 | `text` | singular_presence string | no | 0 | Presence selects the text alternative of ModelRepresentation.RepresentationComponent.TextValue; it is mutually exclusive with: properties. |

## `ToolKitProtoModelRepresentation.RepresentationComponent.VisualValue`

Native protobuf message for model representation.representation component.visual value.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `properties` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the properties alternative of ModelRepresentation.RepresentationComponent.VisualValue; it is mutually exclusive with: transferable. |
| 2 | `transferable` | singular_presence message `<ToolKit.ToolKitProtoModelRepresentation.RepresentationComponent.VisualValue.Transferable>` | no | 0 | Presence selects the transferable alternative of ModelRepresentation.RepresentationComponent.VisualValue; it is mutually exclusive with: properties. |

## `ToolKitProtoModelRepresentation.RepresentationComponent.VisualValue.Transferable`

Native protobuf message for model representation.representation component.visual value.transferable.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `supportedContentTypeIdentifiers` | repeated string | no | 0 | Ordered list of supported content type identifiers values associated with ModelRepresentation.RepresentationComponent.VisualValue.Transferable. |

## `ToolKitProtoPluginModelData`

Native protobuf message for plugin model data.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `value` | singular bytes | no | 0 | The value value associated with PluginModelData. |
| 2 | `bundleIdentifier` | singular string | no | 0 | The bundle identifier value associated with PluginModelData. |

## `ToolKitProtoPullOperationEnd`

Native protobuf message for pull operation end.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `operationId` | singular string | no | 0 | The operation id value associated with PullOperationEnd. |
| 2 | `partition` | singular string | no | 0 | The partition value associated with PullOperationEnd. |
| 3 | `toolsAdded` | singular int32 | no | 0 | The tools added value associated with PullOperationEnd. |
| 4 | `toolsRemoved` | singular int32 | no | 0 | The tools removed value associated with PullOperationEnd. |
| 5 | `error` | singular_presence string | no | 0 | The error value associated with PullOperationEnd. |

## `ToolKitProtoPullOperationStart`

Native protobuf message for pull operation start.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `operationId` | singular string | no | 0 | The operation id value associated with PullOperationStart. |
| 2 | `partition` | singular string | no | 0 | The partition value associated with PullOperationStart. |
| 3 | `fromBookmark` | singular bool | no | 0 | Whether from bookmark is enabled for PullOperationStart. |

## `ToolKitProtoPushDonationEnd`

Native protobuf message for push donation end.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `operationId` | singular string | no | 0 | The operation id value associated with PushDonationEnd. |
| 2 | `partition` | singular string | no | 0 | The partition value associated with PushDonationEnd. |
| 3 | `toolCount` | singular int32 | no | 0 | The tool count value associated with PushDonationEnd. |
| 4 | `removedCount` | singular_presence int32 | no | 0 | The removed count value associated with PushDonationEnd. |
| 5 | `revisionToken` | singular_presence string | no | 0 | The revision token value associated with PushDonationEnd. |
| 6 | `error` | singular_presence string | no | 0 | The error value associated with PushDonationEnd. |
| 7 | `skipped` | singular bool | no | 0 | Whether skipped is enabled for PushDonationEnd. |
| 8 | `removedToolIds` | repeated string | no | 0 | Ordered list of removed tool ids values associated with PushDonationEnd. |

## `ToolKitProtoPushDonationStart`

Native protobuf message for push donation start.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `operationId` | singular string | no | 0 | The operation id value associated with PushDonationStart. |
| 2 | `partition` | singular string | no | 0 | The partition value associated with PushDonationStart. |
| 3 | `donationType` | singular enum `<ToolKit.ToolKitProtoPushDonationStart.DonationType>` | no | 0 | Enumerated donation type setting for PushDonationStart. |
| 4 | `changeset` | singular_presence message `<ToolKit.ToolKitProtoChangeset>` | no | 0 | The changeset value associated with PushDonationStart. |
| 5 | `priorRevisionToken` | singular_presence string | no | 0 | The prior revision token value associated with PushDonationStart. |
| 6 | `currentDbVersion` | singular_presence string | no | 0 | The current db version value associated with PushDonationStart. |
| 7 | `awaitingFullSet` | singular bool | no | 0 | Whether awaiting full set is enabled for PushDonationStart. |
| 8 | `removedToolIdCaptureFailed` | singular bool | no | 0 | Whether removed tool id capture failed is enabled for PushDonationStart. |

## `ToolKitProtoQuery`

Native protobuf message for query.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `predicate` | singular_presence message `<ToolKit.ToolKitProtoQuery.AnyPredicate>` | no | 0 | The predicate value associated with Query. |
| 2 | `sort` | singular enum `<ToolKit.ToolKitProtoQuery.SortOrder>` | no | 0 | Enumerated sort setting for Query. |
| 3 | `limit` | singular_presence int64 | no | 0 | The limit value associated with Query. |

## `ToolKitProtoQuery.AnyPredicate`

Native protobuf message for query.any predicate.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `comparison` | singular_presence message `<ToolKit.ToolKitProtoComparisonPredicate>` | no | 0 | Presence selects the comparison alternative of Query.AnyPredicate; it is mutually exclusive with: compound, stringSearch, idSearch, all, suggested, searchableItem, valid, valueSearch, unique. |
| 2 | `compound` | singular_presence message `<ToolKit.ToolKitProtoCompoundPredicate>` | no | 0 | Presence selects the compound alternative of Query.AnyPredicate; it is mutually exclusive with: comparison, stringSearch, idSearch, all, suggested, searchableItem, valid, valueSearch, unique. |
| 3 | `stringSearch` | singular_presence message `<ToolKit.ToolKitProtoStringSearchPredicate>` | no | 0 | Presence selects the string search alternative of Query.AnyPredicate; it is mutually exclusive with: comparison, compound, idSearch, all, suggested, searchableItem, valid, valueSearch, unique. |
| 4 | `idSearch` | singular_presence message `<ToolKit.ToolKitProtoIdSearchPredicate>` | no | 0 | Presence selects the id search alternative of Query.AnyPredicate; it is mutually exclusive with: comparison, compound, stringSearch, all, suggested, searchableItem, valid, valueSearch, unique. |
| 5 | `all` | singular_presence message `<ToolKit.ToolKitProtoAllPredicate>` | no | 0 | Presence selects the all alternative of Query.AnyPredicate; it is mutually exclusive with: comparison, compound, stringSearch, idSearch, suggested, searchableItem, valid, valueSearch, unique. |
| 6 | `suggested` | singular_presence message `<ToolKit.ToolKitProtoSuggestedPredicate>` | no | 0 | Presence selects the suggested alternative of Query.AnyPredicate; it is mutually exclusive with: comparison, compound, stringSearch, idSearch, all, searchableItem, valid, valueSearch, unique. |
| 7 | `searchableItem` | singular_presence message `<ToolKit.ToolKitProtoSearchableItemPredicate>` | no | 0 | Presence selects the searchable item alternative of Query.AnyPredicate; it is mutually exclusive with: comparison, compound, stringSearch, idSearch, all, suggested, valid, valueSearch, unique. |
| 8 | `valid` | singular_presence message `<ToolKit.ToolKitProtoValidPredicate>` | no | 0 | Presence selects the valid alternative of Query.AnyPredicate; it is mutually exclusive with: comparison, compound, stringSearch, idSearch, all, suggested, searchableItem, valueSearch, unique. |
| 9 | `valueSearch` | singular_presence message `<ToolKit.ToolKitProtoValueSearchPredicate>` | no | 0 | Presence selects the value search alternative of Query.AnyPredicate; it is mutually exclusive with: comparison, compound, stringSearch, idSearch, all, suggested, searchableItem, valid, unique. |
| 10 | `unique` | singular_presence message `<ToolKit.ToolKitProtoUniquePredicate>` | no | 0 | Presence selects the unique alternative of Query.AnyPredicate; it is mutually exclusive with: comparison, compound, stringSearch, idSearch, all, suggested, searchableItem, valid, valueSearch. |

## `ToolKitProtoRestrictionContext`

A constraint union limiting valid values, representation, ranges, text entry, measurement units, or characters.

Corpus presence: 3023 unique nested messages; 4234 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `inSet` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.InSet>` | yes | 2865 | Presence selects the in set alternative of RestrictionContext; it is mutually exclusive with: representableAs, personReachableAs, dateExpressibleAs, textTypedWith, measurementExpressibleAs, inInclusiveRange, characterTypedWith. |
| 2 | `representableAs` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.RepresentableAs>` | yes | 250 | Presence selects the representable as alternative of RestrictionContext; it is mutually exclusive with: inSet, personReachableAs, dateExpressibleAs, textTypedWith, measurementExpressibleAs, inInclusiveRange, characterTypedWith. |
| 3 | `personReachableAs` | singular_presence enum `<ToolKit.ToolKitProtoRestrictionContext.PersonReachableAs>` | yes | 58 | Presence selects the person reachable as alternative of RestrictionContext; it is mutually exclusive with: inSet, representableAs, dateExpressibleAs, textTypedWith, measurementExpressibleAs, inInclusiveRange, characterTypedWith. |
| 4 | `dateExpressibleAs` | singular_presence enum `<ToolKit.ToolKitProtoRestrictionContext.DateExpressibleAs>` | yes | 29 | Presence selects the date expressible as alternative of RestrictionContext; it is mutually exclusive with: inSet, representableAs, personReachableAs, textTypedWith, measurementExpressibleAs, inInclusiveRange, characterTypedWith. |
| 5 | `textTypedWith` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.TextTypedWith>` | yes | 491 | Presence selects the text typed with alternative of RestrictionContext; it is mutually exclusive with: inSet, representableAs, personReachableAs, dateExpressibleAs, measurementExpressibleAs, inInclusiveRange, characterTypedWith. |
| 6 | `measurementExpressibleAs` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.MeasurementExpressibleAs>` | yes | 27 | Presence selects the measurement expressible as alternative of RestrictionContext; it is mutually exclusive with: inSet, representableAs, personReachableAs, dateExpressibleAs, textTypedWith, inInclusiveRange, characterTypedWith. |
| 7 | `inInclusiveRange` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.InInclusiveRange>` | yes | 512 | Presence selects the in inclusive range alternative of RestrictionContext; it is mutually exclusive with: inSet, representableAs, personReachableAs, dateExpressibleAs, textTypedWith, measurementExpressibleAs, characterTypedWith. |
| 8 | `characterTypedWith` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.CharacterTypedWith>` | yes | 2 | Presence selects the character typed with alternative of RestrictionContext; it is mutually exclusive with: inSet, representableAs, personReachableAs, dateExpressibleAs, textTypedWith, measurementExpressibleAs, inInclusiveRange. |

## `ToolKitProtoRestrictionContext.CharacterTypedWith`

Native protobuf message for restriction context.character typed with.

Corpus presence: 2 unique nested messages; 2 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `parameterMode` | singular enum `<ToolKit.ToolKitProtoRestrictionContext.CharacterTypedWith.ParameterMode>` | yes | 2 | Enumerated parameter mode setting for RestrictionContext.CharacterTypedWith. |

## `ToolKitProtoRestrictionContext.InInclusiveRange`

Native protobuf message for restriction context.in inclusive range.

Corpus presence: 52 unique nested messages; 512 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `lowerBound` | singular_presence double | yes | 512 | The lower bound value associated with RestrictionContext.InInclusiveRange. |
| 2 | `upperBound` | singular_presence double | yes | 511 | The upper bound value associated with RestrictionContext.InInclusiveRange. |

## `ToolKitProtoRestrictionContext.InSet`

Native protobuf message for restriction context.in set.

Corpus presence: 2792 unique nested messages; 2865 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `definition` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.InSet.ValueSet>` | yes | 2865 | The definition value associated with RestrictionContext.InSet. |
| 2 | `templates` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Query.PredicateTemplates>` | yes | 2865 | The templates value associated with RestrictionContext.InSet. |

## `ToolKitProtoRestrictionContext.InSet.ValueSet`

Native protobuf message for restriction context.in set.value set.

Corpus presence: 2792 unique nested messages; 2865 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `bundleIdentifier` | singular_presence string | yes | 2750 | The bundle identifier value associated with RestrictionContext.InSet.ValueSet. |
| 2 | `dynamicEnumeration` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.InSet.ValueSet.DynamicEnumeration>` | yes | 817 | Presence selects the dynamic enumeration alternative of RestrictionContext.InSet.ValueSet; it is mutually exclusive with: contentPropertyPossibleValues, linkQuery, standaloneLinkQuery, linkQueryOnParameter, dynamicEnumerationOnTrigger. |
| 3 | `contentPropertyPossibleValues` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.InSet.ValueSet.ContentPropertyPossibleValues>` | yes | 14 | Presence selects the content property possible values alternative of RestrictionContext.InSet.ValueSet; it is mutually exclusive with: dynamicEnumeration, linkQuery, standaloneLinkQuery, linkQueryOnParameter, dynamicEnumerationOnTrigger. |
| 4 | `linkQuery` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.InSet.ValueSet.LinkQuery>` | no | 0 | Presence selects the link query alternative of RestrictionContext.InSet.ValueSet; it is mutually exclusive with: dynamicEnumeration, contentPropertyPossibleValues, standaloneLinkQuery, linkQueryOnParameter, dynamicEnumerationOnTrigger. |
| 5 | `standaloneLinkQuery` | singular_presence string | yes | 663 | Presence selects the standalone link query alternative of RestrictionContext.InSet.ValueSet; it is mutually exclusive with: dynamicEnumeration, contentPropertyPossibleValues, linkQuery, linkQueryOnParameter, dynamicEnumerationOnTrigger. |
| 6 | `linkQueryOnParameter` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.InSet.ValueSet.LinkQuery>` | yes | 1371 | Presence selects the link query on parameter alternative of RestrictionContext.InSet.ValueSet; it is mutually exclusive with: dynamicEnumeration, contentPropertyPossibleValues, linkQuery, standaloneLinkQuery, dynamicEnumerationOnTrigger. |
| 7 | `dynamicEnumerationOnTrigger` | singular_presence message `<ToolKit.ToolKitProtoRestrictionContext.InSet.ValueSet.DynamicTriggerEnumeration>` | no | 0 | Presence selects the dynamic enumeration on trigger alternative of RestrictionContext.InSet.ValueSet; it is mutually exclusive with: dynamicEnumeration, contentPropertyPossibleValues, linkQuery, standaloneLinkQuery, linkQueryOnParameter. |

## `ToolKitProtoRestrictionContext.InSet.ValueSet.ContentPropertyPossibleValues`

Native protobuf message for restriction context.in set.value set.content property possible values.

Corpus presence: 14 unique nested messages; 14 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `contentItemClass` | singular_presence message `<ToolKit.ToolKitProtoContentItemClassDescriptor>` | yes | 14 | The content item class value associated with RestrictionContext.InSet.ValueSet.ContentPropertyPossibleValues. |
| 2 | `propertyName` | singular string | yes | 14 | The property name value associated with RestrictionContext.InSet.ValueSet.ContentPropertyPossibleValues. |

## `ToolKitProtoRestrictionContext.InSet.ValueSet.DynamicEnumeration`

Native protobuf message for restriction context.in set.value set.dynamic enumeration.

Corpus presence: 803 unique nested messages; 817 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `toolIdentifier` | singular string | yes | 817 | The tool identifier value associated with RestrictionContext.InSet.ValueSet.DynamicEnumeration. |
| 2 | `parameterKey` | singular string | yes | 817 | The parameter key value associated with RestrictionContext.InSet.ValueSet.DynamicEnumeration. |

## `ToolKitProtoRestrictionContext.InSet.ValueSet.DynamicTriggerEnumeration`

Native protobuf message for restriction context.in set.value set.dynamic trigger enumeration.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `triggerIdentifier` | singular string | no | 0 | The trigger identifier value associated with RestrictionContext.InSet.ValueSet.DynamicTriggerEnumeration. |
| 2 | `parameterKey` | singular string | no | 0 | The parameter key value associated with RestrictionContext.InSet.ValueSet.DynamicTriggerEnumeration. |

## `ToolKitProtoRestrictionContext.InSet.ValueSet.LinkQuery`

Native protobuf message for restriction context.in set.value set.link query.

Corpus presence: 1314 unique nested messages; 1371 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 4 | `parameterKey` | singular string | yes | 1371 | The parameter key value associated with RestrictionContext.InSet.ValueSet.LinkQuery. |
| 5 | `queryIdentifier` | singular string | yes | 1371 | The query identifier value associated with RestrictionContext.InSet.ValueSet.LinkQuery. |
| 6 | `actionIdentifier` | singular string | yes | 1371 | The action identifier value associated with RestrictionContext.InSet.ValueSet.LinkQuery. |

## `ToolKitProtoRestrictionContext.MeasurementExpressibleAs`

Native protobuf message for restriction context.measurement expressible as.

Corpus presence: 14 unique nested messages; 27 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `unit` | singular_presence string | yes | 21 | The unit value associated with RestrictionContext.MeasurementExpressibleAs. |
| 2 | `unitAdjustForLocale` | singular bool | no | 0 | Whether unit adjust for locale is enabled for RestrictionContext.MeasurementExpressibleAs. |
| 3 | `supportsNegativeNumbers` | singular bool | yes | 1 | Whether supports negative numbers is enabled for RestrictionContext.MeasurementExpressibleAs. |

## `ToolKitProtoRestrictionContext.RepresentableAs`

Native protobuf message for restriction context.representable as.

Corpus presence: 86 unique nested messages; 250 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `typeIdentifiers` | repeated string | yes | 250 | Ordered list of type identifiers values associated with RestrictionContext.RepresentableAs. |

## `ToolKitProtoRestrictionContext.TextTypedWith`

Native protobuf message for restriction context.text typed with.

Corpus presence: 62 unique nested messages; 491 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `multilineAllowed` | singular bool | yes | 112 | Whether multiline allowed is enabled for RestrictionContext.TextTypedWith. |
| 2 | `smartQuotesEnabled` | singular bool | yes | 33 | Whether smart quotes enabled is enabled for RestrictionContext.TextTypedWith. |
| 3 | `smartDashesEnabled` | singular bool | yes | 33 | Whether smart dashes enabled is enabled for RestrictionContext.TextTypedWith. |
| 4 | `keyboardType` | singular enum `<ToolKit.ToolKitProtoRestrictionContext.TextTypedWith.KeyboardType>` | yes | 79 | Enumerated keyboard type setting for RestrictionContext.TextTypedWith. |
| 5 | `autocorrectionType` | singular enum `<ToolKit.ToolKitProtoRestrictionContext.TextTypedWith.AutocorrectionType>` | yes | 156 | Enumerated autocorrection type setting for RestrictionContext.TextTypedWith. |
| 6 | `capitalizationType` | singular enum `<ToolKit.ToolKitProtoRestrictionContext.TextTypedWith.CapitalizationType>` | yes | 29 | Enumerated capitalization type setting for RestrictionContext.TextTypedWith. |

## `ToolKitProtoRuntimePlatformVersion`

Native protobuf message for runtime platform version.

Corpus presence: 66 unique nested messages; 1524 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `major` | singular int32 | yes | 836 | The major value associated with RuntimePlatformVersion. |
| 2 | `minor` | singular int32 | yes | 232 | The minor value associated with RuntimePlatformVersion. |
| 3 | `patch` | singular int32 | no | 0 | The patch value associated with RuntimePlatformVersion. |
| 4 | `isWildcard` | singular bool | yes | 688 | Whether is wildcard is enabled for RuntimePlatformVersion. |

## `ToolKitProtoRuntimeRequirement`

A requirement alternative for platform availability, device capability, feature flag, or device state.

Corpus presence: 98 unique nested messages; 7715 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `platform` | singular_presence message `<ToolKit.ToolKitProtoRuntimeRequirement.AvailabilityAnnotation>` | yes | 7504 | Presence selects the platform alternative of RuntimeRequirement; it is mutually exclusive with: deviceCapability, featureFlag, deviceState. |
| 2 | `deviceCapability` | singular_presence message `<ToolKit.ToolKitProtoRuntimeRequirement.DeviceCapability>` | yes | 19 | Presence selects the device capability alternative of RuntimeRequirement; it is mutually exclusive with: platform, featureFlag, deviceState. |
| 3 | `featureFlag` | singular_presence message `<ToolKit.ToolKitProtoRuntimeRequirement.FeatureFlag>` | yes | 66 | Presence selects the feature flag alternative of RuntimeRequirement; it is mutually exclusive with: platform, deviceCapability, deviceState. |
| 4 | `deviceState` | singular_presence enum `<ToolKit.ToolKitProtoRuntimeRequirement.DeviceState>` | yes | 126 | Presence selects the device state alternative of RuntimeRequirement; it is mutually exclusive with: platform, deviceCapability, featureFlag. |

## `ToolKitProtoRuntimeRequirement.AvailabilityAnnotation`

Native protobuf message for runtime requirement.availability annotation.

Corpus presence: 73 unique nested messages; 7504 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `platform` | singular enum `<ToolKit.ToolKitProtoRuntimePlatform>` | yes | 7504 | Enumerated platform setting for RuntimeRequirement.AvailabilityAnnotation. |
| 2 | `introducingVersion` | singular_presence message `<ToolKit.ToolKitProtoRuntimePlatformVersion>` | yes | 1249 | The introducing version value associated with RuntimeRequirement.AvailabilityAnnotation. |
| 3 | `deprecatingVersion` | singular_presence message `<ToolKit.ToolKitProtoRuntimePlatformVersion>` | yes | 54 | The deprecating version value associated with RuntimeRequirement.AvailabilityAnnotation. |
| 4 | `obsoletingVersion` | singular_presence message `<ToolKit.ToolKitProtoRuntimePlatformVersion>` | yes | 221 | The obsoleting version value associated with RuntimeRequirement.AvailabilityAnnotation. |

## `ToolKitProtoRuntimeRequirement.DeviceCapability`

Native protobuf message for runtime requirement.device capability.

Corpus presence: 12 unique nested messages; 19 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `mobileGestalt` | singular_presence message `<ToolKit.ToolKitProtoRuntimeRequirement.DeviceCapability.MobileGestalt>` | yes | 8 | Presence selects the mobile gestalt alternative of RuntimeRequirement.DeviceCapability; it is mutually exclusive with: capability. |
| 2 | `capability` | singular_presence enum `<ToolKit.ToolKitProtoRuntimeRequirement.DeviceCapability.DeviceCapabilityType>` | yes | 11 | Presence selects the capability alternative of RuntimeRequirement.DeviceCapability; it is mutually exclusive with: mobileGestalt. |

## `ToolKitProtoRuntimeRequirement.DeviceCapability.MobileGestalt`

Native protobuf message for runtime requirement.device capability.mobile gestalt.

Corpus presence: 4 unique nested messages; 8 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `key` | singular string | yes | 8 | The key value associated with RuntimeRequirement.DeviceCapability.MobileGestalt. |
| 2 | `value` | singular bool | yes | 5 | Whether value is enabled for RuntimeRequirement.DeviceCapability.MobileGestalt. |

## `ToolKitProtoRuntimeRequirement.FeatureFlag`

Native protobuf message for runtime requirement.feature flag.

Corpus presence: 8 unique nested messages; 66 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `domain` | singular string | yes | 66 | The domain value associated with RuntimeRequirement.FeatureFlag. |
| 2 | `feature` | singular string | yes | 66 | The feature value associated with RuntimeRequirement.FeatureFlag. |
| 3 | `value` | singular bool | yes | 66 | Whether value is enabled for RuntimeRequirement.FeatureFlag. |

## `ToolKitProtoSampleInvocationDefinition`

Native protobuf message for sample invocation definition.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `phrases` | repeated string | no | 0 | Ordered list of phrases values associated with SampleInvocationDefinition. |
| 2 | `expectedResult` | singular_presence string | no | 0 | The expected result value associated with SampleInvocationDefinition. |
| 3 | `negativePhrases` | repeated string | no | 0 | Ordered list of negative phrases values associated with SampleInvocationDefinition. |

## `ToolKitProtoSearchableItemPredicate`

Native protobuf message for searchable item predicate.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `searchableItem` | singular bytes | no | 0 | The searchable item value associated with SearchableItemPredicate. |

## `ToolKitProtoSearchableItemPredicate.Template`

Native protobuf message for searchable item predicate.template.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoStringSearchPredicate`

Native protobuf message for string search predicate.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `searchString` | singular string | no | 0 | The search string value associated with StringSearchPredicate. |

## `ToolKitProtoStringSearchPredicate.Template`

Native protobuf message for string search predicate.template.

Corpus presence: 1645 unique nested messages; 1686 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoSuggestedPredicate`

Native protobuf message for suggested predicate.

Corpus presence: 1346 unique nested messages; 1398 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoSystemToolProtocol`

A presence-tag union declaring system capabilities and behavioral protocols implemented by a tool.

Corpus presence: 2009 unique nested messages; 4793 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `unknown` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 5 | Presence selects the unknown alternative of SystemToolProtocol; it is mutually exclusive with: undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 2 | `undoable` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 4 | Presence selects the undoable alternative of SystemToolProtocol; it is mutually exclusive with: unknown, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 3 | `sessionStarting` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 3 | Presence selects the session starting alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 4 | `urlRepresentable` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 168 | Presence selects the url representable alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 5 | `conditionallyEnabled` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.ConditionallyEnabled>` | no | 0 | Presence selects the conditionally enabled alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 6 | `foregroundContinuable` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 7 | Presence selects the foreground continuable alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 7 | `changeBinarySetting` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 4 | Presence selects the change binary setting alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 8 | `requiresMdmChecks` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 3 | Presence selects the requires mdm checks alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 9 | `cut` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the cut alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 10 | `copy` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the copy alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 11 | `paste` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the paste alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 12 | `cancel` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the cancel alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 13 | `resize` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the resize alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 14 | `scroll` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the scroll alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 15 | `undo` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the undo alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 16 | `zoom` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the zoom alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 17 | `closeEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 4 | Presence selects the close entity alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 18 | `createEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 24 | Presence selects the create entity alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 19 | `cutEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the cut entity alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 20 | `deleteEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 35 | Presence selects the delete entity alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 21 | `duplicateEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the duplicate entity alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 22 | `favoriteEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the favorite entity alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 23 | `openEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 235 | Presence selects the open entity alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 24 | `previewEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the preview entity alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 25 | `saveEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the save entity alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 26 | `putEntityInContainer` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 3 | Presence selects the put entity in container alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 27 | `playVideo` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.PlayVideo>` | no | 0 | Presence selects the play video alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 28 | `audioStarting` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 32 | Presence selects the audio starting alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 29 | `audioRecording` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 14 | Presence selects the audio recording alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 30 | `pushToTalkTransmission` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the push to talk transmission alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 31 | `startDive` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the start dive alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 32 | `startWorkout` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the start workout alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 33 | `pauseWorkout` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the pause workout alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 34 | `resumeWorkout` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the resume workout alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 35 | `enterMarkup` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the enter markup alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 36 | `exitMarkup` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the exit markup alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 37 | `focusConfiguration` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 4 | Presence selects the focus configuration alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 38 | `widgetConfiguration` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 19 | Presence selects the widget configuration alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 39 | `search` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 4 | Presence selects the search alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 40 | `showSearchResultsInApp` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the show search results in app alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 41 | `showStringSearchResultsInApp` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the show string search results in app alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 42 | `showInAppSearchResults` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the show in app search results alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 43 | `showInAppStringSearchResults` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.ShowInAppStringSearchResults>` | yes | 16 | Presence selects the show in app string search results alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 44 | `moveSpatial` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the move spatial alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 45 | `navigateSequentially` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the navigate sequentially alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 46 | `sting` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the sting alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 47 | `toggle` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the toggle alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 48 | `cameraCapture` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the camera capture alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 49 | `staccatoLongPress` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the staccato long press alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 50 | `entityUpdating` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.EntityUpdating>` | yes | 245 | Presence selects the entity updating alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 51 | `propertyUpdater` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.PropertyUpdater>` | no | 0 | Presence selects the property updater alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 52 | `sendMail` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the send mail alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 53 | `setMailMessageIsRead` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the set mail message is read alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 54 | `siriKitIntent` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.SiriKitIntent>` | yes | 105 | Presence selects the siri kit intent alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 55 | `intentSideEffect` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.IntentSideEffect>` | yes | 204 | Presence selects the intent side effect alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 56 | `assistantSchema` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.AssistantSchema>` | yes | 171 | Presence selects the assistant schema alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 57 | `rewriteWritingTool` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the rewrite writing tool alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 58 | `proofreadWritingTool` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the proofread writing tool alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 59 | `assistantInvocable` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 370 | Presence selects the assistant invocable alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 60 | `appIntent` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.AppIntent>` | yes | 1214 | Presence selects the app intent alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 61 | `systemFrameworkIntent` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 36 | Presence selects the system framework intent alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 62 | `synthesizedTool` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.SynthesizedToolProtocol>` | yes | 483 | Presence selects the synthesized tool alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 63 | `progressReporting` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 35 | Presence selects the progress reporting alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 64 | `controlConfiguration` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 6 | Presence selects the control configuration alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, valueSetting, entityGetter, flowToolSchema, agentIntent, batchable. |
| 65 | `valueSetting` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 13 | Presence selects the value setting alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, entityGetter, flowToolSchema, agentIntent, batchable. |
| 66 | `entityGetter` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 242 | Presence selects the entity getter alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, flowToolSchema, agentIntent, batchable. |
| 67 | `flowToolSchema` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.FlowToolSchema>` | yes | 48 | Presence selects the flow tool schema alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, agentIntent, batchable. |
| 69 | `agentIntent` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.AgentIntent>` | yes | 1 | Presence selects the agent intent alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, batchable. |
| 70 | `batchable` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1030 | Presence selects the batchable alternative of SystemToolProtocol; it is mutually exclusive with: unknown, undoable, sessionStarting, urlRepresentable, conditionallyEnabled, foregroundContinuable, changeBinarySetting, requiresMdmChecks, cut, copy, paste, cancel, resize, scroll, undo, zoom, closeEntity, createEntity, cutEntity, deleteEntity, duplicateEntity, favoriteEntity, openEntity, previewEntity, saveEntity, putEntityInContainer, playVideo, audioStarting, audioRecording, pushToTalkTransmission, startDive, startWorkout, pauseWorkout, resumeWorkout, enterMarkup, exitMarkup, focusConfiguration, widgetConfiguration, search, showSearchResultsInApp, showStringSearchResultsInApp, showInAppSearchResults, showInAppStringSearchResults, moveSpatial, navigateSequentially, sting, toggle, cameraCapture, staccatoLongPress, entityUpdating, propertyUpdater, sendMail, setMailMessageIsRead, siriKitIntent, intentSideEffect, assistantSchema, rewriteWritingTool, proofreadWritingTool, assistantInvocable, appIntent, systemFrameworkIntent, synthesizedTool, progressReporting, controlConfiguration, valueSetting, entityGetter, flowToolSchema, agentIntent. |

## `ToolKitProtoSystemToolProtocol.AgentIntent`

Native protobuf message for system tool protocol.agent intent.

Corpus presence: 1 unique nested messages; 1 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `supportedFeatures` | repeated enum `<ToolKit.ToolKitProtoSystemToolProtocol.AgentIntent.SupportedFeature>` | yes | 1 | Ordered list of supported features values associated with SystemToolProtocol.AgentIntent. |

## `ToolKitProtoSystemToolProtocol.AppIntent`

Native protobuf message for system tool protocol.app intent.

Corpus presence: 1182 unique nested messages; 1214 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `intentTypeName` | singular string | yes | 1214 | The intent type name value associated with SystemToolProtocol.AppIntent. |

## `ToolKitProtoSystemToolProtocol.AssistantSchema`

Native protobuf message for system tool protocol.assistant schema.

Corpus presence: 145 unique nested messages; 171 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoAssistantSchemaIdentifier>` | yes | 171 | The identifier value associated with SystemToolProtocol.AssistantSchema. |

## `ToolKitProtoSystemToolProtocol.ConditionallyEnabled`

Native protobuf message for system tool protocol.conditionally enabled.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `persistState` | singular bool | no | 0 | Whether persist state is enabled for SystemToolProtocol.ConditionallyEnabled. |

## `ToolKitProtoSystemToolProtocol.EntityUpdating`

Native protobuf message for system tool protocol.entity updating.

Corpus presence: 239 unique nested messages; 245 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `entityIdentifier` | singular string | yes | 245 | The entity identifier value associated with SystemToolProtocol.EntityUpdating. |

## `ToolKitProtoSystemToolProtocol.FlowToolSchema`

Native protobuf message for system tool protocol.flow tool schema.

Corpus presence: 44 unique nested messages; 48 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoFlowToolSchemaIdentifier>` | yes | 48 | The identifier value associated with SystemToolProtocol.FlowToolSchema. |

## `ToolKitProtoSystemToolProtocol.IntentSideEffect`

Native protobuf message for system tool protocol.intent side effect.

Corpus presence: 22 unique nested messages; 204 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `unknown` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 139 | Presence selects the unknown alternative of SystemToolProtocol.IntentSideEffect; it is mutually exclusive with: noSideEffect, stateChange, stateChangeWithBehavior. |
| 2 | `noSideEffect` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the no side effect alternative of SystemToolProtocol.IntentSideEffect; it is mutually exclusive with: unknown, stateChange, stateChangeWithBehavior. |
| 3 | `stateChange` | singular_presence int32 | no | 0 | Presence selects the state change alternative of SystemToolProtocol.IntentSideEffect; it is mutually exclusive with: unknown, noSideEffect, stateChangeWithBehavior. |
| 4 | `stateChangeWithBehavior` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.IntentSideEffect.StateChangeWithBehavior>` | yes | 65 | Presence selects the state change with behavior alternative of SystemToolProtocol.IntentSideEffect; it is mutually exclusive with: unknown, noSideEffect, stateChange. |

## `ToolKitProtoSystemToolProtocol.IntentSideEffect.Behavior`

Native protobuf message for system tool protocol.intent side effect.behavior.

Corpus presence: 21 unique nested messages; 65 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `kind` | singular enum `<ToolKit.ToolKitProtoSystemToolProtocol.IntentSideEffect.Behavior.Kind>` | no | 0 | Enumerated kind setting for SystemToolProtocol.IntentSideEffect.Behavior. |
| 2 | `keyPathsToRender` | repeated string | yes | 24 | Ordered list of key paths to render values associated with SystemToolProtocol.IntentSideEffect.Behavior. |

## `ToolKitProtoSystemToolProtocol.IntentSideEffect.StateChangeWithBehavior`

Native protobuf message for system tool protocol.intent side effect.state change with behavior.

Corpus presence: 21 unique nested messages; 65 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `stateChangeRawValue` | singular int32 | yes | 65 | The state change raw value value associated with SystemToolProtocol.IntentSideEffect.StateChangeWithBehavior. |
| 2 | `behavior` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.IntentSideEffect.Behavior>` | yes | 65 | The behavior value associated with SystemToolProtocol.IntentSideEffect.StateChangeWithBehavior. |

## `ToolKitProtoSystemToolProtocol.IntentSideEffectBehavior`

Native protobuf message for system tool protocol.intent side effect behavior.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `kind` | singular_presence message `<ToolKit.ToolKitProtoSystemToolProtocol.IntentSideEffectBehavior.Kind>` | no | 0 | The kind value associated with SystemToolProtocol.IntentSideEffectBehavior. |
| 2 | `keyPathsToRender` | repeated string | no | 0 | Ordered list of key paths to render values associated with SystemToolProtocol.IntentSideEffectBehavior. |

## `ToolKitProtoSystemToolProtocol.IntentSideEffectBehavior.Kind`

Native protobuf message for system tool protocol.intent side effect behavior.kind.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `unknown` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the unknown alternative of SystemToolProtocol.IntentSideEffectBehavior.Kind; it is mutually exclusive with: confirmation, choice. |
| 2 | `confirmation` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the confirmation alternative of SystemToolProtocol.IntentSideEffectBehavior.Kind; it is mutually exclusive with: unknown, choice. |
| 3 | `choice` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the choice alternative of SystemToolProtocol.IntentSideEffectBehavior.Kind; it is mutually exclusive with: unknown, confirmation. |

## `ToolKitProtoSystemToolProtocol.IntentStateChange`

Native protobuf message for system tool protocol.intent state change.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `rawValue` | singular int32 | no | 0 | The raw value value associated with SystemToolProtocol.IntentStateChange. |

## `ToolKitProtoSystemToolProtocol.PlayVideo`

Native protobuf message for system tool protocol.play video.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated string | no | 0 | Ordered list of values values associated with SystemToolProtocol.PlayVideo. |

## `ToolKitProtoSystemToolProtocol.PropertyUpdater`

Native protobuf message for system tool protocol.property updater.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `entityIdentifier` | singular string | no | 0 | The entity identifier value associated with SystemToolProtocol.PropertyUpdater. |
| 2 | `entityProperty` | singular string | no | 0 | The entity property value associated with SystemToolProtocol.PropertyUpdater. |

## `ToolKitProtoSystemToolProtocol.ShowInAppStringSearchResults`

Native protobuf message for system tool protocol.show in app string search results.

Corpus presence: 1 unique nested messages; 16 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated string | yes | 16 | Ordered list of values values associated with SystemToolProtocol.ShowInAppStringSearchResults. |

## `ToolKitProtoSystemToolProtocol.SiriKitIntent`

Native protobuf message for system tool protocol.siri kit intent.

Corpus presence: 103 unique nested messages; 105 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 2 | `intentClassName` | singular string | yes | 105 | The intent class name value associated with SystemToolProtocol.SiriKitIntent. |

## `ToolKitProtoSystemToolProtocol.SynthesizedToolProtocol`

Native protobuf message for system tool protocol.synthesized tool protocol.

Corpus presence: 242 unique nested messages; 483 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `replacingIntents` | repeated string | yes | 241 | Ordered list of replacing intents values associated with SystemToolProtocol.SynthesizedToolProtocol. |

## `ToolKitProtoSystemTypeProtocol`

A presence-tag union declaring system capabilities implemented by a type.

Corpus presence: 183 unique nested messages; 1351 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `unknown` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 125 | Presence selects the unknown alternative of SystemTypeProtocol; it is mutually exclusive with: mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 2 | `mailAccount` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the mail account alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 3 | `mailAddressee` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the mail addressee alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 4 | `mailMessage` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the mail message alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 5 | `mailbox` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the mailbox alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 6 | `intentMessage` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the intent message alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 7 | `messageGroup` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the message group alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 8 | `messageParticipants` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the message participants alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 9 | `uniqueEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 263 | Presence selects the unique entity alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 10 | `intentUpdatableEntity` | singular_presence message `<ToolKit.ToolKitProtoSystemTypeProtocol.IntentUpdatableEntity>` | yes | 3 | Presence selects the intent updatable entity alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 11 | `urlRepresentable` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 323 | Presence selects the url representable alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 12 | `visualSearch` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the visual search alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 13 | `visualSearchOcr` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the visual search ocr alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 14 | `assistantSchema` | singular_presence message `<ToolKit.ToolKitProtoSystemTypeProtocol.AssistantSchema>` | yes | 224 | Presence selects the assistant schema alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 15 | `updatableEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the updatable entity alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 16 | `persistentFileIdentifiable` | singular_presence message `<ToolKit.ToolKitProtoSystemTypeProtocol.PersistentFileIdentifiable>` | yes | 5 | Presence selects the persistent file identifiable alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 17 | `transientEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 308 | Presence selects the transient entity alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, indexedEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 18 | `indexedEntity` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 39 | Presence selects the indexed entity alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, collaborative, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 19 | `collaborative` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 17 | Presence selects the collaborative alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, syncableIdentifier, modelRepresentation, snippetRepresentable. |
| 20 | `syncableIdentifier` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 29 | Presence selects the syncable identifier alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, modelRepresentation, snippetRepresentable. |
| 21 | `modelRepresentation` | singular_presence message `<ToolKit.ToolKitProtoSystemTypeProtocol.ModelRepresentationMetadata>` | yes | 10 | Presence selects the model representation alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, snippetRepresentable. |
| 22 | `snippetRepresentable` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the snippet representable alternative of SystemTypeProtocol; it is mutually exclusive with: unknown, mailAccount, mailAddressee, mailMessage, mailbox, intentMessage, messageGroup, messageParticipants, uniqueEntity, intentUpdatableEntity, urlRepresentable, visualSearch, visualSearchOcr, assistantSchema, updatableEntity, persistentFileIdentifiable, transientEntity, indexedEntity, collaborative, syncableIdentifier, modelRepresentation. |

## `ToolKitProtoSystemTypeProtocol.AssistantSchema`

Native protobuf message for system type protocol.assistant schema.

Corpus presence: 155 unique nested messages; 224 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoAssistantSchemaIdentifier>` | yes | 224 | The identifier value associated with SystemTypeProtocol.AssistantSchema. |

## `ToolKitProtoSystemTypeProtocol.IntentUpdatableEntity`

Native protobuf message for system type protocol.intent updatable entity.

Corpus presence: 3 unique nested messages; 3 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `actionIdentifier` | singular string | yes | 3 | The action identifier value associated with SystemTypeProtocol.IntentUpdatableEntity. |

## `ToolKitProtoSystemTypeProtocol.ModelRepresentationMetadata`

Native protobuf message for system type protocol.model representation metadata.

Corpus presence: 9 unique nested messages; 10 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `supportedLevels` | repeated enum `<ToolKit.ToolKitProtoModelRepresentationLevel>` | yes | 10 | Ordered list of supported levels values associated with SystemTypeProtocol.ModelRepresentationMetadata. |
| 2 | `fullRepresentationPropertyIdentifiers` | repeated string | yes | 9 | Ordered list of full representation property identifiers values associated with SystemTypeProtocol.ModelRepresentationMetadata. |
| 3 | `summaryRepresentationPropertyIdentifiers` | repeated string | yes | 4 | Ordered list of summary representation property identifiers values associated with SystemTypeProtocol.ModelRepresentationMetadata. |
| 4 | `supportedComponentKinds` | repeated enum `<ToolKit.ToolKitProtoModelRepresentationComponentKind>` | yes | 8 | Ordered list of supported component kinds values associated with SystemTypeProtocol.ModelRepresentationMetadata. |

## `ToolKitProtoSystemTypeProtocol.PersistentFileIdentifiable`

Native protobuf message for system type protocol.persistent file identifiable.

Corpus presence: 4 unique nested messages; 5 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `supportedContentTypes` | repeated string | yes | 5 | Ordered list of supported content types values associated with SystemTypeProtocol.PersistentFileIdentifiable. |

## `ToolKitProtoToolDatabaseOpaqueValue`

Native protobuf message for tool database opaque value.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated bytes | no | 0 | Ordered list of values values associated with ToolDatabaseOpaqueValue. |

## `ToolKitProtoToolDefinition`

Native protobuf message for tool definition.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoToolDefinition.Version1`

Native protobuf message for tool definition.version1.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `id` | singular string | no | 0 | The id value associated with ToolDefinition.Version1. |
| 2 | `name` | singular string | no | 0 | The name value associated with ToolDefinition.Version1. |
| 3 | `toolType` | singular enum `<ToolKit.ToolKitProtoToolDefinition.Version1.ToolType>` | no | 0 | Enumerated tool type setting for ToolDefinition.Version1. |
| 4 | `parameters` | repeated message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter>` | no | 0 | Ordered list of parameters values associated with ToolDefinition.Version1. |
| 5 | `outputType` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | no | 0 | The output type value associated with ToolDefinition.Version1. |
| 6 | `outputResultName` | singular_presence string | no | 0 | The output result name value associated with ToolDefinition.Version1. |
| 7 | `sourceApplication` | singular_presence message `<ToolKit.ToolKitProtoAppDefinition>` | no | 0 | The source application value associated with ToolDefinition.Version1. |
| 8 | `descriptionSummary` | singular_presence string | no | 0 | The description summary value associated with ToolDefinition.Version1. |
| 9 | `categories` | repeated message `<ToolKit.ToolKitProtoToolDefinition.Version1.Category>` | no | 0 | Ordered list of categories values associated with ToolDefinition.Version1. |
| 10 | `searchKeywords` | repeated string | no | 0 | Ordered list of search keywords values associated with ToolDefinition.Version1. |
| 11 | `deprecationDefinition` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Deprecation>` | no | 0 | The deprecation definition value associated with ToolDefinition.Version1. |
| 12 | `requirements` | repeated message `<ToolKit.ToolKitProtoRuntimeRequirement>` | no | 0 | Ordered list of requirements values associated with ToolDefinition.Version1. |
| 13 | `flags` | repeated enum `<ToolKit.ToolKitProtoToolDefinition.Version1.Flag>` | no | 0 | Ordered list of flags values associated with ToolDefinition.Version1. |
| 14 | `authenticationPolicy` | singular enum `<ToolKit.ToolKitProtoToolDefinition.Version1.AuthenticationPolicy>` | no | 0 | Enumerated authentication policy setting for ToolDefinition.Version1. |
| 15 | `sampleInvocations` | repeated message `<ToolKit.ToolKitProtoSampleInvocationDefinition>` | no | 0 | Ordered list of sample invocations values associated with ToolDefinition.Version1. |
| 16 | `systemProtocols` | repeated message `<ToolKit.ToolKitProtoSystemToolProtocol>` | no | 0 | Ordered list of system protocols values associated with ToolDefinition.Version1. |
| 17 | `customIcon` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.ToolIcon>` | no | 0 | The custom icon value associated with ToolDefinition.Version1. |
| 18 | `hiddenParameters` | repeated message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter>` | no | 0 | Ordered list of hidden parameters values associated with ToolDefinition.Version1. |
| 19 | `sourceContainer` | singular_presence message `<ToolKit.ToolKitProtoContainerDefinition>` | no | 0 | The source container value associated with ToolDefinition.Version1. |
| 20 | `attributionContainer` | singular_presence message `<ToolKit.ToolKitProtoContainerDefinition>` | no | 0 | The attribution container value associated with ToolDefinition.Version1. |
| 21 | `visibilityFlags` | repeated enum `<ToolKit.ToolKitProtoToolDefinition.Version1.VisibilityFlag>` | no | 0 | Ordered list of visibility flags values associated with ToolDefinition.Version1. |
| 22 | `descriptionAttribution` | singular_presence string | no | 0 | The description attribution value associated with ToolDefinition.Version1. |
| 23 | `descriptionResult` | singular_presence string | no | 0 | The description result value associated with ToolDefinition.Version1. |
| 24 | `descriptionNote` | singular_presence string | no | 0 | The description note value associated with ToolDefinition.Version1. |
| 25 | `descriptionRequires` | singular_presence string | no | 0 | The description requires value associated with ToolDefinition.Version1. |
| 26 | `backingLinkActionIdentifiers` | repeated string | no | 0 | Ordered list of backing link action identifiers values associated with ToolDefinition.Version1. |
| 27 | `additionalAttributionContainers` | repeated message `<ToolKit.ToolKitProtoContainerDefinition>` | no | 0 | Ordered list of additional attribution containers values associated with ToolDefinition.Version1. |

## `ToolKitProtoToolDefinition.Version1.Category`

Native protobuf message for tool definition.version1.category.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `name` | singular string | no | 0 | The name value associated with ToolDefinition.Version1.Category. |

## `ToolKitProtoToolDefinition.Version1.Deprecation`

Native protobuf message for tool definition.version1.deprecation.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `deprecationMessage` | singular string | no | 0 | The deprecation message value associated with ToolDefinition.Version1.Deprecation. |
| 2 | `replacedByToolId` | singular_presence string | no | 0 | The replaced by tool id value associated with ToolDefinition.Version1.Deprecation. |

## `ToolKitProtoToolDefinition.Version1.Parameter`

Native protobuf message for tool definition.version1.parameter.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `key` | singular string | no | 0 | The key value associated with ToolDefinition.Version1.Parameter. |
| 2 | `name` | singular string | no | 0 | The name value associated with ToolDefinition.Version1.Parameter. |
| 3 | `description` | singular_presence string | no | 0 | The description value associated with ToolDefinition.Version1.Parameter. |
| 4 | `valueType` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | no | 0 | The value type value associated with ToolDefinition.Version1.Parameter. |
| 5 | `relationships` | repeated message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.Relationship>` | no | 0 | Ordered list of relationships values associated with ToolDefinition.Version1.Parameter. |
| 6 | `sampleInvocations` | repeated message `<ToolKit.ToolKitProtoSampleInvocationDefinition>` | no | 0 | Ordered list of sample invocations values associated with ToolDefinition.Version1.Parameter. |
| 7 | `flags` | repeated enum `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.ParameterFlags>` | no | 0 | Ordered list of flags values associated with ToolDefinition.Version1.Parameter. |
| 8 | `parentToolMetadata` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.ToolMetadata>` | no | 0 | The parent tool metadata value associated with ToolDefinition.Version1.Parameter. |
| 9 | `booleanMetadata` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.BooleanMetadata>` | no | 0 | The boolean metadata value associated with ToolDefinition.Version1.Parameter. |

## `ToolKitProtoToolDefinition.Version1.Parameter.BooleanMetadata`

Native protobuf message for tool definition.version1.parameter.boolean metadata.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `trueString` | singular string | no | 0 | The true string value associated with ToolDefinition.Version1.Parameter.BooleanMetadata. |
| 2 | `falseString` | singular string | no | 0 | The false string value associated with ToolDefinition.Version1.Parameter.BooleanMetadata. |

## `ToolKitProtoToolDefinition.Version1.Parameter.Relationship`

A dependency from one parameter to another parameter key and a condition over typed values.

Corpus presence: 215 unique nested messages; 832 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `key` | singular string | yes | 832 | The key value associated with ToolDefinition.Version1.Parameter.Relationship. |
| 2 | `relation` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation>` | yes | 832 | The relation value associated with ToolDefinition.Version1.Parameter.Relationship. |

## `ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation`

Native protobuf message for tool definition.version1.parameter.relationship.relation.

Corpus presence: 215 unique nested messages; 832 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `isSome` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 20 | Presence selects the is some alternative of ToolDefinition.Version1.Parameter.Relationship.Relation; it is mutually exclusive with: isNone, equals, notEquals, greaterThan, lessThan, contains, doesNotContain. |
| 2 | `isNone` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the is none alternative of ToolDefinition.Version1.Parameter.Relationship.Relation; it is mutually exclusive with: isSome, equals, notEquals, greaterThan, lessThan, contains, doesNotContain. |
| 3 | `equals` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.Equals>` | yes | 785 | Presence selects the equals alternative of ToolDefinition.Version1.Parameter.Relationship.Relation; it is mutually exclusive with: isSome, isNone, notEquals, greaterThan, lessThan, contains, doesNotContain. |
| 4 | `notEquals` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.NotEquals>` | yes | 27 | Presence selects the not equals alternative of ToolDefinition.Version1.Parameter.Relationship.Relation; it is mutually exclusive with: isSome, isNone, equals, greaterThan, lessThan, contains, doesNotContain. |
| 5 | `greaterThan` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.GreaterThan>` | no | 0 | Presence selects the greater than alternative of ToolDefinition.Version1.Parameter.Relationship.Relation; it is mutually exclusive with: isSome, isNone, equals, notEquals, lessThan, contains, doesNotContain. |
| 6 | `lessThan` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.LessThan>` | no | 0 | Presence selects the less than alternative of ToolDefinition.Version1.Parameter.Relationship.Relation; it is mutually exclusive with: isSome, isNone, equals, notEquals, greaterThan, contains, doesNotContain. |
| 7 | `contains` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.Contains>` | no | 0 | Presence selects the contains alternative of ToolDefinition.Version1.Parameter.Relationship.Relation; it is mutually exclusive with: isSome, isNone, equals, notEquals, greaterThan, lessThan, doesNotContain. |
| 8 | `doesNotContain` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.DoesNotContain>` | no | 0 | Presence selects the does not contain alternative of ToolDefinition.Version1.Parameter.Relationship.Relation; it is mutually exclusive with: isSome, isNone, equals, notEquals, greaterThan, lessThan, contains. |

## `ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.Contains`

Native protobuf message for tool definition.version1.parameter.relationship.relation.contains.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Ordered list of values values associated with ToolDefinition.Version1.Parameter.Relationship.Relation.Contains. |

## `ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.DoesNotContain`

Native protobuf message for tool definition.version1.parameter.relationship.relation.does not contain.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Ordered list of values values associated with ToolDefinition.Version1.Parameter.Relationship.Relation.DoesNotContain. |

## `ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.Equals`

Native protobuf message for tool definition.version1.parameter.relationship.relation.equals.

Corpus presence: 192 unique nested messages; 785 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated message `<ToolKit.ToolKitProtoTypedValue>` | yes | 785 | Ordered list of values values associated with ToolDefinition.Version1.Parameter.Relationship.Relation.Equals. |

## `ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.GreaterThan`

Native protobuf message for tool definition.version1.parameter.relationship.relation.greater than.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Ordered list of values values associated with ToolDefinition.Version1.Parameter.Relationship.Relation.GreaterThan. |
| 2 | `orEqual` | singular bool | no | 0 | Whether or equal is enabled for ToolDefinition.Version1.Parameter.Relationship.Relation.GreaterThan. |

## `ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.LessThan`

Native protobuf message for tool definition.version1.parameter.relationship.relation.less than.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Ordered list of values values associated with ToolDefinition.Version1.Parameter.Relationship.Relation.LessThan. |
| 2 | `orEqual` | singular bool | no | 0 | Whether or equal is enabled for ToolDefinition.Version1.Parameter.Relationship.Relation.LessThan. |

## `ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation.NotEquals`

Native protobuf message for tool definition.version1.parameter.relationship.relation.not equals.

Corpus presence: 16 unique nested messages; 27 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated message `<ToolKit.ToolKitProtoTypedValue>` | yes | 27 | Ordered list of values values associated with ToolDefinition.Version1.Parameter.Relationship.Relation.NotEquals. |

## `ToolKitProtoToolDefinition.Version1.Parameter.ToolMetadata`

Native protobuf message for tool definition.version1.parameter.tool metadata.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `sourceContainerId` | singular string | no | 0 | The source container id value associated with ToolDefinition.Version1.Parameter.ToolMetadata. |
| 2 | `backingLinkActionIdentifiers` | repeated string | no | 0 | Ordered list of backing link action identifiers values associated with ToolDefinition.Version1.Parameter.ToolMetadata. |

## `ToolKitProtoToolDefinition.Version1.ToolIcon`

A tool icon source: Workflow asset, SF Symbol-style icon, or external bundle asset.

Corpus presence: 179 unique nested messages; 264 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `workflowAsset` | singular_presence string | yes | 43 | Presence selects the workflow asset alternative of ToolDefinition.Version1.ToolIcon; it is mutually exclusive with: symbol, externalAsset. |
| 2 | `symbol` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.ToolIcon.ToolSymbolIcon>` | yes | 212 | Presence selects the symbol alternative of ToolDefinition.Version1.ToolIcon; it is mutually exclusive with: workflowAsset, externalAsset. |
| 3 | `externalAsset` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1.ToolIcon.ToolExternalAsset>` | yes | 9 | Presence selects the external asset alternative of ToolDefinition.Version1.ToolIcon; it is mutually exclusive with: workflowAsset, symbol. |

## `ToolKitProtoToolDefinition.Version1.ToolIcon.ToolExternalAsset`

Native protobuf message for tool definition.version1.tool icon.tool external asset.

Corpus presence: 2 unique nested messages; 9 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `name` | singular string | yes | 9 | The name value associated with ToolDefinition.Version1.ToolIcon.ToolExternalAsset. |
| 2 | `bundlePath` | singular string | yes | 9 | The bundle path value associated with ToolDefinition.Version1.ToolIcon.ToolExternalAsset. |

## `ToolKitProtoToolDefinition.Version1.ToolIcon.ToolSymbolIcon`

Native protobuf message for tool definition.version1.tool icon.tool symbol icon.

Corpus presence: 157 unique nested messages; 212 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `name` | singular string | yes | 212 | The name value associated with ToolDefinition.Version1.ToolIcon.ToolSymbolIcon. |
| 2 | `style` | singular enum `<ToolKit.ToolKitProtoToolDefinition.Version1.ToolIcon.ToolSymbolIconStyle>` | yes | 52 | Enumerated style setting for ToolDefinition.Version1.ToolIcon.ToolSymbolIcon. |
| 3 | `foreground` | singular string | yes | 212 | The foreground value associated with ToolDefinition.Version1.ToolIcon.ToolSymbolIcon. |
| 4 | `background` | singular_presence string | yes | 160 | The background value associated with ToolDefinition.Version1.ToolIcon.ToolSymbolIcon. |

## `ToolKitProtoToolDefinitionClosure`

Native protobuf message for tool definition closure.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoToolDefinitionClosure.Version1`

Native protobuf message for tool definition closure.version1.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `toolDefinition` | singular_presence message `<ToolKit.ToolKitProtoToolDefinition.Version1>` | no | 0 | The tool definition value associated with ToolDefinitionClosure.Version1. |
| 2 | `typeDefinitions` | repeated message `<ToolKit.ToolKitProtoTypeDefinition.Version1>` | no | 0 | Ordered list of type definitions values associated with ToolDefinitionClosure.Version1. |

## `ToolKitProtoToolInvocation`

Native protobuf message for tool invocation.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence string | no | 0 | The identifier value associated with ToolInvocation. |
| 2 | `toolIdentifier` | singular_presence string | no | 0 | The tool identifier value associated with ToolInvocation. |
| 3 | `target` | singular_presence message `<ToolKit.ToolKitProtoContainerDefinition.Device>` | no | 0 | The target value associated with ToolInvocation. |
| 4 | `parameterValues` | map message `<InternalSwiftProtobuf.ProtobufString->ToolKit.ToolKitProtoTypedValueResolvable>` | no | 0 | Map of parameter values entries associated with ToolInvocation. |
| 5 | `options` | singular_presence message `<ToolKit.ToolKitProtoToolInvocationOptions>` | no | 0 | The options value associated with ToolInvocation. |

## `ToolKitProtoToolInvocationOptions`

Native protobuf message for tool invocation options.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `interactionMode` | singular_presence enum `<ToolKit.ToolKitProtoToolInvocationOptions.InteractionMode>` | no | 0 | Enumerated interaction mode setting for ToolInvocationOptions. |
| 2 | `locale` | singular_presence string | no | 0 | The locale value associated with ToolInvocationOptions. |
| 3 | `requestIdentifier` | singular_presence string | no | 0 | The request identifier value associated with ToolInvocationOptions. |
| 4 | `interfaceIdiom` | singular_presence enum `<ToolKit.ToolKitProtoToolInvocationOptions.InterfaceIdiom>` | no | 0 | Enumerated interface idiom setting for ToolInvocationOptions. |
| 5 | `shortcutOutput` | singular_presence bool | no | 0 | Whether shortcut output is enabled for ToolInvocationOptions. |
| 6 | `confirmationConditions` | singular_presence enum `<ToolKit.ToolKitProtoToolInvocationOptions.ConfirmationConditions>` | no | 0 | Enumerated confirmation conditions setting for ToolInvocationOptions. |
| 7 | `assistantDismissalPolicy` | singular_presence enum `<ToolKit.ToolKitProtoToolInvocationOptions.AssistantDismissalPolicy>` | no | 0 | Enumerated assistant dismissal policy setting for ToolInvocationOptions. |
| 8 | `userIdentity` | singular_presence message `<ToolKit.ToolKitProtoToolInvocationOptions.UserIdentity>` | no | 0 | The user identity value associated with ToolInvocationOptions. |

## `ToolKitProtoToolInvocationOptions.UserIdentity`

Native protobuf message for tool invocation options.user identity.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `personaUniqueIdentifier` | singular string | no | 0 | The persona unique identifier value associated with ToolInvocationOptions.UserIdentity. |
| 2 | `accessLevel` | singular enum `<ToolKit.ToolKitProtoToolInvocationOptions.AccessLevel>` | no | 0 | Enumerated access level setting for ToolInvocationOptions.UserIdentity. |

## `ToolKitProtoToolInvocationSignature`

Native protobuf message for tool invocation signature.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `visibleParameterKeys` | repeated string | no | 0 | Ordered list of visible parameter keys values associated with ToolInvocationSignature. |
| 2 | `invisibleParameterKeys` | repeated string | no | 0 | Ordered list of invisible parameter keys values associated with ToolInvocationSignature. |
| 3 | `valueConstraints` | map message `<InternalSwiftProtobuf.ProtobufString->ToolKit.ToolKitProtoToolInvocationSignature.ListOfRelations>` | no | 0 | Map of value constraints entries associated with ToolInvocationSignature. |

## `ToolKitProtoToolInvocationSignature.ListOfRelations`

Native protobuf message for tool invocation signature.list of relations.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `relation` | repeated message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter.Relationship.Relation>` | no | 0 | Ordered list of relation values associated with ToolInvocationSignature.ListOfRelations. |

## `ToolKitProtoToolSummaryString`

Native protobuf message for tool summary string.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `components` | repeated message `<ToolKit.ToolKitProtoToolSummaryString.Component>` | no | 0 | Ordered list of components values associated with ToolSummaryString. |

## `ToolKitProtoToolSummaryString.Component`

Native protobuf message for tool summary string.component.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `text` | singular_presence string | no | 0 | Presence selects the text alternative of ToolSummaryString.Component; it is mutually exclusive with: parameter. |
| 2 | `parameter` | singular_presence string | no | 0 | Presence selects the parameter alternative of ToolSummaryString.Component; it is mutually exclusive with: text. |

## `ToolKitProtoToolboxDump`

Native protobuf message for toolbox dump.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `metadata` | singular_presence message `<ToolKit.ToolKitProtoToolboxDump.Metadata>` | no | 0 | The metadata value associated with ToolboxDump. |
| 2 | `tools` | repeated message `<ToolKit.ToolKitProtoToolDefinition.Version1>` | no | 0 | Ordered list of tools values associated with ToolboxDump. |
| 3 | `types` | repeated message `<ToolKit.ToolKitProtoTypeDefinition.Version1>` | no | 0 | Ordered list of types values associated with ToolboxDump. |
| 4 | `visibleTools` | repeated message `<ToolKit.ToolKitProtoToolDefinition.Version1>` | no | 0 | Ordered list of visible tools values associated with ToolboxDump. |
| 5 | `triggers` | repeated message `<ToolKit.ToolKitProtoTriggerDefinition.Version1>` | no | 0 | Ordered list of triggers values associated with ToolboxDump. |

## `ToolKitProtoToolboxDump.Metadata`

Native protobuf message for toolbox dump.metadata.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `build` | singular string | no | 0 | The build value associated with ToolboxDump.Metadata. |
| 2 | `os` | singular string | no | 0 | The os value associated with ToolboxDump.Metadata. |

## `ToolKitProtoTriggerDefinition`

Native protobuf message for trigger definition.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoTriggerDefinition.Version1`

Native protobuf message for trigger definition.version1.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `id` | singular string | no | 0 | The id value associated with TriggerDefinition.Version1. |
| 2 | `name` | singular string | no | 0 | The name value associated with TriggerDefinition.Version1. |
| 3 | `description` | singular_presence string | no | 0 | The description value associated with TriggerDefinition.Version1. |
| 4 | `parameters` | repeated message `<ToolKit.ToolKitProtoToolDefinition.Version1.Parameter>` | no | 0 | Ordered list of parameters values associated with TriggerDefinition.Version1. |
| 5 | `outputType` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | no | 0 | The output type value associated with TriggerDefinition.Version1. |
| 6 | `requirements` | repeated message `<ToolKit.ToolKitProtoRuntimeRequirement>` | no | 0 | Ordered list of requirements values associated with TriggerDefinition.Version1. |
| 7 | `flags` | repeated enum `<ToolKit.ToolKitProtoTriggerDefinition.Version1.Flag>` | no | 0 | Ordered list of flags values associated with TriggerDefinition.Version1. |

## `ToolKitProtoTypeDefinition`

Native protobuf message for type definition.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoTypeDefinition.Version1`

Native protobuf message for type definition.version1.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `primitive` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier.Primitive>` | no | 0 | Presence selects the primitive alternative of TypeDefinition.Version1; it is mutually exclusive with: entity, enumeration, query, codable. |
| 2 | `entity` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity>` | no | 0 | Presence selects the entity alternative of TypeDefinition.Version1; it is mutually exclusive with: primitive, enumeration, query, codable. |
| 3 | `enumeration` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Enumeration>` | no | 0 | Presence selects the enumeration alternative of TypeDefinition.Version1; it is mutually exclusive with: primitive, entity, query, codable. |
| 4 | `query` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Query>` | no | 0 | Presence selects the query alternative of TypeDefinition.Version1; it is mutually exclusive with: primitive, entity, enumeration, codable. |
| 5 | `codable` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Codable>` | no | 0 | Presence selects the codable alternative of TypeDefinition.Version1; it is mutually exclusive with: primitive, entity, enumeration, query. |

## `ToolKitProtoTypeDefinition.Version1.Codable`

Native protobuf message for type definition.version1.codable.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular string | no | 0 | The identifier value associated with TypeDefinition.Version1.Codable. |
| 2 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoTypeDisplayRepresentation>` | no | 0 | The display representation value associated with TypeDefinition.Version1.Codable. |

## `ToolKitProtoTypeDefinition.Version1.Entity`

Native protobuf message for type definition.version1.entity.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | no | 0 | The identifier value associated with TypeDefinition.Version1.Entity. |
| 2 | `properties` | repeated message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.Property>` | no | 0 | Ordered list of properties values associated with TypeDefinition.Version1.Entity. |
| 3 | `runtimeRequirements` | repeated message `<ToolKit.ToolKitProtoRuntimeRequirement>` | no | 0 | Ordered list of runtime requirements values associated with TypeDefinition.Version1.Entity. |
| 4 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoTypeDisplayRepresentation>` | no | 0 | The display representation value associated with TypeDefinition.Version1.Entity. |
| 5 | `sampleInvocations` | repeated message `<ToolKit.ToolKitProtoSampleInvocationDefinition>` | no | 0 | Ordered list of sample invocations values associated with TypeDefinition.Version1.Entity. |
| 6 | `systemProtocols` | repeated message `<ToolKit.ToolKitProtoSystemTypeProtocol>` | no | 0 | Ordered list of system protocols values associated with TypeDefinition.Version1.Entity. |
| 7 | `runtimeFlags` | repeated enum `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.RuntimeFlags>` | no | 0 | Ordered list of runtime flags values associated with TypeDefinition.Version1.Entity. |
| 8 | `coercions` | repeated message `<ToolKit.ToolKitProtoCoercionDefinition>` | no | 0 | Ordered list of coercions values associated with TypeDefinition.Version1.Entity. |
| 9 | `authenticationPolicy` | singular enum `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.AuthenticationPolicy>` | no | 0 | Enumerated authentication policy setting for TypeDefinition.Version1.Entity. |

## `ToolKitProtoTypeDefinition.Version1.Entity.Property`

Native protobuf message for type definition.version1.entity.property.

Corpus presence: 3371 unique nested messages; 3440 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `id` | singular string | yes | 3440 | The id value associated with TypeDefinition.Version1.Entity.Property. |
| 2 | `displayName` | singular string | yes | 3440 | The display name value associated with TypeDefinition.Version1.Entity.Property. |
| 3 | `type` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 3440 | The type value associated with TypeDefinition.Version1.Entity.Property. |
| 4 | `spotlightAttributes` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.Property.SpotlightAttributes>` | yes | 1762 | The spotlight attributes value associated with TypeDefinition.Version1.Entity.Property. |
| 7 | `authenticationPolicy` | singular_presence enum `<ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.AuthenticationPolicy>` | yes | 3440 | Enumerated authentication policy setting for TypeDefinition.Version1.Entity.Property. |

## `ToolKitProtoTypeDefinition.Version1.Entity.Property.SpotlightAttributes`

Native protobuf message for type definition.version1.entity.property.spotlight attributes.

Corpus presence: 1735 unique nested messages; 1762 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `attributeKey` | singular_presence string | yes | 1762 | The attribute key value associated with TypeDefinition.Version1.Entity.Property.SpotlightAttributes. |
| 2 | `customAttributeKey` | singular_presence string | no | 0 | The custom attribute key value associated with TypeDefinition.Version1.Entity.Property.SpotlightAttributes. |

## `ToolKitProtoTypeDefinition.Version1.Enumeration`

Native protobuf message for type definition.version1.enumeration.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | no | 0 | The identifier value associated with TypeDefinition.Version1.Enumeration. |
| 2 | `cases` | repeated message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Enumeration.Case>` | no | 0 | Ordered list of cases values associated with TypeDefinition.Version1.Enumeration. |
| 3 | `runtimeRequirements` | repeated message `<ToolKit.ToolKitProtoRuntimeRequirement>` | no | 0 | Ordered list of runtime requirements values associated with TypeDefinition.Version1.Enumeration. |
| 4 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoTypeDisplayRepresentation>` | no | 0 | The display representation value associated with TypeDefinition.Version1.Enumeration. |
| 5 | `kind` | singular enum `<ToolKit.ToolKitProtoTypeDefinition.Version1.Enumeration.Kind>` | no | 0 | Enumerated kind setting for TypeDefinition.Version1.Enumeration. |
| 6 | `systemProtocols` | repeated message `<ToolKit.ToolKitProtoSystemTypeProtocol>` | no | 0 | Ordered list of system protocols values associated with TypeDefinition.Version1.Enumeration. |

## `ToolKitProtoTypeDefinition.Version1.Enumeration.Case`

Native protobuf message for type definition.version1.enumeration.case.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `id` | singular string | no | 0 | The id value associated with TypeDefinition.Version1.Enumeration.Case. |
| 2 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | no | 0 | The display representation value associated with TypeDefinition.Version1.Enumeration.Case. |

## `ToolKitProtoTypeDefinition.Version1.Query`

Native protobuf message for type definition.version1.query.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | no | 0 | The identifier value associated with TypeDefinition.Version1.Query. |
| 2 | `templates` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Query.PredicateTemplates>` | no | 0 | The templates value associated with TypeDefinition.Version1.Query. |

## `ToolKitProtoTypeDefinition.Version1.Query.PredicateTemplates`

Native protobuf message for type definition.version1.query.predicate templates.

Corpus presence: 2792 unique nested messages; 2865 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `comparison` | repeated message `<ToolKit.ToolKitProtoComparisonPredicate.Template>` | yes | 191 | Ordered list of comparison values associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 2 | `stringSearch` | singular_presence message `<ToolKit.ToolKitProtoStringSearchPredicate.Template>` | yes | 1686 | The string search value associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 3 | `idSearch` | singular_presence message `<ToolKit.ToolKitProtoIdSearchPredicate.Template>` | yes | 1578 | The id search value associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 4 | `all` | singular_presence message `<ToolKit.ToolKitProtoAllPredicate>` | yes | 218 | The all value associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 5 | `suggested` | singular_presence message `<ToolKit.ToolKitProtoSuggestedPredicate>` | yes | 1398 | The suggested value associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 6 | `sampleInvocations` | repeated message `<ToolKit.ToolKitProtoSampleInvocationDefinition>` | no | 0 | Ordered list of sample invocations values associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 7 | `searchableItem` | singular_presence message `<ToolKit.ToolKitProtoSearchableItemPredicate.Template>` | no | 0 | The searchable item value associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 8 | `valid` | singular_presence message `<ToolKit.ToolKitProtoValidPredicate>` | yes | 30 | The valid value associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 9 | `metadata` | singular_presence message `<ToolKit.ToolKitProtoTypeDefinition.Version1.Query.PredicateTemplates.PredicateMetadata>` | yes | 2184 | The metadata value associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 10 | `valueSearch` | singular_presence message `<ToolKit.ToolKitProtoValueSearchPredicate.Template>` | yes | 83 | The value search value associated with TypeDefinition.Version1.Query.PredicateTemplates. |
| 11 | `unique` | singular_presence message `<ToolKit.ToolKitProtoUniquePredicate>` | yes | 523 | The unique value associated with TypeDefinition.Version1.Query.PredicateTemplates. |

## `ToolKitProtoTypeDefinition.Version1.Query.PredicateTemplates.PredicateMetadata`

Native protobuf message for type definition.version1.query.predicate templates.predicate metadata.

Corpus presence: 2119 unique nested messages; 2184 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `queryIdentifier` | singular string | yes | 2184 | The query identifier value associated with TypeDefinition.Version1.Query.PredicateTemplates.PredicateMetadata. |
| 2 | `bundleIdentifier` | singular string | yes | 2184 | The bundle identifier value associated with TypeDefinition.Version1.Query.PredicateTemplates.PredicateMetadata. |

## `ToolKitProtoTypeDisplayRepresentation`

Native protobuf message for type display representation.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `name` | singular string | no | 0 | The name value associated with TypeDisplayRepresentation. |
| 2 | `numericFormat` | singular_presence string | no | 0 | The numeric format value associated with TypeDisplayRepresentation. |
| 3 | `synonyms` | repeated string | no | 0 | Ordered list of synonyms values associated with TypeDisplayRepresentation. |

## `ToolKitProtoTypeIdentifier`

The identity of a value type. Exactly one arm selects a primitive, app-defined custom type, ToolKit builtin, attributed type, or codable type.

Corpus presence: 20113 unique nested messages; 28921 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `primitive` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier.Primitive>` | yes | 14655 | Selects a primitive ToolKit type identifier. |
| 2 | `custom` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier.Custom>` | yes | 13404 | Selects an app-defined type identified by bundle ID and type name. |
| 3 | `builtin` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier.Builtin>` | yes | 862 | Selects a ToolKit builtin domain type. |
| 4 | `attributed` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier.Attributed>` | no | 0 | Presence selects the attributed alternative of TypeIdentifier; it is mutually exclusive with: primitive, custom, builtin, codable. |
| 5 | `codable` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier.Codable>` | no | 0 | Presence selects the codable alternative of TypeIdentifier; it is mutually exclusive with: primitive, custom, builtin, attributed. |

## `ToolKitProtoTypeIdentifier.Attributed`

Native protobuf message for type identifier.attributed.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `sourceContainer` | singular_presence message `<ToolKit.ToolKitProtoContainerDefinition>` | no | 0 | The source container value associated with TypeIdentifier.Attributed. |
| 2 | `attributionContainer` | singular_presence message `<ToolKit.ToolKitProtoContainerDefinition>` | no | 0 | The attribution container value associated with TypeIdentifier.Attributed. |
| 3 | `typeName` | singular string | no | 0 | The type name value associated with TypeIdentifier.Attributed. |

## `ToolKitProtoTypeIdentifier.Builtin`

Native protobuf message for type identifier.builtin.

Corpus presence: 856 unique nested messages; 862 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `app` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 17 | Presence selects the app alternative of TypeIdentifier.Builtin; it is mutually exclusive with: boundNumber, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 2 | `boundNumber` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the bound number alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 3 | `calendar` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the calendar alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 4 | `color` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 5 | Presence selects the color alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 5 | `currency` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the currency alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 6 | `file` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the file alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 7 | `homeArea` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 4 | Presence selects the home area alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 8 | `mediaRoute` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 9 | Presence selects the media route alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 9 | `paymentMethod` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the payment method alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, mediaRoute, podcast, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 10 | `podcast` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the podcast alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, person, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 11 | `person` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the person alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, placemark, rideshareOption, vpn, timeZone, query, measurement. |
| 12 | `placemark` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the placemark alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, rideshareOption, vpn, timeZone, query, measurement. |
| 13 | `rideshareOption` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 2 | Presence selects the rideshare option alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, vpn, timeZone, query, measurement. |
| 14 | `vpn` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the vpn alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, timeZone, query, measurement. |
| 15 | `timeZone` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the time zone alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, query, measurement. |
| 16 | `query` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | yes | 825 | Presence selects the query alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, measurement. |
| 17 | `measurement` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the measurement alternative of TypeIdentifier.Builtin; it is mutually exclusive with: app, boundNumber, calendar, color, currency, file, homeArea, mediaRoute, paymentMethod, podcast, person, placemark, rideshareOption, vpn, timeZone, query. |

## `ToolKitProtoTypeIdentifier.Codable`

Native protobuf message for type identifier.codable.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular string | no | 0 | The identifier value associated with TypeIdentifier.Codable. |

## `ToolKitProtoTypeIdentifier.Custom`

Native protobuf message for type identifier.custom.

Corpus presence: 12274 unique nested messages; 13404 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `bundleIdentifier` | singular string | yes | 13404 | The bundle identifier value associated with TypeIdentifier.Custom. |
| 2 | `typeName` | singular string | yes | 13404 | The type name value associated with TypeIdentifier.Custom. |

## `ToolKitProtoTypeIdentifier.Primitive`

A presence-tag union selecting one primitive value category; measurement additionally carries its unit-family enum.

Corpus presence: 6983 unique nested messages; 14655 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `noneP` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1007 | Presence selects the none p alternative of TypeIdentifier.Primitive; it is mutually exclusive with: bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 2 | `bool` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1984 | Presence selects the bool alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 3 | `int` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 345 | Presence selects the int alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 4 | `number` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 855 | Presence selects the number alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 5 | `decimal` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the decimal alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 6 | `string` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 5169 | Presence selects the string alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 7 | `date` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 2434 | Presence selects the date alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 8 | `dateComponents` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 87 | Presence selects the date components alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 9 | `url` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1281 | Presence selects the url alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 10 | `dictionary` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 6 | Presence selects the dictionary alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 11 | `attributedString` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 186 | Presence selects the attributed string alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 12 | `measurement` | singular_presence enum `<ToolKit.ToolKitProtoTypeIdentifier.Primitive.MeasurementUnitType>` | yes | 106 | Presence selects the measurement alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 13 | `currencyAmount` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 19 | Presence selects the currency amount alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 14 | `paymentMethod` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 3 | Presence selects the payment method alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 15 | `placemark` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 99 | Presence selects the placemark alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 16 | `person` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 179 | Presence selects the person alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 17 | `file` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 724 | Presence selects the file alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 18 | `app` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 77 | Presence selects the app alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 19 | `searchableItem` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the searchable item alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 20 | `intentsFile` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the intents file alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 21 | `shortcut` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 2 | Presence selects the shortcut alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 22 | `recurrenceRule` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 16 | Presence selects the recurrence rule alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, dateInterval, personNameComponents, duration, character. |
| 23 | `dateInterval` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 1 | Presence selects the date interval alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, personNameComponents, duration, character. |
| 24 | `personNameComponents` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 4 | Presence selects the person name components alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, duration, character. |
| 25 | `duration` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 65 | Presence selects the duration alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, character. |
| 26 | `character` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | yes | 3 | Presence selects the character alternative of TypeIdentifier.Primitive; it is mutually exclusive with: noneP, bool, int, number, decimal, string, date, dateComponents, url, dictionary, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, intentsFile, shortcut, recurrenceRule, dateInterval, personNameComponents, duration. |

## `ToolKitProtoTypeInstance`

A recursive type expression. Exactly one arm selects a direct type, collection, optional, union, restricted, deferred, or constrained form.

Corpus presence: 19646 unique nested messages; 32531 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `type` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | yes | 18163 | A direct, non-wrapper type identified by ToolKitProtoTypeIdentifier. |
| 2 | `collection` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 1512 | A collection whose element type is the nested TypeInstance. |
| 3 | `optionalVariant` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance.Optional>` | yes | 7392 | An optional wrapper around a nested value type, optionally carrying a typed default value. |
| 4 | `union` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance.Union>` | yes | 340 | A union accepting any of the nested TypeInstance alternatives. |
| 5 | `restricted` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance.Restricted>` | yes | 4168 | A base type identifier plus one or more value restriction contexts. |
| 6 | `deferred` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance.Deferred>` | yes | 928 | A type expression whose nested identifier/type is resolved later. |
| 7 | `constrained` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance.Constrained>` | yes | 28 | A nested TypeInstance plus one or more restriction contexts. |

## `ToolKitProtoTypeInstance.Constrained`

Native protobuf message for type instance.constrained.

Corpus presence: 27 unique nested messages; 28 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `instance` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 28 | The nested type expression to which constraints apply. |
| 2 | `context` | repeated message `<ToolKit.ToolKitProtoRestrictionContext>` | yes | 28 | The value constraints applied to the nested type expression. |

## `ToolKitProtoTypeInstance.Deferred`

Native protobuf message for type instance.deferred.

Corpus presence: 663 unique nested messages; 928 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 928 | The nested type expression used as the deferred type identity. |

## `ToolKitProtoTypeInstance.Optional`

Native protobuf message for type instance.optional.

Corpus presence: 4050 unique nested messages; 7392 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `value` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 7392 | The wrapped type accepted when the optional is present. |
| 2 | `defaultValue` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | yes | 3713 | The typed value used as this optional type's default. |

## `ToolKitProtoTypeInstance.Restricted`

Native protobuf message for type instance.restricted.

Corpus presence: 2962 unique nested messages; 4168 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | yes | 4168 | The base type to which restrictions apply. |
| 2 | `context` | repeated message `<ToolKit.ToolKitProtoRestrictionContext>` | yes | 4168 | The value restrictions applied to the base type. |

## `ToolKitProtoTypeInstance.Union`

Native protobuf message for type instance.union.

Corpus presence: 324 unique nested messages; 340 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `items` | repeated message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 340 | The alternative type expressions accepted by the union. |

## `ToolKitProtoTypedValue`

A typed literal/default value union covering primitive, enum, entity, collection, codable, query, and deferred storage forms.

Corpus presence: 2567 unique nested messages; 4678 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `primitive` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue>` | yes | 2341 | Presence selects the primitive alternative of TypedValue; it is mutually exclusive with: enumeration, entity, collection, query, entityIdentifier, deferred, codable. |
| 2 | `enumeration` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.EnumerationValue>` | yes | 1246 | Presence selects the enumeration alternative of TypedValue; it is mutually exclusive with: primitive, entity, collection, query, entityIdentifier, deferred, codable. |
| 3 | `entity` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.EntityValue>` | yes | 4 | Presence selects the entity alternative of TypedValue; it is mutually exclusive with: primitive, enumeration, collection, query, entityIdentifier, deferred, codable. |
| 4 | `collection` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.CollectionValue>` | yes | 74 | Presence selects the collection alternative of TypedValue; it is mutually exclusive with: primitive, enumeration, entity, query, entityIdentifier, deferred, codable. |
| 5 | `query` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.QueryValue>` | no | 0 | Presence selects the query alternative of TypedValue; it is mutually exclusive with: primitive, enumeration, entity, collection, entityIdentifier, deferred, codable. |
| 6 | `entityIdentifier` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.EntityIdentifierValue>` | no | 0 | Presence selects the entity identifier alternative of TypedValue; it is mutually exclusive with: primitive, enumeration, entity, collection, query, deferred, codable. |
| 7 | `deferred` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.DeferredValue>` | yes | 1013 | Presence selects the deferred alternative of TypedValue; it is mutually exclusive with: primitive, enumeration, entity, collection, query, entityIdentifier, codable. |
| 8 | `codable` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.CodableValue>` | no | 0 | Presence selects the codable alternative of TypedValue; it is mutually exclusive with: primitive, enumeration, entity, collection, query, entityIdentifier, deferred. |

## `ToolKitProtoTypedValue.CodableValue`

Native protobuf message for typed value.codable value.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular string | no | 0 | The identifier value associated with TypedValue.CodableValue. |
| 2 | `data` | singular bytes | no | 0 | The data value associated with TypedValue.CodableValue. |
| 3 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | no | 0 | The display representation value associated with TypedValue.CodableValue. |

## `ToolKitProtoTypedValue.CollectionValue`

Native protobuf message for typed value.collection value.

Corpus presence: 31 unique nested messages; 74 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `type` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | yes | 74 | The type value associated with TypedValue.CollectionValue. |
| 2 | `values` | repeated message `<ToolKit.ToolKitProtoTypedValue>` | yes | 10 | Ordered list of values values associated with TypedValue.CollectionValue. |
| 3 | `typeInstance` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 74 | The type instance value associated with TypedValue.CollectionValue. |

## `ToolKitProtoTypedValue.DeferredValue`

Native protobuf message for typed value.deferred value.

Corpus presence: 968 unique nested messages; 1013 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `type` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | yes | 1013 | The type value associated with TypedValue.DeferredValue. |
| 2 | `expectedTypeInstance` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 1013 | The expected type instance value associated with TypedValue.DeferredValue. |
| 3 | `storage` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.DeferredValue.Storage>` | yes | 1013 | The storage value associated with TypedValue.DeferredValue. |

## `ToolKitProtoTypedValue.DeferredValue.Storage`

Native protobuf message for typed value.deferred value.storage.

Corpus presence: 968 unique nested messages; 1013 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `contentItemProperty` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.DeferredValue.Storage.ContentItemPropertyStorage>` | no | 0 | Presence selects the content item property alternative of TypedValue.DeferredValue.Storage; it is mutually exclusive with: defaultValue, entityProperty. |
| 2 | `defaultValue` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.DeferredValue.Storage.ActionParameterDefaultValueStorage>` | yes | 1013 | Presence selects the default value alternative of TypedValue.DeferredValue.Storage; it is mutually exclusive with: contentItemProperty, entityProperty. |
| 3 | `entityProperty` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.DeferredValue.Storage.EntityPropertyStorage>` | no | 0 | Presence selects the entity property alternative of TypedValue.DeferredValue.Storage; it is mutually exclusive with: contentItemProperty, defaultValue. |

## `ToolKitProtoTypedValue.DeferredValue.Storage.ActionParameterDefaultValueStorage`

Native protobuf message for typed value.deferred value.storage.action parameter default value storage.

Corpus presence: 968 unique nested messages; 1013 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `actionIdentifier` | singular string | yes | 1013 | The action identifier value associated with TypedValue.DeferredValue.Storage.ActionParameterDefaultValueStorage. |
| 2 | `parameterKey` | singular string | yes | 1013 | The parameter key value associated with TypedValue.DeferredValue.Storage.ActionParameterDefaultValueStorage. |

## `ToolKitProtoTypedValue.DeferredValue.Storage.ContentItemPropertyStorage`

Native protobuf message for typed value.deferred value.storage.content item property storage.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `data` | singular bytes | no | 0 | The data value associated with TypedValue.DeferredValue.Storage.ContentItemPropertyStorage. |
| 2 | `propertyKey` | singular string | no | 0 | The property key value associated with TypedValue.DeferredValue.Storage.ContentItemPropertyStorage. |

## `ToolKitProtoTypedValue.DeferredValue.Storage.EntityPropertyStorage`

Native protobuf message for typed value.deferred value.storage.entity property storage.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `entityType` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | no | 0 | The entity type value associated with TypedValue.DeferredValue.Storage.EntityPropertyStorage. |
| 2 | `instanceIdentifier` | singular_presence message `<ToolKit.ToolKitProtoEntityInstanceIdentifier>` | no | 0 | The instance identifier value associated with TypedValue.DeferredValue.Storage.EntityPropertyStorage. |
| 3 | `propertyKey` | singular string | no | 0 | The property key value associated with TypedValue.DeferredValue.Storage.EntityPropertyStorage. |
| 4 | `entityData` | singular bytes | no | 0 | The entity data value associated with TypedValue.DeferredValue.Storage.EntityPropertyStorage. |

## `ToolKitProtoTypedValue.EntityIdentifierValue`

Native protobuf message for typed value.entity identifier value.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `type` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | no | 0 | The type value associated with TypedValue.EntityIdentifierValue. |
| 2 | `identifier` | singular string | no | 0 | The identifier value associated with TypedValue.EntityIdentifierValue. |
| 3 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | no | 0 | The display representation value associated with TypedValue.EntityIdentifierValue. |
| 4 | `instanceIdentifier` | singular_presence message `<ToolKit.ToolKitProtoEntityInstanceIdentifier>` | no | 0 | The instance identifier value associated with TypedValue.EntityIdentifierValue. |
| 5 | `provenance` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.Provenance>` | no | 0 | The provenance value associated with TypedValue.EntityIdentifierValue. |

## `ToolKitProtoTypedValue.EntityValue`

Native protobuf message for typed value.entity value.

Corpus presence: 4 unique nested messages; 4 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `type` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | yes | 4 | The type value associated with TypedValue.EntityValue. |
| 2 | `identifier` | singular string | yes | 4 | The identifier value associated with TypedValue.EntityValue. |
| 3 | `properties` | map message `<InternalSwiftProtobuf.ProtobufString->ToolKit.ToolKitProtoTypedValue>` | yes | 1 | Map of properties entries associated with TypedValue.EntityValue. |
| 4 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | yes | 4 | The display representation value associated with TypedValue.EntityValue. |
| 5 | `hydratedAppEntity` | singular_presence bytes | no | 0 | The hydrated app entity value associated with TypedValue.EntityValue. |
| 6 | `siriKitEntity` | singular_presence bytes | no | 0 | The siri kit entity value associated with TypedValue.EntityValue. |
| 7 | `protocolProperties` | map message `<InternalSwiftProtobuf.ProtobufString->ToolKit.ToolKitProtoTypedValue.EntityValue.ProtocolPropertyMap>` | no | 0 | Map of protocol properties entries associated with TypedValue.EntityValue. |
| 8 | `instanceIdentifier` | singular_presence message `<ToolKit.ToolKitProtoEntityInstanceIdentifier>` | yes | 4 | The instance identifier value associated with TypedValue.EntityValue. |
| 10 | `provenance` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.Provenance>` | yes | 4 | The provenance value associated with TypedValue.EntityValue. |
| 11 | `modelRepresentation` | singular_presence message `<ToolKit.ToolKitProtoModelRepresentation>` | no | 0 | The model representation value associated with TypedValue.EntityValue. |

## `ToolKitProtoTypedValue.EntityValue.ProtocolPropertyMap`

Native protobuf message for typed value.entity value.protocol property map.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `properties` | map message `<InternalSwiftProtobuf.ProtobufString->ToolKit.ToolKitProtoTypedValue>` | no | 0 | Map of properties entries associated with TypedValue.EntityValue.ProtocolPropertyMap. |

## `ToolKitProtoTypedValue.EnumerationValue`

Native protobuf message for typed value.enumeration value.

Corpus presence: 1180 unique nested messages; 1246 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `type` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | yes | 1246 | The type value associated with TypedValue.EnumerationValue. |
| 2 | `caseValue` | singular string | yes | 1246 | The case value value associated with TypedValue.EnumerationValue. |
| 3 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | yes | 1056 | The display representation value associated with TypedValue.EnumerationValue. |

## `ToolKitProtoTypedValue.ID`

Native protobuf message for typed value.id.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `serializedVariable` | singular bytes | no | 0 | The serialized variable value associated with TypedValue.ID. |
| 2 | `typeInstance` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | no | 0 | The type instance value associated with TypedValue.ID. |
| 3 | `identifier` | singular string | no | 0 | The identifier value associated with TypedValue.ID. |

## `ToolKitProtoTypedValue.PrimitiveValue`

Native protobuf message for typed value.primitive value.

Corpus presence: 384 unique nested messages; 2341 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `noneVariant` | singular_presence enum `<InternalSwiftProtobuf.Google_Protobuf_NullValue>` | no | 0 | Presence selects the none variant alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 2 | `bool` | singular_presence bool | yes | 840 | Presence selects the bool alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 3 | `int` | singular_presence int64 | yes | 39 | Presence selects the int alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 4 | `number` | singular_presence double | yes | 956 | Presence selects the number alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 5 | `decimal` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Decimal>` | no | 0 | Presence selects the decimal alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 6 | `string` | singular_presence string | yes | 485 | Presence selects the string alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 7 | `date` | singular_presence message `<InternalSwiftProtobuf.Google_Protobuf_Timestamp>` | no | 0 | Presence selects the date alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 8 | `dateComponents` | singular_presence bytes | no | 0 | Presence selects the date components alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 9 | `url` | singular_presence string | no | 0 | Presence selects the url alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 10 | `attributedString` | singular_presence bytes | no | 0 | Presence selects the attributed string alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 11 | `measurement` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Measurement>` | yes | 9 | Presence selects the measurement alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 12 | `currencyAmount` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.CurrencyAmount>` | no | 0 | Presence selects the currency amount alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 13 | `paymentMethod` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.PaymentMethod>` | no | 0 | Presence selects the payment method alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 14 | `placemark` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Placemark>` | yes | 8 | Presence selects the placemark alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 15 | `person` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Person>` | no | 0 | Presence selects the person alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 16 | `file` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.File>` | no | 0 | Presence selects the file alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 17 | `app` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.App>` | yes | 4 | Presence selects the app alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 18 | `searchableItem` | singular_presence bytes | no | 0 | Presence selects the searchable item alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 19 | `encodedDateComponents` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.DateComponents>` | no | 0 | Presence selects the encoded date components alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, shortcut, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 20 | `shortcut` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Shortcut>` | no | 0 | Presence selects the shortcut alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, recurrenceRule, dateInterval, personNameComponents, duration, character. |
| 22 | `recurrenceRule` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule>` | no | 0 | Presence selects the recurrence rule alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, dateInterval, personNameComponents, duration, character. |
| 23 | `dateInterval` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.DateInterval>` | no | 0 | Presence selects the date interval alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, personNameComponents, duration, character. |
| 24 | `personNameComponents` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Person.NameComponents>` | no | 0 | Presence selects the person name components alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, duration, character. |
| 25 | `duration` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Duration>` | no | 0 | Presence selects the duration alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, character. |
| 26 | `character` | singular_presence string | no | 0 | Presence selects the character alternative of TypedValue.PrimitiveValue; it is mutually exclusive with: noneVariant, bool, int, number, decimal, string, date, dateComponents, url, attributedString, measurement, currencyAmount, paymentMethod, placemark, person, file, app, searchableItem, encodedDateComponents, shortcut, recurrenceRule, dateInterval, personNameComponents, duration. |

## `ToolKitProtoTypedValue.PrimitiveValue.App`

Native protobuf message for typed value.primitive value.app.

Corpus presence: 4 unique nested messages; 4 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `bundleIdentifier` | singular string | yes | 4 | The bundle identifier value associated with TypedValue.PrimitiveValue.App. |
| 2 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | yes | 4 | The display representation value associated with TypedValue.PrimitiveValue.App. |
| 3 | `provenance` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.Provenance>` | yes | 4 | The provenance value associated with TypedValue.PrimitiveValue.App. |

## `ToolKitProtoTypedValue.PrimitiveValue.CurrencyAmount`

Native protobuf message for typed value.primitive value.currency amount.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `amount` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Decimal>` | no | 0 | The amount value associated with TypedValue.PrimitiveValue.CurrencyAmount. |
| 2 | `currencyIdentifier` | singular string | no | 0 | The currency identifier value associated with TypedValue.PrimitiveValue.CurrencyAmount. |
| 3 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | no | 0 | The display representation value associated with TypedValue.PrimitiveValue.CurrencyAmount. |

## `ToolKitProtoTypedValue.PrimitiveValue.DateComponents`

Native protobuf message for typed value.primitive value.date components.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `calendar` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.DateComponents.Calendar>` | no | 0 | The calendar value associated with TypedValue.PrimitiveValue.DateComponents. |
| 2 | `timeZoneIdentifier` | singular_presence string | no | 0 | The time zone identifier value associated with TypedValue.PrimitiveValue.DateComponents. |
| 3 | `era` | singular_presence int64 | no | 0 | The era value associated with TypedValue.PrimitiveValue.DateComponents. |
| 4 | `year` | singular_presence int64 | no | 0 | The year value associated with TypedValue.PrimitiveValue.DateComponents. |
| 5 | `month` | singular_presence int64 | no | 0 | The month value associated with TypedValue.PrimitiveValue.DateComponents. |
| 6 | `day` | singular_presence int64 | no | 0 | The day value associated with TypedValue.PrimitiveValue.DateComponents. |
| 7 | `hour` | singular_presence int64 | no | 0 | The hour value associated with TypedValue.PrimitiveValue.DateComponents. |
| 8 | `minute` | singular_presence int64 | no | 0 | The minute value associated with TypedValue.PrimitiveValue.DateComponents. |
| 9 | `second` | singular_presence int64 | no | 0 | The second value associated with TypedValue.PrimitiveValue.DateComponents. |
| 10 | `nanosecond` | singular_presence int64 | no | 0 | The nanosecond value associated with TypedValue.PrimitiveValue.DateComponents. |
| 11 | `weekday` | singular_presence int64 | no | 0 | The weekday value associated with TypedValue.PrimitiveValue.DateComponents. |
| 12 | `weekdayOrdinal` | singular_presence int64 | no | 0 | The weekday ordinal value associated with TypedValue.PrimitiveValue.DateComponents. |
| 13 | `quarter` | singular_presence int64 | no | 0 | The quarter value associated with TypedValue.PrimitiveValue.DateComponents. |
| 14 | `weekOfMonth` | singular_presence int64 | no | 0 | The week of month value associated with TypedValue.PrimitiveValue.DateComponents. |
| 15 | `weekOfYear` | singular_presence int64 | no | 0 | The week of year value associated with TypedValue.PrimitiveValue.DateComponents. |
| 16 | `yearForWeekOfYear` | singular_presence int64 | no | 0 | The year for week of year value associated with TypedValue.PrimitiveValue.DateComponents. |

## `ToolKitProtoTypedValue.PrimitiveValue.DateComponents.Calendar`

Native protobuf message for typed value.primitive value.date components.calendar.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular enum `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.DateComponents.CalendarIdentifier>` | no | 0 | Enumerated identifier setting for TypedValue.PrimitiveValue.DateComponents.Calendar. |
| 2 | `timeZoneIdentifier` | singular string | no | 0 | The time zone identifier value associated with TypedValue.PrimitiveValue.DateComponents.Calendar. |
| 3 | `localeIdentifier` | singular_presence string | no | 0 | The locale identifier value associated with TypedValue.PrimitiveValue.DateComponents.Calendar. |
| 4 | `firstWeekday` | singular int64 | no | 0 | The first weekday value associated with TypedValue.PrimitiveValue.DateComponents.Calendar. |
| 5 | `minimumDaysInFirstWeek` | singular int64 | no | 0 | The minimum days in first week value associated with TypedValue.PrimitiveValue.DateComponents.Calendar. |

## `ToolKitProtoTypedValue.PrimitiveValue.DateInterval`

Native protobuf message for typed value.primitive value.date interval.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `start` | singular_presence message `<InternalSwiftProtobuf.Google_Protobuf_Timestamp>` | no | 0 | The start value associated with TypedValue.PrimitiveValue.DateInterval. |
| 2 | `end` | singular_presence message `<InternalSwiftProtobuf.Google_Protobuf_Timestamp>` | no | 0 | The end value associated with TypedValue.PrimitiveValue.DateInterval. |
| 3 | `duration` | singular_presence double | no | 0 | The duration value associated with TypedValue.PrimitiveValue.DateInterval. |

## `ToolKitProtoTypedValue.PrimitiveValue.Decimal`

Native protobuf message for typed value.primitive value.decimal.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `sign` | singular enum `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Decimal.Sign>` | no | 0 | Enumerated sign setting for TypedValue.PrimitiveValue.Decimal. |
| 2 | `exponent` | singular int32 | no | 0 | The exponent value associated with TypedValue.PrimitiveValue.Decimal. |
| 4 | `isCompact` | singular bool | no | 0 | Whether is compact is enabled for TypedValue.PrimitiveValue.Decimal. |
| 5 | `length` | singular uint32 | no | 0 | The length value associated with TypedValue.PrimitiveValue.Decimal. |
| 6 | `mantissa` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Decimal.Mantissa>` | no | 0 | The mantissa value associated with TypedValue.PrimitiveValue.Decimal. |

## `ToolKitProtoTypedValue.PrimitiveValue.Decimal.Mantissa`

Native protobuf message for typed value.primitive value.decimal.mantissa.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `0` | singular uint32 | no | 0 | The 0 value associated with TypedValue.PrimitiveValue.Decimal.Mantissa. |
| 2 | `1` | singular uint32 | no | 0 | The 1 value associated with TypedValue.PrimitiveValue.Decimal.Mantissa. |
| 3 | `2` | singular uint32 | no | 0 | The 2 value associated with TypedValue.PrimitiveValue.Decimal.Mantissa. |
| 4 | `3` | singular uint32 | no | 0 | The 3 value associated with TypedValue.PrimitiveValue.Decimal.Mantissa. |
| 5 | `4` | singular uint32 | no | 0 | The 4 value associated with TypedValue.PrimitiveValue.Decimal.Mantissa. |
| 6 | `5` | singular uint32 | no | 0 | The 5 value associated with TypedValue.PrimitiveValue.Decimal.Mantissa. |
| 7 | `6` | singular uint32 | no | 0 | The 6 value associated with TypedValue.PrimitiveValue.Decimal.Mantissa. |
| 8 | `7` | singular uint32 | no | 0 | The 7 value associated with TypedValue.PrimitiveValue.Decimal.Mantissa. |

## `ToolKitProtoTypedValue.PrimitiveValue.Duration`

Native protobuf message for typed value.primitive value.duration.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `seconds` | singular int64 | no | 0 | The seconds value associated with TypedValue.PrimitiveValue.Duration. |
| 2 | `attoSeconds` | singular int64 | no | 0 | The atto seconds value associated with TypedValue.PrimitiveValue.Duration. |

## `ToolKitProtoTypedValue.PrimitiveValue.File`

Native protobuf message for typed value.primitive value.file.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `file` | singular bytes | no | 0 | The file value associated with TypedValue.PrimitiveValue.File. |
| 2 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | no | 0 | The display representation value associated with TypedValue.PrimitiveValue.File. |
| 3 | `url` | singular_presence string | no | 0 | The url value associated with TypedValue.PrimitiveValue.File. |
| 4 | `provenance` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.Provenance>` | no | 0 | The provenance value associated with TypedValue.PrimitiveValue.File. |

## `ToolKitProtoTypedValue.PrimitiveValue.Measurement`

Native protobuf message for typed value.primitive value.measurement.

Corpus presence: 9 unique nested messages; 9 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `unit` | singular string | yes | 9 | The unit value associated with TypedValue.PrimitiveValue.Measurement. |
| 2 | `value` | singular double | yes | 7 | The value value associated with TypedValue.PrimitiveValue.Measurement. |
| 3 | `unitType` | singular enum `<ToolKit.ToolKitProtoTypeIdentifier.Primitive.MeasurementUnitType>` | yes | 5 | Enumerated unit type setting for TypedValue.PrimitiveValue.Measurement. |

## `ToolKitProtoTypedValue.PrimitiveValue.PaymentMethod`

Native protobuf message for typed value.primitive value.payment method.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `type` | singular enum `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.PaymentMethod.TypeEnum>` | no | 0 | Enumerated type setting for TypedValue.PrimitiveValue.PaymentMethod. |
| 2 | `identificationHint` | singular_presence string | no | 0 | The identification hint value associated with TypedValue.PrimitiveValue.PaymentMethod. |
| 3 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | no | 0 | The display representation value associated with TypedValue.PrimitiveValue.PaymentMethod. |

## `ToolKitProtoTypedValue.PrimitiveValue.Person`

Native protobuf message for typed value.primitive value.person.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `person` | singular_presence bytes | no | 0 | The person value associated with TypedValue.PrimitiveValue.Person. |
| 2 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | no | 0 | The display representation value associated with TypedValue.PrimitiveValue.Person. |
| 3 | `handle` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Person.Handle>` | no | 0 | The handle value associated with TypedValue.PrimitiveValue.Person. |
| 4 | `nameComponents` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Person.NameComponents>` | no | 0 | The name components value associated with TypedValue.PrimitiveValue.Person. |
| 5 | `displayName` | singular string | no | 0 | The display name value associated with TypedValue.PrimitiveValue.Person. |
| 6 | `image` | singular_presence bytes | no | 0 | The image value associated with TypedValue.PrimitiveValue.Person. |
| 7 | `contactIdentifier` | singular_presence string | no | 0 | The contact identifier value associated with TypedValue.PrimitiveValue.Person. |
| 8 | `customIdentifier` | singular_presence string | no | 0 | The custom identifier value associated with TypedValue.PrimitiveValue.Person. |
| 9 | `relationship` | singular_presence string | no | 0 | The relationship value associated with TypedValue.PrimitiveValue.Person. |
| 10 | `contactSuggestion` | singular_presence bool | no | 0 | Whether contact suggestion is enabled for TypedValue.PrimitiveValue.Person. |
| 11 | `isMe` | singular bool | no | 0 | Whether is me is enabled for TypedValue.PrimitiveValue.Person. |
| 12 | `provenance` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.Provenance>` | no | 0 | The provenance value associated with TypedValue.PrimitiveValue.Person. |

## `ToolKitProtoTypedValue.PrimitiveValue.Person.Handle`

Native protobuf message for typed value.primitive value.person.handle.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `value` | singular_presence string | no | 0 | The value value associated with TypedValue.PrimitiveValue.Person.Handle. |
| 2 | `type` | singular enum `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Person.Handle.TypeEnum>` | no | 0 | Enumerated type setting for TypedValue.PrimitiveValue.Person.Handle. |
| 3 | `label` | singular_presence string | no | 0 | The label value associated with TypedValue.PrimitiveValue.Person.Handle. |

## `ToolKitProtoTypedValue.PrimitiveValue.Person.NameComponents`

Native protobuf message for typed value.primitive value.person.name components.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `namePrefix` | singular_presence string | no | 0 | The name prefix value associated with TypedValue.PrimitiveValue.Person.NameComponents. |
| 2 | `givenName` | singular_presence string | no | 0 | The given name value associated with TypedValue.PrimitiveValue.Person.NameComponents. |
| 3 | `middleName` | singular_presence string | no | 0 | The middle name value associated with TypedValue.PrimitiveValue.Person.NameComponents. |
| 4 | `familyName` | singular_presence string | no | 0 | The family name value associated with TypedValue.PrimitiveValue.Person.NameComponents. |
| 5 | `nameSuffix` | singular_presence string | no | 0 | The name suffix value associated with TypedValue.PrimitiveValue.Person.NameComponents. |
| 6 | `nickname` | singular_presence string | no | 0 | The nickname value associated with TypedValue.PrimitiveValue.Person.NameComponents. |
| 7 | `phoneticRepresentation` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Person.NameComponents.PhoneticRepresentation>` | no | 0 | The phonetic representation value associated with TypedValue.PrimitiveValue.Person.NameComponents. |

## `ToolKitProtoTypedValue.PrimitiveValue.Person.NameComponents.PhoneticRepresentation`

Native protobuf message for typed value.primitive value.person.name components.phonetic representation.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `namePrefix` | singular_presence string | no | 0 | The name prefix value associated with TypedValue.PrimitiveValue.Person.NameComponents.PhoneticRepresentation. |
| 2 | `givenName` | singular_presence string | no | 0 | The given name value associated with TypedValue.PrimitiveValue.Person.NameComponents.PhoneticRepresentation. |
| 3 | `middleName` | singular_presence string | no | 0 | The middle name value associated with TypedValue.PrimitiveValue.Person.NameComponents.PhoneticRepresentation. |
| 4 | `familyName` | singular_presence string | no | 0 | The family name value associated with TypedValue.PrimitiveValue.Person.NameComponents.PhoneticRepresentation. |
| 5 | `nameSuffix` | singular_presence string | no | 0 | The name suffix value associated with TypedValue.PrimitiveValue.Person.NameComponents.PhoneticRepresentation. |
| 6 | `nickname` | singular_presence string | no | 0 | The nickname value associated with TypedValue.PrimitiveValue.Person.NameComponents.PhoneticRepresentation. |

## `ToolKitProtoTypedValue.PrimitiveValue.Placemark`

Native protobuf message for typed value.primitive value.placemark.

Corpus presence: 1 unique nested messages; 8 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `placemark` | singular_presence bytes | no | 0 | The placemark value associated with TypedValue.PrimitiveValue.Placemark. |
| 2 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | yes | 8 | The display representation value associated with TypedValue.PrimitiveValue.Placemark. |
| 3 | `type` | singular enum `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.Placemark.TypeEnum>` | yes | 8 | Enumerated type setting for TypedValue.PrimitiveValue.Placemark. |
| 4 | `provenance` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.Provenance>` | yes | 8 | The provenance value associated with TypedValue.PrimitiveValue.Placemark. |

## `ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule`

Native protobuf message for typed value.primitive value.recurrence rule.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `calendar` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.DateComponents.Calendar>` | no | 0 | The calendar value associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 2 | `frequency` | singular enum `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleFrequency>` | no | 0 | Enumerated frequency setting for TypedValue.PrimitiveValue.RecurrenceRule. |
| 3 | `interval` | singular int64 | no | 0 | The interval value associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 4 | `end` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleEnd>` | no | 0 | The end value associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 5 | `matchingPolicy` | singular enum `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.CalendarMatchingPolicy>` | no | 0 | Enumerated matching policy setting for TypedValue.PrimitiveValue.RecurrenceRule. |
| 6 | `repeatedTimePolicy` | singular enum `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.CalendarRepeatedTimePolicy>` | no | 0 | Enumerated repeated time policy setting for TypedValue.PrimitiveValue.RecurrenceRule. |
| 7 | `months` | repeated message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleMonth>` | no | 0 | Ordered list of months values associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 8 | `daysOfTheYear` | repeated int64 | no | 0 | Ordered list of days of the year values associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 9 | `daysOfTheMonth` | repeated int64 | no | 0 | Ordered list of days of the month values associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 10 | `weeks` | repeated int64 | no | 0 | Ordered list of weeks values associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 11 | `weekdays` | repeated message `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleWeekday>` | no | 0 | Ordered list of weekdays values associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 12 | `hours` | repeated int64 | no | 0 | Ordered list of hours values associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 13 | `minutes` | repeated int64 | no | 0 | Ordered list of minutes values associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 14 | `seconds` | repeated int64 | no | 0 | Ordered list of seconds values associated with TypedValue.PrimitiveValue.RecurrenceRule. |
| 15 | `setPositions` | repeated int64 | no | 0 | Ordered list of set positions values associated with TypedValue.PrimitiveValue.RecurrenceRule. |

## `ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleEnd`

Native protobuf message for typed value.primitive value.recurrence rule.recurrence rule end.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `occurences` | singular_presence int64 | no | 0 | The occurences value associated with TypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleEnd. |
| 2 | `date` | singular_presence message `<InternalSwiftProtobuf.Google_Protobuf_Timestamp>` | no | 0 | The date value associated with TypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleEnd. |
| 3 | `never` | singular_presence bool | no | 0 | Whether never is enabled for TypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleEnd. |
| 4 | `occurrences` | singular_presence int64 | no | 0 | The occurrences value associated with TypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleEnd. |

## `ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleMonth`

Native protobuf message for typed value.primitive value.recurrence rule.recurrence rule month.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `index` | singular int64 | no | 0 | The index value associated with TypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleMonth. |
| 2 | `isLeap` | singular bool | no | 0 | Whether is leap is enabled for TypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleMonth. |

## `ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleWeekday`

Native protobuf message for typed value.primitive value.recurrence rule.recurrence rule weekday.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `RecurrenceRuleWeekdayWeekday` | singular enum `<ToolKit.ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.LocaleWeekday>` | no | 0 | Enumerated recurrence rule weekday weekday setting for TypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleWeekday. |
| 2 | `RecurrenceRuleWeekdayEvery` | singular_presence bool | no | 0 | Whether recurrence rule weekday every is enabled for TypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleWeekday. |
| 3 | `RecurrenceRuleWeekdayNth` | singular_presence int64 | no | 0 | The recurrence rule weekday nth value associated with TypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleWeekday. |

## `ToolKitProtoTypedValue.PrimitiveValue.Shortcut`

Native protobuf message for typed value.primitive value.shortcut.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `identifier` | singular string | no | 0 | The identifier value associated with TypedValue.PrimitiveValue.Shortcut. |
| 2 | `displayRepresentation` | singular_presence message `<ToolKit.ToolKitProtoDisplayRepresentation>` | no | 0 | The display representation value associated with TypedValue.PrimitiveValue.Shortcut. |

## `ToolKitProtoTypedValue.Provenance`

Native protobuf message for typed value.provenance.

Corpus presence: 9 unique nested messages; 16 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `clientSpecificMetadata` | map scalar `<InternalSwiftProtobuf.ProtobufString->InternalSwiftProtobuf.ProtobufString>` | no | 0 | Map of client specific metadata entries associated with TypedValue.Provenance. |

## `ToolKitProtoTypedValue.QueryValue`

Native protobuf message for typed value.query value.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `type` | singular_presence message `<ToolKit.ToolKitProtoTypeIdentifier>` | no | 0 | The type value associated with TypedValue.QueryValue. |
| 2 | `query` | singular_presence message `<ToolKit.ToolKitProtoQuery>` | no | 0 | The query value associated with TypedValue.QueryValue. |

## `ToolKitProtoTypedValueResolvable`

Native protobuf message for typed value resolvable.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `value` | singular_presence message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Presence selects the value alternative of TypedValueResolvable; it is mutually exclusive with: reference. |
| 2 | `reference` | singular_presence message `<ToolKit.ToolKitProtoTypedValue.ID>` | no | 0 | Presence selects the reference alternative of TypedValueResolvable; it is mutually exclusive with: value. |

## `ToolKitProtoUniquePredicate`

Native protobuf message for unique predicate.

Corpus presence: 522 unique nested messages; 523 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoVacuumOperationEnd`

Native protobuf message for vacuum operation end.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `operationId` | singular string | no | 0 | The operation id value associated with VacuumOperationEnd. |
| 2 | `error` | singular_presence string | no | 0 | The error value associated with VacuumOperationEnd. |

## `ToolKitProtoVacuumOperationStart`

Native protobuf message for vacuum operation start.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `operationId` | singular string | no | 0 | The operation id value associated with VacuumOperationStart. |

## `ToolKitProtoValidPredicate`

Native protobuf message for valid predicate.

Corpus presence: 30 unique nested messages; 30 weighted database occurrences.

No defined fields (presence-only empty message).

## `ToolKitProtoValueSearchPredicate`

Native protobuf message for value search predicate.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `values` | repeated message `<ToolKit.ToolKitProtoTypedValue>` | no | 0 | Ordered list of values values associated with ValueSearchPredicate. |

## `ToolKitProtoValueSearchPredicate.Template`

Native protobuf message for value search predicate.template.

Corpus presence: 77 unique nested messages; 83 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `input` | singular_presence message `<ToolKit.ToolKitProtoTypeInstance>` | yes | 83 | The input value associated with ValueSearchPredicate.Template. |

## `ToolKitProtoWALOperationEnd`

Native protobuf message for waloperation end.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `operationId` | singular string | no | 0 | The operation id value associated with WALOperationEnd. |
| 2 | `busy` | singular_presence bool | no | 0 | Whether busy is enabled for WALOperationEnd. |
| 3 | `totalFrames` | singular_presence int32 | no | 0 | The total frames value associated with WALOperationEnd. |
| 4 | `checkpointedFrames` | singular_presence int32 | no | 0 | The checkpointed frames value associated with WALOperationEnd. |
| 5 | `error` | singular_presence string | no | 0 | The error value associated with WALOperationEnd. |

## `ToolKitProtoWALOperationStart`

Native protobuf message for waloperation start.

Corpus presence: 0 unique nested messages; 0 weighted database occurrences.

| # | Native name | Shape | Observed | Weighted count | Semantic meaning |
|---:|---|---|---:|---:|---|
| 1 | `operationId` | singular string | no | 0 | The operation id value associated with WALOperationStart. |

# Enum Ledger

Enum names and numeric values come from live ToolKit name maps and enum decoder entrypoints under LLDB.

## `ToolKitProtoAppDefinition.Origin`

Native enumeration selecting the app definition.origin setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `OriginUnspecified` | Selects the origin unspecified case of app definition.origin. |
| 1 | `OriginFirstParty` | Selects the origin first party case of app definition.origin. |
| 2 | `OriginThirdParty` | Selects the origin third party case of app definition.origin. |

## `ToolKitProtoCoercionDefinition.CoercionDirection`

Native enumeration selecting the coercion definition.coercion direction setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `CoercionDirectionImport` | Selects the coercion direction import case of coercion definition.coercion direction. |
| 1 | `CoercionDirectionExport` | Selects the coercion direction export case of coercion definition.coercion direction. |

## `ToolKitProtoCompoundPredicate.Operator`

Native enumeration selecting the compound predicate.operator setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `OperatorUnspecified` | Selects the operator unspecified case of compound predicate.operator. |
| 1 | `OperatorAnd` | Selects the operator and case of compound predicate.operator. |
| 2 | `OperatorOr` | Selects the operator or case of compound predicate.operator. |

## `ToolKitProtoContainerDefinition.Origin`

Native enumeration selecting the container definition.origin setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `OriginUnspecified` | Selects the origin unspecified case of container definition.origin. |
| 1 | `OriginFirstParty` | Selects the origin first party case of container definition.origin. |
| 2 | `OriginThirdParty` | Selects the origin third party case of container definition.origin. |

## `ToolKitProtoContainerDefinition.TypeEnum`

Native enumeration selecting the container definition.type enum setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `TypeApp` | Selects the type app case of container definition.type enum. |
| 1 | `TypeDaemon` | Selects the type daemon case of container definition.type enum. |
| 2 | `TypeExtension` | Selects the type extension case of container definition.type enum. |
| 3 | `TypeFramework` | Selects the type framework case of container definition.type enum. |
| 4 | `TypeUnknown` | Selects the type unknown case of container definition.type enum. |

## `ToolKitProtoDisplayRepresentation.DisplayValue.DisplayValueEnum`

Native enumeration selecting the display representation.display value.display value enum setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `DisplayValueEnumImage` | Selects the display value enum image case of display representation.display value.display value enum. |
| 1 | `DisplayValueEnumSubtitle` | Selects the display value enum subtitle case of display representation.display value.display value enum. |
| 2 | `DisplayValueEnumAltText` | Selects the display value enum alt text case of display representation.display value.display value enum. |

## `ToolKitProtoIndexingStep.Phase`

Native enumeration selecting the indexing step.phase setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `PhaseUnspecified` | Selects the phase unspecified case of indexing step.phase. |
| 1 | `PhaseStart` | Selects the phase start case of indexing step.phase. |
| 2 | `PhaseEnd` | Selects the phase end case of indexing step.phase. |

## `ToolKitProtoModelRepresentation.RepresentationComponent.Label.Kind`

Native enumeration selecting the model representation.representation component.label.kind setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `KindDefault` | Selects the kind default case of model representation.representation component.label.kind. |
| 1 | `KindCustom` | Selects the kind custom case of model representation.representation component.label.kind. |

## `ToolKitProtoModelRepresentationComponentKind`

Native enumeration selecting the model representation component kind setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `ModelRepresentationComponentKindUnspecified` | Selects the model representation component kind unspecified case of model representation component kind. |
| 1 | `ModelRepresentationComponentKindText` | Selects the model representation component kind text case of model representation component kind. |
| 2 | `ModelRepresentationComponentKindVisual` | Selects the model representation component kind visual case of model representation component kind. |

## `ToolKitProtoModelRepresentationLevel`

Native enumeration selecting the model representation level setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `ModelRepresentationLevelUnspecified` | Selects the model representation level unspecified case of model representation level. |
| 1 | `ModelRepresentationLevelSummary` | Selects the model representation level summary case of model representation level. |
| 2 | `ModelRepresentationLevelFull` | Selects the model representation level full case of model representation level. |

## `ToolKitProtoPushDonationStart.DonationType`

Native enumeration selecting the push donation start.donation type setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `DonationTypeUnspecified` | Selects the donation type unspecified case of push donation start.donation type. |
| 1 | `DonationTypeFull` | Selects the donation type full case of push donation start.donation type. |
| 2 | `DonationTypeIncremental` | Selects the donation type incremental case of push donation start.donation type. |
| 3 | `DonationTypeIncrementalFullFallback` | Selects the donation type incremental full fallback case of push donation start.donation type. |

## `ToolKitProtoQuery.SortOrder`

Native enumeration selecting the query.sort order setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `SortOrderUnspecified` | Selects the sort order unspecified case of query.sort order. |
| 1 | `SortOrderForward` | Selects the sort order forward case of query.sort order. |
| 2 | `SortOrderReverse` | Selects the sort order reverse case of query.sort order. |

## `ToolKitProtoRestrictionContext.CharacterTypedWith.ParameterMode`

Native enumeration selecting the restriction context.character typed with.parameter mode setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `ParameterModeUnspecified` | Selects the parameter mode unspecified case of restriction context.character typed with.parameter mode. |
| 1 | `ParameterModeStandard` | Selects the parameter mode standard case of restriction context.character typed with.parameter mode. |
| 2 | `ParameterModeEmoji` | Selects the parameter mode emoji case of restriction context.character typed with.parameter mode. |

## `ToolKitProtoRestrictionContext.DateExpressibleAs`

Native enumeration selecting the restriction context.date expressible as setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `DateExpressibleAsUnspecified` | Selects the date expressible as unspecified case of restriction context.date expressible as. |
| 1 | `DateExpressibleAsDate` | Selects the date expressible as date case of restriction context.date expressible as. |
| 2 | `DateExpressibleAsTime` | Selects the date expressible as time case of restriction context.date expressible as. |
| 3 | `DateExpressibleAsDateAndTime` | Selects the date expressible as date and time case of restriction context.date expressible as. |
| 4 | `DateExpressibleAsYearlessDate` | Selects the date expressible as yearless date case of restriction context.date expressible as. |
| 5 | `DateExpressibleAsYearlessOrFullDate` | Selects the date expressible as yearless or full date case of restriction context.date expressible as. |

## `ToolKitProtoRestrictionContext.PersonReachableAs`

Native enumeration selecting the restriction context.person reachable as setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `PersonReachableAsUnspecified` | Selects the person reachable as unspecified case of restriction context.person reachable as. |
| 1 | `PersonReachableAsContact` | Selects the person reachable as contact case of restriction context.person reachable as. |
| 2 | `PersonReachableAsPhone` | Selects the person reachable as phone case of restriction context.person reachable as. |
| 3 | `PersonReachableAsEmail` | Selects the person reachable as email case of restriction context.person reachable as. |
| 4 | `PersonReachableAsEmailOrPhone` | Selects the person reachable as email or phone case of restriction context.person reachable as. |

## `ToolKitProtoRestrictionContext.TextTypedWith.AutocorrectionType`

Native enumeration selecting the restriction context.text typed with.autocorrection type setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `AutocorrectionTypeDefault` | Selects the autocorrection type default case of restriction context.text typed with.autocorrection type. |
| 1 | `AutocorrectionTypeOn` | Selects the autocorrection type on case of restriction context.text typed with.autocorrection type. |
| 2 | `AutocorrectionTypeOff` | Selects the autocorrection type off case of restriction context.text typed with.autocorrection type. |

## `ToolKitProtoRestrictionContext.TextTypedWith.CapitalizationType`

Native enumeration selecting the restriction context.text typed with.capitalization type setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `CapitalizationTypeNone` | Selects the capitalization type none case of restriction context.text typed with.capitalization type. |
| 1 | `CapitalizationTypeWords` | Selects the capitalization type words case of restriction context.text typed with.capitalization type. |
| 2 | `CapitalizationTypeSentences` | Selects the capitalization type sentences case of restriction context.text typed with.capitalization type. |
| 3 | `CapitalizationTypeAllCharacters` | Selects the capitalization type all characters case of restriction context.text typed with.capitalization type. |

## `ToolKitProtoRestrictionContext.TextTypedWith.KeyboardType`

Native enumeration selecting the restriction context.text typed with.keyboard type setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `KeyboardTypeDefault` | Selects the keyboard type default case of restriction context.text typed with.keyboard type. |
| 1 | `KeyboardTypeAsciiCapable` | Selects the keyboard type ascii capable case of restriction context.text typed with.keyboard type. |
| 2 | `KeyboardTypeNumbersAndPunctuation` | Selects the keyboard type numbers and punctuation case of restriction context.text typed with.keyboard type. |
| 3 | `KeyboardTypeUrl` | Selects the keyboard type url case of restriction context.text typed with.keyboard type. |
| 4 | `KeyboardTypeNumberPad` | Selects the keyboard type number pad case of restriction context.text typed with.keyboard type. |
| 5 | `KeyboardTypePhonePad` | Selects the keyboard type phone pad case of restriction context.text typed with.keyboard type. |
| 6 | `KeyboardTypeNamePhonePad` | Selects the keyboard type name phone pad case of restriction context.text typed with.keyboard type. |
| 7 | `KeyboardTypeEmailAddress` | Selects the keyboard type email address case of restriction context.text typed with.keyboard type. |
| 8 | `KeyboardTypeDecimalPad` | Selects the keyboard type decimal pad case of restriction context.text typed with.keyboard type. |
| 9 | `KeyboardTypeTwitter` | Selects the keyboard type twitter case of restriction context.text typed with.keyboard type. |
| 10 | `KeyboardTypeWebSearch` | Selects the keyboard type web search case of restriction context.text typed with.keyboard type. |
| 11 | `KeyboardTypeAsciiCapableNumberPad` | Selects the keyboard type ascii capable number pad case of restriction context.text typed with.keyboard type. |

## `ToolKitProtoRuntimePlatform`

Native enumeration selecting the runtime platform setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `RuntimePlatformUnspecified` | Selects the runtime platform unspecified case of runtime platform. |
| 1 | `RuntimePlatformPhone` | Selects the runtime platform phone case of runtime platform. |
| 2 | `RuntimePlatformPad` | Selects the runtime platform pad case of runtime platform. |
| 3 | `RuntimePlatformMacintosh` | Selects the runtime platform macintosh case of runtime platform. |
| 4 | `RuntimePlatformWatch` | Selects the runtime platform watch case of runtime platform. |
| 5 | `RuntimePlatformTv` | Selects the runtime platform tv case of runtime platform. |
| 6 | `RuntimePlatformVision` | Selects the runtime platform vision case of runtime platform. |
| 7 | `RuntimePlatformaudioAccessory` | Selects the runtime platformaudio accessory case of runtime platform. |
| 8 | `RuntimePlatformother` | Selects the runtime platformother case of runtime platform. |

## `ToolKitProtoRuntimeRequirement.DeviceCapability.DeviceCapabilityType`

Native enumeration selecting the runtime requirement.device capability.device capability type setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `DeviceCapabilityTypePersonalHotspot` | Selects the device capability type personal hotspot case of runtime requirement.device capability.device capability type. |
| 1 | `DeviceCapabilityTypePosters` | Selects the device capability type posters case of runtime requirement.device capability.device capability type. |
| 2 | `DeviceCapabilityTypeCellularTelephony` | Selects the device capability type cellular telephony case of runtime requirement.device capability.device capability type. |
| 3 | `DeviceCapabilityTypeCellularData` | Selects the device capability type cellular data case of runtime requirement.device capability.device capability type. |
| 4 | `DeviceCapabilityTypeStageManager` | Selects the device capability type stage manager case of runtime requirement.device capability.device capability type. |
| 5 | `DeviceCapabilityTypeRemovingBackgrounds` | Selects the device capability type removing backgrounds case of runtime requirement.device capability.device capability type. |
| 6 | `DeviceCapabilityTypeAlwaysOnDisplay` | Selects the device capability type always on display case of runtime requirement.device capability.device capability type. |
| 7 | `DeviceCapabilityTypeVibration` | Selects the device capability type vibration case of runtime requirement.device capability.device capability type. |
| 8 | `DeviceCapabilityTypeBatteryChargeLimit` | Selects the device capability type battery charge limit case of runtime requirement.device capability.device capability type. |

## `ToolKitProtoRuntimeRequirement.DeviceState`

Native enumeration selecting the runtime requirement.device state setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `DeviceStateUnspecified` | Selects the device state unspecified case of runtime requirement.device state. |
| 1 | `DeviceStateUnlocked` | Selects the device state unlocked case of runtime requirement.device state. |
| 2 | `DeviceStateWritingToolsAvailable` | Selects the device state writing tools available case of runtime requirement.device state. |
| 3 | `DeviceStateUseModelAvailable` | Selects the device state use model available case of runtime requirement.device state. |
| 4 | `DeviceStatePhotosMemoriesAvailable` | Selects the device state photos memories available case of runtime requirement.device state. |
| 5 | `DeviceStateImagePlaygroundAvailable` | Selects the device state image playground available case of runtime requirement.device state. |
| 6 | `DeviceStateVisualIntelligenceCameraAvailable` | Selects the device state visual intelligence camera available case of runtime requirement.device state. |

## `ToolKitProtoSystemToolProtocol.AgentIntent.SupportedFeature`

Native enumeration selecting the system tool protocol.agent intent.supported feature setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `SupportedFeatureUnspecified` | Selects the supported feature unspecified case of system tool protocol.agent intent.supported feature. |
| 1 | `SupportedFeatureSystemAssistant` | Selects the supported feature system assistant case of system tool protocol.agent intent.supported feature. |
| 2 | `SupportedFeatureImagePlayground` | Selects the supported feature image playground case of system tool protocol.agent intent.supported feature. |
| 4 | `SupportedFeatureWritingTools` | Selects the supported feature writing tools case of system tool protocol.agent intent.supported feature. |
| 8 | `SupportedFeatureVisualIntelligence` | Selects the supported feature visual intelligence case of system tool protocol.agent intent.supported feature. |
| 16 | `SupportedFeatureShortcuts` | Selects the supported feature shortcuts case of system tool protocol.agent intent.supported feature. |

## `ToolKitProtoSystemToolProtocol.IntentSideEffect.Behavior.Kind`

Native enumeration selecting the system tool protocol.intent side effect.behavior.kind setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `KIND_UNKNOWN` | Selects the kind unknown case of system tool protocol.intent side effect.behavior.kind. |
| 1 | `KIND_CONFIRMATION` | Selects the kind confirmation case of system tool protocol.intent side effect.behavior.kind. |
| 2 | `KIND_CHOICE` | Selects the kind choice case of system tool protocol.intent side effect.behavior.kind. |

## `ToolKitProtoToolDefinition.Version1.AuthenticationPolicy`

Native enumeration selecting the tool definition.version1.authentication policy setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `AuthenticationPolicyUnspecified` | Selects the authentication policy unspecified case of tool definition.version1.authentication policy. |
| 1 | `AuthenticationPolicyNone` | Selects the authentication policy none case of tool definition.version1.authentication policy. |
| 2 | `AuthenticationPolicyRequiresAuthenticationOnOrigin` | Selects the authentication policy requires authentication on origin case of tool definition.version1.authentication policy. |
| 3 | `AuthenticationPolicyRequiresAuthenticationOnOriginAndRemote` | Selects the authentication policy requires authentication on origin and remote case of tool definition.version1.authentication policy. |

## `ToolKitProtoToolDefinition.Version1.Flag`

Native enumeration selecting the tool definition.version1.flag setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `FlagUnspecified` | Selects the flag unspecified case of tool definition.version1.flag. |
| 1 | `FlagOpensAppWhenRun` | Selects the flag opens app when run case of tool definition.version1.flag. |
| 2 | `FlagIsDiscontinued` | Selects the flag is discontinued case of tool definition.version1.flag. |
| 4 | `FlagIsUndiscoverable` | Selects the flag is undiscoverable case of tool definition.version1.flag. |
| 8 | `FlagDoesNotImplementPerform` | Selects the flag does not implement perform case of tool definition.version1.flag. |
| 16 | `FlagShowsOpenWhenRun` | Selects the flag shows open when run case of tool definition.version1.flag. |
| 32 | `FlagOutputHasSnippet` | Selects the flag output has snippet case of tool definition.version1.flag. |
| 64 | `FlagOutputProvidesDialog` | Selects the flag output provides dialog case of tool definition.version1.flag. |
| 128 | `FlagIsHomeResidentCompatible` | Selects the flag is home resident compatible case of tool definition.version1.flag. |

## `ToolKitProtoToolDefinition.Version1.Parameter.ParameterFlags`

Native enumeration selecting the tool definition.version1.parameter.parameter flags setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `ParameterFlagsUnspecified` | Selects the parameter flags unspecified case of tool definition.version1.parameter.parameter flags. |
| 1 | `ParameterFlagsHidden` | Selects the parameter flags hidden case of tool definition.version1.parameter.parameter flags. |
| 2 | `ParameterFlagsSynthesized` | Selects the parameter flags synthesized case of tool definition.version1.parameter.parameter flags. |

## `ToolKitProtoToolDefinition.Version1.ToolIcon.ToolSymbolIconStyle`

Native enumeration selecting the tool definition.version1.tool icon.tool symbol icon style setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `ToolSymbolIconStyleMulticolor` | Selects the tool symbol icon style multicolor case of tool definition.version1.tool icon.tool symbol icon style. |
| 1 | `ToolSymbolIconStyleTinted` | Selects the tool symbol icon style tinted case of tool definition.version1.tool icon.tool symbol icon style. |

## `ToolKitProtoToolDefinition.Version1.ToolType`

Native enumeration selecting the tool definition.version1.tool type setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `ToolTypeUnspecified` | Selects the tool type unspecified case of tool definition.version1.tool type. |
| 1 | `ToolTypeAppIntent` | Selects the tool type app intent case of tool definition.version1.tool type. |
| 2 | `ToolTypeSiriIntent` | Selects the tool type siri intent case of tool definition.version1.tool type. |
| 3 | `ToolTypeAction` | Selects the tool type action case of tool definition.version1.tool type. |
| 4 | `ToolTypeFlowTool` | Selects the tool type flow tool case of tool definition.version1.tool type. |

## `ToolKitProtoToolDefinition.Version1.VisibilityFlag`

Native enumeration selecting the tool definition.version1.visibility flag setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `VisibilityFlagUnspecified` | Selects the visibility flag unspecified case of tool definition.version1.visibility flag. |
| 1 | `VisibilityFlagVisibleForShortcuts` | Selects the visibility flag visible for shortcuts case of tool definition.version1.visibility flag. |
| 2 | `VisibilityFlagVisibleForAssistant` | Selects the visibility flag visible for assistant case of tool definition.version1.visibility flag. |
| 4 | `VisibilityFlagApproved` | Selects the visibility flag approved case of tool definition.version1.visibility flag. |

## `ToolKitProtoToolInvocationOptions.AccessLevel`

Native enumeration selecting the tool invocation options.access level setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `AccessLevelUnknown` | Selects the access level unknown case of tool invocation options.access level. |
| 1 | `AccessLevelHigh` | Selects the access level high case of tool invocation options.access level. |
| 2 | `AccessLevelLow` | Selects the access level low case of tool invocation options.access level. |

## `ToolKitProtoToolInvocationOptions.AssistantDismissalPolicy`

Native enumeration selecting the tool invocation options.assistant dismissal policy setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `AssistantDismissalPolicyUnknown` | Selects the assistant dismissal policy unknown case of tool invocation options.assistant dismissal policy. |
| 1 | `AssistantDismissalPolicyRetain` | Selects the assistant dismissal policy retain case of tool invocation options.assistant dismissal policy. |
| 2 | `AssistantDismissalPolicyDismiss` | Selects the assistant dismissal policy dismiss case of tool invocation options.assistant dismissal policy. |

## `ToolKitProtoToolInvocationOptions.ConfirmationConditions`

Native enumeration selecting the tool invocation options.confirmation conditions setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `ConfirmationConditionsUnknown` | Selects the confirmation conditions unknown case of tool invocation options.confirmation conditions. |
| 1 | `ConfirmationConditionsSkipAllSideEffectsConfirmation` | Selects the confirmation conditions skip all side effects confirmation case of tool invocation options.confirmation conditions. |
| 2 | `ConfirmationConditionsForceSideEffectsConfirmation` | Selects the confirmation conditions force side effects confirmation case of tool invocation options.confirmation conditions. |

## `ToolKitProtoToolInvocationOptions.InteractionMode`

Native enumeration selecting the tool invocation options.interaction mode setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `InteractionModeUnspecified` | Selects the interaction mode unspecified case of tool invocation options.interaction mode. |
| 1 | `InteractionModeDisplayForward` | Selects the interaction mode display forward case of tool invocation options.interaction mode. |
| 2 | `InteractionModeDisplayOnly` | Selects the interaction mode display only case of tool invocation options.interaction mode. |
| 3 | `InteractionModeVoiceOnly` | Selects the interaction mode voice only case of tool invocation options.interaction mode. |
| 4 | `InteractionModeVoiceForward` | Selects the interaction mode voice forward case of tool invocation options.interaction mode. |

## `ToolKitProtoToolInvocationOptions.InterfaceIdiom`

Native enumeration selecting the tool invocation options.interface idiom setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `InterfaceIdiomUnspecified` | Selects the interface idiom unspecified case of tool invocation options.interface idiom. |
| 1 | `InterfaceIdiomCarPlay` | Selects the interface idiom car play case of tool invocation options.interface idiom. |
| 2 | `InterfaceIdiomEyesFree` | Selects the interface idiom eyes free case of tool invocation options.interface idiom. |
| 3 | `InterfaceIdiomHomePod` | Selects the interface idiom home pod case of tool invocation options.interface idiom. |
| 4 | `InterfaceIdiomMac` | Selects the interface idiom mac case of tool invocation options.interface idiom. |
| 5 | `InterfaceIdiomAirPods` | Selects the interface idiom air pods case of tool invocation options.interface idiom. |
| 6 | `InterfaceIdiomPhone` | Selects the interface idiom phone case of tool invocation options.interface idiom. |
| 7 | `InterfaceIdiomPad` | Selects the interface idiom pad case of tool invocation options.interface idiom. |
| 8 | `InterfaceIdiomWatch` | Selects the interface idiom watch case of tool invocation options.interface idiom. |
| 9 | `InterfaceIdiomTv` | Selects the interface idiom tv case of tool invocation options.interface idiom. |
| 10 | `InterfaceIdiomVision` | Selects the interface idiom vision case of tool invocation options.interface idiom. |

## `ToolKitProtoTriggerDefinition.Version1.Flag`

Native enumeration selecting the trigger definition.version1.flag setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `FlagUnspecified` | Selects the flag unspecified case of trigger definition.version1.flag. |
| 1 | `FlagIsAllowedToRunAutomatically` | Selects the flag is allowed to run automatically case of trigger definition.version1.flag. |
| 2 | `FlagRequiresNotification` | Selects the flag requires notification case of trigger definition.version1.flag. |
| 4 | `FlagIsUserInitiated` | Selects the flag is user initiated case of trigger definition.version1.flag. |

## `ToolKitProtoTypeDefinition.Version1.Entity.AuthenticationPolicy`

Native enumeration selecting the type definition.version1.entity.authentication policy setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `AuthenticationPolicyUnspecified` | Selects the authentication policy unspecified case of type definition.version1.entity.authentication policy. |
| 1 | `AuthenticationPolicyNone` | Selects the authentication policy none case of type definition.version1.entity.authentication policy. |
| 2 | `AuthenticationPolicyRequiresAuthenticationOnOrigin` | Selects the authentication policy requires authentication on origin case of type definition.version1.entity.authentication policy. |
| 3 | `AuthenticationPolicyRequiresAuthenticationOnOriginAndRemote` | Selects the authentication policy requires authentication on origin and remote case of type definition.version1.entity.authentication policy. |

## `ToolKitProtoTypeDefinition.Version1.Entity.RuntimeFlags`

Native enumeration selecting the type definition.version1.entity.runtime flags setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `RuntimeFlagsUnspecified` | Selects the runtime flags unspecified case of type definition.version1.entity.runtime flags. |
| 1 | `RuntimeFlagsTransientAppEntity` | Selects the runtime flags transient app entity case of type definition.version1.entity.runtime flags. |

## `ToolKitProtoTypeDefinition.Version1.Enumeration.Kind`

Native enumeration selecting the type definition.version1.enumeration.kind setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `KindUnknown` | Selects the kind unknown case of type definition.version1.enumeration.kind. |
| 1 | `KindAppEnum` | Selects the kind app enum case of type definition.version1.enumeration.kind. |
| 2 | `KindActionEnum` | Selects the kind action enum case of type definition.version1.enumeration.kind. |
| 3 | `KindTriggerEnum` | Selects the kind trigger enum case of type definition.version1.enumeration.kind. |

## `ToolKitProtoTypeIdentifier.Primitive.MeasurementUnitType`

Native enumeration selecting the type identifier.primitive.measurement unit type setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `MeasurementUnitTypeUnspecified` | Selects the measurement unit type unspecified case of type identifier.primitive.measurement unit type. |
| 1 | `MeasurementUnitTypeLength` | Selects the measurement unit type length case of type identifier.primitive.measurement unit type. |
| 2 | `MeasurementUnitTypeMass` | Selects the measurement unit type mass case of type identifier.primitive.measurement unit type. |
| 3 | `MeasurementUnitTypeTemperature` | Selects the measurement unit type temperature case of type identifier.primitive.measurement unit type. |
| 4 | `MeasurementUnitTypeVolume` | Selects the measurement unit type volume case of type identifier.primitive.measurement unit type. |
| 5 | `MeasurementUnitTypeSpeed` | Selects the measurement unit type speed case of type identifier.primitive.measurement unit type. |
| 6 | `MeasurementUnitTypeEnergy` | Selects the measurement unit type energy case of type identifier.primitive.measurement unit type. |
| 7 | `MeasurementUnitTypeDuration` | Selects the measurement unit type duration case of type identifier.primitive.measurement unit type. |
| 8 | `MeasurementUnitTypeAcceleration` | Selects the measurement unit type acceleration case of type identifier.primitive.measurement unit type. |
| 9 | `MeasurementUnitTypeAngle` | Selects the measurement unit type angle case of type identifier.primitive.measurement unit type. |
| 10 | `MeasurementUnitTypeArea` | Selects the measurement unit type area case of type identifier.primitive.measurement unit type. |
| 11 | `MeasurementUnitTypeConcentrationMass` | Selects the measurement unit type concentration mass case of type identifier.primitive.measurement unit type. |
| 12 | `MeasurementUnitTypeDispersion` | Selects the measurement unit type dispersion case of type identifier.primitive.measurement unit type. |
| 13 | `MeasurementUnitTypeElectricCharge` | Selects the measurement unit type electric charge case of type identifier.primitive.measurement unit type. |
| 14 | `MeasurementUnitTypeElectricCurrent` | Selects the measurement unit type electric current case of type identifier.primitive.measurement unit type. |
| 15 | `MeasurementUnitTypeElectricPotentialDifference` | Selects the measurement unit type electric potential difference case of type identifier.primitive.measurement unit type. |
| 16 | `MeasurementUnitTypeElectricResistance` | Selects the measurement unit type electric resistance case of type identifier.primitive.measurement unit type. |
| 17 | `MeasurementUnitTypeFrequency` | Selects the measurement unit type frequency case of type identifier.primitive.measurement unit type. |
| 18 | `MeasurementUnitTypeFuelEfficiency` | Selects the measurement unit type fuel efficiency case of type identifier.primitive.measurement unit type. |
| 19 | `MeasurementUnitTypeIlluminance` | Selects the measurement unit type illuminance case of type identifier.primitive.measurement unit type. |
| 20 | `MeasurementUnitTypeInformationStorage` | Selects the measurement unit type information storage case of type identifier.primitive.measurement unit type. |
| 21 | `MeasurementUnitTypePower` | Selects the measurement unit type power case of type identifier.primitive.measurement unit type. |
| 22 | `MeasurementUnitTypePressure` | Selects the measurement unit type pressure case of type identifier.primitive.measurement unit type. |

## `ToolKitProtoTypedValue.PrimitiveValue.DateComponents.CalendarIdentifier`

Native enumeration selecting the typed value.primitive value.date components.calendar identifier setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `CalendarIdentifierUnspecified` | Selects the calendar identifier unspecified case of typed value.primitive value.date components.calendar identifier. |
| 1 | `CalendarIdentifierGregorian` | Selects the calendar identifier gregorian case of typed value.primitive value.date components.calendar identifier. |
| 2 | `CalendarIdentifierBuddhist` | Selects the calendar identifier buddhist case of typed value.primitive value.date components.calendar identifier. |
| 3 | `CalendarIdentifierChinese` | Selects the calendar identifier chinese case of typed value.primitive value.date components.calendar identifier. |
| 4 | `CalendarIdentifierCoptic` | Selects the calendar identifier coptic case of typed value.primitive value.date components.calendar identifier. |
| 5 | `CalendarIdentifierEthiopicAmeteMihret` | Selects the calendar identifier ethiopic amete mihret case of typed value.primitive value.date components.calendar identifier. |
| 6 | `CalendarIdentifierEthiopicAmeteAlem` | Selects the calendar identifier ethiopic amete alem case of typed value.primitive value.date components.calendar identifier. |
| 7 | `CalendarIdentifierHebrew` | Selects the calendar identifier hebrew case of typed value.primitive value.date components.calendar identifier. |
| 8 | `CalendarIdentifierIso8601` | Selects the calendar identifier iso8601 case of typed value.primitive value.date components.calendar identifier. |
| 9 | `CalendarIdentifierIndian` | Selects the calendar identifier indian case of typed value.primitive value.date components.calendar identifier. |
| 10 | `CalendarIdentifierIslamic` | Selects the calendar identifier islamic case of typed value.primitive value.date components.calendar identifier. |
| 11 | `CalendarIdentifierIslamicCivil` | Selects the calendar identifier islamic civil case of typed value.primitive value.date components.calendar identifier. |
| 12 | `CalendarIdentifierJapanese` | Selects the calendar identifier japanese case of typed value.primitive value.date components.calendar identifier. |
| 13 | `CalendarIdentifierPersian` | Selects the calendar identifier persian case of typed value.primitive value.date components.calendar identifier. |
| 14 | `CalendarIdentifierRepublicOfChina` | Selects the calendar identifier republic of china case of typed value.primitive value.date components.calendar identifier. |
| 15 | `CalendarIdentifierIslamicTabular` | Selects the calendar identifier islamic tabular case of typed value.primitive value.date components.calendar identifier. |
| 16 | `CalendarIdentifierIslamicUmmAlQura` | Selects the calendar identifier islamic umm al qura case of typed value.primitive value.date components.calendar identifier. |
| 17 | `CalendarIdentifierBangla` | Selects the calendar identifier bangla case of typed value.primitive value.date components.calendar identifier. |
| 18 | `CalendarIdentifierGujarati` | Selects the calendar identifier gujarati case of typed value.primitive value.date components.calendar identifier. |
| 19 | `CalendarIdentifierKannada` | Selects the calendar identifier kannada case of typed value.primitive value.date components.calendar identifier. |
| 20 | `CalendarIdentifierMalayalam` | Selects the calendar identifier malayalam case of typed value.primitive value.date components.calendar identifier. |
| 21 | `CalendarIdentifierMarathi` | Selects the calendar identifier marathi case of typed value.primitive value.date components.calendar identifier. |
| 22 | `CalendarIdentifierOdia` | Selects the calendar identifier odia case of typed value.primitive value.date components.calendar identifier. |
| 23 | `CalendarIdentifierTamil` | Selects the calendar identifier tamil case of typed value.primitive value.date components.calendar identifier. |
| 24 | `CalendarIdentifierTelugu` | Selects the calendar identifier telugu case of typed value.primitive value.date components.calendar identifier. |
| 25 | `CalendarIdentifierVikram` | Selects the calendar identifier vikram case of typed value.primitive value.date components.calendar identifier. |
| 26 | `CalendarIdentifierDangi` | Selects the calendar identifier dangi case of typed value.primitive value.date components.calendar identifier. |
| 27 | `CalendarIdentifierVietnamese` | Selects the calendar identifier vietnamese case of typed value.primitive value.date components.calendar identifier. |

## `ToolKitProtoTypedValue.PrimitiveValue.Decimal.Sign`

Native enumeration selecting the typed value.primitive value.decimal.sign setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `SignUnspecified` | Selects the sign unspecified case of typed value.primitive value.decimal.sign. |
| 1 | `SignMinus` | Selects the sign minus case of typed value.primitive value.decimal.sign. |
| 2 | `SignPlus` | Selects the sign plus case of typed value.primitive value.decimal.sign. |

## `ToolKitProtoTypedValue.PrimitiveValue.PaymentMethod.TypeEnum`

Native enumeration selecting the typed value.primitive value.payment method.type enum setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `TypeUnspecified` | Selects the type unspecified case of typed value.primitive value.payment method.type enum. |
| 1 | `TypeChecking` | Selects the type checking case of typed value.primitive value.payment method.type enum. |
| 2 | `TypeSavings` | Selects the type savings case of typed value.primitive value.payment method.type enum. |
| 3 | `TypeBrokerage` | Selects the type brokerage case of typed value.primitive value.payment method.type enum. |
| 4 | `TypeDebit` | Selects the type debit case of typed value.primitive value.payment method.type enum. |
| 5 | `TypeCredit` | Selects the type credit case of typed value.primitive value.payment method.type enum. |
| 6 | `TypePrepaid` | Selects the type prepaid case of typed value.primitive value.payment method.type enum. |
| 7 | `TypeStore` | Selects the type store case of typed value.primitive value.payment method.type enum. |
| 8 | `TypeApplePay` | Selects the type apple pay case of typed value.primitive value.payment method.type enum. |

## `ToolKitProtoTypedValue.PrimitiveValue.Person.Handle.TypeEnum`

Native enumeration selecting the typed value.primitive value.person.handle.type enum setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `TypeUnknown` | Selects the type unknown case of typed value.primitive value.person.handle.type enum. |
| 1 | `TypeEmailAddress` | Selects the type email address case of typed value.primitive value.person.handle.type enum. |
| 2 | `TypePhoneNumber` | Selects the type phone number case of typed value.primitive value.person.handle.type enum. |

## `ToolKitProtoTypedValue.PrimitiveValue.Placemark.TypeEnum`

Native enumeration selecting the typed value.primitive value.placemark.type enum setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `TypeUnknown` | Selects the type unknown case of typed value.primitive value.placemark.type enum. |
| 1 | `TypePlacemark` | Selects the type placemark case of typed value.primitive value.placemark.type enum. |
| 2 | `TypeCurrentLocation` | Selects the type current location case of typed value.primitive value.placemark.type enum. |

## `ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.CalendarMatchingPolicy`

Native enumeration selecting the typed value.primitive value.recurrence rule.calendar matching policy setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `CalendarMatchingPolicyUnspecified` | Selects the calendar matching policy unspecified case of typed value.primitive value.recurrence rule.calendar matching policy. |
| 1 | `CalendarMatchingPolicyNextTime` | Selects the calendar matching policy next time case of typed value.primitive value.recurrence rule.calendar matching policy. |
| 2 | `CalendarMatchingPolicyNextTimePreservingSmallerComponents` | Selects the calendar matching policy next time preserving smaller components case of typed value.primitive value.recurrence rule.calendar matching policy. |
| 3 | `CalendarMatchingPolicyPreviousTimePreservingSmallerComponents` | Selects the calendar matching policy previous time preserving smaller components case of typed value.primitive value.recurrence rule.calendar matching policy. |
| 4 | `CalendarMatchingPolicyStrict` | Selects the calendar matching policy strict case of typed value.primitive value.recurrence rule.calendar matching policy. |

## `ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.CalendarRepeatedTimePolicy`

Native enumeration selecting the typed value.primitive value.recurrence rule.calendar repeated time policy setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `CalendarRepeatedTimePolicyUnspecified` | Selects the calendar repeated time policy unspecified case of typed value.primitive value.recurrence rule.calendar repeated time policy. |
| 1 | `CalendarRepeatedTimePolicyFirst` | Selects the calendar repeated time policy first case of typed value.primitive value.recurrence rule.calendar repeated time policy. |
| 2 | `CalendarRepeatedTimePolicyLast` | Selects the calendar repeated time policy last case of typed value.primitive value.recurrence rule.calendar repeated time policy. |

## `ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.LocaleWeekday`

Native enumeration selecting the typed value.primitive value.recurrence rule.locale weekday setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `LocaleWeekdayUnspecified` | Selects the locale weekday unspecified case of typed value.primitive value.recurrence rule.locale weekday. |
| 1 | `LocaleWeekdayMonday` | Selects the locale weekday monday case of typed value.primitive value.recurrence rule.locale weekday. |
| 2 | `LocaleWeekdayTuesday` | Selects the locale weekday tuesday case of typed value.primitive value.recurrence rule.locale weekday. |
| 3 | `LocaleWeekdayWednesday` | Selects the locale weekday wednesday case of typed value.primitive value.recurrence rule.locale weekday. |
| 4 | `LocaleWeekdayThursday` | Selects the locale weekday thursday case of typed value.primitive value.recurrence rule.locale weekday. |
| 5 | `LocaleWeekdayFriday` | Selects the locale weekday friday case of typed value.primitive value.recurrence rule.locale weekday. |
| 6 | `LocaleWeekdaySaturday` | Selects the locale weekday saturday case of typed value.primitive value.recurrence rule.locale weekday. |
| 7 | `LocaleWeekdaySunday` | Selects the locale weekday sunday case of typed value.primitive value.recurrence rule.locale weekday. |

## `ToolKitProtoTypedValue.PrimitiveValue.RecurrenceRule.RecurrenceRuleFrequency`

Native enumeration selecting the typed value.primitive value.recurrence rule.recurrence rule frequency setting.

| Value | Native name | Semantic meaning |
|---:|---|---|
| 0 | `RecurrenceRuleFrequencyUnspecified` | Selects the recurrence rule frequency unspecified case of typed value.primitive value.recurrence rule.recurrence rule frequency. |
| 1 | `RecurrenceRuleFrequencyMinutely` | Selects the recurrence rule frequency minutely case of typed value.primitive value.recurrence rule.recurrence rule frequency. |
| 2 | `RecurrenceRuleFrequencyHourly` | Selects the recurrence rule frequency hourly case of typed value.primitive value.recurrence rule.recurrence rule frequency. |
| 3 | `RecurrenceRuleFrequencyDaily` | Selects the recurrence rule frequency daily case of typed value.primitive value.recurrence rule.recurrence rule frequency. |
| 4 | `RecurrenceRuleFrequencyWeekly` | Selects the recurrence rule frequency weekly case of typed value.primitive value.recurrence rule.recurrence rule frequency. |
| 5 | `RecurrenceRuleFrequencyMonthly` | Selects the recurrence rule frequency monthly case of typed value.primitive value.recurrence rule.recurrence rule frequency. |
| 6 | `RecurrenceRuleFrequencyYearly` | Selects the recurrence rule frequency yearly case of typed value.primitive value.recurrence rule.recurrence rule frequency. |

