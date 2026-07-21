// Program: VoiceShortcutClient
// Function: $partial
// Entry: 2087ce140


/* static VoiceShortcutClient.LinkSnapshot.partial(_: Swift.Set<Swift.String>,
   failIfContainerNotFound: Swift.Bool) async throws -> VoiceShortcutClient.LinkSnapshot */

LinkSnapshot
VoiceShortcutClient::LinkSnapshot::_partial
          (Set<String> param_1,bool failIfContainerNotFound,LinkSnapshot param_3)

{
  code *pcVar1;
  LinkSnapshot LVar2;
  ulong uVar3;
  undefined1 uVar4;
  long *plVar5;
  long unaff_x22;
  ulong unaff_x30;
  
  uVar4 = SUB81(param_3.unknown,0);
  uVar3 = (ulong)failIfContainerNotFound;
  ::_OUTLINED_FUNCTION_10();
  plVar5 = (long *)(ulong)DAT_208839164;
  *(undefined1 *)(unaff_x22 + 0x38) = uVar4;
  *(undefined **)(unaff_x22 + 0x18) = param_1.unknown;
  *(ulong *)(unaff_x22 + 0x20) = uVar3;
  FUN_21004fed0();
  *(long **)(unaff_x22 + 0x28) = plVar5;
  *plVar5 = unaff_x22;
  plVar5[1] = (long)FUN_2087ce1dc;
  if (((unaff_x30 ^ unaff_x30 << 1) >> 0x3e & 1) != 0) {
                    /* WARNING: Does not return */
    pcVar1 = (code *)SoftwareBreakpoint(0xc471,0x2087ce1d8);
    (*pcVar1)();
  }
  LVar2 = _complete((undefined *)(unaff_x22 + 0x10));
  return (LinkSnapshot)LVar2.unknown;
}


