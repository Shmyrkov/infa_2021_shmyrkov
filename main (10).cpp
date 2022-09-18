#include <iostream>
#include <string>
using namespace std;

struct Point 
{
 
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
 
    void print1() const {
        cout<<'('<<x<<','<<y<<')';
    }
 
};
 
class Rectangle
{
 
    Point a;
 
public:
    
    Rectangle(): a(Point(0, 0)) {}
 
    Rectangle(Point const &point): a(point) {}
 
    Rectangle operator+(const Rectangle &c) 
    { 
        Point q = c.a.maxx(this->a).maxy(this->a);
	    return Rectangle(q);
    }
 
    Rectangle operator*(const Rectangle &c) 
    { 
        Point q = c.a.minx(this->a).miny(this->a);
	    return Rectangle(q);
    }
 
    void print2() const 
    {
        a.print1();
    }
};

 

int main()
{
    char a, b, c, d;
    int a1,b1,c1,d1;
    string s;
    getline(cin, s);
    int k = 0;
    for (auto i : s)
    {
        int u = int(i);
        if ((int(i) >= 48) & (int(i) <= 58))
        {
            if (k == 0) a = i;
            if (k == 1) b = i;
            if (k == 2) c = i;
            if (k == 3) d = i;
            k++;
        }
    }
    a1 = a - '0';
    b1 = b - '0';
    c1 = c - '0';
    d1 = d - '0';
    Point q(a1,b1);
    Point w(c1,d1);
    Rectangle e(q);
    Rectangle r(w);
    Rectangle plus = e + r;
    Rectangle umn = e*r;
    if (s[6]=='*') umn.print2();
    else plus.print2();
    
    
}