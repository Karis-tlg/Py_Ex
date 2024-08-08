#include <bits/stdc++.h>
using namespace std;

int dc(vector<int> a) {
    unordered_map<int, int> b;
    int t = 0, s = 0;

    for (int i : a) {
        s += i;
        if (s == 0) {
            t++;
        }
        if (b.find(s) != b.end()) {
            t += b[s];
        }
        b[s]++;
    } return t;
}

int main() {
    freopen("DEMCAP.INP", "r", stdin);
    freopen("DEMCAP.OUT", "w", stdout);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    cout << dc(a);
}
