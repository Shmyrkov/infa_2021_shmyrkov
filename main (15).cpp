#include <iostream>
using namespace std;

template <typename T>
struct Comparator 
{
    virtual bool operator()(T const &, T const &) const = 0;

};

struct IntComparator final: Comparator<int> 
{
    bool operator()(int const &lha, int const &rha) const override 
    {
        return (lha < rha);
    }
};


template <typename T>
void hoarasort(T * a, int first, int  last)
{
    auto cmp = IntComparator();
    auto i = first, j = last;
    auto tmp = 0, x = a[(first + last) / 2];
 
    do {
        while (cmp(a[i], x))
            i++;
        while (cmp(a[j] , x))
            j--;
 
        if (cmp(i , j) )
        {
            if (cmp(i , j))
            {
                tmp=a[i];
                a[i]=a[j];
                a[j]=tmp;
            }
        i++;
        j--;
        }
        } while (cmp(i , j));
 
    if (cmp(i , last))
        hoarasort(a, i, last);
    if (cmp(first , j))
        hoarasort(a, first,j);
}


int main()
{

    int a[4] = {1, 4, 5, 2};
    hoarasort(a, 0, 4-1);
    for (int i=0; i<4; i++)
    {
        cout<<a[i]<< ' '  ;
        
    }
}
