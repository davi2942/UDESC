%Cálculo da Indução Magnética ao longo do eixo z
clc;
close all;
clear all;
%Valores pré definidos
R=10e-2;
Z=5e-2;
I=1;
u0=4*pi*10^(-7);     %Constante
x=0;                 %Zerando a variável x
y=0;                 %Zerando a variável y
z=-1:0.01:1;         %Variando z com passo de 1m

n=1;                 %Número de voltas da hélice a ser considerado
N=1000;              %Número de discretizações
dphil=2*pi*n/N;      %Discretizando a variável de integração

%Zerando rho e phi
rho=0;
phi=0;

%Variando z e salvando o valor de indução magnética em um vetor
for h=1: length(z)
    Bx1=0;
    By1=0;
    Bz1=0;
%Cálculo da Integral    
for j=1:N
    Bx1=Bx1+(z(h)*R*cos(j*dphil)+Z*R*(sin(j*dphil)-j*dphil*cos(j*dphil))/(2*pi))/(R^2+(z(h)-Z*j*dphil/(2*pi))^2)^(3/2)*dphil;
    By1=By1+(z(h)*R*sin(j*dphil)-Z*R*(j*dphil*sin(j*dphil)+cos(j*dphil))/(2*pi))/(R^2+(z(h)-Z*j*dphil/(2*pi))^2)^(3/2)*dphil;
    Bz1=Bz1+(R)/(R^2+(z(h)-Z*j*dphil/(2*pi))^2)^(3/2)*dphil;
end
%Multiplicando o valor da integral pelas constantes
Bx(h)=u0*I/(4*pi)*Bx1;
By(h)=u0*I/(4*pi)*By1;
Bz(h)=u0*I*R/(4*pi)*Bz1;
Bmod(h)=(Bx(h)^2+By(h)^2+Bz(h)^2)^(1/2);
end
%Gerando os gráficos em figuras seperadas
figure(1)
plot(z,Bx);grid on
title('Indução ao longo de z de Bx');   %Definindo o título do gráfico
xlabel('z'); ylabel('Bx');              %Definindo nome nos eixos

figure(2)
plot(z,By);grid on
title('Indução ao longo de z de By');   %Definindo o título do gráfico
xlabel('z'); ylabel('By');              %Definindo nome nos eixos

figure(3)
plot(z,Bz);grid on
title('Indução ao longo de z de Bz');   %Definindo o título do gráfico
xlabel('z'); ylabel('Bz');              %Definindo nome nos eixos
