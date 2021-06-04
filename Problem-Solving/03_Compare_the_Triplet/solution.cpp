#include <iostream>
using namespace std;

int main()
{
    int a1, a2, a3, b1, b2, b3, pa=0, pb=0;
    cin>>a1>>a2>>a3>>b1>>b2>>b3;
    
    if(a1>b1)
        pa++;
    else if(b1>a1)
        pb++;
    
    if(a2>b2)
        pa++;
    else if(b2>a2)
        pb++;
    
    if(a3>b3)
        pa++;
    else if(b3>a3)
        pb++;
    
    cout<<pa<<" "<<pb;
    
    return 0;    
    
}