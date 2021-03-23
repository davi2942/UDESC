#include<iostream>

using namespace std;

void soma();
int x,i,y;

int main(){
	
	cout<<"Digite tres numeros inteiros!\n";
	soma();
	
system("pause");
return 0;
}

void soma(){
	
	for(i=0;i<3;i++){
		cin>>x;
		y=y+x;
	}
	
	cout<<"Este eh o valor da soma dos 3 numeros!\n"<<y<<endl;
}
