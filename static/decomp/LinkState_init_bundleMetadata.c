// Program: VoiceShortcutClient
// Function: init
// Entry: 2087cbfd0


/* VoiceShortcutClient.LinkSnapshot.State.init(bundleMetadata: __C.LNRegisteredBundleMetadata) ->
   VoiceShortcutClient.LinkSnapshot.State */

State VoiceShortcutClient::LinkSnapshot::State::init(LNRegisteredBundleMetadata *bundleMetadata)

{
  LNRegisteredBundleMetadata *pLVar1;
  LNRegisteredBundleMetadata *pLVar2;
  LNRegisteredBundleMetadata *pLVar3;
  undefined8 in_x1;
  undefined8 uVar4;
  undefined8 *in_x8;
  
  pLVar1 = bundleMetadata;
  FUN_21001af80();
  FUN_21004f880();
  pLVar2 = pLVar1;
  FUN_21004e040();
  uVar4 = in_x1;
  FUN_21004ceb0(pLVar1);
  pLVar1 = bundleMetadata;
  FUN_21001e2c0();
  FUN_21004f880();
  pLVar3 = pLVar1;
  FUN_21004d4f0();
  FUN_21004ceb0(pLVar1);
  FUN_21004ceb0();
  *in_x8 = pLVar2;
  in_x8[1] = in_x1;
  in_x8[2] = pLVar3;
  in_x8[3] = uVar4;
  return (State)bundleMetadata;
}


