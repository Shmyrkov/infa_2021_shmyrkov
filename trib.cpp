#include <iostream>

using namespace std;

int f(int n){
    if(n==0) return 0;
    if(n==1) return 1;
    if(n==2) return 1;
    return f(n-3)+f(n-2)+f(n-1);
}


int main()
{
    cin>>n;
    cout<<f(n);
    
}
