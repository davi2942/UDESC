#include<iostream>

using namespace std;

void flag();
int i,c=0;
char vet[100],y;

int main(){
	
	cout<<"Digite letras para serem armazenadas:\n";
	cout<<"Para parar o programa digite y.\n";
	flag();
	
system("pause");
return 0;
}

void flag(){
	while(y!='y'){
	cin>>y;
	vet[c]=y;
	c++;	
}
	c=c-1;
	cout<<endl;
	for(i=0;i<c;i++)
	cout<<vet[i]<<"\t";	
	cout<<endl;	
}
