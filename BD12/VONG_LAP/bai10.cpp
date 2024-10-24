#include <bits/stdc++.h>
using namespace std;

bool snt(int n) {
    if (n <= 1) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    string n;
    cin >> n;

    int t = 0;
    for (char i : n) {
        if (snt(i - '0')) t += 1;
    }
    cout << t;
}
