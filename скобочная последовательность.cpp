#include <iostream>

int summ = 0;


int check(char c)
{
	if (c == '(') {
		summ++;

	}
	else {
		summ--;
	}
	if (summ < 0) {
		return -1;
	}
	else {
		return summ;
	}
}

int main()
{
	int n;
	std::cin >> n;
	for (int i = 0; i < n; ++i)
	{
		char c;
		int a;
		std::cin >> c;
		a = check(c);
		if (a < 0) {
			std::cout << "- 1" << std::endl;
			break;
		}


	}

	if (summ == 0) {
		std::cout << '1' << std::endl;
	}
	if (summ > 0) {
		std::cout << " - 1" << std::endl;
	}





}