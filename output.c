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
	int (*Stringeq)(struct String *, struct String *);
	struct String * (*Stringadd)(struct String *, struct String *);
	char * (*StringtoString)(struct String *);
} String;
int Stringeq(String * this, String * other) {
 return strcmp(this->content,other->content);
}
String* Stringadd(String * this, String * other) {
 unsigned long len = strlen(other->content);;
this->content = realloc(this->content, sizeof(other->content)+this->length+len-1);;
strcpy(this->content+this->length, other->content);
this->length += len;
return this;
}
char* StringtoString(String * this) {
 return this->content;
}
void StringString(String * this, char * str) {
	this->Stringeq = &Stringeq;
	this->Stringadd = &Stringadd;
	this->StringtoString = &StringtoString;
	this->content = malloc(sizeof(char)+strlen(str)-1);;
	strcpy(this->content, str);
	this->length = strlen(str);;
}
int main() {
 	String * s1 = malloc(sizeof(String));
	StringString(s1, "Hey");
	String * s2 = malloc(sizeof(String));
	StringString(s2, "");
	s2 = s2->Stringadd(s2, s1);
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
