#include <bits/stdc++.h>
using namespace std;

const int b = 1500000;
vector<bool> a(b + 1, true);

void sang() {
    a[0] = a[1] = false;
    for (int i = 2; i * i <= b; i++) {
        if (a[i]) {
            for (int j = i * i; j <= b; j += i) {
                a[j] = false;
            }
        }
    }
}

int main() {
    freopen("DSNT.INP", "r", stdin);
    freopen("DSNT.OUT", "w", stdout);

    int n;
    cin >> n;
    sang();
    int t = n, i = 2;
    while (t > 0) {
        if (a[i]) {
            cout << i << " ";
            t--;
        } i++;
    }
}
