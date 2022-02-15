#include <iostream>
#include <random>

int main()
{
    int summ = 0;
    int time = 0;
    for (int i=0; i<100; ++i){
        int x=i/2;
        int y=i/2;
        for (int j=0; j<10; ++j)
            while ((x!=i) and (y!=i) and (x!=0) and (y!=0)){
                std::random_device dev;
                std::mt19937 rng(dev());
                std::uniform_int_distribution<int>dist(0,100);
                std::uniform_real_distribution<double> dist2(0,1);
                if ((dist(rng))>=50){
                    if ((dist(rng))%2==0){
                        x++;
                        time++;
                    }
                    else{
                        x--;
                        time++;
                    }
                }
                else{
                    if ((dist(rng))%2==0){
                        y++;
                        time++;
                    }
                    else{
                        y--;
                        time++;
                    }
                }
            }
            summ = summ + time;
            time = 0;
        std::cout<<summ/10<<std::endl;
}
}
