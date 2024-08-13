int printf(char *, ...);

class Point1D {
    int x;
    Point1D(int x) {
        this->x = x;
    }

    int getX() {
        return this->x;
    }
}

class Point2D {
    Point1D * p1d;
    int y;
    Point2D(Point1D * p1d, int y) {
        this->p1d = p1d;
        this->y = y;
    }

    int getX() {
        return this->p1d->getX();
    }

    int getY() {
        return this->y;
    }
}

class Point3D {
    Point2D * p2d;
    int z;
    Point3D(Point2D * p2d, int z) {
        this->p2d = p2d;
        this->z = z;
    }

    int getX() {
        return this->p2d->getX();
    }

    int getY() {
        return this->p2d->getY();
    }

    int getZ() {
        return this->z;
    }
}


int main() {
    long * x = "asdasdadadaa";
    printf("%s\n", x);
    Point1D p1d = new Point1D(10);
    Point2D p2d = new Point2D(p1d, 20);
    Point3D p3d = new Point3D(p2d, 30);
    p3d.z = 155;
    printf("%d %d %d\n", p3d.getX(), p3d.getY(), p3d.getZ());
    return 0;
}

