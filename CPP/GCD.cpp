#include <bits/stdc++.h>
using namespace std;

int ucln(int a, int b) {
    while (b != 0) {
        int c = a;
        a = b;
        b = c % b;
    }
    return a;
}

int main () {
    freopen("GCD.INP", "r", stdin);
    freopen("GCD.OUT", "w", stdout);

    int a, b;
    cin >> a;
    cin >> b;

    cout << ucln(a, b);
}
