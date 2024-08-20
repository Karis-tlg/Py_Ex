#include <bits/stdc++.h>
using namespace std;

int main() {
    unsigned long long mod = 1e18;
    vector<unsigned long long> fib(401);
    fib[0] = 0; fib[1] = 1;
    for (int i = 2; i <= 400; i++) {
        fib[i] = (fib[i - 1] + fib[i - 2]) % mod;
    }

    freopen("LFIB.INP", "r", stdin);
    freopen("LFIB.OUT", "w", stdout);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b; string s;
        cin >> a >> b >> s;

        unsigned long long t = 0;
        for (char i : s) {
            t = (t * 10 + (i - '0')) % mod;
        }

        if ((fib[a] + fib[b] == t)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}
