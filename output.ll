; ModuleID = "example"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i8* @"a"()

declare i32**** @"b"(i8* %".1")

declare i32 @"c"(i32 %".1", i32 %".2")

define i32 @"main"()
{
entry:
  %".2" = add i32 7, 7
  %".3" = add i32 %".2", 3
  %"x" = alloca i32
  store i32 %".3", i32* %"x"
  store i32 10, i32* %"x"
  %".6" = load i32, i32* %"x"
  ret i32 %".6"
}
