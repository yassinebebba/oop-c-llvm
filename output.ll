; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

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
  store i8* getelementptr ([49 x i8], [49 x i8]* @".str.2", i64 0, i64 0), i8** %"fmt"
  %".10" = load i16, i16* %"x"
  %".11" = sext i16 %".10" to i32
  %".12" = load i8*, i8** %"fmt"
  %".13" = load i32*, i32** %"t"
  %".14" = load i32, i32* %"a"
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".11", i32* %".13", i32 %".14", [7 x i8]* @".str.3")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [4 x i8] c"abc\00"
@".str.2" = private unnamed_addr constant [49 x i8] c"%d %s %d %s\0a(IGNORE need fix null-termination)->\00"
@".str.3" = internal constant [7 x i8] c"asdsad\00"