#include<iostream>
using namespace std;
int main(){
    int n, scr[60];
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>scr[i]; 
		switch(scr[i]){
        	case 38:	case 39: 	scr[i] = 40;	break;
        	case 43:	case 44:	scr[i] = 45;	break;
        	case 48:	case 49: 	scr[i] = 50;	break;
        	case 53:	case 54:	scr[i] = 55;	break;
        	case 58:	case 59: 	scr[i] = 60;	break;
        	case 63:	case 64:	scr[i] = 65;	break;
        	case 68:	case 69: 	scr[i] = 70;	break;
        	case 73:	case 74:	scr[i] = 75;	break;
        	case 78:	case 79: 	scr[i] = 80;	break;
        	case 83:	case 84:	scr[i] = 85;	break;
        	case 88:	case 89: 	scr[i] = 90;	break;
        	case 93:	case 94:	scr[i] = 95;	break;
        	case 98:	case 99:	scr[i] = 100;	break;
        }
    }
        for (int i = 0; i < n; ++i)
        {
        	cout<<scr[i]<<"\n";
        }

}