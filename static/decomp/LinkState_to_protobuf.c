// Program: ToolKit
// Function: $protobuf
// Entry: 29691cfb4


/* (extension in ToolKit):VoiceShortcutClient.LinkSnapshot.State.protobuf(useCase:
   VoiceShortcutClient.ProtobufUseCase) throws -> ToolKit.ToolKitProtoLinkSnapshot.State */

State (extension_ToolKit)::LinkSnapshot::State::_protobuf(ProtobufUseCase useCase)

{
  ulong uVar1;
  ulong uVar2;
  State SVar3;
  ulong in_x1;
  ulong uVar4;
  ulong *in_x8;
  
  uVar1 = (ulong)(byte)useCase.value;
  FUN_2980b24f0();
  uVar2 = uVar1;
  uVar4 = in_x1;
  FUN_2980b2500();
  SVar3 = ::ToolKit::ToolKitProtoLinkSnapshot::State::typeMetadataAccessor();
  FUN_298076950((long)in_x8 + (long)*(int *)(SVar3.unknown + 0x18));
  *in_x8 = uVar1;
  in_x8[1] = in_x1;
  in_x8[2] = uVar2;
  in_x8[3] = uVar4;
  return (State)SVar3.unknown;
}


