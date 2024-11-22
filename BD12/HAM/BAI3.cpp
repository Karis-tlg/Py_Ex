#include <bits/stdc++.h>
#define LL long long
using namespace std;

bool scp(LL n) {
    LL num = (LL)sqrt(n);
    return num * num == n;
}

int main() {
    freopen("BAI3.INP", "r", stdin);
    //freopen("BAI3.OUT", "w", stdout);

    LL n; cin >> n;
    cout << (scp(n) ? "yes" : "no");
}
