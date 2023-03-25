; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"class.Player" = type {i16, i16, i64, i32, i32}
%"class.Target" = type {i32, %"class.Player"}
declare i32 @"printf"(i8* %".1", ...)

@"T" = dso_local global i32 1
@"d" = dso_local global i8 0
define void @"_ZN6Player6PlayerEPS_ii"(%"class.Player"* %"this", i32 %"x", i32 %"y")
{
entry:
  %".5" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 3
  store i32 %"x", i32* %".5"
  %".7" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 4
  store i32 %"y", i32* %".7"
  ret void
}

define i32 @"_ZN6Player4getxEPS_"(%"class.Player"* %"this")
{
entry:
  %".3" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 3
  %".4" = load i32, i32* %".3"
  %".5" = call i32 @"_ZN6Player4getyEPS_"(%"class.Player"* %"this")
  %".6" = add i32 %".4", %".5"
  %".7" = add i32 %".6", 2
  ret i32 %".7"
}

define i32 @"_ZN6Player4getyEPS_"(%"class.Player"* %"this")
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
define i32 @"_ZN6Target4getaEPS_"(%"class.Target"* %"this")
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
  call void @"_ZN6Player6PlayerEPS_ii"(%"class.Player"* %"player", i32 1, i32 2)
  %"target" = alloca %"class.Target"
  call void @"_ZN6Target6TargetEPS_"(%"class.Target"* %"target")
  %"a" = alloca i64
  %".4" = trunc i32 62 to i64
  store i64 %".4", i64* %"a"
  %".6" = call i32 @"_ZN6Target4getaEPS_"(%"class.Target"* %"target")
  %".7" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.2", i64 0, i64 0), i32 %".6")
  %"fmt" = alloca i8*
  store i8* getelementptr ([105 x i8], [105 x i8]* @".str.3", i64 0, i64 0), i8** %"fmt"
  %".9" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([5 x i8], [5 x i8]* @".str.4", i64 0, i64 0))
  %".10" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 3
  %".11" = load i32, i32* %".10"
  %".12" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 4
  %".13" = load i32, i32* %".12"
  %".14" = call i32 @"_ZN6Player4getxEPS_"(%"class.Player"* %"player")
  %".15" = call i32 @"_ZN6Player4getyEPS_"(%"class.Player"* %"player")
  %".16" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 3
  %".17" = load i32, i32* %".16"
  %".18" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 4
  %".19" = load i32, i32* %".18"
  %".20" = add i32 %".17", %".19"
  %".21" = call i32 @"_ZN6Player4getxEPS_"(%"class.Player"* %"player")
  %".22" = call i32 @"_ZN6Player4getyEPS_"(%"class.Player"* %"player")
  %".23" = add i32 %".21", %".22"
  %".24" = load i8*, i8** %"fmt"
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %".11", i32 %".13", i32 %".14", i32 %".15", i32 %".20", i32 %".23")
  %".26" = call i8* @"_ZN6Player8__repr__EPS_"(%"class.Player"* %"player")
  %".27" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([3 x i8], [3 x i8]* @".str.5", i64 0, i64 0), i8* %".26")
  ret i32 0
}

@".str.2" = private unnamed_addr constant [8 x i8] c"hey %d\0a\00"
@".str.3" = private unnamed_addr constant [105 x i8] c"player.x = %d\0aplayer.y = %d\0aplayer.getx() = %d\0aplayer.gety() = %d\0aadd x + y = %d\0aadd getters x + y = %d\0a\00"
@".str.4" = private unnamed_addr constant [5 x i8] c"hey\0a\00"
@".str.5" = private unnamed_addr constant [3 x i8] c"%s\00"