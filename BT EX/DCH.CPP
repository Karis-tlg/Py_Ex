#include <bits/stdc++.h>

using namespace std;
int x,n,i;
int main()
{
    freopen("DCH.INP","r",stdin);
    freopen("DCH.OUT","w",stdout);
    cin>>n;
    for (i=1;i<=n;i++)
        {
            cin>>x;
            if ((x%5==0) && (x%2!=0)) cout<<x<<" ";
        }
    return 0;
}
