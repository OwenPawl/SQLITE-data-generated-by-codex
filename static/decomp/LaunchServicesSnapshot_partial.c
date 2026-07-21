// Program: VoiceShortcutClient
// Function: $partial
// Entry: 2087eb060


/* static VoiceShortcutClient.LaunchServicesSnapshot.partial(_: Swift.Set<Swift.String>,
   failIfContainerNotFound: Swift.Bool) async throws -> VoiceShortcutClient.LaunchServicesSnapshot
    */

LaunchServicesSnapshot
VoiceShortcutClient::LaunchServicesSnapshot::_partial
          (Set<String> param_1,bool failIfContainerNotFound,LaunchServicesSnapshot param_3)

{
  long unaff_x22;
  
  *(char *)(unaff_x22 + 0x29) = (char)param_3.unknown;
  *(undefined **)(unaff_x22 + 0x30) = param_1.unknown;
  *(ulong *)(unaff_x22 + 0x38) = (ulong)failIfContainerNotFound;
  ::_OUTLINED_FUNCTION_4();
  return (LaunchServicesSnapshot)param_1.unknown;
}


