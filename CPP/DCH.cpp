#include <iostream>
using namespace std;

int main(){
    freopen("DCH.INP", "r", stdin);
    freopen("DCH.OUT", "w", stdout);
    int n, m;
    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> m;
        if (m % 2 != 0 && m % 5 == 0){
            cout << m << " ";
        }
    }
}
