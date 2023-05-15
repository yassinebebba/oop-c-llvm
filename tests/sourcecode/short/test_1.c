int printf(char *, ...);

int main() {
    short a;
    a = 10;
    printf("a = %d\n", a);
    a = 20;
    printf("a = %d\n", a);
    a = 10 + 20;
    printf("a = %d\n", a);
    return 0;
}