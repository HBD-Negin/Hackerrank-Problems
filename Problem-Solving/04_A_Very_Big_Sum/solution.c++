#include <iostream>
using namespace std;

int main()
{
    int N;
    unsigned long int arr[10], sum=0;
    cin>>N;
    for(int i=0; i<N; i++)
    {
        cin>>arr[i];
    }
     for(int i=0; i<N; i++)
    {
        sum+=arr[i];
    }
    
    cout<<sum;
    return 0;
}