/*
############################################
THIS FILE IS NOT MEANT TO BE EDITED BY HAND
############################################
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct Integer {
 	int n;
	bool (*Integereq)(struct Integer *, struct Integer *);
	bool (*Integergt)(struct Integer *, struct Integer *);
	bool (*Integergte)(struct Integer *, struct Integer *);
	bool (*Integerlt)(struct Integer *, struct Integer *);
	bool (*Integerlte)(struct Integer *, struct Integer *);
	void (*Integerfree)(struct Integer *);
	char * (*IntegertoString)(struct Integer *);
} Integer;
bool Integereq(Integer * this, Integer * other) {
 	return this->n==other->n;
}
bool Integergt(Integer * this, Integer * other) {
 	return this->n>other->n;
}
bool Integergte(Integer * this, Integer * other) {
 	return this->n>=other->n;
}
bool Integerlt(Integer * this, Integer * other) {
 	return this->n<other->n;
}
bool Integerlte(Integer * this, Integer * other) {
 	return this->n<=other->n;
}
void Integerfree(Integer * this) {
 	this = NULL;
	free(this);
}
char * IntegertoString(Integer * this) {
	char * str = malloc(sizeof(char *) * 30);
	sprintf(str, "<Integer object at %p>\n", this);
	return str;
}
void IntegerInteger(Integer * this, int n) {
	this->Integereq = &Integereq;
	this->Integergt = &Integergt;
	this->Integergte = &Integergte;
	this->Integerlt = &Integerlt;
	this->Integerlte = &Integerlte;
	this->Integerfree = &Integerfree;
	this->IntegertoString = &IntegertoString;
	this->n = n;
}
typedef struct String {
 	char * string;
	char * (*StringtoString)(struct String *);
} String;
char * StringtoString(String * this) {
 	return this->string;
}
void StringString(String * this, char * string) {
	this->StringtoString = &StringtoString;
	this->string = string;
}
typedef struct Player {
 	int x;
	int y;
	void (*Playerup)(struct Player *);
	void (*Playerdown)(struct Player *);
	void (*Playerright)(struct Player *);
	void (*Playerleft)(struct Player *);
	bool (*Playereq)(struct Player *, struct Player *);
	char * (*PlayertoString)(struct Player *);
} Player;
void Playerup(Player * this) {
 	this->y += 1;
}
void Playerdown(Player * this) {
 	this->y -= 1;
}
void Playerright(Player * this) {
 	this->x += 1;
}
void Playerleft(Player * this) {
 	this->x -= 1;
}
bool Playereq(Player * this, Player * other) {
 	if ( this->x==other->x && ! this->y == ! other->y) {
 		return true;
	}

	return false;
}
char * PlayertoString(Player * this) {
	char * str = malloc(sizeof(char *) * 29);
	sprintf(str, "<Player object at %p>\n", this);
	return str;
}
void PlayerPlayer(Player * this, int x, int y) {
	this->Playerup = &Playerup;
	this->Playerdown = &Playerdown;
	this->Playerright = &Playerright;
	this->Playerleft = &Playerleft;
	this->Playereq = &Playereq;
	this->PlayertoString = &PlayertoString;
	this->x = x;
	this->y = y;
}
typedef struct Box {
 	Player * player;
	void (*Boxcheck_player)(struct Box *);
	char * (*BoxtoString)(struct Box *);
} Box;
void Boxcheck_player(Box * this) {
 	if ( this->player->x>1) {
 		printf("outside the box\n");
	}
	else {
 		printf("inside the box\n");
	}

}
char * BoxtoString(Box * this) {
	char * str = malloc(sizeof(char *) * 26);
	sprintf(str, "<Box object at %p>\n", this);
	return str;
}
void BoxBox(Box * this, Player * player) {
	this->Boxcheck_player = &Boxcheck_player;
	this->BoxtoString = &BoxtoString;
	this->player = player;
}
void x(Player * p) {
 	p->Playerup(p);
	printf("\nx=%d\n", p->y);
}
int main() {
 	Integer * n1 = malloc(sizeof(Integer));
	IntegerInteger(n1, 1);
	Integer * n2 = malloc(sizeof(Integer));
	IntegerInteger(n2, 1);
	n1->Integerfree(n1);
	printf("%d\n", n1->Integereq(n1, n2));
	printf("%d\n", n1->Integergt(n1, n2));
	printf("%d\n", n1->Integergte(n1, n2));
	printf("%d\n", n1->Integerlt(n1, n2));
	printf("%d\n", n1->Integerlte(n1, n2));
	return 0;
}
