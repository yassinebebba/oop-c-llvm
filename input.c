int printf(char *, ...);

int main() {
    short a = 2;
    int b = 10;
    long c = b + 10;
    a = b;
    char * str = "a = %d\n";
    char * str2 = str;
    printf(str2, c);
    return 0;
}