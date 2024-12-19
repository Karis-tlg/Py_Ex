#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("TAOXAU.INP", "r", stdin);
    freopen("TAOXAU.OUT", "w", stdout);

    string n, s;
    cin >> n;

    for (char i : n) {
        s += i;
        reverse(s.begin(), s.end());
    }

    cout << s;
}
