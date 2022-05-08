#include <iostream>
using namespace std;

void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

void Heapify(int *array, int n, int i)
{
    int left = 2*i + 1;
    int right = 2*i + 2;
    int largest = i;
    if (left < n and array[left] > array[largest])
    {
        largest = left;
    }
    if (right < n and array[right] > array[largest])
    {
        largest = right;
    }
    if (largest != i)
    {
        swap(array[largest], array[i]);
        Heapify(array, n, largest);
    }
}

void Build_Heap(int *array, int n)
{
    for (int i = n/2 - 1; i >= 0; i--)
    {
        Heapify(array, n, i);
    }
}

void Heap_sort(int *array, int n)
{
    Build_Heap(array, n);
    for (int i = n-1; i >= 0; i--)
    {
        swap(array[0], array[i]);
        Heapify(array, i, 0);
    }
}

void print(int *array, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << array[i] << " ";
    }
}

int main()
{
    int n = 5;
    int* array = new int[n];
    for (int u = 0; u < n; u++)
    {
        cin>>array[u];
    }
    Heap_sort(array, n);
    print(array, n);
    delete[] array;
}
