int printf(char *, ...);

int T = 1;
char d;
class Player {
    int x;
    int y;
    void Player(int x, int y) {
        this->x = x;
        this->y = y;
    }

    int getx() {
        return this->x;
    }

    int gety() {
        return this->y;
    }
}

int main() {
    Player player = new Player(1, 2);
    char * fmt = "player.x = %d\n"
                 "player.y = %d\n"
                 "player.getx() = %d\n"
                 "player.gety() = %d\n"
                 "add x + y = %d\n"
                 "add getters x + y = %d\n";
    printf(fmt, player.x, player.y, player.getx(), player.gety(),
                player.x + player.y,player.getx()+ player.gety());
    return 0;
}