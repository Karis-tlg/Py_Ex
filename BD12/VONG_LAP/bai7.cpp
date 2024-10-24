#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    double s = 0.0;
    for (int i = 1; i <= n; i++) {
        s += 1.0 / i;
    }
    cout << fixed << setprecision(3) << s << endl;
    return 0;
}
