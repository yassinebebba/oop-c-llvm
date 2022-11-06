#include <stdio.h>
#include <stdlib.h>
typedef struct String {
 	char * first_name;
	char * last_name;
	int age;
	int (*StringgetAge)(struct String *);
	void (*Stringset_age)(struct String *, int);
	char * (*StringtoString)(struct String *);
} String;
int StringgetAge(String * this) {
 	return this->age;
}
void Stringset_age(String * this, int age) {
 	if (age < 2) {
 		printf("you must be older than 2\n");
	}
	else {
 		this->age = age;
	}

}
char * StringtoString(String * this) {
 	char * str;
	sprintf(str, "<String object at %p>", this);
	return str;
}
void StringString(String * this, char * first_name, char * last_name, int age) {
	this->StringgetAge = &StringgetAge;
	this->Stringset_age = &Stringset_age;
	this->StringtoString = &StringtoString;
	this->first_name = first_name;
	this->last_name = last_name;
	this->age = age;
}
typedef struct Animal {
 	char * name;
} Animal;
void AnimalAnimal(Animal * this, char * name) {
	this->name = name;
}
void test(String * a) {
 	String * string = malloc(sizeof(String));
	StringString(string, "Malte", "Ressin", 41);
	printf("Hi my name is %s %s and I am %d years old.\n", string->first_name, string->last_name, string->StringgetAge(string));
	printf("Test Hi my name is %s %s and I am %d years old.\n", a->first_name, a->last_name, a->StringgetAge(a));
}
int main() {
 	String * string = malloc(sizeof(String));
	StringString(string, "Malte", "Ressin", 41);
	test(string);
	printf("%s\n", string->StringtoString(string));
	string->Stringset_age(string, 1);
	String * secondString = malloc(sizeof(String));
	StringString(secondString, "Yassine", "Bebba", 23);
	printf("Hi my name is %s %s and I am %d years old.\n", string->first_name, string->last_name, string->StringgetAge(string));
	printf("Hi my name is %s %s and I am %d years old.\n", secondString->first_name, secondString->last_name, secondString->age);
	Animal * animal = malloc(sizeof(Animal));
	AnimalAnimal(animal, "Lion");
	printf("My animal name is %s.\n", animal->name);
	free(string);
	free(secondString);
	return 0;
}
