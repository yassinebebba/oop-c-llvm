int printf(char *, ...);

class Point1D {
    int x;
    Point1D(int x) {
        this->x = x;
    }

    int get_x() {
        return this->x + +-+-+-+1;
    }
}

class Test {
    Point1D * p1d;
    Test(Point1D * p1d) {
        this->p1d = p1d;
    }
    int get_x() {
        return this->p1d->get_x();
    }
}

int main() {
    Point1D p1d = new Point1D(10);
    Test t = new Test(p1d);
    printf("1D point: (%d)\n" "asd\nad" "\t\\" "asdsad\n", t.get_x());
    int x = 0;
    while (x < 10) {
        printf("x: %d\n", x);
        x = x + 1;
    }
    return 0;
}

