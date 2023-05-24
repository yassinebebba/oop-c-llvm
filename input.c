int printf(char *, ...);

class Point {
    int x;
    int y;
    Point(int x, int y) {
        this->x = x;
        this->y = y;
    }

    int get_x() {
        return this->x;
    }

    int get_y() {
        return this->y;
    }

    void set_x(int x) {
        this->x = x;
    }
}

class Target {

    int get_t() {
    return 1;
    }

}

int main() {
    Point p = new Point(1, 2);
    p.set_x(10);
    printf("%d %d\n", p.x, p.y);
    printf("%d\n", p.get_x());
    printf("%d\n", p.get_y());
    Target t = new Target();
    printf("%d\n", t.get_t());
    return 0;
}