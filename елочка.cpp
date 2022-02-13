#include <iostream> 

int main()
{
    int k = 1;
    int n;
    std::cin >> n;
    for (int i = 'a'; i < 'a' + (char)n; ++i) {
        std::cout << char(i);
    }
    for (int i = 'a' + (char)n - 2; i >= 'a'; --i) {
        std::cout << char(i);
    }
    std::cout << "" << std::endl;
    for (int i = n; i > 1; i--) {
        for (int j = 'a'; j < 'a' + (char)n; ++j) {
            if (j >= 'a' + char(i) - 1) {
                std::cout << " ";
            }
            else {
                std::cout << char(j);
            }
        }
        for (int z = 'a' + (char)n - 2; z >= 'a'; --z) {
            if (z > 'a' + (char)i - 2 ) {
                std::cout << " ";
            }
            else {
                std::cout << char(z);
            }
        }
        std::cout << "" << std::endl;
    }

    
}