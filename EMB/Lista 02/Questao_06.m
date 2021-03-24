%Cálculo da Indução Magnética com z=0
clc;
close all;
clear all;
%Valores pré definidos
R=10e-2;
Z=5e-2;
I=1;
u0=4*pi*10^(-7);    %Constante
x=-1:0.05:1;        %Variando x com passo de 0,05
y=-1:0.05:1;        %Variando y com passo de 0,05
z=0;                %Zerando a variável z

n=5;                %Número de voltas da hélice a ser considerado
N=5000;             %Número de discretizações
dphil=2*pi*n/N;     %Discretizando a variável de integração

%Zerando as matrizes e definindo o seu tamanho
phi=zeros(length(x),length(y));
rho=zeros(length(x),length(y));
Bx=zeros(length(x),length(y));
By=zeros(length(x),length(y));
Bz=zeros(length(x),length(y));

%Variando x e y e salvando os valores de indução magnética em matrizes
for k=1: length(x)
    for h=1: length(y)

Bx1=0;
By1=0;
Bz1=0;
    %Definindo rho e phi em função de k e h
    rho(k,h)=(x(k)^2+y(h)^2)^(1/2);
    phi(k,h)=atan2(x(k),y(h));
%Cálculo da Integral
for j=1:N
    Bx1=Bx1+(z*R*cos(j*dphil)-Z*rho(k,h)*sin(phi(k,h))/(2*pi)+Z*R*(sin(j*dphil)-j*dphil*cos(j*dphil))/(2*pi))/(rho(k,h)^2+R^2-2*rho(k,h)*R*cos(phi(k,h)-j*dphil)+(z-Z*j*dphil/(2*pi))^2)^(3/2)*dphil;
    By1=By1+(z*R*sin(j*dphil)+Z*rho(k,h)*cos(phi(k,h))/(2*pi)-Z*R*(j*dphil*sin(j*dphil)+cos(j*dphil))/(2*pi))/(rho(k,h)^2+R^2-2*rho(k,h)*R*cos(phi(k,h)-j*dphil)+(z-Z*j*dphil/(2*pi))^2)^(3/2)*dphil;
    Bz1=Bz1+(R-rho(k,h)*cos(phi(k,h)-j*dphil))/(rho(k,h)^2+R^2-2*rho(k,h)*R*cos(phi(k,h)-j*dphil)+(z-Z*j*dphil/(2*pi))^2)^(3/2)*dphil; 
end
%Multiplicando o valor da integral pelas constantes
Bx(k,h)=u0*I/(4*pi)*Bx1;
By(k,h)=u0*I/(4*pi)*By1;
Bz(k,h)=u0*I*R/(4*pi)*Bz1;
Bmod(k,h)=(Bx(k,h)^2+By(k,h)^2+Bz(k,h)^2)^(1/2); %Cálculo do módulo da Integral
unx(k,h)=Bx(k,h)/Bmod(k,h);                      %Cálculo de Bx unitário
uny(k,h)=By(k,h)/Bmod(k,h);                      %Cálculo de By unitário
    end
end
%Gerando as superfícies em figuras separadas
figure(1)
grid on
surf(x,y,Bx),title('Indução Magnética de Bx');          %Definindo o título do gráfico
xlabel('x'), ylabel('y');                               %Definindo nome nos eixos

figure(2)
surf(x,y,By),title('Indução Magnética de By');          %Definindo o título do gráfico
xlabel('x'), ylabel('y');                               %Definindo nome nos eixos

figure(3)
surf(x,y,Bz),title('Indução Magnética de Bz');          %Definindo o título do gráfico
xlabel('x'), ylabel('y');                               %Definindo nome nos eixos

figure(4)
surf(x,y,Bmod),title('Módulo da Indução Magnética');    %Definindo o título do gráfico
xlabel('x'), ylabel('y');                               %Definindo nome nos eixos

figure(5)
contour(x,y,Bmod) %Contornos equipotenciais
hold on
quiver(x,y,unx,uny) %mapa vetorial
title('Contorno Equipotencial e Mapa Vetorial');        %Definindo o título do gráfico
xlabel('x'), ylabel('y');                               %Definindo nome nos eixos
