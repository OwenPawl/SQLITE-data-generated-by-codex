// Program: ToolKit
// Function: is
// Entry: 296b4c310


/* static ToolKit.ToolVisibilityFilter.is(ToolKit.ToolVisibilityFlag) ->
   ToolKit.ToolVisibilityFilter */

ToolVisibilityFilter
ToolKit::ToolVisibilityFilter::is(ToolVisibilityFlag param_1,ToolVisibilityFilter param_2)

{
  undefined8 *in_x8;
  
  *in_x8 = *(undefined8 *)param_1.rawValue;
  return (ToolVisibilityFilter)param_1.rawValue;
}


