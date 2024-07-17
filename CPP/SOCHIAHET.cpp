#include <bits/stdc++.h>
using namespace std;

bool ck(int n) {
    string a = to_string(n);
    int t = 0;

    for (char i : a) {
        int b = i - '0';
        if (b != 0 && n % b == 0) {
            t += 1;
        }
    }
    return t == a.length();
}

int main() {
    freopen("SOCHIAHET.INP", "r", stdin);
    freopen("SOCHIAHET.OUT", "w", stdout);

    int n, m;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> m;
        if (ck(m)) {
            cout << m << " ";
        }
    }
}
