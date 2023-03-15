// @str_fmt = private unnamed_addr constant [3 x i8] c"%d\00"

// declare i32 @printf(i8*, ...)

//const int d = 0;
int printf(char *, ...);

int main() {
    short int x = 45;
    int * t = "abc";
    char * fmt = "%d %s %s\n(IGNORE need fix null-termination)->";
    printf(fmt, x, t, "asdsad");
    return 0;
}