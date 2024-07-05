#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("BOI3.INP", "r", stdin);
    freopen("BOI3.OUT", "w", stdout);

    int n;
    cin >> n;

    int a[n];

    for (int i = 0; i < n; i++){
        cin >> a[i];
        if (a[i] % 2 == 0 && a[i] % 3 == 0){
            cout << a[i] << " ";
        }
    };
    return 0;
}
