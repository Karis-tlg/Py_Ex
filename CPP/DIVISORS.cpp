#include <bits/stdc++.h>
using namespace std;

int gt(int n) {
    int s = 1;
    for (int i = 1; i <= n; i++) {
        s *= i;
    }
    return s;
}

int tu(int n) {
    int t = 1;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            t++;
            if (i != n / i) {
                t ++;
            }
        }
    }
    return t;
}

int main() {
    freopen("DIVISORS.INP", "r", stdin);
    //freopen("DIVISORS.OUT", "w", stdout);

    int n;
    cin >> n;
    cout << tu(gt(n));
}
