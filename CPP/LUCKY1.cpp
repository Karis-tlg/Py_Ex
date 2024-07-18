#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("LUCKY1.INP", "r", stdin);
    freopen("LUCKY1.OUT", "w", stdout);

    int n, k, t = 0;
    cin >> n >> k;

    int m[n];

    for (int i = 0; i < n; i++) {
        cin >> m[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
                if (m[i] + m[j] == k) {
                    t += 1;
            }
        }
    }
    cout << t;
}
