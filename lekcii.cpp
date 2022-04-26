#include <iostream>

using namespace std;

int main()
{
    int n;
    int summ=0;
    cin>>n;
    int* nachalo = new int[n];
    int* konec = new int[n];
    int* life = new int[n];
    for (int u=0; u<n; u++){
        cin>>nachalo[u]>>konec[u];
        life[u] = 1;
    }
    for (int i = 0; i<n; i++){
        if (life[i] != 0){
            for (int j = 1; j<n; j++)
            {
                if (j!=i){
                    if (konec[i]<konec[j] and konec[i]>nachalo[j]){
                        life[j]=0;
                    }
                }
            }
        }
    }
    for (int i=0; i<n; i++){
        summ+=life[i];
    }
    cout<<summ;
    delete[] nachalo;
    delete[] konec;
    delete[] life;
}
