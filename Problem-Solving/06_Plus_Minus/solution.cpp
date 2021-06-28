#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
   int arr[2000], i;
    double fz, fp, fn,  T, cop, cn=0, cp=0, cz=0;;
    cin>>T;
    cop=T;
    for(i=0; i<T; i++)
    {
        cin>>arr[i];
    }
    
    for(i=0; i<T; i++)
    {
        if(arr[i]==0)
            cz++;
        else if (arr[i]>0)
            cp++;
        else
            cn++;
    }
    
    fz=(cz/T);
    fn=(cn/T);
    fp=(cp/T);
    cout<<fixed<<setprecision(6)<<fp<<endl;
    cout<<fixed<<setprecision(6)<<fn<<endl;
    cout<<fixed<<setprecision(6)<<fz;
    
    return 0;
}