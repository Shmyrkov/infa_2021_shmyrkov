#include <iostream>
#include <string>
using namespace std;
 
struct Point {
  int x, y;
 
  Point(unsigned long long x, unsigned long long y) :
      x(x), y(y) {}
 
  Point minx(Point const& rha) const {
    return Point(rha.x < x ? rha.x : x, y);
  }
 
  Point miny(Point const& rha) const {
    return Point(x, rha.y < y ? rha.y : y);
  }
 
  static Point conj(const Point& arg_1, const Point& arg_2) {
    return Point(min(arg_1.x, arg_2.x), min(arg_1.y, arg_2.y));
  }
 
  static Point disj(const Point& arg_1, const Point& arg_2) {
    return Point(max(arg_1.x, arg_2.x), max(arg_1.y, arg_2.y));
  }
};
 
class Rectangle {
  Point point;
 
 public:
  Rectangle() : point(Point(0, 0)) {}
 
  Rectangle(Point const& point) : point(point) {}
 
  Rectangle operator+(const Rectangle& c) {
    Point res_point = Point::disj(point, c.point);
    return Rectangle(res_point);
  }
 
  Rectangle operator*(const Rectangle& c) {
    Point res_point = Point::conj(point, c.point);
    return Rectangle(res_point);
  }
 
  Point get_point() {
    return point;
  }
};
 
Rectangle get_coord(const string& expr, int begin, int end) { // [begin, end)
  bool b = false;
  int i = begin;
  Point point(0, 0);
  while (i < end) {
    if (expr[i] == ')') break;
    if (expr[i] == ' ' or expr[i] == '(') {
      ++i;
      continue;
    }
    if (expr[i] == ',') {
      b = true;
      ++i;
      continue;
    }
    if (!b) {
      point.x *= 10;
      point.x += expr[i] - '0';
    } else {
      point.y *= 10;
      point.y += expr[i] - '0';
    }
    ++i;
  }
  return Rectangle(point);
}
 
int find_operator(const string& expr, int begin, int end, char op) {
  int res = end;
  for (int i = begin; i < end; ++i) {
    if (expr[i] == op) {
      res = i;
      break;
    }
  }
  return res;
}
 
Rectangle conj(const string& expr, int begin, int end) {
  int conj_pos = find_operator(expr, begin, end, '*');
  if (conj_pos == end) {
    return get_coord(expr, begin, end);
  } else {
    Rectangle left_operand = conj(expr, begin, conj_pos - 1);
    Rectangle right_operand = conj(expr, conj_pos + 1, end);
    return left_operand * right_operand;
  }
}
 
Rectangle get_ans(const string& expr, int begin, int end) {
  int disj_pos = find_operator(expr, begin, end, '+');
  if (disj_pos == end) {
    conj(expr, begin, end);
  } else {
    Rectangle left_operand = get_ans(expr, begin, disj_pos - 1);
    Rectangle right_operand = get_ans(expr, disj_pos + 1, end);
    auto left_point = left_operand.get_point();
    auto right_point = right_operand.get_point();
    return left_operand + right_operand;
  }
}
 
int main() 
{
  while (true) 
  {
    string expr;
    getline(cin, expr);
    Rectangle res = get_ans(expr, 0, expr.size());
    Point point = res.get_point();
    cout << "x = " << point.x << "\ny = " << point.y << '\n';
  }
  return 0;
}
