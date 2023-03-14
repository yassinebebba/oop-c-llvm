// @str_fmt = private unnamed_addr constant [3 x i8] c"%d\00"

// declare i32 @printf(i8*, ...)

//const int d = 0;
int printf(char *, ...);

int main(int a) {
    short int x = 1 + 2 * 3;
//    int x = 1 + 2 * 3 * 4 / 5 - 6 ;
  // call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_fmt, i32 0, i32 0), i32 %".3")
    char * fmt = "%d %s\n(IGNORE need fix null-termination)->";
    printf(fmt, x, "asdsad");
    return 0;
}