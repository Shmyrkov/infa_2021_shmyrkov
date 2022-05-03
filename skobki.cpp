#include <iostream>
#include <string>
using std::string;


bool skob(string seq, char *arr, int l){
    int p = 0;
    if (l%2 == 1)
        return false;
    for (int i=0; i<l; i++) 
    {
        if ((seq[i] == '(') || (seq[i] == '[') || (seq[i] == '{')) 
        {
            arr[p] = seq[i];
            p++;
        } 
        else 
        {
            if (p == 0)
                return false;
            if (seq[i] == ')')
            {
                if (arr[p - 1] != '(')
                {
                    return false;
                }
                p--;
            }
            if (seq[i] == ']')
            {
                if (arr[p - 1] != '[')
                {
                    return false;
                }
                p--;
            }
            if (seq[i] == '}')
            {
                if (arr[p - 1] != '{')
                {
                    return false;
                }
                p--;
            }
        }
    }
    if (p == 0)
        return true;
    else
        return false;
}


int main() {
    string seq = "(([{}]))[]{}";
    int l = seq.length();
    char* arr = new char[l/2];
    std::cout << skob(seq, arr, l);
    delete[] arr;
}
