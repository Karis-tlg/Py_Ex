#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("MERLIN.INP", "r", stdin);
    freopen("MERLIN.OUT", "w", stdout);

    int n;
    cin >> n;

    vector<long long> a(n);
    vector<long long> b(n + 1, 0);
    int res = 0;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; i++) {
        b[i + 1] = b[i] + a[i];
    }

    long long d, r;
    for (int i = n; i > 0; --i) {
        d = a[i - 1] * i - b[i];
        r = b[n] - b[i];
        if (r >= d) {
            res = n - i;
            break;
        }
    }

    cout << res << endl;
}