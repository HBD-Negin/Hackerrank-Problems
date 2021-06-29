#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int N;
    cin>>N;
    for(int i=1; i<=N; i++)
    {
        cout<<setw(N-i+1);
        for(int j=1; j<=i; j++)
               cout<<"#";

        cout<<endl;

    }
    return 0;
}