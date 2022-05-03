#include <iostream>
#include <string>
using std::string;

bool skob(string seq){
    int l = seq.length();
    int p = 0;
    if (l%2 == 1)
        return false;
    char* arr = new char[l/2];
    for (int i=0; i<l; i++) {
        if ((seq[i] == '(') || (seq[i] == '[') || (seq[i] == '{')) {
            arr[p] = seq[i];
            p++;
        } else {
            if (p == 0)
                return false;
            if (seq[i] == ')')
            {
                if (arr[p - 1] != '(')
                {
                    break;
                }
                p--;
            }
            if (seq[i] == ']')
            {
                if (arr[p - 1] != '[')
                {
                    break;
                }
                p--;
            }
            if (seq[i] == '}')
            {
                if (arr[p - 1] != '{')
                {
                    break;
                }
                p--;
            }
            }
        }
    delete[] arr;
    if (p == 0)
        return true;
    else
        return false;
}


int main() {
    string seq = "(([{}]))";
    std::cout << skob(seq);
}
