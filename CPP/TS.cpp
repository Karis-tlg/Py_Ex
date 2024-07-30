#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("TS.INP", "r", stdin);
    freopen("TS.OUT", "w", stdout);

    int n;
    cin >> n;

    int a[n], b[n];
    int c[11] = {0};

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        c[a[i]]++;
    }

    for (int i = 0; i < n; i++) {
        cin >> b[i];
        c[b[i]]++;
    }

    for (int i = 0; i < n; i++) {
        cout << a[i] << " " << b[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < 10; i++) {
        if (c[i] > 0) {
            cout << i << " " << c[i] << endl;
        }
    }
}
