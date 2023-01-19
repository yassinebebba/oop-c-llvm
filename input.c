#include <stdio.h>
#include <stdlib.h>

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
    char * toString() {
        char * str;
        // this syntax should error
        // asdad
        sprintf(str, "<Player object at %p>", this);
        // printf("%s\n", str);
        // return local variable will be garbage collected
        return str;
    }
    char * __repr__() {
        char * str;
        // this syntax should error
        // asdad
        sprintf(str, "Player(x=%d, y=%d)", this->x, this->y);
        // printf("%s\n", str);
        // return local variable will be garbage collected
        return str;
    }
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

int main() {
    Player * player = new Player(0, 0);
    Box * box = new Box(player);
    player->up();
//    box->player->up();
    box->check_player();
    player->up();
    box->check_player();
    player->right();
    box->check_player();
    player->right();
    box->check_player();

    printf("%s\n", player->__repr__());
    return 0;
}