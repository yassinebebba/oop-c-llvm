; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"(i32 %"a")
{
entry:
  %"x" = alloca i16
  %".3" = trunc i32 45 to i16
  store i16 %".3", i16* %"x"
  %".5" = trunc i32 45 to i16
  store i16 %".5", i16* %"x"
  %"fmt" = alloca i8*
  store i8* getelementptr ([43 x i8], [43 x i8]* @".str.1", i32 0, i32 0), i8** %"fmt"
  %".8" = load i8*, i8** %"fmt"
  %".9" = load i16, i16* %"x"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".8", i16 %".9", [7 x i8]* @".str.2")
  ret i32 0
}

@".str.1" = internal constant [43 x i8] c"%d %s\0a(IGNORE need fix null-termination)->\00"
@".str.2" = internal constant [7 x i8] c"asdsad\00"