; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"Foo" = type {i32, i32}
declare i32 @"printf"(i8* %".1", ...)

@"T" = dso_local global i32 1
@"d" = dso_local global i8 0
define i32 @"main"()
{
entry:
  %"x" = alloca %"Foo"
  %".2" = getelementptr inbounds %"Foo", %"Foo"* %"x", i32 0, i32 0
  store i32 10, i32* %".2"
  %".4" = getelementptr %"Foo", %"Foo"* %"x", i32 0, i32 1
  store i32 20, i32* %".4"
  %"fmt" = alloca i8*
  store i8* getelementptr ([4 x i8], [4 x i8]* @".str.1", i64 0, i64 0), i8** %"fmt"
  %".7" = getelementptr %"Foo", %"Foo"* %"x", i32 0, i32 1
  %".8" = load i32, i32* %".7"
  %".9" = load i8*, i8** %"fmt"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [4 x i8] c"%d\0a\00"