#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("MATKHAU.INP", "r", stdin);
    freopen("MATKHAU.OUT", "w", stdout);

    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int kq = a[0];
    for (int i = 1; i < n; ++i) {
        int T = kq * a[i];
        int du = kq % a[i];
        while (du != 0) {
            kq = a[i];
            a[i] = du;
            du = kq % a[i];
        }
        kq = T / a[i];
    }
    cout << kq;
}
