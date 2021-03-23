#include <iostream>
using namespace std;

	int main()
{
	setlocale(LC_ALL, "Portuguese");


//Inicialização de Variáveis

	int vidas, tiros, mortes, status=0;
	float acertos;
	string nome;

//Entrada de dados
/*
	cout<<"Qual o nome do jogador?\n";
	cin>>nome;
	
	cout<<"Quantas vidas o jogador iniciará?\n";
	cin>>vidas;
	
	while(vidas>=0)
{	
	
	cout<<"O jogador "<<nome<<" tem "<<vidas<<" vidas"<<endl;

	cout<<"O jogador já morreu quantas vezes?\n";
	cin>>mortes;
	
	cout<<"Quantos tiros ele efetuou?\n";
	cin>>tiros;
	
	cout<<"Quantos tiros ele acertou?\n";
	cin>> acertos;

//Teste de condição
if(acertos>tiros){
	acertos=tiros;
	cout<<"Impossível acertar mais tiros do que os disparados!";
}
	vidas = vidas - mortes + ((acertos)/2);
	
	if(vidas>=0)
{

	cout<<"\n O jogador está vivo...\n ...por enquanto kkk\n";
	
}
	
}

	cout<<"\nGame Over\n";

system("pause");
return 0;
}
*/
	cout<<"Qual o nome do jogador?\n";
	cin>>nome;
	
	cout<<"Quantas vidas o jogador tem?\n";
	cin>>vidas;
	
	cout<<"O jogador "<<nome<<" tem "<<vidas<<" vidas"<<endl;

	cout<<"O jogador já morreu quantas vezes?\n";
	cin>>mortes;

	cout<<"Quantos tiros ele sofreu?\n";
	cin>>tiros;
	
	status = vidas - mortes ;

if(tiros>=5)
{
	cout<<"Game Over, morreu por excessos de tiros.";
	status = -1;
}

	if(status<0)
{
	
	cout<<"\nGame Over\n";
}
	else
{
	cout<<"\n O jogador está vivo...\n ...por enquanto kkk\n";
}



system("pause");
return 0;
}

