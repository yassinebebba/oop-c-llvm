#include <stdio.h>
#include <stdlib.h>
typedef struct String {
 	char * first_name;
	char * last_name;
	int age;
	int (*String_getAge)(struct String *);
	void (*String_set_age)(struct String *, int);
} String;
int String_getAge(String * self) {
 	return self->age;
}
void String_set_age(String * self, int age) {
 	if (age < 2) {
 		printf("you must be older than 2");
	}
	else {
 		self->age = age;
	}

}
void String___init__(String * self, char * first_name, char * last_name, int age) {
	self->String_getAge = &String_getAge;
	self->String_set_age = &String_set_age;
	self->first_name = first_name;
	self->last_name = last_name;
	self->age = age;
}
typedef struct Animal {
 	char * name;
} Animal;
void Animal___init__(Animal * self, char * name) {
	self->name = name;
}
int main() {
 	String * string = malloc(sizeof(String));
	String___init__(string, "Malte", "Ressin", 41);
	string->String_set_age(string, 1);
	string->String_set_age(string, 2);
	string->String_set_age(string, 3);
	string->String_set_age(string, 4);
	String * secondString = malloc(sizeof(String));
	String___init__(secondString, "Yassine", "Bebba", 23);
	printf("Hi my name is %s %s and I am %d years old.\n", string->first_name, string->last_name, string->String_getAge(string));
	printf("Hi my name is %s %s and I am %d years old.\n", secondString->first_name, secondString->last_name, secondString->age);
	Animal * animal = malloc(sizeof(Animal));
	Animal___init__(animal, "Lion");
	printf("My animal name is %s.\n", animal->name);
	free(string);
	free(secondString);
	return 0;
}
