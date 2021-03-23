#include <stdlib.h>
#include <locale.h>
#include <iostream>
#include <cmath>

using namespace std;

    int main()
{
	setlocale(LC_ALL, "Portuguese");

    float delta, rdelta,ndelta;
	float x1,x2,y,a,b,c;
    cout<<"Informe o valor de a da equação\n";
    cin>>a;
    cout<<"Informe o valor de b da equacao\n";
    cin>>b;
    cout<<"Informe o valor de c da equacao\n";
    cin>>c;

	if(a==0){		
	if(b==0){
	cout<<"y = "<<c<<endl;
}
	else{
		
	y = (-c)/b;
	
	cout<<"x = "<<y<<endl;
	system("pause");
}}
	else{
		    
    delta = ((b*b)-4*a*c);
    rdelta = sqrt(delta);
    
    if(delta>=0){
    	
    x1 = ((-b + rdelta)/(2*a));
    x2 = ((-b - rdelta)/(2*a));
    
    cout<<"x1 = "<<x1<<endl;
    cout<<"x2 = "<<x2<<endl;
    system("pause");
}
 else{     
    ndelta= (delta*(-1));   
    
    x1 = ((-b + (sqrt(ndelta)))/(2*a));
    x2 = ((-b - (sqrt(ndelta)))/(2*a));
    
    cout<<"x1 = "<<x1<<"i"<<endl;
    cout<<"x2 = "<<x2<<"i"<<endl;
    
  system("pause");

}}
 return 0;
}


