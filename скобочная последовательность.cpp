#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

int compare(const void * x1, const void * x2)
{
    return ( *(int*)x1 - *(int*)x2 );
}

void swap(void* x1, void* x2, size_t size)
{
    void* save = malloc(size);
    memcpy(save, x1, size);
    memcpy(x1, x2, size);
    memcpy(x2, save, size);
    free(save);
}

void qqsort (void * first, size_t number, size_t size, int (*comparator) (const void *, const void*))
{
    void *baze = (char *) first + (number - 1) * size;
    int i = 0;
    for (int j = 0; j < number; j++)
    {
        if (comparator((char *) first + j * size, baze) <= 0)
        {
            swap((char *) first + j * size, (char *) first + i * size, size);
            i = i + 1;
        }
    }

    if (i - 1 > 1)
        qqsort(first, i - 1, size, compare);
    if (number - i > 1)
        qqsort((char*) first + i * size, number - i, size, compare);
}

int main()
{
    int n = 0;
    cin>>n;
    int *mass1 = new int[n];
    for (int i = 0; i < n; i++) 
    {
        cin>>mass1[i];
    }
    qqsort(mass1, n, sizeof(int), compare);

    for (int i = 0; i < n; i++)
    {
        cout<<mass1[i]<<" ";
    }
    delete [] mass1;
}
