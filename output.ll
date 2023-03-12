; ModuleID = "example"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"(i32 %"a")
{
entry:
  %"x" = alloca i32
  store i32 150, i32* %"x"
  %".4" = load i32, i32* %"x"
  ret i32 %".4"
}
