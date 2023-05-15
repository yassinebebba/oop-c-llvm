; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"a" = alloca i16
  %".2" = load i16, i16* %"a"
  %".3" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.1", i64 0, i64 0), i16 %".2")
  %".4" = trunc i32 10 to i16
  store i16 %".4", i16* %"a"
  %".6" = load i16, i16* %"a"
  %".7" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.2", i64 0, i64 0), i16 %".6")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [8 x i8] c"a = %d\0a\00"
@".str.2" = private unnamed_addr constant [8 x i8] c"a = %d\0a\00"