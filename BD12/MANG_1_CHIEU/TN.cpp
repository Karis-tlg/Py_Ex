#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

int main() {
    freopen("TN.INP", "r", stdin);
    freopen("TN.OUT", "w", stdout);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int m = a[0];
    for (int i = 1; i < n; i++) {
        m = lcm(m, a[i]);
    } cout << m << endl;

    for (int i = 0; i < n; i++) {
        cout << m / a[i] << " ";
    } cout << endl;
}
