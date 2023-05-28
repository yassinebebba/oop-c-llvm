int printf(char *, ...);

class Point1D {
    int x;
    Point1D(int x) {
        this->x = x;
    }

    int get_x() {
        return this->x;
    }
}

class Test {
    Point1D * p1d;
    Test(Point1D * p1d) {
        this->p1d = p1d;
    }
}

int main() {
    Point1D p1d = new Point1D(10);
    Test t = new Test(p1d);
    p1d.x = 20;
    Point1D p1d2 = new Point1D(30);
    t.p1d = p1d2;
    printf("1D point: (%d)\n", t.p1d->get_x());
    return 0;
}

