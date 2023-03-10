; ModuleID = "example"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

declare i8* @"a"()

declare i32**** @"b"(i8* %".1")

declare i32 @"c"(i32 %".1", i32 %".2")

define i32 @"main"()
{
entry:
  %".2" = mul i32 2, 3
  %".3" = mul i32 %".2", 4
  %".4" = sdiv i32 %".3", 5
  %".5" = add i32 1, %".4"
  %".6" = sub i32 %".5", 6
  %".7" = icmp eq i32 %".6", 1
  %".8" = icmp eq i1 %".7", 2
  %"x" = alloca i32
  %".9" = zext i1 %".8" to i32
  store i32 %".9", i32* %"x"
  ret i32 0
}
