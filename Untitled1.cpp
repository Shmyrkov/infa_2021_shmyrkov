#include <iostream>
#include <cstdlib>
#include <cstring>

void generic_swap(void *lha, void *rha, std::size_t element_byte_size)
{
    void * tmp = malloc(element_byte_size);
    std::memcpy(tmp, lha, element_byte_size);
    std::memcpy(lha, rha, element_byte_size);
    std::memcpy(rha, tmp, element_byte_size);
    free(tmp);

}

int compare(const void *a, const void *b)
{
    int q = *(const int *)a;
    int c = *(const int *)b;
    return (c<q) - (q<c);
}

void qsort(void *src_begin, size_t n_memb, size_t type_size, int(*compare)(const void *, const void *))
{
    int i = 0;
    int j = n_memb - 1;
    const char *p = (const char *)src_begin + n_memb * type_size / 2 ;
    do
    {
        while (compare((const char *)src_begin + i*type_size, p)<0)
        {
            i++;
        }
        while (compare((const char *)src_begin + j*type_size, p)>0)
        {
            j--;
        }
        if (i<=j)
        {
            generic_swap((char *)src_begin+i*type_size, (char *)src_begin + j*type_size, type_size);
            i++;
            j++;

        }
    } while (i<=j);

    if (j>0)
    {
        qsort (src_begin, j+1, type_size, (*compare));
    }
    if (i<n_memb)
    {
        qsort(src_begin + i*type_size, n_memb - i, type_size, (*compare));
    }
}

int main()
{
    int arr[3] = {2, 1, 5};
    qsort(arr, 3, sizeof(int), (*compare));
    std::cout<<arr[0];
}
