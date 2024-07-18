#include <bits/stdc++.h>
using namespace std;

int main () {
    freopen("DEM.INP", "r", stdin);
    freopen("DEM.OUT", "w", stdout);

    int m, n, x;
    cin >> m >> n;

    int t = m * n;

    int a[t] = {0};
    for (int i; i < t; i++) {
        cin >> x;
        a[x] += 1;
    }

    for (int i = 0; i < t; i++) {
        if (a[i] > 0) {
            cout << i << " " << a[i] << endl;
        }
    }
}
