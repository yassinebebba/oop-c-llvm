#include <stdio.h>
#include <stdlib.h>
typedef struct String {
 	char * first_name;
	char * last_name;
	int age;
	int (*String_getAge)(struct String * this);
	void (*String_set_age)(struct String * this, int);
} String;
int String_getAge(String * this) {
 	return this->age;
}
void String_set_age(String * this, int age) {
 	if (age < 2) {
 		printf("you must be older than 2\n");
	}
	else {
 		this->age = age;
	}

}
void String_String(String * this, char * first_name, char * last_name, int age) {
	this->String_getAge = &String_getAge;
	this->String_set_age = &String_set_age;
	this->first_name = first_name;
	this->last_name = last_name;
	this->age = age;
}
typedef struct Animal {
 	char * name;
} Animal;
void AnimalAnimal(Animal * this) {
// Not implemented
}
int test(String * string) {
 
}
int main() {
 	String * string = malloc(sizeof(String));
	StringString(string, "Malte", "Ressin", 41);
	string->String_set_age(string, 1);
	String * secondString = malloc(sizeof(String));
	StringString(secondString, "Yassine", "Bebba", 23);
	printf("Hi my name is %s %s and I am %d years old.\n", string->first_name, string->last_name, string->String_getAge(string));
	printf("Hi my name is %s %s and I am %d years old.\n", secondString->first_name, secondString->last_name, secondString->age);
	Animal * animal = malloc(sizeof(Animal));
	AnimalAnimal(animal, "Lion");
	printf("My animal name is %s.\n", animal->name);
	free(string);
	free(secondString);
	return 0;
}
