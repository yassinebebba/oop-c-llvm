#include <stdio.h>
#include <stdlib.h>
typedef struct String {
 	char * first_name;
	char * last_name;
	int age;
	int (*StringgetAge)(struct String * this);
	void (*Stringset_age)(struct String * this, int);
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
void StringString(String * this, char * first_name, char * last_name, int age) {
	this->StringgetAge = &StringgetAge;
	this->Stringset_age = &Stringset_age;
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
