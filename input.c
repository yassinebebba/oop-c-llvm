#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


class Integer {
    int n;

    void Integer(int n) {
        this->n = n;
    }

    bool eq(Integer * other) {
        return this->n == other->n;
    }

    bool gt(Integer * other) {
        return this->n > other->n;
    }

    bool gte(Integer * other) {
        return this->n >= other->n;
    }

    bool lt(Integer * other) {
        return this->n < other->n;
    }

    bool lte(Integer * other) {
        return this->n <= other->n;
    }

    void free() {
        this = NULL;
        free(this);
    }
}


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
        if (this->x == other->x && !this->y == !other->y) {
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
    Integer * n1 = new Integer(1);
    Integer * n2 = new Integer(1);
//    printf("%s", player->toString());
//    printf("%s", p->toString());
//    printf("%s", box->toString());
    n1->free();
    printf("%d\n", n1 == n2);
    printf("%d\n", n1 > n2);
    printf("%d\n", n1 >= n2);
    printf("%d\n", n1 < n2);
    printf("%d\n", n1 <= n2);
    return 0;
}


//int main() {
//    String * string = new String("Yassine");
//    printf("%s", string->toString());
//    Player * player = new Player(0, 0);
//    Player * p = new Player(0, 0);
//    Player * p2 = new Player(0, 0);
//    Box * box = new Box(player);
//    player->up();
//    // this should be fixed:
//    // this works x() without a semicolon, it needs to be x();
//    x(player);
//    box->player->up();
//    box->check_player();
//    player->up();
//    box->check_player();
//    player->right();
//    box->check_player();
//    player->right();
//    box->check_player();
//    printf("%s", player->toString());
//    printf("%s", p->toString());
//    printf("%s", box->toString());
//    printf("%d\n", p2 == p);
//    return 0;
//}