#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


class String {
    char * string;
    void String(char * string) {
        this->string = string;
    }

    char * toString() {
        return this->string;
    }
}

class Player {
    int x;
    int y;
    void Player(int x, int y) {
        this->x = x;
        this->y = y;
    }
    void up() {
      // ++this->y;
      this->y += 1;
    }
    void down() {
        this->y -= 1;
    }
    void right() {
        this->x += 1;
    }
    void left() {
        this->x -= 1;
    }
    bool eq(Player * other) {
        if (this->x == other->x) {
            return true;
        }
        return false;
    }
//    char * toString() {
//        char * str;
//        sprintf(str, "<Player object at %p>", this);
//        return str;
//    }
}

class Box {
    Player * player;
    void Box(Player * player) {
        this->player = player;
    }
    void check_player() {
        if (this->player->x > 1) {
            printf("outside the box\n");
        } else {
            printf("inside the box\n");
        }
    }
}

void x(Player * p) {
    p->up();
    printf("\nx=%d\n", p->y);
}

int main() {
    String * string = new String("Yassine");
    printf("%s", string->toString());
    Player * player = new Player(0, 0);
    Player * p = new Player(0, 0);
    Player * p2 = new Player(0, 0);
    Box * box = new Box(player);
    player->up();
    // this should be fixed:
    // this works x() without a semicolon, it needs to be x();
    x(player);
    box->player->up();
    box->check_player();
    player->up();
    box->check_player();
    player->right();
    box->check_player();
    player->right();
    box->check_player();
    printf("%s", player->toString());
    printf("%s", p->toString());
    printf("%s", box->toString());
    printf("%d\n", p2->eq(p));
    return 0;
}