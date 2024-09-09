#include <bits/stdc++.h>
using namespace std;

void sang(int k, int h) {
    vector<bool> snt(h - k + 1, true);
    if (k <= 1) {
        for (int i = 0; i <= 1 - k; ++i) {
            snt[i] = false;
        }
    }

    for (int i = 2; i * i <= h; i++) {
        for (int j = max(i * i, (k + i - 1) / i * i); j <= h; j += i) {
            snt[j - k] = false;
        }
    }

    int s = 0, t = 0;

    for (int i = max(2, k); i <= h; i++) {
        if (snt[i - k]) {
            s += i;
            t++;
        }
    }
    cout << round(s / t) << endl;
}

int main() {
    freopen("SNT.INP", "r", stdin);

    int n, k, h;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> k >> h;
        sang(k, h);
    }
}
