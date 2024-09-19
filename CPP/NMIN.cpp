#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e7 + 1;

int solve(vector<int>& a, int n) {
    bool b[maxn] = {false};
    for (int i = 0; i < n; i++) {
        if (a[i] >= 0 && a[i] < maxn) {
            b[a[i]] = true;
        }
    }
    for (int i = 0; i < maxn; i++) {
        if (!b[i]) return i;
    }
    return maxn;
}

int main() {
    freopen("NMIN.INP", "r", stdin);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << solve(a, n) << endl;
}
