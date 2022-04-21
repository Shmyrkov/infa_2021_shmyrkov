#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;


int main()
{
    int n, w;
    cin >> n;
    int* price = new int[n];
    int* len = new int[n];
    cin >> w;
    int** das = new int* [n];
    for (int i = 0; i < n; i++)
    {
        cin >> len[i] >> price[i];
    }
    for (int i = 0; i < n; ++i)
    {
        das[i] = new int[w+1];
    }
    for (int j = 0; j < w; j++) {
        das[0][j] = 0;
    }

    for (int i = 1; i < n; i++)
    {
        for (int c = 0; c <= w; c++)
        {
            if (c <= len[i] - 1)
            {
                das[i][c] = das[i - 1][c];
            }
            if (c >= len[i])
            {
                das[i][c] = max(das[i - 1][c], das[i][c - len[i]] + price[i]);
            }
        }
    }
    cout<<das[n-1][w];
}
