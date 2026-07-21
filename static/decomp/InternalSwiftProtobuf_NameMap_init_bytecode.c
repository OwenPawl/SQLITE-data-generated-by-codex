// Program: InternalSwiftProtobuf
// Function: init
// Entry: 1d7053fe4


/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */
/* InternalSwiftProtobuf._NameMap.init(bytecode: Swift.StaticString) ->
   InternalSwiftProtobuf._NameMap */

_NameMap InternalSwiftProtobuf::_NameMap::init(StaticString bytecode)

{
  undefined8 uVar1;
  long lVar2;
  long lVar3;
  undefined *puVar4;
  long *in_x8;
  undefined1 auStack_70 [16];
  undefined *local_60;
  
  lVar3 = 0;
  FUN_1d70540d4();
  ::_OUTLINED_FUNCTION_19();
  lVar2 = _DAT_1e023e428;
  *(long *)(lVar3 + 0x10) = _DAT_1e023e428;
  *in_x8 = lVar3;
  uVar1 = _DAT_1e023d240;
  ::_OUTLINED_FUNCTION_7();
  lVar3 = lVar2;
  FUN_1d807e490(lVar2,uVar1);
  in_x8[1] = lVar3;
  FUN_1d7037238();
  ::_OUTLINED_FUNCTION_11();
  in_x8[2] = lVar3;
  ::_OUTLINED_FUNCTION_11();
  in_x8[3] = lVar3;
  in_x8[4] = lVar2;
  in_x8[5] = lVar2;
  puVar4 = &DAT_1eed17978;
  ::_OUTLINED_FUNCTION_19();
  *(undefined8 *)(puVar4 + 0x10) = 0;
  local_60 = puVar4;
  FUN_1d7054c9c(FUN_1d7058aa8,auStack_70,bytecode.unknown);
  FUN_1d8063ed0();
  return SUB82(puVar4,0);
}


