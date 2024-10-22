#include <bits/stdc++.h>
using namespace std;

int lenv(int x1, int y1, int x2, int y2) {
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

int main() {
    freopen("HINHVUONG.INP", "r", stdin);

    int a[4][2];
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> a[i][j];
        }
    }

    //sort(a.begin(), a.end());
    if (a[0][0] == a[1][0] && a[2][0] == a[3][0] && a[0][1] == a[3][1] && a[1][1] == a[2][1]) {
        int AB = lenv(a[0][0], a[0][1], a[1][0], a[1][1]);
        int BC = lenv(a[1][0], a[1][1], a[2][0], a[2][1]);
        int CD = lenv(a[2][0], a[2][1], a[3][0], a[3][1]);
        int DA = lenv(a[3][0], a[3][1], a[0][0], a[0][1]);


        if (AB == BC && BC == CD && CD == DA) {
            cout << AB * BC;
        } else cout << -1;
    } else cout << -1;
}
