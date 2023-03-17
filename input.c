// @str_fmt = private unnamed_addr constant [3 x i8] c"%d\00"

// declare i32 @printf(i8*, ...)

//const int d = 0;
int printf(char *, ...);

int T = 1;
char d;
class Foo {
    int i;
    int d;
    void Foo(int i, int d) {
        this->i = i;
        this->d = d;
    }
}

int main() {
    Foo x = new Foo(2, 2);
    char * fmt = "%d %d\n";
    printf(fmt, x.i, x.d + x.i);
    return 0;
}