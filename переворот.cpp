#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::string;


bool isBalanced(string seq){
    int l = seq.length();
    int p = 0;
    if (l%2 == 1)
        return false;
    char arr[l/2];
    for (int i=0; i<l; i++) {
        if ((seq[i] == '(') || (seq[i] == '[') || (seq[i] == '{') || (seq[i] == '<')) {
            arr[p] = seq[i];
            p++;
        } else {
            if (p == 0)
                return false;
            switch (seq[i]) {
                case ')':
                    if (arr[p - 1] != '(')
                        return false;
                    p--;
                    break;
                case ']':
                    if (arr[p - 1] != '[')
                        return false;
                    p--;
                    break;
                case '}':
                    if (arr[p - 1] != '{')
                        return false;
                    p--;
                    break;
                case '>':
                    if (arr[p - 1] != '<')
                        return false;
                    p--;
                    break;
            }
        }
    }
    if (p == 0)
        return true;
    else
        return false;
}


int main() {
    string seq = "([])<>([{}])<()>[]";
    cout << isBalanced(seq);
}
