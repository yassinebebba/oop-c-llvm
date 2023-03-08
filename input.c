#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


class String {
    unsigned long length;
    char * content;

    String * String(char * str) {
        // this is implicitly declared because it has to be hmmm
        // String * this = malloc(sizeof(String));
        this->content = malloc(sizeof(char) + strlen(str) - 1);
        strcpy(this->content, str);
        this->length = strlen(str);
        return this;
    }


    int eq(String * other) {
        return strcmp(this->content, other->content);
    }

     String * lshift(String * other) {
        // has to check if there is enough space
        unsigned long len = strlen(other->content);
        this->content = realloc(this->content, sizeof(other->content) + this->length + len + 20);
        strcpy(this->content + this->length, other->content);
        this->length += len;
        return this;
    }

//    String * mult(unsigned int times) {
//        // has to check if there is enough space
//        char temp[1000];
//        strcpy(temp, string->content);
//        for (unsigned long i = 0; i < c * string->length; ++i) {
//            string->content[i] = temp[i % string->length];
//        }
//        string->length = c * string->length;
//    }

    String * mult(String * other) {

    }

    String * add(String * other) {
        // has to check if there is enough space
        char * temp = malloc(this->length + other->length + 1);
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
    String * s1 = new String("Hello ");
    String * s2 = new String("Malte ");
    String * s3 = new String("Ressin");
//    s1->add(s1, s1->add(s1, s2));
    String * s4 = s1 + s2 + s3 + s1;
    s1 << s2 << s3;
    printf("%s\n", s1->toString());
    printf("%s\n", s4->toString());
    printf("%s\n", s2->toString());
    int r = s1 == s2;
    if (r == 0) {
        printf("They are the same\n");
    } else {
        printf("They are not the same\n");
    }
    return 0;
}