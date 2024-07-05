#include <bits/stdc++.h>
using namespace std;

bool snt(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int uc(int n) {
    if (snt(n)) return n;
    for (int i = sqrt(n); i >= 1; --i) {
        if (n % i == 0) {
            if (snt(n / i)) return n / i;
            if (snt(i)) return i;
        }
    }
    return 1;
}

int main() {
    int a, b;

    freopen("TT.INP", "r", stdin);
    freopen("TT.OUT", "w", stdout);

    cin >> a >> b;


    int uca = uc(a);
    int ucb = uc(b);

    cout << uca << " " << ucb << " " << endl;

    if (uca == ucb) {
        cout << "La cap so than thiet";
    } else {
        cout << "Khong than thiet";
    }

    return 0;
}
