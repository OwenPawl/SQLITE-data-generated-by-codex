// Program: ToolKit
// Function: $decodeMessage
// Entry: 296bd5bd8


/* WARNING: Removing unreachable block (ram,0x000296bd5c7c) */
/* WARNING: Removing unreachable block (ram,0x000296bd5c6c) */
/* WARNING: Removing unreachable block (ram,0x000296bd5c4c) */
/* WARNING: Removing unreachable block (ram,0x000296bd5c5c) */
/* WARNING: Removing unreachable block (ram,0x000296bd5c3c) */
/* WARNING: Removing unreachable block (ram,0x000296bd5c8c) */
/* ToolKit.ToolKitProtoTypeInstance.decodeMessage<A where A: InternalSwiftProtobuf.Decoder>(decoder:
   inout A) throws -> () */

void ToolKit::ToolKitProtoTypeInstance::_decodeMessage
               (undefined *decoder,ToolKitProtoTypeInstance param_2)

{
  undefined1 in_ZR;
  undefined1 *puVar1;
  long unaff_x21;
  
  ::_OUTLINED_FUNCTION_30();
  while( true ) {
    _OUTLINED_FUNCTION_182();
    FUN_2980769d0();
    if ((unaff_x21 != 0) || (::_OUTLINED_FUNCTION_91(), (bool)in_ZR)) break;
    puVar1 = decoder + -1;
    in_ZR = puVar1 == (undefined1 *)0x6;
    if (puVar1 < &LAB_00000007) {
      in_ZR = puVar1 == (undefined1 *)0x6;
      switch(puVar1) {
      default:
        ::_OUTLINED_FUNCTION_28();
        FUN_296bd5cac();
        break;
      case (undefined1 *)0x1:
        ::_OUTLINED_FUNCTION_28();
        FUN_296bd5fd4();
        break;
      case (undefined1 *)0x2:
        ::_OUTLINED_FUNCTION_28();
        FUN_296bd6304();
        break;
      case (undefined1 *)0x3:
        ::_OUTLINED_FUNCTION_28();
        FUN_296bd6634();
        break;
      case (undefined1 *)0x4:
        ::_OUTLINED_FUNCTION_28();
        FUN_296bd6964();
        break;
      case (undefined1 *)0x5:
        ::_OUTLINED_FUNCTION_28();
        FUN_296bd6c90();
        break;
      case (undefined1 *)0x6:
        ::_OUTLINED_FUNCTION_28();
        FUN_296bd6fc4();
      }
    }
  }
  return;
}


