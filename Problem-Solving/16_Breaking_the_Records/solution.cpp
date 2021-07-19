#include<iostream>
using namespace std;

int main(){
    int n, i, nMin=0, nMax=0;
    long int sc[1000], min, max;
    cin>>n;
    for(i = 0; i < n; i++)
        cin>>sc[i];
    min=max=sc[0];
    for(i = 1; i < n; i++){
        if( sc[i] < min){
            min = sc[i];
            nMin++;
        }
        if( sc[i] > max){
            max = sc[i];
            nMax++;
        }
    }
    cout<<nMax<<" "<<nMin;
    return 0;
}