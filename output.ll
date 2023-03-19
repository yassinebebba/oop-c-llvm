; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"Player" = type {i32, i32, i32 (%"Player"*)*, i32 (%"Player"*)*, i8* (%"Player"*)*, void (%"Player"*, i32, i32)*}
%"Target" = type {i32, i32 (%"Target"*)*, void (%"Target"*)*}
declare i32 @"printf"(i8* %".1", ...)

@"T" = dso_local global i32 1
@"d" = dso_local global i8 0
define i32 @"Player.getx"(%"Player"* %"this")
{
entry:
  %".3" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 0
  %".4" = load i32, i32* %".3"
  %".5" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 3
  %".6" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".5"
  %".7" = call i32 %".6"(%"Player"* %"this")
  %".8" = add i32 %".4", %".7"
  ret i32 %".8"
}

define i32 @"Player.gety"(%"Player"* %"this")
{
entry:
  %".3" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 1
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define i8* @"Player.__repr__"(%"Player"* %"this")
{
entry:
  ret i8* getelementptr ([25 x i8], [25 x i8]* @".str.1", i64 0, i64 0)
}

@".str.1" = private unnamed_addr constant [25 x i8] c"This is a Player object\0a\00"
define void @"Player.Player"(%"Player"* %"this", i32 %"x", i32 %"y")
{
entry:
  %".5" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 2
  store i32 (%"Player"*)* @"Player.getx", i32 (%"Player"*)** %".5"
  %".7" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 3
  store i32 (%"Player"*)* @"Player.gety", i32 (%"Player"*)** %".7"
  %".9" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 4
  store i8* (%"Player"*)* @"Player.__repr__", i8* (%"Player"*)** %".9"
  %".11" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 0
  store i32 %"x", i32* %".11"
  %".13" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 1
  store i32 %"y", i32* %".13"
  ret void
}

define i32 @"Target.geta"(%"Target"* %"this")
{
entry:
  %".3" = getelementptr %"Target", %"Target"* %"this", i32 0, i32 0
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define void @"Target.Target"(%"Target"* %"this")
{
entry:
  %".3" = getelementptr %"Target", %"Target"* %"this", i32 0, i32 1
  store i32 (%"Target"*)* @"Target.geta", i32 (%"Target"*)** %".3"
  ret void
}

define i32 @"main"()
{
entry:
  %"player" = alloca %"Player"
  call void @"Player.Player"(%"Player"* %"player", i32 1, i32 2)
  %"target" = alloca %"Target"
  call void @"Target.Target"(%"Target"* %"target")
  %".4" = getelementptr %"Target", %"Target"* %"target", i32 0, i32 1
  %".5" = load i32 (%"Target"*)*, i32 (%"Target"*)** %".4"
  %".6" = call i32 %".5"(%"Target"* %"target")
  %".7" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.2", i64 0, i64 0), i32 %".6")
  %"fmt" = alloca i8*
  store i8* getelementptr ([105 x i8], [105 x i8]* @".str.3", i64 0, i64 0), i8** %"fmt"
  %".9" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([5 x i8], [5 x i8]* @".str.4", i64 0, i64 0))
  %".10" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 0
  %".11" = load i32, i32* %".10"
  %".12" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 1
  %".13" = load i32, i32* %".12"
  %".14" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 2
  %".15" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".14"
  %".16" = call i32 %".15"(%"Player"* %"player")
  %".17" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 3
  %".18" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".17"
  %".19" = call i32 %".18"(%"Player"* %"player")
  %".20" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 0
  %".21" = load i32, i32* %".20"
  %".22" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 1
  %".23" = load i32, i32* %".22"
  %".24" = add i32 %".21", %".23"
  %".25" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 2
  %".26" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".25"
  %".27" = call i32 %".26"(%"Player"* %"player")
  %".28" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 3
  %".29" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".28"
  %".30" = call i32 %".29"(%"Player"* %"player")
  %".31" = add i32 %".27", %".30"
  %".32" = load i8*, i8** %"fmt"
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".32", i32 %".11", i32 %".13", i32 %".16", i32 %".19", i32 %".24", i32 %".31")
  %".34" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 4
  %".35" = load i8* (%"Player"*)*, i8* (%"Player"*)** %".34"
  %".36" = call i8* %".35"(%"Player"* %"player")
  %".37" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([3 x i8], [3 x i8]* @".str.5", i64 0, i64 0), i8* %".36")
  ret i32 0
}

@".str.2" = private unnamed_addr constant [8 x i8] c"hey %d\0a\00"
@".str.3" = private unnamed_addr constant [105 x i8] c"player.x = %d\0aplayer.y = %d\0aplayer.getx() = %d\0aplayer.gety() = %d\0aadd x + y = %d\0aadd getters x + y = %d\0a\00"
@".str.4" = private unnamed_addr constant [5 x i8] c"hey\0a\00"
@".str.5" = private unnamed_addr constant [3 x i8] c"%s\00"