#include <iostream>
using namespace std;

int main()
{
	
    unsigned long int arr[5], min, pos, minsum=0, maxsum=0;;
    
	for(int k=0; k<5; k++)
		cin>>arr[k];

	for(int i=0; i<4; i++)
	{
		min=arr[i];
		pos=i;

		for(int j=i+1; j<5; j++)
			if(arr[j]<min)
			{
				min=arr[j];
				pos=j;
			}

	if(pos!=i)
	{
		arr[pos]=arr[i];
		arr[i]=min;
	}

	}

	for(int l=0; l<4; l++)
		minsum+=arr[l];
	for(int m=1; m<5; m++)
		maxsum+=arr[m];

	cout<<minsum<<" "<<maxsum;


	return 0;
}