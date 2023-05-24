int printf(char *, ...);

int add(int a, int b) {
    return a + b;
}

int main() {
    printf("%d\n", -add(1, 2));
    return 0;
}