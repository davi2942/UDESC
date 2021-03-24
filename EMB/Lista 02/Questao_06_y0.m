%Cálculo da Indução Magnética com y=0
clc;
close all;
clear all;
%Valores pré definidos
R=10e-2;
Z=5e-2;
I=1;
u0=4*pi*10^(-7);    %Constante
x=-1:0.05:1;        %Variando x com passo de 0,05
y=0;                %Zerando a variável y
z=-1:0.05:1;        %Variando z com passo de 0,05

n=5;                %Número de voltas da hélice a ser considerado
N=5000;             %Número de discretizações
dphil=2*pi*n/N;     %Discretizando a variável de integração
phi=0;

%Zerando as matrizes e definindo o seu tamanho
rho=zeros(length(x),1);
Bx=zeros(length(x),length(z));
By=zeros(length(x),length(z));
Bz=zeros(length(x),length(z));

%Variando x e z e salvando os valores de indução magnética em matrizes
for k=1: length(x)
    for h=1: length(z)

Bx1=0;
By1=0;
Bz1=0;
    %Definindo rho e phi em função de k e h
    rho(k)=abs(x(k));                  %Como y=0, rho se resume a x
    %Cálculo da Integral
for j=1:N
    Bx1=Bx1+(z(h)*R*cos(j*dphil)-Z*rho(k)*sin(phi)/(2*pi)+Z*R*(sin(j*dphil)-j*dphil*cos(j*dphil))/(2*pi))/(rho(k)^2+R^2-2*R*rho(k)*cos(phi-j*dphil)+(z(h)-(Z*j*dphil)/(2*pi))^2)^(3/2)*dphil;
    By1=By1+(z(h)*R*sin(j*dphil)+Z*rho(k)*cos(phi)/(2*pi)-Z*R*(j*dphil*sin(j*dphil)+cos(j*dphil))/(2*pi))/(rho(k)^2+R^2-2*R*rho(k)*cos(phi-j*dphil)+(z(h)-(Z*j*dphil)/(2*pi))^2)^(3/2)*dphil;
    Bz1=Bz1+(R-rho(k)*cos(phi-j*dphil))/(rho(k)^2+R^2-2*R*rho(k)*cos(phi-j*dphil)+(z(h)-(Z*j*dphil)/(2*pi))^2)^(3/2)*dphil;
end
%Multiplicando o valor da integral pelas constantes
Bx(k,h)=u0*I/(4*pi)*Bx1;
By(k,h)=u0*I/(4*pi)*By1;
Bz(k,h)=u0*I*R/(4*pi)*Bz1;
Bmod(k,h)=(Bx(k,h)^2+By(k,h)^2+Bz(k,h)^2)^(1/2); %Cálculo do módulo da Integral
unx(k,h)=Bx(k,h)/Bmod(k,h);                      %Cálculo de Bx unitário
unz(k,h)=Bz(k,h)/Bmod(k,h);                      %Cálculo de Bz unitário
    end
end
%Gerando as superfícies em figuras separadas
figure(1)
grid on
surf(x,z,Bx),title('Indução Magnética de Bx');
xlabel('x'), ylabel('z');

figure(2)
surf(x,z,By),title('Indução Magnética de By');
xlabel('x'), ylabel('z');

figure(3)
surf(x,z,Bz),title('Indução Magnética de Bz');
xlabel('x'), ylabel('z');
figure(4)
surf(x,z,Bmod),title('Módulo da Indução Magnética');
xlabel('x'), ylabel('z');

figure(5)
contour(x,z,Bmod) %Contornos equipotenciais
hold on
quiver(x,z,unx,unz) %mapa vetorial
title('Contorno Equipotencial e Mapa Vetorial');
xlabel('x'), ylabel('z');
