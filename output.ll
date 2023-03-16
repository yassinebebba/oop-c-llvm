; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

@"T" = dso_local global i32 1
@"d" = dso_local global i8 0
define i32 @"main"()
{
entry:
  %"x" = alloca i16
  %".2" = trunc i32 -12 to i16
  store i16 %".2", i16* %"x"
  %"a" = alloca i32
  %".4" = load i16, i16* %"x"
  %".5" = sext i16 %".4" to i32
  store i32 %".5", i32* %"a"
  %"t" = alloca i32*
  %".7" = bitcast i8* getelementptr ([4 x i8], [4 x i8]* @".str.1", i64 0, i64 0) to i32*
  store i32* %".7", i32** %"t"
  %"fmt" = alloca i8*
  store i8* getelementptr ([57 x i8], [57 x i8]* @".str.2", i64 0, i64 0), i8** %"fmt"
  %".10" = load i8*, i8** %"fmt"
  %".11" = load i16, i16* %"x"
  %".12" = load i32*, i32** %"t"
  %".13" = load i32, i32* %"a"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".10", i16 %".11", i32* %".12", i32 %".13", [10 x i8]* @".str.3")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [4 x i8] c"abc\00"
@".str.2" = private unnamed_addr constant [57 x i8] c"%d %s %d %s\0a(IGNORE need fix null-termination)->sada\5c\22sa\00"
@".str.3" = private unnamed_addr constant [10 x i8] c"asdsad132\00"