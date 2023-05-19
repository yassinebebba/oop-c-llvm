int printf(char *, ...);

class Player {
    short a;
    short int b;
    long c;
    int x;
    int y;
    void Player(int x, long y) {
        this->x = x;
        this->y = y;
    }

    int get_x() {
        return this->x + this->get_y() + 2;
    }

    int get_y() {
        return this->y;
    }

    char * __repr__() {
        return "This is a Player object\n";
    }
}


class Target {
    int a;
    Player player;
//    void Target(Player player) {
//        this->a = 1;
//        this->player = player;
//    }
//    int test(Player player) {
//        printf("player.x = %d\n", player.x);
//    }
    int get_a() {
        return this->a;
    }
}

int main() {
    Player player = new Player(1, 2);
//    Target target = new Target(player);
//    printf("target.a = %d\n", target.a);
    char * fmt = "player.x = %d\n"
                 "player.y = %d\n"
                 "player.getx() = %d\n"
                 "player.gety() = %d\n"
                 "add x + y = %d\n"
                 "add getters x + y = %d\n";
    printf(fmt,
           player.x,
           player.y,
           player.get_x(),
           player.get_y(),
           player.x + player.y,
           player.get_x() + player.get_y()
           );
    printf("%s", player.__repr__());
    return 0;
}