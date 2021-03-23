#include<iostream>

using namespace std;

int main(){
	int x,y,n,i,j;
	
	cout<<"Digite um numero N!\n";
	cin>>n;
	int vet[n];
	cout<<"Digite "<<n<<" numeros.\n";
	
	for(i=0;i<n;i++){
	cin>>x;
	vet[i]=x;
}

 for (j=0; j<n; j++)
{
for(i=0;i<n;i++)
{
  if (vet[i] > vet[i+1])
  {
     y=vet[i];
     vet[i] = vet[i+1];
     vet[i+1] = y;
  }
}}
	
	for(i=0;i<n;i++)
	cout<<vet[i]<<"\t";
	cout<<endl;
	
system("pause");
return 0;	
}
