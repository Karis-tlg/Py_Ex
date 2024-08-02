#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("FIND.INP", "r", stdin);
    freopen("FIND.OUT", "w", stdout);

    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < m; i++) {
        int u, v, k;
        cin >> u >> v >> k;

        vector<int> b;
        for (int j = u - 1; j < v; j++) {
            b.push_back(a[j]);
        }
        sort(b.begin(), b.end());
        cout << b[k - 1] << endl;
    }
}
