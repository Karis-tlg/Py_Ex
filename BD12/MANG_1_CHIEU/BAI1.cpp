#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("BAI1.INP", "r", stdin);
    freopen("BAI1.OUT", "w", stdout);

    int n;
    cin >> n;

    pair<int, int> a[100];
    for (int i = 0; i < n; i++) {
        cin >> a[i].first >> a[i].second;
    }

    sort(a, a + n);
    for (int i = 0; i < n; i++) {
        cout << a[i].first << " " << a[i].second << endl;
    }
}
