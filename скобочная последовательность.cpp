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

#include <iostream>
#include <cstdlib>
#include <cstring>

void generic_swap(void *lha, void *rha, size_t element_byte_size) {
    void *tmp = malloc(element_byte_size);
    std::memcpy(tmp, lha, element_byte_size);
    std::memcpy(lha, rha, element_byte_size);
    std::memcpy(rha, tmp, element_byte_size);
    free(tmp);
}

void qsort ( void * src_begin , size_t n_memb , size_t type_size , int (* compare ) ( const void * ,
                                                                                      const void *) ) {
    int i = 0;
    int j = n_memb - 1;
    int mid = n_memb / 2;
    do {
        while(compare(( const char *)src_begin + i * type_size, ( const char *)src_begin + mid * type_size)) i++;
        while(compare(( const char *)src_begin + mid * type_size, ( const char *)src_begin + j * type_size)) j++;
        if (i <= j) {
            generic_swap((char *)src_begin + i * type_size, (char *)src_begin + j * type_size, type_size);
            i++;
            j--;
        }
    } while (i <= j);
    if(j > 0) {
        qsort(src_begin, j + 1, type_size, compare);
    }
    if (i < n_memb) {
        qsort((char *)src_begin + i * type_size, n_memb - i, type_size, compare);
    }
}


struct Student {
    size_t id ;
    size_t money ;
};


int student_cmp ( const void * lha , const void * rha ) {
    size_t a = (( const Student *) lha ) -> id ;
    size_t b = (( const Student *) rha ) -> id ;
    return int(a<b) ;
}

int main() {
    Student b[4] = {{42 , 100 } , {137 , 150 } , {993 , 1000 }, {114, 10}};
    qsort(b, 4, sizeof(Student), student_cmp);
    for (int i = 0; i < 4; i++) {
        std::cout << b[i].id << " ";
    }
    return 0;
}
