#include <bits/stdc++.h>
using namespace std;

#include <iostream>

int sumi(int n) {
    int t = 0;
    while (n != 0 || t > 9) {
        if (n == 0) {
            n = t;
            t = 0;
        }
        t += n % 10;
        n /= 10;
    }
    return t;
}

int main () {
    freopen("LUCKY.INP", "r", stdin);
    freopen("LUCKY.OUT", "w", stdout);

    int a[10] = {0};
    int n, m;
    cin >> n;

    for (int i; i < n; i++) {
        cin >> m;
        a[sumi(m)] += 1;
    }

    int j = 0;
    for (int i = 0; i < 10; i++) {
        if (a[i] > a[j]) {
            j = i;
        }
    }
    cout << j;
}
