#include <bits/stdc++.h>
using namespace std;

bool snt(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= (int)sqrt(n); ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

bool str(int n) {
    int s = 0;
    for (char i: to_string(n)) {
        int m = i - '0';
        s += m * m;
    }
    return snt(s);
}

int main() {
    int n;
    freopen("SMM.INP", "r", stdin);
    freopen("SMM.OUT", "w", stdout);

    cin >> n;

    int i = 11;
    while (n > 0) {
        if (str(i)) {
            cout << i << " ";
            n--;
        }
        i++;
    }
}
