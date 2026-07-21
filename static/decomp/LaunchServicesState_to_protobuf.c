// Program: ToolKit
// Function: protobuf
// Entry: 29691c60c


/* (extension in ToolKit):VoiceShortcutClient.LaunchServicesSnapshot.State.protobuf(useCase:
   VoiceShortcutClient.ProtobufUseCase) -> ToolKit.ToolKitProtoLaunchServicesSnapshot.State */

State (extension_ToolKit)::LaunchServicesSnapshot::State::protobuf(ProtobufUseCase useCase)

{
  ulong uVar1;
  ulong uVar2;
  ulong uVar3;
  State SVar4;
  ulong in_x1;
  ulong uVar5;
  ulong *in_x8;
  
  uVar1 = (ulong)(byte)useCase.value;
  FUN_2980b27d0();
  uVar2 = uVar1;
  uVar5 = in_x1;
  FUN_2980b27b0();
  uVar3 = uVar2;
  FUN_298074220();
  FUN_298075be0(uVar2);
  SVar4 = ::ToolKit::ToolKitProtoLaunchServicesSnapshot::State::typeMetadataAccessor();
  FUN_298076950((long)in_x8 + (long)*(int *)(SVar4.unknown + 0x18));
  *in_x8 = uVar1;
  in_x8[1] = in_x1;
  in_x8[2] = uVar3;
  in_x8[3] = uVar5;
  return (State)SVar4.unknown;
}


