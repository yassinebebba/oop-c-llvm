; ModuleID = "example"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i8* @"a"()

declare i32**** @"b"(i8* %".1")

declare i32 @"c"(i32 %".1", i32 %".2")

define i32 @"main"()
{
entry:
  %".2" = mul i32 1, 2
  %".3" = add i32 1, %".2"
  %"x" = alloca i32
  store i32 %".3", i32* %"x"
  %".5" = mul i32 1, 2
  %".6" = add i32 1, %".5"
  ret i32 0
}
