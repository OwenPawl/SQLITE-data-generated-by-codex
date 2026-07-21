# Tools.requirements protobuf structure

## Top-level wrapper

```text
Tools.requirements
└── field 1: repeated ToolKitProtoRuntimeRequirement
```

## Runtime requirement

```text
ToolKitProtoRuntimeRequirement
├── field 1: availabilityAnnotation : AvailabilityAnnotation
├── field 2: deviceCapability       : DeviceCapability
├── field 3: featureFlag            : FeatureFlag
└── field 4: deviceState            : DeviceState
```

`ToolKitProtoRuntimeRequirement` behaves like a oneof-style requirement wrapper.

## Availability annotation

```text
AvailabilityAnnotation
├── field 1: platform           : ToolKitProtoRuntimePlatform
├── field 2: introducingVersion : RuntimePlatformVersion
├── field 3: deprecatingVersion : RuntimePlatformVersion
└── field 4: obsoletingVersion  : RuntimePlatformVersion
```

## Runtime platform version

```text
RuntimePlatformVersion
├── field 1: major      : varint
├── field 2: minor      : varint
├── field 3: patch      : varint
└── field 4: isWildcard : bool
```

## Feature flag

```text
FeatureFlag
├── field 1: domain  : string
├── field 2: feature : string
└── field 3: value   : bool
```

## Device capability

```text
DeviceCapability
├── field 1: mobileGestalt        : MobileGestalt
└── field 2: deviceCapabilityType : DeviceCapabilityType
```

## MobileGestalt

```text
MobileGestalt
├── field 1: key   : string
└── field 2: value : bool
```

If `MobileGestalt.value` is omitted, it means the default bool value, `false`.

## ToolKitProtoRuntimePlatform enum

```text
0 = invalid / throws
1 = RuntimePlatformPhone          -> iOS
2 = RuntimePlatformPad            -> iPadOS
3 = RuntimePlatformMacintosh      -> macOS
4 = RuntimePlatformWatch          -> watchOS
5 = RuntimePlatformTv             -> tvOS
6 = RuntimePlatformVision         -> visionOS
7 = RuntimePlatformaudioAccessory -> Audio Accessor
8 = RuntimePlatformother          -> Unknown
```

## DeviceCapabilityType enum

```text
0 = DeviceCapabilityTypePersonalHotspot
1 = DeviceCapabilityTypePosters
2 = DeviceCapabilityTypeCellularTelephony
3 = DeviceCapabilityTypeCellularData
4 = DeviceCapabilityTypeStageManager
5 = DeviceCapabilityTypeRemovingBackgrounds
6 = DeviceCapabilityTypeAlwaysOnDisplay
7 = DeviceCapabilityTypeVibration
8 = DeviceCapabilityTypeBatteryChargeLimit
```

## DeviceState enum

```text
0 = DeviceStateUnspecified
1 = DeviceStateUnlocked
2 = DeviceStateWritingToolsAvailable
3 = DeviceStateUseModelAvailable
4 = DeviceStatePhotosMemoriesAvailable
5 = DeviceStateImagePlaygroundAvailable
6 = DeviceStateVisualIntelligenceCameraAvailable
```

## Raw decode shapes

```text
1 { 1 { ... } } = availabilityAnnotation
1 { 2 { ... } } = deviceCapability
1 { 3 { ... } } = featureFlag
1 { 4: N }      = deviceState
```

## Mental model

```text
Tools.requirements =
[
  availability/platform/version requirement,
  device capability requirement,
  feature flag requirement,
  device state requirement,
  ...
]
```
