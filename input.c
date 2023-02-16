#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


class String {
    unsigned long length;
    char * content;

    void String(char * str) {
        this->content = malloc(sizeof(char) + strlen(str) - 1);
        strcpy(this->content, str);
        this->length = strlen(str);
    }

    int eq(String * other) {
        return strcmp(this->content, other->content);
    }

    char * toString() {
        return this->content;
    }
}

int main() {
    String * s1 = new String("Hey");
    String * s2 = new String("Hi");
    int r = s1 == s2;
    if (r == 0) {
        printf("They are the same\n");
    } else {
        printf("They are not the same\n");
    }
    return 0;
}