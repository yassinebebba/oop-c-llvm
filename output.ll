; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"class.Point" = type {i32, i32}
%"class.Target" = type {}
declare i32 @"printf"(i8* %".1", ...)

define void @"_ZN5Point5PointEPS_ii"(%"class.Point"* %"this", i32 %"x", i32 %"y")
{
entry:
  %".5" = getelementptr %"class.Point", %"class.Point"* %"this", i32 0, i32 0
  store i32 %"x", i32* %".5"
  %".7" = getelementptr %"class.Point", %"class.Point"* %"this", i32 0, i32 1
  store i32 %"y", i32* %".7"
  ret void
}

define i32 @"_ZN5Point5get_xEPS_"(%"class.Point"* %"this")
{
entry:
  %".3" = getelementptr %"class.Point", %"class.Point"* %"this", i32 0, i32 0
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define i32 @"_ZN5Point5get_yEPS_"(%"class.Point"* %"this")
{
entry:
  %".3" = getelementptr %"class.Point", %"class.Point"* %"this", i32 0, i32 1
  %".4" = load i32, i32* %".3"
  ret i32 %".4"
}

define void @"_ZN5Point5set_xEPS_i"(%"class.Point"* %"this", i32 %"x")
{
entry:
  %".4" = getelementptr %"class.Point", %"class.Point"* %"this", i32 0, i32 0
  store i32 %"x", i32* %".4"
  ret void
}

define i32 @"_ZN6Target5get_tEPS_"(%"class.Target"* %"this")
{
entry:
  ret i32 1
}

define void @"_ZN6Target6TargetEPS_"(%"class.Target"* %"this")
{
entry:
  ret void
}

define i32 @"main"()
{
entry:
  %"p" = alloca %"class.Point"
  call void @"_ZN5Point5PointEPS_ii"(%"class.Point"* %"p", i32 1, i32 2)
  call void @"_ZN5Point5set_xEPS_i"(%"class.Point"* %"p", i32 10)
  %".4" = getelementptr %"class.Point", %"class.Point"* %"p", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  %".6" = getelementptr %"class.Point", %"class.Point"* %"p", i32 0, i32 1
  %".7" = load i32, i32* %".6"
  %".8" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([7 x i8], [7 x i8]* @".str.1", i64 0, i64 0), i32 %".5", i32 %".7")
  %".9" = call i32 @"_ZN5Point5get_xEPS_"(%"class.Point"* %"p")
  %".10" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([4 x i8], [4 x i8]* @".str.2", i64 0, i64 0), i32 %".9")
  %".11" = call i32 @"_ZN5Point5get_yEPS_"(%"class.Point"* %"p")
  %".12" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([4 x i8], [4 x i8]* @".str.3", i64 0, i64 0), i32 %".11")
  %"t" = alloca %"class.Target"
  call void @"_ZN6Target6TargetEPS_"(%"class.Target"* %"t")
  %".14" = call i32 @"_ZN6Target5get_tEPS_"(%"class.Target"* %"t")
  %".15" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([4 x i8], [4 x i8]* @".str.4", i64 0, i64 0), i32 %".14")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [7 x i8] c"%d %d\0a\00"
@".str.2" = private unnamed_addr constant [4 x i8] c"%d\0a\00"
@".str.3" = private unnamed_addr constant [4 x i8] c"%d\0a\00"
@".str.4" = private unnamed_addr constant [4 x i8] c"%d\0a\00"