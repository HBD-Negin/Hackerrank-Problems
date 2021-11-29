#include<iostream>
using namespace std;
int main(){
    int n, ar[100], d, m, i, j, count, flag=0;
    cin>>n;
    for(i=0; i<n; i++){
        cin>>ar[i];
    }
    cin>>d>>m;
    for(i=0; i<n-m+1; i++){
        count=0;
        for(j=0; j<m; j++){
            count+=ar[i+j];
        }
        if(d==count){
            flag++;
        }
    }
    cout<<flag;
return 0;
}
