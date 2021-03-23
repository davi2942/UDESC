#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<math.h>

using namespace std;

void bhaskara();
float a,b,c,x1,x2,ndelta;
void grad();
float delta,y;

int main(){
	
	setlocale(LC_ALL, "Portuguese");
	
	cout<<"Informe os valores das constantes para o cálculo:\n";
	cin>>a;
	cin>>b;
	cin>>c;
	grad();
	bhaskara();
	return 0;
}

void grad(){
	delta = (b*b)-(4*a*c);
}

void bhaskara(){
	
	if(a==0)
		cout<<"Não é uma parábola!!\n";	
	else{
		
		if(delta>=0){
		x1 = (-b + sqrt(delta))/(2*a);
		x2 = (-b - sqrt(delta))/(2*a);
		cout<<"Existem raízes reais e elas são \n"<<"x1 = "<<x1<<endl<<"x2 = "<<x2<<endl;
}
	else{
	
		ndelta= (delta*(-1));   
    
    	x1 = ((-b + (sqrt(ndelta)))/(2*a));
    	x2 = ((-b - (sqrt(ndelta)))/(2*a));
    
    	cout<<"Nao existem raízes reais, elas sao complexas!!\n";
    	cout<<"x1 = "<<x1<<"i"<<endl;
    	cout<<"x2 = "<<x2<<"i"<<endl;
		
}}}

