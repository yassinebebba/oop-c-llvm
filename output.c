/*
############################################
THIS FILE IS NOT MEANT TO BE EDITED BY HAND
############################################
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


typedef struct String {
 	unsigned long length;
	char * content;
	struct String * (*StringString)(char *);
	int (*Stringeq)(struct String *, struct String *);
	struct String * (*Stringlshift)(struct String *, struct String *);
	struct String * (*Stringmult)(struct String *, struct String *);
	struct String * (*Stringadd)(struct String *, struct String *);
	char * (*StringtoString)(struct String *);
} String;

struct String * StringString(char *);
int Stringeq(struct String *, struct String *);
struct String * Stringlshift(struct String *, struct String *);
struct String * Stringmult(struct String *, struct String *);
struct String * Stringadd(struct String *, struct String *);
char * StringtoString(struct String *);

String* StringString(char * str) {
	String* this = malloc(sizeof(String));
	this->StringString = &StringString;
	this->Stringeq = &Stringeq;
	this->Stringlshift = &Stringlshift;
	this->Stringmult = &Stringmult;
	this->Stringadd = &Stringadd;
	this->StringtoString = &StringtoString;
	this->content = malloc(sizeof(char)+strlen(str)-1);;
	strcpy(this->content, str);
	this->length = strlen(str);;
	return this;
}
int Stringeq(String * this, String * other) {
 	return strcmp(this->content,other->content);
}
String* Stringlshift(String * this, String * other) {
 	unsigned long len = strlen(other->content);;
	this->content = realloc(this->content, sizeof(other->content)+this->length+len+20);;
	strcpy(this->content+this->length, other->content);
	this->length += len;
	return this;
}
String* Stringmult(String * this, String * other) {
 
}
String* Stringadd(String * this, String * other) {
 	char * temp = malloc(this->length+other->length+1);;
	strcpy(temp, this->content);
	strcpy(temp+this->length, other->content);
	String * str = StringString(temp);
	return str;
}
char* StringtoString(String * this) {
 	return this->content;
}

int main() {
 	String * s1 = StringString("Hello ");
	String * s2 = StringString("Malte ");
	String * s3 = StringString("Ressin");
	String * s4 = s1->Stringadd(s1, s2)->Stringadd(s1, s3)->Stringadd(s1, s1);
	s1->Stringlshift(s1, s2)->Stringlshift(s1, s3);
	printf("%s\n", s1->StringtoString(s1));
	printf("%s\n", s4->StringtoString(s4));
	printf("%s\n", s2->StringtoString(s2));
	int r = s1->Stringeq(s1, s2);
	if ( r==0) {
 		printf("They are the same\n");
	}
	else {
 		printf("They are not the same\n");
	}

	return 0;
}
