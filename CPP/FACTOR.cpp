#include <iostream>
using namespace std;

void unt(int n) {
    int i = 2;
    int a[n];
    int dem = 0;
    while (n > 1) {
        if (n % i == 0) {
            dem += 1;
            a[dem] = i;
            n /= i;
        } else {
            i += 1;
        }
    }
    for (int i = 1; i < dem; i++) {
        cout << a[i] << "*";
    }
    cout << a[dem];
}

int main() {
    freopen("FACTOR.INP", "r", stdin);
    freopen("FACTOR.OUT", "w", stdout);

    int n;
    cin >> n;

    unt(n);

    return 0;
}
