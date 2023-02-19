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

//     String * add(String * other) {
//        // has to check if there is enough space
//        unsigned long len = strlen(other->content);
//        this->content = realloc(this->content, sizeof(other->content) + this->length + len - 1);
//        strcpy(this->content + this->length, other->content);
//        this->length += len;
//        return this;
//    }


    String * add(String * other) {
        // has to check if there is enough space
        char * temp = malloc(strlen(this->content) + strlen(other->content));
        unsigned long len = strlen(other->content);
        this->content = realloc(this->content, sizeof(other->content) + this->length + len - 1);
        strcpy(this->content + this->length, other->content);
        strcpy(temp, this->content);
        strcpy(temp + this->length, other->content);
        String * str = new String(temp);
        return str;
    }

    char * toString() {
        return this->content;
    }
}

int main() {
    String * s1 = new String("Hey");
    String * s2 = new String("");
    String * s3 = s2 + s1;
    printf("%s\n", s2->toString());
    int r = s1 == s2;
    if (r == 0) {
        printf("They are the same\n");
    } else {
        printf("They are not the same\n");
    }
    return 0;
}