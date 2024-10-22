#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("BAI3.INP", "r", stdin);
    freopen("BAI3.OUT", "w", stdout);

    int n, t = 0;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] % 2 == 0) t += 1;
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; i++) cout << a[i] << " ";

    cout << endl << t << endl;
}
