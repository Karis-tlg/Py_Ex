#include <bits/stdc++.h>
using namespace std;

bool snt(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= (int)sqrt(n); ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    freopen("SNT.INP", "r", stdin);
    freopen("SNT.OUT", "w", stdout);

    int a, b;
    cin >> a >> b;

    for (int i = a; i <= b; i++) {
        if (snt(i)) cout << i << " ";
    }
}
