#include <bits/stdc++.h>
#define LL long long
using namespace std;

void fib(LL n) {
    if (n == 0) return;
    if (n == 1) {
        cout << 1;
        return;
    }

    vector<LL> f(n);
    f[0] = f[1] = 1;
    for (int i = 2; i < n; i++) {
        f[i] = f[i - 1] + f[i - 2];
    }
    for (int i = 0; i < n; i++) {
        cout << f[i] << " ";
    }
}

int main() {
    freopen("BAI6.INP", "r", stdin);
    freopen("BAI6.OUT", "w", stdout);

    LL n;
    cin >> n;

    fib(n);
}
