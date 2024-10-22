#include <bits/stdc++.h>>
using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int lcm(int a, int b) {
    return (a / gcd(a, b)) * b;
}

int tlcm(vector<int>& a) {
    int t = a[0];
    for (int i = 1; i < a.size(); ++i) {
        t = lcm(t, a[i]);
    }
    return t;
}

int main() {
    freopen("BAI2.INP", "r", stdin);
    freopen("BAI2.OUT", "w", stdout);

    int n;
    cin >> n;

    vector<int> a(n);
    int s = 0;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        s += a[i];
    }

    for (int i = 0; i < n; ++i) {
        cout << a[i] << " ";
    } cout << endl << s << endl;
    cout << tlcm(a) << endl;
}
