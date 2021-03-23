#include<iostream>
#include<stdlib.h>
using namespace std;

int main(){
		setlocale(LC_ALL,"");
	float c, f;
	
	for(f=32;f<=212; f+=5)
{		
	c=(f-32)*5/9;
		
	cout<<"\n"<<f<<" é igual a "<<c<<" graus C";
}
	
	cout<<"\n";

	for(c=0; c<101; c+=5)
{
	f = 1.8*c+32;
	cout<<"\n"<<c<<" é igual a "<<f<<" graus Fahrenheit";

	if(c==50)
	break;
}
	cout<<"\n";
	
system("pause");
return 0;
}
