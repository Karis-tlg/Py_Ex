#include <bits/stdc++.h>
using namespace std;

bool scp(int n) {
    int can = sqrt(n);
    return can * can == n;
}

int main () {
    freopen("CP.INP", "r", stdin);
    freopen("CP.OUT", "w", stdout);

    int n, x;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        if (x % 2 != 0 && scp(x)) {
            cout << x << " ";
        }
    }
    return 0;
}
