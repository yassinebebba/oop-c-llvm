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
  %".4" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  %".6" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 1
  %".7" = load i32, i32* %".6"
  %".8" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 2
  %".9" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".8"
  %".10" = call i32 %".9"(%"Player"* %"player")
  %".11" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 3
  %".12" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".11"
  %".13" = call i32 %".12"(%"Player"* %"player")
  %".14" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 0
  %".15" = load i32, i32* %".14"
  %".16" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 1
  %".17" = load i32, i32* %".16"
  %".18" = add i32 %".15", %".17"
  %".19" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 2
  %".20" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".19"
  %".21" = call i32 %".20"(%"Player"* %"player")
  %".22" = getelementptr %"Player", %"Player"* %"player", i32 0, i32 3
  %".23" = load i32 (%"Player"*)*, i32 (%"Player"*)** %".22"
  %".24" = call i32 %".23"(%"Player"* %"player")
  %".25" = add i32 %".21", %".24"
  %".26" = load i8*, i8** %"fmt"
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".26", i32 %".5", i32 %".7", i32 %".10", i32 %".13", i32 %".18", i32 %".25")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [105 x i8] c"player.x = %d\0aplayer.y = %d\0aplayer.getx() = %d\0aplayer.gety() = %d\0aadd x + y = %d\0aadd getters x + y = %d\0a\00"