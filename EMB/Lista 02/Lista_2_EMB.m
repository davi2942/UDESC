%Cálculo da Força Magnética Questão 02
clc;
close all;
clear all;
%Valores pré definidos
R1=10*10^-2;
R2=15*10^-2;
i=1;
d=7*10^-2;
u0=4*pi*10^-7;                  %Constante
k=((-u0*i^2*R1*R2)/(4*pi));     %Cálculo da constante que multiplicará a Integral

N=1000;                         %Número de discretizações
dtheta=(2*pi)/N;                %Discretizando a variável de Integração
dphi=(2*pi)/N;                  %Discretizando a variável de Integração

Fx1=0;
Fy1=0;
Fz1=0;
%Cálculo da Integral
for i=1: N
    for j=1: N
     Fx1=Fx1+(cos(j*dphi)*(R1-R2*cos(i*dtheta-j*dphi))/(R1^2+R2^2+d^2-2*R1*R2*cos(i*dtheta-j*dphi))^(3/2))*dtheta*dphi;
     Fy1=Fy1+((sin(j*dphi)*(R1-R2*cos(i*dtheta-j*dphi)))/(R1^2+R2^2+d^2-2*R1*R2*cos(i*dtheta-j*dphi))^(3/2))*dtheta*dphi;
     Fz1=Fz1+((cos(i*dtheta-j*dphi))/(R1^2+R2^2+d^2-2*R1*R2*cos(i*dtheta-j*dphi))^(3/2))*dtheta*dphi;
    end
end
%Valor final da força
%Multiplicando a Integral pela constante calculada anteriormente
Fx=k*Fx1
Fy=k*Fy1
Fz=-k*d*Fz1

%%
%Cálculo da Indução Magnética com z=0 Questão 06
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

n=1;                %Número de voltas da hélice a ser considerado
N=1000;             %Número de discretizações
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

% figure(4)
% surf(x,y,Bmod),title('Módulo da Indução Magnética');    %Definindo o título do gráfico
% xlabel('x'), ylabel('y');                               %Definindo nome nos eixos

figure(5)
contour(x,y,Bmod) %Contornos equipotenciais
hold on
quiver(x,y,unx,uny) %mapa vetorial
title('Contorno Equipotencial e Mapa Vetorial');        %Definindo o título do gráfico
xlabel('x'), ylabel('y');                               %Definindo nome nos eixos

%%
%Cálculo da Indução Magnética com y=0 Questão 06
clc;
close all;
clear all;
%Valores pré definidos
R=10e-2;
Z=5e-2;
I=1;
u0=4*pi*10^(-7);    %Constante
x=-1:0.1:1;        %Variando x com passo de 0,05
y=0;                %Zerando a variável y
z=-1:0.1:1;        %Variando z com passo de 0,05

n=1;                %Número de voltas da hélice a ser considerado
N=1000;             %Número de discretizações
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

%%
%Cálculo da Indução Magnética ao longo do eixo z Questão 06
%Como foi pedido a indução magnética ao longo do eixo z, zerei as variáveis
%x e y e variei o z, gerando um gráfico dos pontos de indução magnética das
%três direções (x,y e z) em relação ao eixo z. No gráfico é possível obter
%o valor da indução magnética em cada ponto.
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
