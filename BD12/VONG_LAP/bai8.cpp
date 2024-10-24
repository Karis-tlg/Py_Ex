#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    cout << endl;

    //hinh 1
    int t = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            t += 1;
            cout << t << " ";
        }
        cout << endl;
    }
    cout << endl;

    //hinh 2
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n + i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
    cout << endl;

    //hinh 3
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < n - i; j++) {
            cout << "~";
        }
        for (int k = 0; k < i; k++) {
            cout << i;
        }
        cout << endl;
    }
    cout << endl;
}
