// Program: ToolKit
// Function: shouldFilterOut
// Entry: 296b4c9c8


/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */
/* ToolKit.ToolDefinitionQuery.shouldFilterOut(model: ToolKit.ToolDefinition) -> Swift.Bool */

bool ToolKit::ToolDefinitionQuery::shouldFilterOut(ToolDefinition model,ToolDefinitionQuery param_2)

{
  ulong uVar1;
  ToolDefinition *pTVar2;
  ulong uVar3;
  undefined8 uVar4;
  ulong uVar5;
  ulong uVar6;
  ToolDefinition *__return_storage_ptr__;
  undefined8 uVar7;
  char cVar8;
  code *pcVar9;
  bool bVar10;
  bool bVar11;
  long lVar12;
  ulong uVar13;
  ulong uVar14;
  ulong uVar15;
  undefined8 *puVar16;
  undefined8 uVar17;
  undefined8 *puVar18;
  ToolDefinition *pTVar19;
  long unaff_x20;
  ulong uVar20;
  ulong uVar21;
  
  cVar8 = *(char *)(unaff_x20 + 0x80);
  if (cVar8 == -1) {
    return false;
  }
  uVar1 = *(ulong *)(unaff_x20 + 0x50);
  uVar5 = *(ulong *)(unaff_x20 + 0x58);
  pTVar2 = *(ToolDefinition **)(unaff_x20 + 0x60);
  uVar6 = *(ulong *)(unaff_x20 + 0x68);
  uVar3 = *(ulong *)(unaff_x20 + 0x70);
  __return_storage_ptr__ = *(ToolDefinition **)(unaff_x20 + 0x78);
  lVar12 = 0;
  ToolDefinition::typeMetadataAccessor(__return_storage_ptr__);
  uVar21 = 0;
  lVar12 = *(long *)(model.id.str + *(int *)(lVar12 + 0x5c));
  uVar20 = *(ulong *)(lVar12 + 0x10);
  uVar15 = _DAT_2c019f118;
  do {
    puVar18 = (undefined8 *)(lVar12 + uVar21 * 0x40);
    do {
      puVar16 = puVar18;
      if (uVar20 == uVar21) {
        lVar12 = *(long *)(uVar15 + 0x10);
        puVar18 = (undefined8 *)(uVar15 + 0x30);
        goto LAB_296b4cafc;
      }
      if (uVar20 <= uVar21) {
                    /* WARNING: Does not return */
        pcVar9 = (code *)SoftwareBreakpoint(1,0x296b4cbf8);
        (*pcVar9)();
      }
      uVar21 = uVar21 + 1;
      puVar18 = puVar16 + 8;
    } while (*(char *)(puVar16 + 0xb) != '\0');
    uVar4 = puVar16[6];
    uVar7 = puVar16[7];
    uVar17 = puVar16[8];
    uVar13 = uVar15;
    FUN_298076060();
    uVar14 = uVar15;
    if ((uVar13 & 1) == 0) {
      uVar14 = 0;
      FUN_296870dd4(0,*(long *)(uVar15 + 0x10) + 1,1,uVar15);
    }
    uVar13 = *(ulong *)(uVar14 + 0x10);
    uVar15 = uVar14;
    if (*(ulong *)(uVar14 + 0x18) >> 1 <= uVar13) {
      uVar15 = (ulong)(1 < *(ulong *)(uVar14 + 0x18));
      FUN_296870dd4(uVar15,uVar13 + 1,1,uVar14);
    }
    *(ulong *)(uVar15 + 0x10) = uVar13 + 1;
    puVar18 = (undefined8 *)(uVar15 + 0x20 + uVar13 * 0x18);
    *puVar18 = uVar4;
    puVar18[1] = uVar7;
    puVar18[2] = uVar17;
  } while( true );
LAB_296b4cafc:
  bVar10 = lVar12 != 0;
  lVar12 = lVar12 + -1;
  if (!bVar10) {
LAB_296b4cbc8:
    FUN_298075e00(uVar15);
    return bVar10;
  }
  uVar21 = puVar18[-2];
  uVar20 = puVar18[-1];
  pTVar19 = (ToolDefinition *)*puVar18;
  switch(cVar8) {
  default:
    if ((uVar21 == uVar1 && uVar20 == uVar5) && pTVar19 == pTVar2) goto LAB_296b4cbc0;
    goto LAB_296b4cbc8;
  case '\x01':
    bVar11 = uVar1 <= uVar21;
    if ((uVar21 == uVar1) && (bVar11 = uVar5 <= uVar20, uVar20 == uVar5)) {
      bVar11 = pTVar2 <= pTVar19;
    }
    break;
  case '\x02':
    bVar11 = uVar21 <= uVar1;
    if ((uVar1 == uVar21) && (bVar11 = uVar20 <= uVar5, uVar5 == uVar20)) {
      bVar11 = pTVar19 <= pTVar2;
    }
    break;
  case '\x03':
    bVar11 = uVar1 <= uVar6;
    if ((uVar6 == uVar1) && (bVar11 = uVar5 <= uVar3, uVar3 == uVar5)) {
      bVar11 = pTVar2 <= __return_storage_ptr__;
    }
    if (!bVar11) {
                    /* WARNING: Does not return */
      pcVar9 = (code *)SoftwareBreakpoint(1,0x296b4cbfc);
      (*pcVar9)();
    }
    bVar11 = uVar1 <= uVar21;
    if ((uVar21 == uVar1) && (bVar11 = uVar5 <= uVar20, uVar20 == uVar5)) {
      bVar11 = pTVar2 <= pTVar19;
    }
    if (!bVar11) goto LAB_296b4cbc8;
    bVar11 = uVar21 <= uVar6;
    if ((uVar6 == uVar21) && (bVar11 = uVar20 <= uVar3, uVar3 == uVar20)) {
      bVar11 = pTVar19 <= __return_storage_ptr__;
    }
    break;
  case '\x04':
    goto LAB_296b4cbc0;
  }
  if (!bVar11) goto LAB_296b4cbc8;
LAB_296b4cbc0:
  puVar18 = puVar18 + 3;
  goto LAB_296b4cafc;
}


