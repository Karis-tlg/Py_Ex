#include <bits/stdc++.h>
using namespace std;

int qd(int a[], int n) {
    if (n == 1) return a[0];
    if (n == 2) return a[0] + a[1];

    int f[n];
    f[0] = a[0];
    f[1] = a[0] + a[1];
    f[2] = max(a[0] + a[1], max(a[1] + a[2], a[0] + a[2]));

    for (int i = 3; i < n; ++i) {
        f[i] = max(f[i - 1], max(a[i] + f[i - 2], a[i] + a[i - 1] + f[i - 3]));
    }

    return f[n - 1];
}

int main() {
    freopen("PTHUONG.INP", "r", stdin);
    freopen("PTHUONG.OUT", "w", stdout);

    int n;
    cin >> n;
    int a[n];

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    cout << qd(a, n);
    return 0;
}
