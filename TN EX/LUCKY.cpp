#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAXN=1e5;
ll n,k,a[MAXN+5],ans;
map<ll,ll>cnt;
int main()
{
    freopen("LUCKY.inp","r",stdin);
    freopen("LUCKY.out","w",stdout);
    cin.tie(0)->sync_with_stdio(false);
    cin>>n>>k;
    for(int i=1;i<=n;++i){
        cin>>a[i];
        ans+=cnt[k-a[i]];
        if(k!=0)
            ans+=cnt[-k-a[i]];
        cnt[a[i]]+=1;
    }
    cout<<ans;
    return 0;
}







