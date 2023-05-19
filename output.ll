; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"class.Player" = type {i16, i16, i64, i32, i32}
%"class.Target" = type {i32, %"class.Player"}
declare i32 @"printf"(i8* %".1", ...)

define void @"_ZN6Player6PlayerEPS_il"(%"class.Player"* %"this", i32 %"x", i64 %"y")
{
entry:
  %".5" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 3
  store i32 %"x", i32* %".5"
  %".7" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 4
  %".8" = trunc i64 %"y" to i32
  store i32 %".8", i32* %".7"
  ret void
}

define i32 @"_ZN6Player5get_xEPS_"(%"class.Player"* %"this")
{
entry:
  %".3" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 3
  %".4" = load i32, i32* %".3"
  %".5" = call i32 @"_ZN6Player5get_yEPS_"(%"class.Player"* %"this")
  %".6" = add i32 %".4", %".5"
  %".7" = add i32 %".6", 2
  ret i32 %".7"
}

define i32 @"_ZN6Player5get_yEPS_"(%"class.Player"* %"this")
{
entry:
  %".3" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 4
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define i8* @"_ZN6Player8__repr__EPS_"(%"class.Player"* %"this")
{
entry:
  ret i8* getelementptr ([25 x i8], [25 x i8]* @".str.1", i64 0, i64 0)
}

@".str.1" = private unnamed_addr constant [25 x i8] c"This is a Player object\0a\00"
define i32 @"_ZN6Target5get_aEPS_"(%"class.Target"* %"this")
{
entry:
  %".3" = getelementptr %"class.Target", %"class.Target"* %"this", i32 0, i32 0
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define void @"_ZN6Target6TargetEPS_"(%"class.Target"* %"this")
{
entry:
  ret void
}

define i32 @"main"()
{
entry:
  %"player" = alloca %"class.Player"
  %".2" = sext i32 2 to i64
  call void @"_ZN6Player6PlayerEPS_il"(%"class.Player"* %"player", i32 1, i64 %".2")
  %"fmt" = alloca i8*
  store i8* getelementptr ([105 x i8], [105 x i8]* @".str.2", i64 0, i64 0), i8** %"fmt"
  %".5" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 3
  %".6" = load i32, i32* %".5"
  %".7" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 4
  %".8" = load i32, i32* %".7"
  %".9" = call i32 @"_ZN6Player5get_xEPS_"(%"class.Player"* %"player")
  %".10" = call i32 @"_ZN6Player5get_yEPS_"(%"class.Player"* %"player")
  %".11" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 3
  %".12" = load i32, i32* %".11"
  %".13" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 4
  %".14" = load i32, i32* %".13"
  %".15" = add i32 %".12", %".14"
  %".16" = call i32 @"_ZN6Player5get_xEPS_"(%"class.Player"* %"player")
  %".17" = call i32 @"_ZN6Player5get_yEPS_"(%"class.Player"* %"player")
  %".18" = add i32 %".16", %".17"
  %".19" = load i8*, i8** %"fmt"
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".6", i32 %".8", i32 %".9", i32 %".10", i32 %".15", i32 %".18")
  %".21" = call i8* @"_ZN6Player8__repr__EPS_"(%"class.Player"* %"player")
  %".22" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([3 x i8], [3 x i8]* @".str.3", i64 0, i64 0), i8* %".21")
  ret i32 0
}

@".str.2" = private unnamed_addr constant [105 x i8] c"player.x = %d\0aplayer.y = %d\0aplayer.getx() = %d\0aplayer.gety() = %d\0aadd x + y = %d\0aadd getters x + y = %d\0a\00"
@".str.3" = private unnamed_addr constant [3 x i8] c"%s\00"