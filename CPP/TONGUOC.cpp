#include <bits/stdc++.h>
using namespace std;

long long uoc(int n) {
    long long t = 0;
    for (int i = 1; i * i <= n; ++i) {
        if (n % i == 0) {
            t += i;
            if (i != n/i) {
                t += n/i;
            }
        }
    }
    return t;
}

int main() {
    freopen("TONGUOC.INP", "r", stdin);
    freopen("TONGUOC.OUT", "w", stdout);

    long long n;
    cin >> n;

    cout << uoc(n);
}
