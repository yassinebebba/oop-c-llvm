; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"a" = alloca i16
  %".2" = trunc i32 10 to i16
  store i16 %".2", i16* %"a"
  %".4" = load i16, i16* %"a"
  %".5" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.1", i64 0, i64 0), i16 %".4")
  %".6" = trunc i32 20 to i16
  store i16 %".6", i16* %"a"
  %".8" = load i16, i16* %"a"
  %".9" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.2", i64 0, i64 0), i16 %".8")
  %".10" = add i32 10, 20
  %".11" = trunc i32 %".10" to i16
  store i16 %".11", i16* %"a"
  %".13" = load i16, i16* %"a"
  %".14" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([8 x i8], [8 x i8]* @".str.3", i64 0, i64 0), i16 %".13")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [8 x i8] c"a = %d\0a\00"
@".str.2" = private unnamed_addr constant [8 x i8] c"a = %d\0a\00"
@".str.3" = private unnamed_addr constant [8 x i8] c"a = %d\0a\00"