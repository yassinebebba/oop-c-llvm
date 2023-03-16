// @str_fmt = private unnamed_addr constant [3 x i8] c"%d\00"

// declare i32 @printf(i8*, ...)

//const int d = 0;
int printf(char *, ...);

int T = 1;
char d;

int main() {
    short int x = -12;
    int a;
    a = x;
    int * t = "abc";
    char * fmt = "%d %s %d %s\n(IGNORE need fix null-termination)->" "sada\"sa";
    printf(fmt, x, t,a, "asdsad" "132");
    return 0;
}