#include<iostream>
#include<stdio.h>
#include<conio.h>
#include<math.h>

using namespace std;

void bhaskara();
float delta, rdelta,ndelta, x1,x2,y,a,b,c;

int main(){
	setlocale(LC_ALL, "Portuguese");
	
	cout<<"Informe o valor de a da equação\n";
    cin>>a;
    cout<<"Informe o valor de b da equacao\n";
    cin>>b;
    cout<<"Informe o valor de c da equacao\n";
    cin>>c;
	bhaskara();
	
return 0;
}

void bhaskara(){
	
	if(a==0){
	cout<<"Não é uma parábola!";
}
	else{
		
    delta = ((b*b)-4*a*c);
    rdelta = sqrt(delta);
    
    if(delta>0){
    	
    x1 = ((-b + rdelta)/(2*a));
    x2 = ((-b - rdelta)/(2*a));
    
    cout<<"x1 = "<<x1<<endl;
    cout<<"x2 = "<<x2<<endl;
}
 else{     
    ndelta= (delta*(-1));   
    
    x1 = ((-b + (sqrt(ndelta)))/(2*a));
    x2 = ((-b - (sqrt(ndelta)))/(2*a));
    
    cout<<"x1 = "<<x1<<"i"<<endl;
    cout<<"x2 = "<<x2<<"i"<<endl;

}}}
/*
void triangulo();
int a, b, c;
void rect();
int x, y;*/
	/*
	cout<<"Digite a, b e c:\n";
	cin>>a;
	cin>>b;
	cin>>c;
	triangulo();
	
	cout<<"Digite dois valores para a figura geometrica:\n";
	cin>>x;
	cin>>y;
	rect();
	*/
/*
void triangulo(){

	if((a<b+c)&&(b<c+a)&&(c<a+b)){
	if((a==b)&&(b==c))
	cout<<"Triangulo equilatero\n";
	
	else
	if((a==b)||(b==c)||(c==a))
	cout<<"Triangulo isoceles\n";
	else
	cout<<"Triangulo escaleno\n";
}
	else
	cout<<"Nao eh um triangulo!\n";
}

void rect(){
	if(x==y)
	cout<<"Eh um quadrado!\n";
	else
	if(x<y)
	cout<<"Eh um retangulo e o lado maior esta na direcao de y!\n";
	else{
	cout<<"Eh um retangulo e o lado maior esta no x!\n";}
}
*/
