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