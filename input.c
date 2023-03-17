// @str_fmt = private unnamed_addr constant [3 x i8] c"%d\00"

// declare i32 @printf(i8*, ...)

//const int d = 0;
int printf(char *, ...);

int T = 1;
char d;
class Foo {
    int i;
    int d;
    void Foo(int i) {
        this.i = i;
    }
}

int main() {
    Foo x = new Foo(1);
    x.i = 20;
    char * fmt = "%d\n";
    printf(fmt, x.i);
    return 0;
}