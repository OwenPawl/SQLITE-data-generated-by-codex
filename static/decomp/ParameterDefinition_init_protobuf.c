// Program: ToolKit
// Function: $init
// Entry: 296b18570


/* WARNING: Removing unreachable block (ram,0x000296b188ac) */
/* WARNING: Removing unreachable block (ram,0x000296b18830) */
/* WARNING: Removing unreachable block (ram,0x000296b18900) */
/* WARNING: Removing unreachable block (ram,0x000296b18908) */
/* WARNING: Removing unreachable block (ram,0x000296b187d8) */
/* WARNING: Removing unreachable block (ram,0x000296b1883c) */
/* WARNING: Removing unreachable block (ram,0x000296b18854) */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */
/* ToolKit.ParameterDefinition.init(protobuf: ToolKit.ToolKitProtoToolDefinition.Version1.Parameter)
   throws -> ToolKit.ParameterDefinition */

void ToolKit::ParameterDefinition::_init
               (ParameterDefinition *__return_storage_ptr__,Parameter_conflict protobuf)

{
  ulong *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  byte bVar8;
  char *pcVar9;
  char *pcVar10;
  undefined8 *extraout_x8;
  undefined8 extraout_x8_00;
  long extraout_x8_01;
  long extraout_x8_02;
  long extraout_x8_03;
  Parameter_conflict *__return_storage_ptr___00;
  long extraout_x8_04;
  long extraout_x8_05;
  long extraout_x8_06;
  long lVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  long unaff_x21;
  long lVar14;
  long lVar15;
  byte *pbVar16;
  ulong uVar17;
  ulong uVar18;
  undefined8 unaff_x30;
  undefined8 in_stack_00000008;
  undefined8 uStack0000000000000058;
  long local_40;
  undefined8 uStack_38;
  undefined8 uStack_30;
  undefined8 uStack_28;
  undefined8 local_20;
  undefined8 uStack_18;
  undefined8 local_10;
  
  pcVar9 = protobuf.key.str;
  ::_OUTLINED_FUNCTION_39();
  uStack0000000000000058 = unaff_x30;
  ::_OUTLINED_FUNCTION_74();
  ::_OUTLINED_FUNCTION_36();
  ::_OUTLINED_FUNCTION_20();
  (*_DAT_2c770b588)();
  ::_OUTLINED_FUNCTION_24();
  ::_OUTLINED_FUNCTION_55();
  ::_OUTLINED_FUNCTION_36();
  ::_OUTLINED_FUNCTION_20();
  (*_DAT_2c770b588)();
  ::_OUTLINED_FUNCTION_24();
  ::_OUTLINED_FUNCTION_27();
  ::_OUTLINED_FUNCTION_36();
  ::_OUTLINED_FUNCTION_20();
  (*_DAT_2c770b588)();
  lVar14 = _DAT_2c019f118;
  uVar2 = *(undefined8 *)pcVar9;
  uVar5 = *(undefined8 *)(pcVar9 + 8);
  uVar3 = *(undefined8 *)(pcVar9 + 0x10);
  uVar6 = *(undefined8 *)(pcVar9 + 0x18);
  uVar4 = *(undefined8 *)(pcVar9 + 0x38);
  uVar7 = *(undefined8 *)(pcVar9 + 0x40);
  lVar15 = *(long *)(pcVar9 + 0x30);
  lVar11 = *(long *)(lVar15 + 0x10);
  if (lVar11 == 0) {
    uVar18 = *(ulong *)(_DAT_2c019f118 + 0x10);
    FUN_298075e10();
    FUN_298075e10(uVar6);
    FUN_298075e10(uVar7);
    if (uVar18 == 0) {
      uVar17 = 0;
      goto LAB_296b18740;
    }
  }
  else {
    _OUTLINED_FUNCTION_169();
    local_40 = extraout_x8_03;
    FUN_298075e10();
    FUN_298075e10(uVar6);
    FUN_298075e10(uVar7);
    FUN_29687af50(0,lVar11,0);
    pbVar16 = (byte *)(lVar15 + 0x20);
    uVar17 = *(ulong *)(local_40 + 0x10);
    do {
      bVar8 = *pbVar16;
      uVar18 = uVar17 + 1;
      if (*(ulong *)(local_40 + 0x18) >> 1 <= uVar17) {
        ::_OUTLINED_FUNCTION_15();
        FUN_29687af50();
      }
      *(ulong *)(local_40 + 0x10) = uVar18;
      *(ulong *)(local_40 + uVar17 * 8 + 0x20) = (ulong)bVar8;
      lVar11 = lVar11 + -1;
      lVar14 = local_40;
      pbVar16 = pbVar16 + 1;
      uVar17 = uVar18;
    } while (lVar11 != 0);
  }
  uVar17 = 0;
  lVar11 = 0x20;
  do {
    puVar1 = (ulong *)(lVar14 + lVar11);
    lVar11 = lVar11 + 8;
    uVar17 = *puVar1 | uVar17;
    uVar18 = uVar18 - 1;
  } while (uVar18 != 0);
LAB_296b18740:
  FUN_298075e00(lVar14);
  lVar11 = 0;
  ToolKitProtoToolDefinition::Version1::Parameter::typeMetadataAccessor(__return_storage_ptr___00);
  ::_OUTLINED_FUNCTION_19((long)*(int *)(lVar11 + 0x28));
  FUN_2968e9610(pcVar9 + extraout_x8_04,extraout_x8_01 - extraout_x8_02);
  FUN_296884988();
  ::_OUTLINED_FUNCTION_65();
  FUN_2980b26b0(extraout_x8_01 - extraout_x8_02);
  if (unaff_x21 == 0) {
    uVar12 = *(undefined8 *)(pcVar9 + 0x20);
    FUN_296b1d6e4();
    FUN_298075e10();
    FUN_2980b2b40();
    ::_OUTLINED_FUNCTION_64((long)*(int *)(lVar11 + 0x2c));
    pcVar10 = pcVar9 + extraout_x8_05;
    FUN_2968e9610(pcVar10,extraout_x8_01);
    FUN_296b1d738();
    FUN_2980b26a0(&local_20,extraout_x8_01,
                  &__type_metadata_for_ToolKit_ParameterDefinition_ToolMetadata,pcVar10);
    uVar13 = *(undefined8 *)(pcVar9 + 0x28);
    FUN_296b1d78c();
    FUN_298075e10();
    FUN_2980b2b40();
    ::_OUTLINED_FUNCTION_60((long)*(int *)(lVar11 + 0x30));
    pcVar9 = pcVar9 + extraout_x8_06;
    FUN_2968e9610(pcVar9,extraout_x8_00);
    FUN_296b1d7e0();
    FUN_2980b26a0(&local_40,extraout_x8_00,
                  &__type_metadata_for_ToolKit_ParameterDefinition_BooleanMetadata,pcVar9);
    ::_OUTLINED_FUNCTION_4();
    extraout_x8[10] = uStack_38;
    extraout_x8[9] = local_40;
    *extraout_x8 = uVar2;
    extraout_x8[1] = uVar5;
    extraout_x8[2] = uVar3;
    extraout_x8[3] = uVar6;
    extraout_x8[4] = uVar4;
    extraout_x8[5] = uVar7;
    extraout_x8[6] = uVar17;
    extraout_x8[7] = in_stack_00000008;
    extraout_x8[8] = uVar12;
    extraout_x8[0xc] = uStack_28;
    extraout_x8[0xb] = uStack_30;
    extraout_x8[0xe] = uStack_18;
    extraout_x8[0xd] = local_20;
    extraout_x8[0xf] = local_10;
    extraout_x8[0x10] = uVar13;
  }
  else {
    ::_OUTLINED_FUNCTION_4();
    FUN_298075e00(uVar5);
    FUN_298075e00(uVar6);
    FUN_298075e00(uVar7);
  }
  ::_OUTLINED_FUNCTION_38(uStack0000000000000058);
  return;
}


