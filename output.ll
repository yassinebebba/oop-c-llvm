; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"Player" = type {i32, i32, i32 (%"Player"*)*, i32 (%"Player"*)*, void (%"Player"*, i32, i32)*}
declare i32 @"printf"(i8* %".1", ...)

@"T" = dso_local global i32 1
@"d" = dso_local global i8 0
define i32 @"Player.getx"(%"Player"* %"this")
{
entry:
  %".3" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 0
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define i32 @"Player.gety"(%"Player"* %"this")
{
entry:
  %".3" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 1
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define void @"Player.Player"(%"Player"* %"this", i32 %"x", i32 %"y")
{
entry:
  %".5" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 2
  store i32 (%"Player"*)* @"Player.getx", i32 (%"Player"*)** %".5"
  %".7" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 3
  store i32 (%"Player"*)* @"Player.gety", i32 (%"Player"*)** %".7"
  %".9" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 0
  store i32 %"x", i32* %".9"
  %".11" = getelementptr %"Player", %"Player"* %"this", i32 0, i32 1
  store i32 %"y", i32* %".11"
  ret void
}

define i32 @"main"()
{
entry:
  %"player" = alloca %"Player"
  call void @"Player.Player"(%"Player"* %"player", i32 1, i32 2)
  %"fmt" = alloca i8*
  store i8* getelementptr ([105 x i8], [105 x i8]* @".str.1", i64 0, i64 0), i8** %"fmt"
  %".4" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([5 x i8], [5 x i8]* @".str.2", i64 0, i64 0))
  %".5" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 0
  %".6" = load i32, i32* %".5"
  %".7" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 1
  %".8" = load i32, i32* %".7"
  %".9" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 2
  %".10" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".9"
  %".11" = call i32 %".10"(%"Player"* %"player")
  %".12" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 3
  %".13" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".12"
  %".14" = call i32 %".13"(%"Player"* %"player")
  %".15" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 0
  %".16" = load i32, i32* %".15"
  %".17" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 1
  %".18" = load i32, i32* %".17"
  %".19" = add i32 %".16", %".18"
  %".20" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 2
  %".21" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".20"
  %".22" = call i32 %".21"(%"Player"* %"player")
  %".23" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 3
  %".24" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".23"
  %".25" = call i32 %".24"(%"Player"* %"player")
  %".26" = add i32 %".22", %".25"
  %".27" = load i8*, i8** %"fmt"
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %".6", i32 %".8", i32 %".11", i32 %".14", i32 %".19", i32 %".26")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [105 x i8] c"player.x = %d\0aplayer.y = %d\0aplayer.getx() = %d\0aplayer.gety() = %d\0aadd x + y = %d\0aadd getters x + y = %d\0a\00"
@".str.2" = private unnamed_addr constant [5 x i8] c"hey\0a\00"