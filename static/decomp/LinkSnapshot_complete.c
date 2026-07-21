// Program: VoiceShortcutClient
// Function: $complete
// Entry: 2087ce46c


/* WARNING: Removing unreachable block (ram,0x0002087ce4cc) */
/* static VoiceShortcutClient.LinkSnapshot.complete() async throws ->
   VoiceShortcutClient.LinkSnapshot */

LinkSnapshot VoiceShortcutClient::LinkSnapshot::_complete(LinkSnapshot param_1)

{
  code *pcVar1;
  long lVar2;
  ulong uVar3;
  long extraout_x8;
  long extraout_x8_00;
  long unaff_x22;
  ulong unaff_x30;
  
  ::_OUTLINED_FUNCTION_10();
  ::_OUTLINED_FUNCTION_5();
  *(undefined **)(unaff_x22 + 0x18) = param_1.unknown;
  lVar2 = 0;
  FUN_21004d980();
  *(long *)(unaff_x22 + 0x20) = lVar2;
  lVar2 = *(long *)(lVar2 + -8);
  *(long *)(unaff_x22 + 0x28) = lVar2;
  uVar3 = *(long *)(lVar2 + 0x40) + 0xfU & 0xfffffffffffffff0;
  FUN_21004fed0();
  ::_OUTLINED_FUNCTION_5();
  *(ulong *)(unaff_x22 + 0x30) = uVar3;
  pcVar1 = FUN_2087ce544;
  if (extraout_x8_00 != extraout_x8) {
                    /* WARNING: Subroutine does not return */
    FUN_21004c960();
  }
  if (((unaff_x30 ^ unaff_x30 << 1) >> 0x3e & 1) == 0) {
    FUN_21004ff00(FUN_2087ce544,0,0);
    return (LinkSnapshot)pcVar1;
  }
                    /* WARNING: Does not return */
  pcVar1 = (code *)SoftwareBreakpoint(0xc471,0x2087ce53c);
  (*pcVar1)();
}


