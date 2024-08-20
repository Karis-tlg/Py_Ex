#include <bits/stdc++.h>
using namespace std;

int bs(vector<int>& a, int n, int x) {
    int l = 0, r = n - 1;
    int kq = -1;
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (a[m] > x) {
            kq = m;
            r = m - 1;
        } else {
            l = m + 1;
        }
    }
    return kq;
}

int main() {
    freopen("UPPERBOUND.INP", "r", stdin);
    freopen("UPPERBOUND.OUT", "w", stdout);

    int n, q;
    cin >> n >> q;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < q; i++) {
        int x = 0;
        cin >> x;
        int pos = bs(a, n, x);
        if (pos == -1) {
            cout << -1 << endl;
        } else {
            cout << pos + 1 << endl;
        }
    }
}


