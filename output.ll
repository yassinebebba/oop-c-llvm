; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"Foo" = type {i32, i32, void (%"Foo"*, i32, i32)*}
declare i32 @"printf"(i8* %".1", ...)

@"T" = dso_local global i32 1
@"d" = dso_local global i8 0
define void @"Foo.Foo"(%"Foo"* %"this", i32 %"i", i32 %"d")
{
entry:
  %".5" = getelementptr %"Foo", %"Foo"* %"this", i32 0, i32 0
  store i32 %"i", i32* %".5"
  %".7" = getelementptr %"Foo", %"Foo"* %"this", i32 0, i32 1
  store i32 %"d", i32* %".7"
  ret void
}

define i32 @"main"()
{
entry:
  %"x" = alloca %"Foo"
  call void @"Foo.Foo"(%"Foo"* %"x", i32 2, i32 2)
  %"fmt" = alloca i8*
  store i8* getelementptr ([7 x i8], [7 x i8]* @".str.1", i64 0, i64 0), i8** %"fmt"
  %".4" = getelementptr %"Foo", %"Foo"* %"x", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  %".6" = getelementptr %"Foo", %"Foo"* %"x", i32 0, i32 1
  %".7" = load i32, i32* %".6"
  %".8" = getelementptr %"Foo", %"Foo"* %"x", i32 0, i32 0
  %".9" = load i32, i32* %".8"
  %".10" = add i32 %".7", %".9"
  %".11" = load i8*, i8** %"fmt"
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".5", i32 %".10")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [7 x i8] c"%d %d\0a\00"