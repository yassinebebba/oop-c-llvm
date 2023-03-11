; ModuleID = "example"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i8* @"a"(i32 %"x")

declare i32**** @"b"(i8* %"a")

declare i32 @"c"(i32 %"a", i32 %"b")

define i32 @"main"(i32 %"a")
{
entry:
  %"x" = alloca i32
  store i32 2000, i32* %"x"
  %".4" = load i32, i32* %"x"
  ret i32 %".4"
}
