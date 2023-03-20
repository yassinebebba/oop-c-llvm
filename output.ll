; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"class.Player" = type {i32, i32, void (%"class.Player"*, i32, i32)*, i32 (%"class.Player"*)*, i32 (%"class.Player"*)*, i8* (%"class.Player"*)*, void (%"class.Player"*, i32, i32)*}
%"class.Target" = type {i32, i32 (%"class.Target"*)*, void (%"class.Target"*)*}
declare i32 @"printf"(i8* %".1", ...)

@"T" = dso_local global i32 1
@"d" = dso_local global i8 0
define i32 @"_ZN6Player4getxEPS_"(%"class.Player"* %"this")
{
entry:
  %".3" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 0
  %".4" = load i32, i32* %".3"
  %".5" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 4
  %".6" = load i32 (%"class.Player"*)*, i32 (%"class.Player"*)** %".5"
  %".7" = call i32 %".6"(%"class.Player"* %"this")
  %".8" = add i32 %".4", %".7"
  ret i32 %".8"
}

define i32 @"_ZN6Player4getyEPS_"(%"class.Player"* %"this")
{
entry:
  %".3" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 1
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define i8* @"_ZN6Player8__repr__EPS_"(%"class.Player"* %"this")
{
entry:
  ret i8* getelementptr ([25 x i8], [25 x i8]* @".str.1", i64 0, i64 0)
}

@".str.1" = private unnamed_addr constant [25 x i8] c"This is a Player object\0a\00"
define void @"_ZN6Player6PlayerEPS_ii"(%"class.Player"* %"this", i32 %"x", i32 %"y")
{
entry:
  %".5" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 3
  store i32 (%"class.Player"*)* @"_ZN6Player4getxEPS_", i32 (%"class.Player"*)** %".5"
  %".7" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 4
  store i32 (%"class.Player"*)* @"_ZN6Player4getyEPS_", i32 (%"class.Player"*)** %".7"
  %".9" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 5
  store i8* (%"class.Player"*)* @"_ZN6Player8__repr__EPS_", i8* (%"class.Player"*)** %".9"
  %".11" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 0
  store i32 %"x", i32* %".11"
  %".13" = getelementptr %"class.Player", %"class.Player"* %"this", i32 0, i32 1
  store i32 %"y", i32* %".13"
  ret void
}

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
  %".3" = getelementptr %"class.Target", %"class.Target"* %"this", i32 0, i32 1
  store i32 (%"class.Target"*)* @"_ZN6Target4getaEPS_", i32 (%"class.Target"*)** %".3"
  ret void
}

define i32 @"main"()
{
entry:
  %"player" = alloca %"class.Player"
  call void @"_ZN6Player6PlayerEPS_ii"(%"class.Player"* %"player", i32 1, i32 2)
  %"target" = alloca %"class.Target"
  call void @"_ZN6Target6TargetEPS_"(%"class.Target"* %"target")
  %".4" = getelementptr %"class.Target", %"class.Target"* %"target", i32 0, i32 1
  %".5" = load i32 (%"class.Target"*)*, i32 (%"class.Target"*)** %".4"
  %".6" = call i32 %".5"(%"class.Target"* %"target")
  %".7" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.2", i64 0, i64 0), i32 %".6")
  %"fmt" = alloca i8*
  store i8* getelementptr ([105 x i8], [105 x i8]* @".str.3", i64 0, i64 0), i8** %"fmt"
  %".9" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([5 x i8], [5 x i8]* @".str.4", i64 0, i64 0))
  %".10" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 0
  %".11" = load i32, i32* %".10"
  %".12" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 1
  %".13" = load i32, i32* %".12"
  %".14" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 3
  %".15" = load i32 (%"class.Player"*)*, i32 (%"class.Player"*)** %".14"
  %".16" = call i32 %".15"(%"class.Player"* %"player")
  %".17" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 4
  %".18" = load i32 (%"class.Player"*)*, i32 (%"class.Player"*)** %".17"
  %".19" = call i32 %".18"(%"class.Player"* %"player")
  %".20" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 0
  %".21" = load i32, i32* %".20"
  %".22" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 1
  %".23" = load i32, i32* %".22"
  %".24" = add i32 %".21", %".23"
  %".25" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 3
  %".26" = load i32 (%"class.Player"*)*, i32 (%"class.Player"*)** %".25"
  %".27" = call i32 %".26"(%"class.Player"* %"player")
  %".28" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 4
  %".29" = load i32 (%"class.Player"*)*, i32 (%"class.Player"*)** %".28"
  %".30" = call i32 %".29"(%"class.Player"* %"player")
  %".31" = add i32 %".27", %".30"
  %".32" = load i8*, i8** %"fmt"
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".32", i32 %".11", i32 %".13", i32 %".16", i32 %".19", i32 %".24", i32 %".31")
  %".34" = getelementptr %"class.Player", %"class.Player"* %"player", i32 0, i32 5
  %".35" = load i8* (%"class.Player"*)*, i8* (%"class.Player"*)** %".34"
  %".36" = call i8* %".35"(%"class.Player"* %"player")
  %".37" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([3 x i8], [3 x i8]* @".str.5", i64 0, i64 0), i8* %".36")
  ret i32 0
}

@".str.2" = private unnamed_addr constant [8 x i8] c"hey %d\0a\00"
@".str.3" = private unnamed_addr constant [105 x i8] c"player.x = %d\0aplayer.y = %d\0aplayer.getx() = %d\0aplayer.gety() = %d\0aadd x + y = %d\0aadd getters x + y = %d\0a\00"
@".str.4" = private unnamed_addr constant [5 x i8] c"hey\0a\00"
@".str.5" = private unnamed_addr constant [3 x i8] c"%s\00"