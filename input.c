#include <stdio.h>
#include <stdlib.h>

class String {
    char * first_name;
    char * last_name;
    int age;
    void String(char* first_name, char * last_name, int age) {
        this->first_name = first_name;
        this->last_name = last_name;
        this->age = age;
    }
    int getAge() {
        return this->age;
    }
    void set_age(int age) {
        if (age < 2) {
            printf("you must be older than 2\n");
        } else {
            this->age = age;
        }
    }

    char * toString() {
        char * str;
        // this syntax should error
        // asdad
        sprintf(str, "<String object at %p>", this);
//        printf("%s\n", str);
        // return local variable will be garbage collected
        return str;
    }
}

class Animal {
    char * name;
    void Animal(char * name) {
        this->name = name;
    }
}

void test(String * a) {
  String * string = new String("Malte", "Ressin", 41);
  printf("Hi my name is %s %s and I am %d years old.\n", string->first_name, string->last_name, string->getAge());
  printf("Test Hi my name is %s %s and I am %d years old.\n", a->first_name, a->last_name, a->getAge());
}

int main() {
    String * string = new String("Malte", "Ressin", 41);
    test(string);
    printf("%s\n", string->toString());
    string->set_age(1);
    String *secondString = new String("Yassine", "Bebba", 23);
    printf("Hi my name is %s %s and I am %d years old.\n", string->first_name, string->last_name, string->getAge());
    printf("Hi my name is %s %s and I am %d years old.\n", secondString->first_name, secondString->last_name, secondString->age);
    Animal * animal = new Animal("Lion");
    printf("My animal name is %s.\n", animal->name);
    free(string);
    free(secondString);
    return 0;
}