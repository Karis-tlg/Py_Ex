#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("THREE.INP", "r", stdin);

    int n, k;
    cin >> n >> k;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    int t = 0;
    for (int i = 0; i < n - 2; ++i) {
        for (int j = i + 1; j < n - 1; ++j) {
            if (a[j] == a[i] * k) {
                for (int l = j + 1; l < n; ++l) {
                    if (a[l] == a[j] * k) {
                        t++;
                    }
                }
            }
        }
    }
    cout << t;
}
