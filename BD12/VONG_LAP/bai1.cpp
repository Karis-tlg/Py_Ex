#include <bits/stdc++.h>
#define LL long long
using namespace std;

LL uoc(LL n) {
    LL t = 0;
    for (int i = 1; i < sqrt(n); i++) {
        if (n % i == 0) {
            t += i;
            if (i != n / i) t += n / i;
        }
    } return t;
}

int main() {
    LL n;
    cin >> n;
    cout << uoc(n) << endl;
    return 0;
}
