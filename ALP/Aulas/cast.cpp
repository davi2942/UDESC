#include<iostream>

using namespace std;

int main(){
	
	int a,b;
	float rdcc,rdsc;
	
	a=13;
	b=26;
	
	rdcc = (float) a/b;
	rdsc = a/b;
	
	cout<<"\nResultado da divisao *sem cast* = "<<rdsc;
	cout<<"\nResultado da divisao *com cast* = "<<rdcc;
	
return 0;	
}
