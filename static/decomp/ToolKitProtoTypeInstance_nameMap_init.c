// Program: ToolKit
// Function: FUN_296c5be9c
// Entry: 296c5be9c


void FUN_296c5be9c(undefined8 param_1,long *param_2,code *param_3,undefined8 param_4,
                  undefined8 param_5)

{
  code *pcVar1;
  long lVar2;
  long lVar3;
  ulong unaff_x30;
  
  if (*param_2 != -1) {
    FUN_298076080(param_2,param_5);
  }
  lVar2 = 0;
  (*param_3)();
  lVar3 = lVar2;
  ___swift_project_value_buffer();
  if (((unaff_x30 ^ unaff_x30 << 1) >> 0x3e & 1) != 0) {
                    /* WARNING: Does not return */
    pcVar1 = (code *)SoftwareBreakpoint(0xc471,0x296c5bf28);
    (*pcVar1)();
  }
                    /* WARNING: Could not recover jumptable at 0x000296c5bf2c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*(long *)(lVar2 + -8) + 0x10))(param_1,lVar3,lVar2);
  return;
}


