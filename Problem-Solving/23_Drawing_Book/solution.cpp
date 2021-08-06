#include<iostream>
using namespace std;

int main(){
    int i,  n, p, cf=0, cb=0;
    cin>>n;
    cin>>p;
    for(i=0; i<n; i+=2){
        if( i == p || i+1 == p ){
            break;        
        }else{
            cf++;
        }
    }
    if(n%2 ==0)
        n++;
    for(i=n; i>=0; i-=2){
        if( i == p || i-1 == p)
            break;
        else
            cb++;
    }
    (cf < cb)?cout<<cf:cout<<cb;
return 0;
}

