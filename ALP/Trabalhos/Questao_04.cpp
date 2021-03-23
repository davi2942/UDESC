#include<iostream>
#include<stdio.h>

using namespace std;

void conversao();
float atm,pascal,psi,bar;
int x;

int main(){
	cout<<"Digite a pressao em atm.\n";
	cin>>atm;
	system("cls");
	cout<<"Digite 1 para converter de atm para Pascal\n";
	cout<<"Digite 2 para converter de atm para Psi\n";
	cout<<"Digite 3 para converter de atm para Bar\n";
	conversao();
	
return 0;
}

void conversao(){
	cin>>x;
	switch (x){
		case 1:
		pascal = (101325*atm);
		cout<<"Este eh o valor em Pascal: "<<pascal<<" Pa\n";
		break;
		
		case 3:
		bar = (1.01325*atm);
		cout<<"Este eh o valor em Bar "<<bar<<" bars\n";
		break;
		
		case 2:
		psi = (14.6959*atm);
		cout<<"Este eh o valor em psi "<<psi<<" psi\n";
		break;
	}
}

