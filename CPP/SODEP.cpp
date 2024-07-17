#include <bits/stdc++.h>
using namespace std;

bool cp(int n) {
    int c = sqrt(n);
    return (c * c == n);
}

int re(int n) {
    string a = to_string(n);
    reverse(a.begin(), a.end());

    return stoi(a);
}

int main() {
    freopen("SODEP.INP", "r", stdin);
    freopen("SODEP.OUT", "w", stdout);

    int m, n;
    bool ck = false;
    cin >> m >> n;

    for (int i = m; i <= n; i++) {
        if (cp(i + re(i))) {
            cout << i << " ";
            ck = true;
        } else {
            cout << "khong co";
            break;
        }
    }
}
