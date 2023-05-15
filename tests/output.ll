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
  %"b" = alloca i16
  %".4" = trunc i32 3 to i16
  store i16 %".4", i16* %"b"
  %".6" = load i16, i16* %"b"
  store i16 %".6", i16* %"a"
  %".8" = load i16, i16* %"a"
  %".9" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.1", i64 0, i64 0), i16 %".8")
  %".10" = load i16, i16* %"b"
  %".11" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.2", i64 0, i64 0), i16 %".10")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [8 x i8] c"a = %d\0a\00"
@".str.2" = private unnamed_addr constant [8 x i8] c"b = %d\0a\00"