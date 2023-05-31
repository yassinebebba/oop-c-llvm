; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"class.Point1D" = type {i32}
%"class.Test" = type {%"class.Point1D"*}
declare i32 @"printf"(i8* %".1", ...)

define void @"_ZN7Point1D7Point1DEPS_i"(%"class.Point1D"* %"this", i32 %"x")
{
entry:
  %".4" = getelementptr %"class.Point1D", %"class.Point1D"* %"this", i32 0, i32 0
  store i32 %"x", i32* %".4"
  ret void
}

define i32 @"_ZN7Point1D5get_xEPS_"(%"class.Point1D"* %"this")
{
entry:
  %".3" = load %"class.Point1D", %"class.Point1D"* %"this"
  %".4" = getelementptr %"class.Point1D", %"class.Point1D"* %"this", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  ret i32 %".5"
}

define void @"_ZN4Test4TestEPS_P7Point1D"(%"class.Test"* %"this", %"class.Point1D"* %"p1d")
{
entry:
  %".4" = getelementptr %"class.Test", %"class.Test"* %"this", i32 0, i32 0
  store %"class.Point1D"* %"p1d", %"class.Point1D"** %".4"
  ret void
}

define i32 @"_ZN4Test5get_xEPS_"(%"class.Test"* %"this")
{
entry:
  %".3" = load %"class.Test", %"class.Test"* %"this"
  %".4" = getelementptr %"class.Test", %"class.Test"* %"this", i32 0, i32 0
  %".5" = load %"class.Point1D"*, %"class.Point1D"** %".4"
  %".6" = load %"class.Point1D", %"class.Point1D"* %".5"
  %".7" = call i32 @"_ZN7Point1D5get_xEPS_"(%"class.Point1D"* %".5")
  ret i32 %".7"
}

define i32 @"main"()
{
entry:
  %"p1d" = alloca %"class.Point1D"
  call void @"_ZN7Point1D7Point1DEPS_i"(%"class.Point1D"* %"p1d", i32 10)
  %"t" = alloca %"class.Test"
  call void @"_ZN4Test4TestEPS_P7Point1D"(%"class.Test"* %"t", %"class.Point1D"* %"p1d")
  %".4" = call i32 @"_ZN4Test5get_xEPS_"(%"class.Test"* %"t")
  %".5" = mul i32 %".4", 2
  %".6" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([16 x i8], [16 x i8]* @".str.1", i64 0, i64 0), i32 %".5")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [16 x i8] c"1D point: (%d)\0a\00"