#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("MATHE.INP", "r", stdin);
    string s, t;
    getline(cin, s);
    int n = 1;

    for (char i : s) {
        if (isdigit(i)) {
            n *= (i - '0');
        } else {
            t += i;
        }
    }

    cout << n << t;
}
