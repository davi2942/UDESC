#include<iostream>
#include<iomanip>

using namespace std;

void calculo();
	int i,j;
	float M[10][4],m,m1,m2,m3,m4,m5,m6,m7,m8,m9,m0;

int main(){
	
	cout << fixed << setprecision(1);
	cout<<"Digite as notas dos alunos:\n\n\n\n\n\n\n\n";
	system("pause");
	calculo();

system("pause");
return 0;
}

void calculo(){
	inicio:
	system("cls");
for(i=0;i<10;i++){
	for(j=0;j<3;j++){
	cin>>M[i][j];
	if((M[i][j]<0)||(M[i][j]>10)){
	cout<<"Nao existe essa nota!\n";
	system("pause");
	goto inicio;
}
	m=m+ M[i][j];
}
	if(i==0)
	m1 = m/3;
	if(i==1)
	m2 = m/3;
	if(i==2)
	m3=m/3;
	if(i==3)
	m4=m/3;
	if(i==4)
	m5=m/3;
	if(i==5)
	m6=m/3;
	if(i==6)
	m7=m/3;
	if(i==7)
	m8=m/3;
	if(i==8)
	m9=m/3;
	if(i==9)
	m0=m/3;
	m=0;
}	
	M[0][3]=m1;
	M[1][3]=m2;
	M[2][3]=m3;
	M[3][3]=m4;
	M[4][3]=m5;
	M[5][3]=m6;
	M[6][3]=m7;
	M[7][3]=m8;
	M[8][3]=m9;
	M[9][3]=m0;
	
	system("cls");
	cout<<"Nota 01\tNota 02\tNota 03\tMedia\n";
	for(i=0;i<10;i++){
	for(j=0;j<4;j++)
	cout<<M[i][j]<<"\t";
	cout<<"\n";
}
}
