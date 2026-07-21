// Program: ToolKit
// Function: $init
// Entry: 296912600


/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */
/* ToolKit.EntityDefinition.RuntimeFlags.init(protobuf:
   [ToolKit.ToolKitProtoTypeDefinition.Version1.Entity.RuntimeFlags]) throws ->
   ToolKit.EntityDefinition.RuntimeFlags */

RuntimeFlags ToolKit::EntityDefinition::RuntimeFlags::_init(ulong *param_1,long param_2)

{
  code *pcVar1;
  undefined *puVar2;
  undefined8 *puVar3;
  long lVar4;
  ulong *puVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  
  lVar4 = _DAT_2c019f118;
  lVar7 = *(long *)(param_2 + 0x10);
  if (lVar7 == 0) {
    FUN_298075e00(param_2);
    lVar4 = _DAT_2c019f118;
  }
  else {
    FUN_29687ae74(0,lVar7,0);
    lVar8 = *(long *)(param_2 + 0x10);
    lVar9 = 0x20;
    do {
      if (lVar8 == 0) {
                    /* WARNING: Does not return */
        pcVar1 = (code *)SoftwareBreakpoint(1,0x2969127f0);
        (*pcVar1)();
      }
      if (*(char *)(param_2 + lVar9) != '\x01') {
        puVar2 = &DAT_2c4e462a0;
        ___swift_instantiateConcreteTypeFromMangledNameV2(&DAT_2c4e462a0,&DAT_296cfe3f8);
        puVar3 = (undefined8 *)&DAT_2c4e462a8;
        FUN_2968e9658(&DAT_2c4e462a8,&DAT_2c4e462a0,&DAT_296cfe3f8);
        FUN_298075d90(puVar2,puVar3,0,0);
        *puVar3 = &__type_metadata_for_ToolKit_EntityDefinition_RuntimeFlags;
        (**(code **)(*(long *)(puVar2 + -8) + 0x68))(puVar3,*_DAT_2c017f3a0,puVar2);
        FUN_2980761e0();
        FUN_298076090(lVar4);
        FUN_298075e00();
        return (RuntimeFlags)param_2;
      }
      uVar6 = *(ulong *)(lVar4 + 0x10);
      if (*(ulong *)(lVar4 + 0x18) >> 1 <= uVar6) {
        FUN_29687ae74(1 < *(ulong *)(lVar4 + 0x18),uVar6 + 1,1);
      }
      *(ulong *)(lVar4 + 0x10) = uVar6 + 1;
      *(undefined8 *)(lVar4 + 0x20 + uVar6 * 8) = 1;
      lVar8 = lVar8 + -1;
      lVar9 = lVar9 + 1;
      lVar7 = lVar7 + -1;
    } while (lVar7 != 0);
    FUN_298075e00(param_2);
  }
  lVar7 = *(long *)(lVar4 + 0x10);
  if (lVar7 == 0) {
    uVar6 = 0;
  }
  else {
    uVar6 = 0;
    puVar5 = (ulong *)(lVar4 + 0x20);
    do {
      uVar6 = *puVar5 | uVar6;
      lVar7 = lVar7 + -1;
      puVar5 = puVar5 + 1;
    } while (lVar7 != 0);
  }
  FUN_298075e00();
  *param_1 = uVar6;
  return (RuntimeFlags)lVar4;
}


