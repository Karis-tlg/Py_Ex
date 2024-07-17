#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("PYTAGO.INP", "r", stdin);
    freopen("PYTAGO.OUT", "w", stdout);

    int n, t = 0;
    cin >> n;

    int a[n];
    unordered_set<int> b;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n; i++) {
        b.insert(a[i] * a[i]);
    }

    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (b.find(a[i] * a[i] + a[j] * a[j]) != b.end()) {
                t += 1;
            }
        }
    }
    cout << t;
}
