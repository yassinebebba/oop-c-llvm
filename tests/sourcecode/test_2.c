int printf(char *, ...);

int main() {
    short a;
    short int b;
    int c;
    long d;
    long int e;
    long long f;
    long long int g;
    char * fmt = "a = %d\n"
                 "b = %d\n"
                 "c = %d\n"
                 "d = %d\n"
                 "e = %d\n"
                 "f = %d\n"
                 "g = %d\n";
    printf(fmt,
           a,
           b,
           c,
           d,
           e,
           f,
           g
          );
    return 0;
}