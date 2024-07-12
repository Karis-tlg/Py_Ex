#include <bits/stdc++.h>
#define maxN 10005
using namespace std;
bool kt(int n)
{
    int s=0,p=n;
    while (n!=0)
    {
        s=s*10+(n%10);
        n=n/10;
    }
    int k=sqrt(s+p);
    if (k*k==s+p) return 1;
    return 0;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    freopen("SODEP.inp","r",stdin);
    freopen("SODEP.out","w",stdout);
    int l,r,i,d=0;cin>>l>>r;
    for (i=l;i<=r;i++)
        if (kt(i))
        {
            cout<<i<<" ";d=1;
        }
    if (d==0) cout<<"Khong co";
    return 0;
}


















