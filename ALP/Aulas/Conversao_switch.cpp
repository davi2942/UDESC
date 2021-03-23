#include <stdio.h>
#include <iostream>

using namespace std;

    int main()
{
	setlocale(LC_ALL,"");
cout<<"Digite 1 para o cálculo altomático.\n";
cout<<"Digite 2 para converter de Fahrenheit para graus Celcius.\n";
cout<<"Digite 3 para converter de Celcius para graus Fahrenheit.\n";
int resposta;
cout<<"Digite um número de 1 a 3\n";
cin>>resposta;

switch (resposta){
	case 1: cout<<"Digitou 1.\n";
	for(f=0;f<=50; f+=5){
	c=(f-32)*1.8;		
	cout<<"\n"<<f<<" é igual a "<<c<<" graus C";
}
	break;

	case 2: cout<<"Digitou 2. \n";
	break;

	case 3: cout<<"Digitou 3. \n";
	break;

	default:
		cout<<"Opção inválida\n";
}









system("pause");
return 0;
}




