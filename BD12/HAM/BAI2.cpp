#include <bits/stdc++.h>
#define LL long long
using namespace std;

LL tong(LL n) {
    return (n * (n + 1)) / 2;
}

int main() {
    freopen("BAI2.INP", "r", stdin);
    //freopen("BAI2.OUT", "w", stdout);
    LL n; cin >> n;
    cout << tong(n);
}
