; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"add"(i32 %"a", i32 %"b")
{
entry:
  %".4" = add i32 %"a", %"b"
  ret i32 %".4"
}

define i32 @"main"()
{
entry:
  %".2" = call i32 @"add"(i32 1, i32 2)
  %".3" = sub i32 0, %".2"
  %".4" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([4 x i8], [4 x i8]* @".str.1", i64 0, i64 0), i32 %".3")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [4 x i8] c"%d\0a\00"