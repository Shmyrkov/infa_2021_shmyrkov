#include <iostream>

int main()
{
    int dlin, abil, n, ost = 0;
    bool flag = false;
    std::cin >> dlin >> abil;
    std::cin >> n;
    int* koords = new int[n];
    for (int i = 0; i < n; i++)
    {
        std::cin >> koords[i];
    }
    int self_coord = 0;
    int ost_number = 0;
    while (self_coord < dlin - abil)
    {
        if ((koords[ost_number] - self_coord <= abil) and (ost_number < n))
        {
            ost_number++;
            flag = true;
        }
        else {
            if (flag == true)
            {
                self_coord = koords[ost_number - 1];
                ost++;
                flag = false;
            }
            else
            {
                ost = -1;
                break;
            }
        }
    }
    std::cout << ost;
}
