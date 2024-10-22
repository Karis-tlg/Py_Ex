#include <bits/stdc++.h>
using namespace std;

int tinh(vector<int>&a, vector<char>&b) {
    int s = a[0];
    for (int i = 0; i < b.size(); i++) {
        if (b[i] == '*') {
            s *= a[i + 1];
        } else {
            s += a[i + 1];
        }
    } return s;
}

int main() {
    freopen("EXPRESS.INP", "r", stdin);
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int maxn = -1;

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            vector<char> b(n - 1, '+');
            b[i] = '*';
            b[j] = '*';

            int num = tinh(a, b);
            maxn = max(num, maxn);
        }
    } cout << maxn;
}
