// Program: VoiceShortcutClient
// Function: init
// Entry: 2087e90d8


/* VoiceShortcutClient.LaunchServicesSnapshot.State.init(bundleId: Swift.String,
   persistentIdentifier: __C.LSPersistentIdentifier) ->
   VoiceShortcutClient.LaunchServicesSnapshot.State */

State VoiceShortcutClient::LaunchServicesSnapshot::State::init
                (undefined8 *param_1,State param_2,undefined8 param_3,undefined8 param_4)

{
  *param_1 = param_2.unknown;
  param_1[1] = param_3;
  param_1[2] = param_4;
  return (State)param_2.unknown;
}


