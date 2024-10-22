#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("BAI4.INP", "r", stdin);
    freopen("BAI4.OUT", "w", stdout);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> a[i];
    }

    cout << *max_element(a.begin(), a.end()) << endl;
    sort(a.begin(), a.end(), greater<int>());
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 != 0) cout << a[i] << " ";
    } cout << endl;
}
