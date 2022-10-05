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

struct DoubleComparator final: Comparator<double>
{
    bool operator()(double const &lha, double const &rha) const override
    {
        return (lha < rha);
    }
};

struct FloatComparator final: Comparator<float>
{
    bool operator()(float const &lha, float const &rha) const override
    {
        return (lha < rha);
    }
};

template <typename T>
void hoarasort(T * a, int first, int  last)
{
    auto cmp = DoubleComparator();
    int i = first, j = last;
    auto tmp = 0, x = a[(first + last) / 2];

    do {
        while (cmp(a[i],x))
            i++;
        while (!cmp(a[j], x) and (a[j]!=x))
            j--;

        if (i<=j)
        {
            if ((i < j))
            {
                tmp=a[i];
                a[i]=a[j];
                a[j]=tmp;
            }
            i++;
            j--;
        }
    } while (i <=j);

    if (cmp(i , last))
        hoarasort(a, i, last);
    if (cmp(first , j))
        hoarasort(a, first,j);
}


int main()
{

    double a[5] = {4.54, 1.3, 5, 29.23, 1.2};
    hoarasort<double>(a, 0, 5-1);
    for (int i=0; i<5; i++)
    {
        cout<<a[i]<< ' '  ;

    }
}
