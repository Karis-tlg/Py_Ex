#include <bits/stdc++.h>
using namespace std;

bool snt(int n) {
    if (n <= 1) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    } return true;
}

int rv(int n) {
    int t = 0;
    while (n > 0) {
        t = t * 10 + n % 10;
        n /= 10;
    } return t;
}

int main() {
    freopen("CPRIME.INP", "r", stdin);
    freopen("CPRIME.OUT", "w", stdout);

    int n;
    cin >> n;

    if (snt(n) && snt(rv(n))) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }
}
