#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


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
 	if (this->x == other->x) {
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
 	if (this->player->x > 1) {
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
 	String * string = malloc(sizeof(String));
	StringString(string, "Yassine");
	printf("%s", string->StringtoString(string));
	Player * player = malloc(sizeof(Player));
	PlayerPlayer(player, 0, 0);
	Player * p = malloc(sizeof(Player));
	PlayerPlayer(p, 0, 0);
	Player * p2 = malloc(sizeof(Player));
	PlayerPlayer(p2, 0, 0);
	Box * box = malloc(sizeof(Box));
	BoxBox(box, player);
	player->Playerup(player);
	x(player);
	box->player->Playerup(box->player);
	box->Boxcheck_player(box);
	player->Playerup(player);
	box->Boxcheck_player(box);
	player->Playerright(player);
	box->Boxcheck_player(box);
	player->Playerright(player);
	box->Boxcheck_player(box);
	printf("%s", player->PlayertoString(player));
	printf("%s", p->PlayertoString(p));
	printf("%s", box->BoxtoString(box));
	printf("%d\n", p2->Playereq(p2, p));
	return 0;
}
