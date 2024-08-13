; ModuleID = "main"
target triple = "x86_64-redhat-linux-gnu"
target datalayout = ""

%"class.Point1D" = type {i32}
%"class.Point2D" = type {%"class.Point1D"*, i32}
%"class.Point3D" = type {%"class.Point2D"*, i32}
declare i32 @"printf"(i8* %".1", ...)

define void @"_ZN7Point1D7Point1DEPS_i"(%"class.Point1D"* %"this", i32 %"x")
{
entry:
  %".4" = getelementptr %"class.Point1D", %"class.Point1D"* %"this", i32 0, i32 0
  store i32 %"x", i32* %".4"
  ret void
}

define i32 @"_ZN7Point1D4getXEPS_"(%"class.Point1D"* %"this")
{
entry:
  %".3" = load %"class.Point1D", %"class.Point1D"* %"this"
  %".4" = getelementptr %"class.Point1D", %"class.Point1D"* %"this", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  ret i32 %".5"
}

define void @"_ZN7Point2D7Point2DEPS_P7Point1Di"(%"class.Point2D"* %"this", %"class.Point1D"* %"p1d", i32 %"y")
{
entry:
  %".5" = getelementptr %"class.Point2D", %"class.Point2D"* %"this", i32 0, i32 0
  store %"class.Point1D"* %"p1d", %"class.Point1D"** %".5"
  %".7" = getelementptr %"class.Point2D", %"class.Point2D"* %"this", i32 0, i32 1
  store i32 %"y", i32* %".7"
  ret void
}

define i32 @"_ZN7Point2D4getXEPS_"(%"class.Point2D"* %"this")
{
entry:
  %".3" = load %"class.Point2D", %"class.Point2D"* %"this"
  %".4" = getelementptr %"class.Point2D", %"class.Point2D"* %"this", i32 0, i32 0
  %".5" = load %"class.Point1D"*, %"class.Point1D"** %".4"
  %".6" = load %"class.Point1D", %"class.Point1D"* %".5"
  %".7" = call i32 @"_ZN7Point1D4getXEPS_"(%"class.Point1D"* %".5")
  ret i32 %".7"
}

define i32 @"_ZN7Point2D4getYEPS_"(%"class.Point2D"* %"this")
{
entry:
  %".3" = load %"class.Point2D", %"class.Point2D"* %"this"
  %".4" = getelementptr %"class.Point2D", %"class.Point2D"* %"this", i32 0, i32 1
  %".5" = load i32, i32* %".4"
  ret i32 %".5"
}

define void @"_ZN7Point3D7Point3DEPS_P7Point2Di"(%"class.Point3D"* %"this", %"class.Point2D"* %"p2d", i32 %"z")
{
entry:
  %".5" = getelementptr %"class.Point3D", %"class.Point3D"* %"this", i32 0, i32 0
  store %"class.Point2D"* %"p2d", %"class.Point2D"** %".5"
  %".7" = getelementptr %"class.Point3D", %"class.Point3D"* %"this", i32 0, i32 1
  store i32 %"z", i32* %".7"
  ret void
}

define i32 @"_ZN7Point3D4getXEPS_"(%"class.Point3D"* %"this")
{
entry:
  %".3" = load %"class.Point3D", %"class.Point3D"* %"this"
  %".4" = getelementptr %"class.Point3D", %"class.Point3D"* %"this", i32 0, i32 0
  %".5" = load %"class.Point2D"*, %"class.Point2D"** %".4"
  %".6" = load %"class.Point2D", %"class.Point2D"* %".5"
  %".7" = call i32 @"_ZN7Point2D4getXEPS_"(%"class.Point2D"* %".5")
  ret i32 %".7"
}

define i32 @"_ZN7Point3D4getYEPS_"(%"class.Point3D"* %"this")
{
entry:
  %".3" = load %"class.Point3D", %"class.Point3D"* %"this"
  %".4" = getelementptr %"class.Point3D", %"class.Point3D"* %"this", i32 0, i32 0
  %".5" = load %"class.Point2D"*, %"class.Point2D"** %".4"
  %".6" = load %"class.Point2D", %"class.Point2D"* %".5"
  %".7" = call i32 @"_ZN7Point2D4getYEPS_"(%"class.Point2D"* %".5")
  ret i32 %".7"
}

define i32 @"_ZN7Point3D4getZEPS_"(%"class.Point3D"* %"this")
{
entry:
  %".3" = load %"class.Point3D", %"class.Point3D"* %"this"
  %".4" = getelementptr %"class.Point3D", %"class.Point3D"* %"this", i32 0, i32 1
  %".5" = load i32, i32* %".4"
  ret i32 %".5"
}

define i32 @"main"()
{
entry:
  %"x" = alloca i64*
  %".2" = bitcast i8* getelementptr ([13 x i8], [13 x i8]* @".str.1", i64 0, i64 0) to i64*
  store i64* %".2", i64** %"x"
  %".4" = load i64*, i64** %"x"
  %".5" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([4 x i8], [4 x i8]* @".str.2", i64 0, i64 0), i64* %".4")
  %"p1d" = alloca %"class.Point1D"
  call void @"_ZN7Point1D7Point1DEPS_i"(%"class.Point1D"* %"p1d", i32 10)
  %"p2d" = alloca %"class.Point2D"
  call void @"_ZN7Point2D7Point2DEPS_P7Point1Di"(%"class.Point2D"* %"p2d", %"class.Point1D"* %"p1d", i32 20)
  %"p3d" = alloca %"class.Point3D"
  call void @"_ZN7Point3D7Point3DEPS_P7Point2Di"(%"class.Point3D"* %"p3d", %"class.Point2D"* %"p2d", i32 30)
  %".9" = getelementptr %"class.Point3D", %"class.Point3D"* %"p3d", i32 0, i32 1
  store i32 155, i32* %".9"
  %".11" = call i32 @"_ZN7Point3D4getXEPS_"(%"class.Point3D"* %"p3d")
  %".12" = call i32 @"_ZN7Point3D4getYEPS_"(%"class.Point3D"* %"p3d")
  %".13" = call i32 @"_ZN7Point3D4getZEPS_"(%"class.Point3D"* %"p3d")
  %".14" = call i32 (i8*, ...) @"printf"(i8* getelementptr ([10 x i8], [10 x i8]* @".str.3", i64 0, i64 0), i32 %".11", i32 %".12", i32 %".13")
  ret i32 0
}

@".str.1" = private unnamed_addr constant [13 x i8] c"asdasdadadaa\00"
@".str.2" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str.3" = private unnamed_addr constant [10 x i8] c"%d %d %d\0a\00"