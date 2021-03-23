#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	setlocale(LC_ALL,"");
int resposta;
cout<<"Digite um número de 1 a 3\n";
cin>>resposta;

switch (resposta){
	case 1: cout<<"Digitou 1.\n";
	break;
	case 2: cout<<"Digitou 2. \n";
	break;
	case 3: cout<<"Digitou 3. \n";
	break;
	default:
		cout<<"opção inválida\n";
}

system("pause");
return 0;
}
