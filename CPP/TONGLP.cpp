#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("TONGLP.INP", "r", stdin);
    freopen("TONGLP.OUT", "w", stdout);

    int n, t = 0;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j++) {
            if (pow(i, 3) + pow(j, 3) == n) {
                cout << i << " " << j << endl;
                t++;
            }
        }
    }
    cout << t;
}
