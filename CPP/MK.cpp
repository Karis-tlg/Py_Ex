#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("MK.INP", "r", stdin);
    freopen("MK.OUT", "w", stdout);

    string n;
    cin >> n;

    long long t = 0;

    for (char i : n) {
        t += i - '0';
    }

    cout << t;
}
