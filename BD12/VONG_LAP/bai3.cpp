#include <bits/stdc++.h>
using namespace std;

int main() {  
    int n, t = 1;
    cin >> n;

    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            t *= i;
            if (i != n / i) t *= n / i;
        }
    } cout << t;
}

