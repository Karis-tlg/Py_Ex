#include <iostream>
#include <vector>

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    int i = 5;
    while (i * i <= n) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
        i += 6;
    }
    return true;
}

int main() {
    int start, end;
    std::cout << "Nh?p do?n [start, end]: ";
    std::cin >> start >> end;

    std::vector<int> primes;
    for (int i = start; i <= end; ++i) {
        if (is_prime(i)) {
            primes.push_back(i);
        }
    }

    std::cout << "Các s? nguyên t? trong do?n [" << start << ", " << end << "] là: ";
    for (std::vector<int>::iterator it = primes.begin(); it != primes.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    return 0;
}

