#include <iostream>
#include <random>


int* Rand_coords_x(int* x_coords, int numb, int razm)
{
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<int>dist(0, razm);
    std::uniform_real_distribution<double> dist2(0, 1);
    for (int i = 0; i < numb; ++i) {
        x_coords[i] = dist(rng);
    }
    return x_coords;

}

int* Rand_coords_y(int* y_coords, int numb, int razm)
{
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<int>dist(0, razm);
    std::uniform_real_distribution<double> dist2(0, 1);
    for (int i = 0; i < numb; ++i) {
        y_coords[i] = dist(rng);
    }
    return y_coords;

}

int* Kasanie_check(int* x_coords, int* y_coords, int numb, int* life, int size)
{
    for (int i = 0; i < numb; ++i)
    {
        if (x_coords[i] == 0 or x_coords[i] == size or y_coords[i] == 0 or y_coords[i] == size)
        {
            life[i] = 0;
        }
        for (int j = 0; j < numb; ++j)
        {
            if ((abs((x_coords[i] - x_coords[j])) == 1 or abs(y_coords[i] - y_coords[j]) == 1))
            {
                life[i] = 0;
                life[j] = 0;
            }
        }
    }
    return life;

}

int* check_sonapr_x(int* x_coords, int numb, int* life, int napr)
{
    for (int i = 0; i < numb; i++)
    {
        for (int j = 0; j < numb; j++)
        {
            if ((x_coords[i] == x_coords[j]) and i != j)
            {
                x_coords[i] = x_coords[i] + 1 * napr;

            }
        }
    }
    return x_coords;
}

int* mooving_x(int* x_coords, int numb, int* life)
{
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<int>dist(0, 100);
    std::uniform_real_distribution<double> dist2(0, 1);
    for (int i = 0; i < numb; ++i)
    {
        if (life[i] != 0)
        {
            if ((dist(rng)) % 2 == 0) {
                x_coords[i]++;
                check_sonapr_x(x_coords, numb, life, -1);
            }
            else {
                x_coords[i]--;
                check_sonapr_x(x_coords, numb, life, 1);
            }

        }
    }
    return x_coords;

}

int* check_sonapr_y(int* y_coords, int numb, int* life, int napr)
{
    for (int i = 0; i < numb; i++)
    {
        for (int j = 0; j < numb; j++)
        {
            if ((y_coords[i] == y_coords[j]) and i != j)
            {
                y_coords[i] = y_coords[i] + 1 * napr;

            }
        }
    }
    return y_coords;
}

int* mooving_y(int* y_coords, int numb, int* life)
{
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<int>dist(0, 100);
    std::uniform_real_distribution<double> dist2(0, 1);
    for (int i = 0; i < numb; ++i)
    {
        if (life[i] != 0)
        {
            if ((dist(rng)) % 2 == 0) {
                y_coords[i]++;
                check_sonapr_y(y_coords, numb, life, -1);
            }
            else {
                y_coords[i]--;
                check_sonapr_y(y_coords, numb, life, 1);
            }

        }
    }
    return y_coords;

}


int main()
{
    int timer = 0;
    int summ = 0;
    int life_summ;
    int numb = 1;
    int x_coords[5];
    int y_coords[5];
    int life[5];
    int size = 100;
    Rand_coords_x(x_coords, numb, 100);
    Rand_coords_y(y_coords, numb, 100);
    for (int i = 0; i < numb; ++i)
    {
        life[i] = 1;
    }
    life_summ = numb;
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<int>dist(0, 100);
    std::uniform_real_distribution<double> dist2(0, 1);
    for (int i = 5; i < size; ++i)
    {
        for (int j = 0; j < 30; j++)
        {
            while (life_summ > 0)
            {
                if ((dist(rng)) >= 50)
                {
                    mooving_x(x_coords, numb, life);
                    timer++;
                }
                else
                {
                    mooving_y(y_coords, numb, life);
                    timer++;
                }
                Kasanie_check(x_coords, y_coords, numb, life, i);
                for (int k = 0; k < numb; ++k)
                {
                    if (life[k] == 0)
                    {
                        life_summ--;
                    }
                }
            }

            Rand_coords_x(x_coords, numb, i);
            Rand_coords_y(y_coords, numb, i);
            summ = summ + timer;
            timer = 0;
            life_summ = numb;
            for (int o = 0; o < numb; ++o)
            {
                life[o] = 1;
            }
        }
        std::cout << summ / 30 << std::endl;
        summ = 0;
        timer = 0;

    }
}
