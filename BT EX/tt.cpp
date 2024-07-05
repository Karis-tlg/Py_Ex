#include <bits/stdc++.h>
using namespace std;
int a,b;
bool nto(int n)
{
    if (n < 2) return false;
    for (int i=2; i <= trunc(sqrt( n)); i++)
        if (n % i == 0) return false;
    return true;
}
int unt(int a)
{
    if (nto(a)) return a;
    for (int i = (a / 2); i>=a; i--)
        if ((a % i == 0) && (nto(i))) return i;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    freopen("tt.inp","r",stdin);
    freopen("tt.out","w",stdout);
    cin >> a >> b;
    cout << unt(a) << " " << unt(b) << endl;
    if (unt(a) == unt(b)) cout << " la cap so than thiet ";
        else cout << " khong than thiet ";
}
