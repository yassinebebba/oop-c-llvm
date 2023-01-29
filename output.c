#include <stdio.h>
#include <stdlib.h>

typedef struct Player {
 	int x;
	int y;
	void (*Playerup)(struct Player *);
	void (*Playerdown)(struct Player *);
	void (*Playerright)(struct Player *);
	void (*Playerleft)(struct Player *);
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
char * PlayertoString(Player * this) {
	char * str = malloc(sizeof(char *) * 28);
	sprintf(str, "<Player object at %p>", this);
	return str;
}
void PlayerPlayer(Player * this, int x, int y) {
	this->Playerup = &Playerup;
	this->Playerdown = &Playerdown;
	this->Playerright = &Playerright;
	this->Playerleft = &Playerleft;
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
	char * str = malloc(sizeof(char *) * 25);
	sprintf(str, "<Box object at %p>", this);
	return str;
}
void BoxBox(Box * this, Player * player) {
	this->Boxcheck_player = &Boxcheck_player;
	this->BoxtoString = &BoxtoString;
	this->player = player;
}
void x(Player * p) {
 	p->Playerup(p);
	printf("x=%d\n", p->y);
}
int main() {
 	Player * player = malloc(sizeof(Player));
	PlayerPlayer(player, 0, 0);
	Player * p = malloc(sizeof(Player));
	PlayerPlayer(p, 0, 0);
	Box * box = malloc(sizeof(Box));
	BoxBox(box, player);
	player->Playerup(player);
	x(player);
	box->player->Playerup(player);
	box->Boxcheck_player(box);
	player->Playerup(player);
	box->Boxcheck_player(box);
	player->Playerright(player);
	box->Boxcheck_player(box);
	player->Playerright(player);
	box->Boxcheck_player(box);
	printf("%s\n", player->PlayertoString(player));
	printf("%s\n", p->PlayertoString(p));
	printf("%s\n", box->BoxtoString(box));
	return 0;
}
