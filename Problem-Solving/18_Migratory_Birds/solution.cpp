#include<iostream>
using namespace std;
int main(){
  int n, i, temp, ar[5];
  for(i=0; i<5; i++){
    ar[i]=0;
  }
  cin>>n;
  for(i=0; i<n; i++){
    cin>>temp;
    switch (temp) {
      case 1: ar[0]++;
              break;
      case 2: ar[1]++;
              break;
      case 3: ar[2]++;
              break;
      case 4: ar[3]++;
              break;
      case 5: ar[4]++;
              break;
    }
  }
  int big=0;
  for(i=0; i<5; i++){
    if(ar[i] > ar[big])
      big = i;
  }
  cout<<big+1;
return 0;
}