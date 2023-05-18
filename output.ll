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
  %".5" = sext i16 %".4" to i32
  %".6" = sub i32 7, %".5"
  %".7" = sub i32 10, %".6"
  %"b" = alloca i32
  store i32 %".7", i32* %"b"
  %"c" = alloca i64
  %".9" = load i32, i32* %"b"
  %".10" = sext i32 %".9" to i64
  store i64 %".10", i64* %"c"
  %".12" = load i32, i32* %"b"
  %".13" = trunc i32 %".12" to i16
  store i16 %".13", i16* %"a"
  %"str" = alloca i8*
  store i8* getelementptr ([8 x i8], [8 x i8]* @".str.1", i64 0, i64 0), i8** %"str"
  %"str2" = alloca i8*
  %".16" = load i8*, i8** %"str"
  store i8* %".16", i8** %"str2"
  %".18" = load i8*, i8** %"str2"
  %".19" = load i64, i64* %"c"
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".18", i64 %".19")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [8 x i8] c"a = %d\0a\00"