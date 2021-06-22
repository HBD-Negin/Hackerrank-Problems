#include <cmath>
#include <iostream>
using namespace std;

int main()
{
  int i, j, mds=0, ods=0, N, mat[100][100];
  cin>>N;

  for(i=0; i<N; i++)
    for(j=0; j<N; j++)
      cin>>mat[i][j];
      
  for(i=0; i<N; i++)
    mds+=mat[i][i];
  
  for(i=0, j=N-1; i<N; i++, j--)
    ods+=mat[i][j];
  
  cout<<abs(ods-mds);
  return 0;
}