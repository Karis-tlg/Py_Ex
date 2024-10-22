#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("XEPHCN.INP", "r", stdin);

    int n; cin >> n;
    int a[n][2];

    for (int i = 0; i < n; i++) {
        cin >> a[i][0] >> a[i][1];
        if (a[i][0] > a[i][1]) {
            swap(a[i][1], a[i][0]);
        }
    }

    for (int i = 0; i < n; i++) {
        cout << a[i][0] << " " << a[i][1] << endl;
    }

    return 0;
}
