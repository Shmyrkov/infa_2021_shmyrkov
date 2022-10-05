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

template <typename T, typename Comp>
void hoarasort(T * a, int first, int  last)
{

    Comp cmp;
    int i = first, j = last;
    T tmp = 0, x = a[(first + last) / 2];

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
        hoarasort<T, Comp>(a, i, last);
    if (cmp(first , j))
        hoarasort<T, Comp>(a, first,j);
}


int main()
{

    float a[5] = {4.565, 1.567, 5, 29, 2.32};
    hoarasort<float, FloatComparator>(a, 0, 5-1);
    for (int i=0; i<5; i++)
    {
        cout<<a[i]<< ' '  ;

    }
}
