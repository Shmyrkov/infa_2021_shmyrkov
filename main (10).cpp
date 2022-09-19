#include <iostream>
#include <string>
using namespace std;
 
string expr;
uint32_t i = 1;
int oper_place1 = 0;
int oper_place2 = 0;
int k = 0;

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

pair<int, int> chisl1 (int a1, int b1)
{
  bool b = false;
  while (i < expr.size()) {
    if (expr[i] == ')') break;
    if (expr[i] == ' ' or expr[i] == '(' ) continue;
    if (expr[i] == ',') 
    {
      b = true;
      ++i;
    }
    if (b==false) 
    {
      a1 *= 10;
      a1 += expr[i] - '0';
    } 
    else 
    {
      b1 *= 10;
      b1 += expr[i] - '0';
    }
    ++i;
  }
  return {a1, b1};
  
}

void place1()
{
    
    while ( k<expr.size() )
    {
        k++;
        if (expr[k] == '*' or expr[k] == '+') {
            break;
        }
    }
}
    
bool check2()
{
    int f = 0;
    int l = 0;
    while (l<expr.size())
    {
        if (expr[l] == ')') f++;
        l++;
    }
    if (f==3) return true;
    else return false;
}
    

 

int main()
{
    getline(cin, expr);
    int a1 = 0, a2 = 0, b1 = 0, b2 = 0, c1 = 0, c2 =0, o = 0;
    auto res = chisl1(a1,b1);
    Point q(res.first,res.second);
    Rectangle t(q);
    i+=5;
    auto res2 = chisl1(b1,b2);
    Point v(res2.first,res2.second);
    Rectangle plus = t + v;
    Rectangle umn = t * v;
    place1();
    check2();
    if (check2() == false) 
    {
        if (expr[k] == '*') umn.print2();
        else plus.print2();
    }
    else 
    {
        o = k;
        k++;
        i+=5;
        auto res3 = chisl1(a1,b1);
        place1();
        Point g(res3.first,res3.second);
        Rectangle l(g);
        Rectangle pl = plus + l;
        Rectangle umnn = umn * l;
        Rectangle plumn = umn + l;
        Rectangle umn2 = l*v;
        Rectangle last = t + umn2;
        if (expr[o]=='+' and expr[k]=='+') pl.print2();
        if (expr[o]=='*' and expr[k]=='*') umnn.print2();
        if (expr[o]=='*' and expr[k]=='+') plumn.print2();
        if (expr[o]=='+' and expr[k]=='*') last.print2();
    }
}
