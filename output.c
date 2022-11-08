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
	char * (*Player__repr__)(struct Player *);
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
 	char * str;
	sprintf(str, "<Player object at %p>", this);
	return str;
}
char * Player__repr__(Player * this) {
 	char * str;
	sprintf(str, "Player(x=%d, y=%d)", this->x, this->y);
	return str;
}
void PlayerPlayer(Player * this, int x, int y) {
	this->Playerup = &Playerup;
	this->Playerdown = &Playerdown;
	this->Playerright = &Playerright;
	this->Playerleft = &Playerleft;
	this->PlayertoString = &PlayertoString;
	this->Player__repr__ = &Player__repr__;
	this->x = x;
	this->y = y;
}
typedef struct Box {
 	Player * player;
	void (*Boxcheck_player)(struct Box *);
} Box;
void Boxcheck_player(Box * this) {
 	if (this->player->x > 1) {
 		printf("outside the box\n");
	}
	else {
 		printf("inside the box\n");
	}

}
void BoxBox(Box * this, Player * player) {
	this->Boxcheck_player = &Boxcheck_player;
	this->player = player;
}
int main() {
 	Player * player = malloc(sizeof(Player));
	PlayerPlayer(player, 0, 0);
	Box * box = malloc(sizeof(Box));
	BoxBox(box, player);
	player->Playerup(player);
	box->Boxcheck_player(box);
	player->Playerup(player);
	box->Boxcheck_player(box);
	player->Playerright(player);
	box->Boxcheck_player(box);
	player->Playerright(player);
	box->Boxcheck_player(box);
	printf("%s\n", player->Player__repr__(player));
	return 0;
}
