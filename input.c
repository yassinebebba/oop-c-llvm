int printf(char *, ...);

class Point1D {
    int x;
    Point1D(int x) {
        this->x = x;
    }

    int get_x() {
        return this->x;
    }

    int get_y() {
        return this->y;
    }
}

int main() {
    Point1D p1d = new Point1D(10);
    printf("1D point: (%d)\n", p1d.get_x());
    return 0;
}