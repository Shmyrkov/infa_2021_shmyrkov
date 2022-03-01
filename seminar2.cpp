#include <iostream>

void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

void vsort(int *array, int size)
{
    for (int i = 0; i < size; ++i)
    {
        int max_id = 0;
        for (int j = 0; j < size - i; j++)
        {
            if (array[j] > array[max_id])
            {
                max_id = j;
            }
        }
        swap(array[size-i-1], array[max_id]);
    }
}

int main()
{
    int n = 5;
    int* array = new int[n];
    for (int u=0; u<n; u++){
        std::cin>>array[u];
    }
    vsort(array, n);
    for (int u=0; u<5; u++)
    {
        std::cout<<array[u]<<" ";
    }
}
