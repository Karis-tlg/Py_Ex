#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("SUM.INP", "r", stdin);
    freopen("SUM.OUT", "w", stdout);

    int n, k; long long b;
    cin >> n >> k >> b;

    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];

    int dem = (b - 1) % n;

    long long sum = 0;
    for (int i = 0; i < k; i++) sum += a[(dem + i) % n];

    cout << sum;

    return 0;
}
