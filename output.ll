; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca i16
  %".2" = trunc i32 45 to i16
  store i16 %".2", i16* %"x"
  %"t" = alloca i32*
  %".4" = bitcast i8* getelementptr ([4 x i8], [4 x i8]* @".str.1", i64 0, i64 0) to i32*
  store i32* %".4", i32** %"t"
  %"fmt" = alloca i8*
  store i8* getelementptr ([46 x i8], [46 x i8]* @".str.2", i64 0, i64 0), i8** %"fmt"
  %".7" = load i8*, i8** %"fmt"
  %".8" = load i16, i16* %"x"
  %".9" = load i32*, i32** %"t"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".7", i16 %".8", i32* %".9", [7 x i8]* @".str.3")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [4 x i8] c"abc\00"
@".str.2" = private unnamed_addr constant [46 x i8] c"%d %s %s\0a(IGNORE need fix null-termination)->\00"
@".str.3" = internal constant [7 x i8] c"asdsad\00"