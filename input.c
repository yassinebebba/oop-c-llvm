int printf(char *, ...);

int main() {
    short a = 2;
    int b = 10 - 7 + a;
    long c = b;
    a = b;
    char * str = "a = %d\n";
    char * str2 = str;
    printf(str2, c);
    return 0;
}