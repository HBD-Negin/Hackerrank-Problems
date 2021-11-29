#include<iostream>
using namespace std;

int main(){
    int n, k, sumS=0, temp, costNS, i, charged, actual;
    cin>>n>>k;
    for(i=0; i<n; i++){
        if(i == k){
            cin>>costNS;
        }else{
            cin>>temp;
            sumS+=temp;
        }
    }
    cin>>charged;
    actual = sumS/2;
    if(actual == charged){
        cout<<"Bon Appetit";
    }else{
        cout<<charged-actual;
    }
return 0;
}
