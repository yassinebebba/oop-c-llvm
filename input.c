// @str_fmt = private unnamed_addr constant [3 x i8] c"%d\00"

// declare i32 @printf(i8*, ...)

//const int d = 0;
int printf(char *, ...);

int main(int a) {
    short int x = 45;
    // x = "";
    char * fmt = "%d %s\n(IGNORE need fix null-termination)->";
    printf(fmt, x, "asdsad");
    return 0;
}