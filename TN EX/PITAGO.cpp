#include<bits/stdc++.h>
#define ll long long
#define ii pair<ll,ll>
#define mll map<ll,ll>
#define fi first
#define se second

const int N=1e6+5;
const ll mo=1e9+7;

using namespace std;
ll n,a[N],d=0;
int main()
{
    freopen("PITAGO.INP","r",stdin);
    freopen("PITAGO.OUT","w",stdout);
    ios_base::sync_with_stdio(false);
      cin.tie(NULL);
        cout.tie(NULL);
          cin>>n;
          for (int i=1;i<=n;i++)
                  cin>>a[i];
          sort(a+1,a+n+1);
          for (int i=1;i<=n;i++)
           {
               ll l=1,r=i-1;
               while(l<r)
               {
                   if (a[i]*a[i]==a[l]*a[l]+a[r]*a[r])
                      {
                          d++;
                          l++;
                          r--;
                      }
                   else
                    if (a[i]*a[i]<a[l]*a[l]+a[r]*a[r])
                       r--;
                   else
                       l++;
               }
           }
           cout<<d;
          return 0;
}
