#include <iostream>
using namespace std;

int main(){
    int n;
    cout << "Nhap n: ";
    cin >> n;

    int a[n];

    for (int i = 0; i < n; i++){
        cout << "Nhap so thu " << i + 1 << ": ";
        cin >> a[i];
    }

    for (int i = 0; i < n; i++){
        if (a[i] % 2 == 0 && a[i] % 3 == 0){
            cout << a[i] << " ";
        }
    }
    cout << endl;
}
