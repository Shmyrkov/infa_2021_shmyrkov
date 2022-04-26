#include <iostream>
#include <stack>
 
using namespace std;
 
int main() {
  string s = "";
  cin >> s;
  stack <char> st;
  bool b = true;
  int sz = int(s.size());
  for (int i = 0; i < sz; i++) {
    if (s[i] == '{' || s[i] == '(' || s[i] == '[')
    {
        st.push(s[i]);
    }
    else if (!st.empty()) 
    {
      if (s[i] == ']')
      {
          if (st.top() != '[')
          {
              b = false; 
              break; 
          } 
          else
            st.pop(); 
      }
      else if (s[i] == ')') 
      {
          if (st.top() != '(')
          {
              b = false; 
              break; 
          } 
          else 
            st.pop(); 
      }
      else if (s[i] == '}') 
      {
          if (st.top() != '{') 
          {
              b = false; 
              break; 
          } 
          else 
            st.pop(); 
      }
    }
    else 
    {
        b = false; 
        break; 
    }
  }
 
  if (int(st.size()) != 0) b = false;
  if (b == true) 
  {
    cout << "yes";
  }
  else 
  {
      cout << "no";
  }
}