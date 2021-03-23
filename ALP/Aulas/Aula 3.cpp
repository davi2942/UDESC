#include <stdlib.h>
#include <locale.h>
#include <iostream>
#include <cmath>

using namespace std;
/*
int main()
{
    setlocale(LC_ALL, "Portuguese");
    
    //Inicialização de Variaveis
    int dinheiro;
    string nome;
    
    //Programa pergunta
    cout<<"Qual o nome do Player?\n";
    //Programa armazena a informação em uma string
    
    cin>>nome;
    
    cout<<"Quantos dolares o Player comprou?"<<endl;
    cin>>dinheiro;
    
    //Programa apresenta resultado da string e do valor armazenado:
               
    cout<<"\nO Player "<<nome<<" tem "<<dinheiro<<" dolares \n";
    system("pause");
    return 0;
}
  */
  int main()
  {
      setlocale(LC_ALL, "Portuguese");
      
      string cpf1, cpf2, cpf3;
      
      string aluno1, aluno2, aluno3;
      
      string curso1, curso2, curso3;

      cout<<"Informe o nome do primeiro aluno."<<endl;
      cin>> aluno1;
      cout<<"Qual o curso do aluno?"<<endl;      
      cin>>curso1;      
      cout<<"Informe o cpf, apenas números\n";
      cin>>cpf1;
      //Aluno 1
      
      cout<<"Informe o nome do segundo aluno."<<endl;
      cin>> aluno2;
      cout<<"Qual o curso do aluno?"<<endl;
      cin>>curso2;
      cout<<"Informe o cpf, apenas números\n";
      cin>>cpf2;
      //Aluno 2
      
      cout<<"Informe o nome do terceiro aluno."<<endl;
      cin>> aluno3;
      cout<<"Qual o curso do aluno?"<<endl;
      cin>>curso3;      
      cout<<"Informe o cpf, apenas números\n";      
      cin>>cpf3;
      //Aluno 3    
      
      cout<<"O aluno "<<aluno1<<" realizou a matrícula no curso de\n"<<curso1<<" e o seu cpf é:"<<cpf1<<endl;
      cout<<"O aluno "<<aluno2<<" realizou a matrícula no curso de\n"<<curso2<<" e o seu cpf é:"<<cpf2<<endl;   
      cout<<"O aluno "<<aluno3<<" realizou a matrícula no curso de\n"<<curso3<<" e o seu cpf é:"<<cpf3<<endl;
   
   
   
      
      system("pause");
return 0;
}


 
