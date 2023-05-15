int printf(char *, ...);

int main() {
    short a = 2;
    short b = 3;
    a = b;
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    return 0;
}