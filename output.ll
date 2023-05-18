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
  %"b" = alloca i32
  store i32 10, i32* %"b"
  %".5" = load i32, i32* %"b"
  %".6" = add i32 %".5", 10
  %"c" = alloca i64
  %".7" = sext i32 %".6" to i64
  store i64 %".7", i64* %"c"
  %".9" = load i32, i32* %"b"
  %".10" = trunc i32 %".9" to i16
  store i16 %".10", i16* %"a"
  %"str" = alloca i8*
  store i8* getelementptr ([8 x i8], [8 x i8]* @".str.1", i64 0, i64 0), i8** %"str"
  %"str2" = alloca i8*
  %".13" = load i8*, i8** %"str"
  store i8* %".13", i8** %"str2"
  %".15" = load i8*, i8** %"str2"
  %".16" = load i64, i64* %"c"
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".15", i64 %".16")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [8 x i8] c"a = %d\0a\00"