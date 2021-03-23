clc;
clear all;
close all;

%Dimensões do problema
Lx = 0.1; Ly = 0.1; Lz = 0.1;
Nx = 50; Ny = 50; Nz = 50;
dx = Lx/Nx; dy = Ly/Ny; dz = Lz/Nz;
Vo = 1;
N=150;

%Condições de contorno
Vx = 0; Vy = 0; Vz = 0;
VxNx = 0; VyNy = 0; VzNx = 0; VzNy = 0;
VzNxNy = 0;
Vx1Nz = Vo/2; Vx2Nz = -Vo/2;

%Inicializa matriz de potencial
for i=1:Nx
    for j=1:Ny
        for k=1:Nz
            V(i,j,k) = Vo;
        end
    end
end

%Inicializa variáveis auxiliares
Va=V;
varmax=1;
ct=0;
tol=1e-6;

%Calcula potencial por método iterativo de Gauss-Seidel
while varmax>tol
   ct=ct+1;
   varmax=0;
   for i=1:Nx
       for j=1:Ny
           for k=1:Nz
               %Acrescenta potencial V(i-1,j)
                if i>1
                    V(i,j,k)=dy^2*dz^2*V(i-1,j,k);
                else
                    V(i,j,k)=dy^2*dz^2*Vx;
                end
                %Acrescenta potencial V(i+1,j,k)
                if i<Nx
                    V(i,j,k)=V(i,j,k)+dy^2*dz^2*V(i+1,j,k);
                else
                    V(i,j,k)=V(i,j,k)+dy^2*dz^2*VxNx;
                end
                %Acrescenta potencial V(i,j-1,k)
                if j>1
                    V(i,j,k)=V(i,j,k)+dx^2*dz^2*V(i,j-1,k);
                else
                    V(i,j,k)=V(i,j,k)+dx^2*dz^2*Vy;
                end
                %Acrescenta potencial V(i,j+1,k)
                if j<Ny
                    V(i,j,k)=V(i,j,k)+dx^2*dz^2*V(i,j+1,k);
                else
                    V(i,j,k)=V(i,j,k)+dx^2*dz^2*VyNy;
                end
                %Acrescenta potencial V(i,j,k-1)
                if k>1
                    V(i,j,k)=V(i,j,k)+dx^2*dy^2*V(i,j,k-1);
                else
                    V(i,j,k)=V(i,j,k)+dx^2*dy^2*Vz;
                end
                %Acrescenta potencial V(i,j,k+1)
                if k<Nz
                    V(i,j,k)=V(i,j,k)+dx^2*dy^2*V(i,j,k+1);
                else
                    if (i<25 && j<25)
                        V(i,j,k)=V(i,j,k)+dx^2*dy^2*Vx1Nz;
                    end
                    if (i>25 && j<25)
                        V(i,j,k)=V(i,j,k)+dx^2*dy^2*Vx2Nz;
                    end
                    if (i<25 && j>25)
                        V(i,j,k)=V(i,j,k)+dx^2*dy^2*Vx2Nz;
                    end
                    if (i>25 && j>25)
                        V(i,j,k)=V(i,j,k)+dx^2*dy^2*Vx1Nz;
                    end
                end
             %Potencial na posição (i,j,k)
             V(i,j,k)=V(i,j,k)/(2*(dy^2*dz^2+dx^2*dz^2+dx^2*dy^2));
            %Variação do potencial entre duas iterações sucessivas
            dif=abs(V(i,j,k)-Va(i,j,k));
            if dif>varmax
               varmax=dif;
            end
         end
      end
   end
   %Atualiza matriz anterior
   Va=V;
   Var(ct)=varmax;
end
%Define eixos
for i=1:Nx
   x(i)=dx+(i-1)*(Lx-2*dx)/(Nx-1);
end

for j=1:Ny
   y(j)=dy+(j-1)*(Ly-2*dy)/(Ny-1);
end

for k=1:Nz
    z(k)=dz+(k-1)*(Lz-2*dz)/(Nz-1);
end

for i=1:Nx
    for j=1:Ny
        VD(i,j)=V(i,j,50);
    end
end

%Gráfico de superfície
figure(1)
surf(x,y,VD);
xlabel('x(m)');
ylabel('y(m)');
zlabel('V(V)');
title('Distribuição de Potencial Elétrico - Numérico');
colorbar;

%Cálculo do Campo Elétrico
for i=1:Nx
   for j=1:Ny
      if i<Nx
         Ex(i,j)=(VD(i,j)-VD(i+1,j))/dx;
      else
         Ex(i,j)=(VD(i,j)-VxNx)/dx;
      end
		if j<Ny
         Ey(i,j)=(VD(i,j)-V(i,j+1))/dy;
      else
          Ey(i,j)=(VD(i,j)-VyNy)/dy;
      end
      unx(i,j)=Ex(i,j)/sqrt(Ex(i,j)^2+Ey(i,j)^2);
      uny(i,j)=Ey(i,j)/sqrt(Ex(i,j)^2+Ey(i,j)^2);
   end
end

figure(2)
contour(x,y,VD);
hold on
quiver(x,y,uny,unx);
hold off
xlabel('x(m)');
ylabel('y(m)');
title('Linhas Equipotenciais');
colorbar;

%Comparação com modelo analítico
%Potencial no eixo x;
% j=10;
% for i=1:Nx
%    Veixox(i)=VD(i,j);
%    Vteixox(i)=0;
%    for n=1:N
%        Knm1=(1-cos(n*pi/2))*(1-cos(n*pi/2));
%        Knm2=(cos(n*pi)-cos(n*pi/2))*(1-cos(n*pi/2));
%        Knm3=(1-cos(n*pi/2))*(cos(n*pi)-cos(n*pi/2));
%        Knm4=(cos(n*pi)-cos(n*pi/2))*(cos(n*pi)-cos(n*pi/2));
%        Knm=2*Vo/(n^2*pi^2)*(Knm1+Knm2+Knm3+Knm4);
%        Vteixox(i)=Vteixox(i)+Knm*(sin(n*pi*x(i)/Lx)*sin(n*pi*y(j)/Ly));
%    end
% end
% 
% %Potencial no eixo y;
% i=10;
% for j=1:Ny
%    Veixoy(j)=VD(i,j);
%    Vteixoy(j)=0;
%     for n=1:N
%         Knm1=(1-cos(n*pi/2))*(1-cos(n*pi/2));
%         Knm2=(cos(n*pi)-cos(n*pi/2))*(1-cos(n*pi/2));
%         Knm3=(1-cos(n*pi/2))*(cos(n*pi)-cos(n*pi/2));
%         Knm4=(cos(n*pi)-cos(n*pi/2))*(cos(n*pi)-cos(n*pi/2));
%         Knm=2*Vo/(n^2*pi^2)*(Knm1+Knm2+Knm3+Knm4);
%         Vteixoy(j)=Vteixoy(j)+Knm*(sin(n*pi*x(i)/Lx)*sin(n*pi*y(j)/Ly));
%     end
% end
% 
% figure(3)
% subplot(2,1,1),plot(x,Veixox,'k-',x,Vteixox,'ro');
% xlabel('x(m)');
% ylabel('V(V)');
% title('Potencial Elétrico ao longo do eixo j=10');
% grid;
% legend('numérico','analítico');
% subplot(2,1,2),plot(y,Veixoy,'k-',y,Vteixoy,'ro');
% xlabel('y(m)');
% ylabel('V(V)');
% title('Potencial Elétrico ao longo do eixo i=10');
% grid;
% legend('numérico','analítico');
