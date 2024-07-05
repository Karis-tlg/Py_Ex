#include <bits/stdc++.h>
#define maxN 1000000
using namespace std;
int a[maxN];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    freopen("BOI3.inp","r",stdin);
    freopen("BOI3.out","w",stdout);
    int n;cin>>n;
    for (int i=1;i<=n;i++)
    {
        cin>>a[i];
        if ((a[i]%2==0) && (a[i]%3==0)) cout<<a[i]<<' ';
    }
    return 0;
}
