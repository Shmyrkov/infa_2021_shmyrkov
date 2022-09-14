#include <iostream>
using namespace std;

struct Point {

    unsigned long long const x,y;

    Point(unsigned long long x, unsigned long long y):
        x(x), y(y) { }

    Point minx(Point const &rha) const {
        return Point(rha.x < x ? rha.x : x, y);
    }

    Point miny(Point const &rha) const {
        return Point(x, rha.y < y ? rha.y : y);
    }

    Point maxx(Point const &rha) const {
        return Point(rha.x > x ? rha.x : x, y);
    }

    Point maxy(Point const &rha) const {
        return Point (x, rha.y > y ? rha.y : y);
    }

    void print() const {
        cout<<'('<<x<<','<<y<<')';
    }

};

class Rectangle
{
    Point x;
public:
    Rectangle operatorr+(Rectangle const &rha) const {
        return Rectangle
    }

    }
};

int main()
{
    Point b(10, 15);
    Point a(5, 3);
    b.minx(a).print();
    b.miny(a).minx(a).print();
}
