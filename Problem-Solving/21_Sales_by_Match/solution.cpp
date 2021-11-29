#include<iostream>
using namespace std;

int main(){
    int i, j, n, ar[100], temp, min, count=0;
    cin>>n;
    for(i=0; i<n; i++)
        cin>>ar[i];
    for(i=0; i<n-1; i++){
        min = i;
        for(j=i+1; j<n; j++){
            if(ar[j] < ar[min]){
                min = j;
            }
        }
        if(min != i){
            temp = ar[i];
            ar[i] = ar[min];
            ar[min] = temp;
        }
    }

    for(i=0; i<n; i+=2){
        if(ar[i] == ar[i+1]){
                count++;
        }else{
            i-=1;
        }
    }
    cout<<count;
return 0;
}