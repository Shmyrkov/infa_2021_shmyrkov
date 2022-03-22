#include <iostream>
#include <random>

void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

void qsort(int *array, int size)
{
    int i = 0;
    int j = size - 1;
    int p = array[size/2];
    do
    {
        while (array[i] < p)
        {
            ++i;
        }
        while (array[j] > p)
        {
            --j;
        }
        if (i<=j)
        {
            swap(array[i], array[j]);
            ++i;
            --j;
        }
    } while (i<=j);

    if (j>0)
    {
        qsort(array, j+1);
    }
    if (i<size)
    {
        qsort(&array[i], size - i)
    }
}

int main()
{
    int n = 10;
    int* array = new int[n];
    for (int u=0; u<n; u++){
        array[u] = n-u;
    }
    qsort(array, n)
}
