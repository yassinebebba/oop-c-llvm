int printf(char *, ...);

int T = 1;
char d;
class Player {
    short a;
    short int b;
    long c;
    int x;
    int y;
    void Player(int x, int y) {
        this->x = x;
        this->y = y;
    }

    int getx() {
        return this->x + this->gety() + -+-+-+-2;
    }

    int gety() {
        return this->y;
    }

    char * __repr__() {
        return "This is a Player object\n";
    }
}


class Target {
    int a;
    Player player;
//    int test(Player player) {
//        return 1;
//    }
    int geta() {
        return this->a;
    }
}

int main() {
    Player player = new Player(1, 2);
    Target target =  new Target();
//    long a = 62;
//    printf("hey %d\n", target.test(player));
    printf("hey %d\n", target.geta());
    char * fmt = "player.x = %d\n"
                 "player.y = %d\n"
                 "player.getx() = %d\n"
                 "player.gety() = %d\n"
                 "add x + y = %d\n"
                 "add getters x + y = %d\n";
    printf("hey\n");
    printf(fmt,
           player.x,
           player.y,
           player.getx(),
           player.gety(),
           player.x + player.y,
           player.getx() + player.gety()
           );
    printf("%s", player.__repr__());
    return 0;
}