clc;
clear all;
close all;

Lx=0.1; Ly=0.1; Lz=0.1;
Nx=50; Ny=50;
dx=Lx/(Nx-1); dy=Ly/(Ny-1);
Vo=1;
N=150; M=150;
z=Lz;

for i=1:Nx
    x(i)=(i-1)*dx;
end
for j=1:Ny
    y(j)=(j-1)*dy;
end

for i=1:Nx
    for j=1:Ny
        Va(i,j)=0;
        for n=1:N
            for m=1:M
                %Definindo Knm
                Knm1=(1-cos(n*pi/2))*(1-cos(m*pi/2));
                Knm2=(cos(n*pi)-cos(n*pi/2))*(1-cos(m*pi/2));
                Knm3=(1-cos(n*pi/2))*(cos(m*pi)-cos(m*pi/2));
                Knm4=(cos(n*pi)-cos(n*pi/2))*(cos(m*pi)-cos(m*pi/2));
                Knm=2*Vo/(n*m*pi^2)*(Knm1+Knm2+Knm3+Knm4);
                Va(i,j)=Va(i,j)+Knm*(sin(n*pi*x(i)/Lx)*sin(m*pi*y(j)/Ly));
            end
        end
    end
end

figure(1);
surf(x,y,Va);
xlabel('x (m)');
ylabel('y (m)');
zlabel('V (V)');
title('Distribuição do Potêncial Elétrico - Analítico')
colorbar;
