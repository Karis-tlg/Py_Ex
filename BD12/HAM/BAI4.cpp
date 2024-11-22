#include <bits/stdc++.h>
#define LL long long
using namespace std;

bool snt(int n) {
    if (n <= 1) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int k = 5; k * k <= n; k += 6) {
        if (n % k == 0 || n % (k + 2) == 0) return false;
    } return true;
}

bool shh(LL n) {
    for (int p = 2; p <= 63; p++) {
        if (snt(p)) {
            LL tam1 = (1LL << p) - 1;
            if (snt(tam1)) {
                LL tam2 = (1LL << (p - 1));
                if (tam1 > 0 && tam2 > 0 && tam1 * tam2 == n) {
                    return true;
                }
            }
        }
    } return false;
}

int main() {
    freopen("BAI4.INP", "r", stdin);
    freopen("BAI4.OUT", "w", stdout);

    LL n; cin >> n;
    cout << (shh(n) ? "yes" : "no");
}
