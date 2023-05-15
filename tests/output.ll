; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"a" = alloca i16
  %".2" = trunc i32 2 to i16
  store i16 %".2", i16* %"a"
  %".4" = load i16, i16* %"a"
  store i16 %".4", i16* %"a"
  %".6" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.1", i64 0, i64 0), i32 2)
  ret i32 0
}

@".str.1" = private unnamed_addr constant [8 x i8] c"a = %d\0a\00"