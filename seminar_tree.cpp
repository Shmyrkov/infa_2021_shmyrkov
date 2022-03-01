#include <iostream>

int s = 1;

void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

void tree_sort(int *array, int size)
{
    for (int i = 0; i < size/2 ; ++i)
    {
        if (array[i]<array[2*i+2])
        {
            swap(array[i], array[2*i+2]);
        }
        if (array[i]<array[2*i+1])
        {
            swap(array[i], array[2*i+1]);
        }
    }
    if (s+1>=5)
    {
        return;
    }
    else
    {
        swap(array[0], array[size-s]);
        s++;
        tree_sort(array, size-s);
    }
        
}

int main()
{
    int n = 5;
    int* array = new int[n];
    for (int u=0; u<n; u++){
        std::cin>>array[u];
    }
    tree_sort(array, n);
    for (int u=0; u<n; u++)
    {
        std::cout<<array[u];
    }
}
