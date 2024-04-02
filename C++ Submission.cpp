#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll a[51],n,k;
bool good(ll x){
	ll sum=0;
	for(int i=0;i<n;i++){
		sum+=min(x,a[i]);
	}
	return sum>=x*k;
}
int main() {
	cin>>k>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	ll l=0,r=1e17;
	while(l+1<r){
		ll m=(l+r)/2;
		if(good(m)==true){
			l=m;
		}
		else r=m;
	}
	cout<<l;
}
