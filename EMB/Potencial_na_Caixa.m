clc;
clear all;
close all;

%Cálculo Analítico %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Lx = 0.1; Ly = 0.1; Lz = 0.1;
Nx = 50; Ny = 50; Nz = 50;
dxa=Lx/(Nx-1); dya=Ly/(Ny-1);
Vo = 1;
N=150; M=150;

for i=1:Nx
    xa(i)=(i-1)*dxa;
end
for j=1:Ny
    ya(j)=(j-1)*dya;
end

for i=1:Nx
    for j=1:Ny
        Van(i,j)=0;
        for n=1:N
            for m=1:M
                %Definindo Knm
                Knm1 = (1-cos(n*pi/2))*(1-cos(m*pi/2));
                Knm2 = (cos(n*pi)-cos(n*pi/2))*(1-cos(m*pi/2));
                Knm3 = (1-cos(n*pi/2))*(cos(m*pi)-cos(m*pi/2));
                Knm4 = (cos(n*pi)-cos(n*pi/2))*(cos(m*pi)-cos(m*pi/2));
                Knm = 2*Vo/(n*m*pi^2)*(Knm1+Knm2+Knm3+Knm4);
                Van(i,j) = Van(i,j)+Knm*(sin(n*pi*xa(i)/Lx)*sin(m*pi*ya(j)/Ly));
            end
        end
    end
end

% figure(1);
% surf(xa,ya,Van);
% xlabel('x (m)');
% ylabel('y (m)');
% zlabel('V (V)');
% title('Distribuição do Potêncial Elétrico - Analítico')
% colorbar;

%Cálculo Numérico %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Dimensões do problema
dx = Lx/Nx; dy = Ly/Ny; dz = Lz/Nz;

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
                    if (i<Nx/2 && j<Ny/2)
                        V(i,j,k)=V(i,j,k)+dx^2*dy^2*Vx1Nz;
                    end
                    if (i>Nx/2 && j<Ny/2)
                        V(i,j,k)=V(i,j,k)+dx^2*dy^2*Vx2Nz;
                    end
                    if (i<Nx/2 && j>Ny/2)
                        V(i,j,k)=V(i,j,k)+dx^2*dy^2*Vx2Nz;
                    end
                    if (i>Nx/2 && j>Ny/2)
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
        VD(i,j)=V(i,j,Nz);
    end
end

%Gráfico de superfície
% figure(2)
% surf(x,y,VD);
% xlabel('x(m)');
% ylabel('y(m)');
% zlabel('V(V)');
% title('Distribuição de Potencial Elétrico - Numérico');
% colorbar;

%Cálculo do Campo Elétrico
j=Ny/4+0.5;
for i=1:Nx
   for k=1:Nz
      if i<Nx
         Ex(i,j,k)=(V(i,j,k)-V(i+1,j,k))/dx;
      else
         Ex(i,j,k)=(V(i,j,k)-VxNx)/dx;
      end
		if k<Nz
         Ez(i,j,k)=(V(i,j,k)-V(i,j,k+1))/dz;
      else
          Ez(i,j,k)=(V(i,j,k)-VyNy)/dz;
      end
      unx(i,k)=Ex(i,j,k)/sqrt(Ex(i,j,k)^2+Ez(i,j,k)^2);
      unz(i,k)=Ez(i,j,k)/sqrt(Ex(i,j,k)^2+Ez(i,j,k)^2);
   end
end

for i=1:Nx
    for k=1:Ny
        Vxz(i,k)=V(i,Ny/4+0.5,k);
    end
end

% figure(3)
% contour(x,z,Vxz);
% hold on
% quiver(x,z,unz,unx);
% hold off
% xlabel('z(m)');
% ylabel('x(m)');
% title('Linhas Equipotenciais');
% colorbar;

%Comparação com modelo analítico
% Potencial no eixo x;
j=13;
for i=1:Nx
   Veixox(i)=VD(i,j);
%    Vteixox(i)=0;
   Vteixox(i)= Van(i,j);
end

%Potencial no eixo y;
i=13;
for j=1:Ny
   Veixoy(j)=VD(i,j);
%    Vteixoy(j)=0;
   Vteixoy(j)= Van(i,j);
end

% figure(4)
% subplot(2,1,1)
% plot(x,Veixox,'k-',x,Vteixox,'ro');
% xlabel('x(m)');
% ylabel('V(V)');
% title('Potencial Elétrico ao longo do eixo j=13');
% grid on;
% legend('Numérico','Analítico');
% subplot(2,1,2)
% plot(y,Veixoy,'k-',y,Vteixoy,'ro');
% xlabel('y(m)');
% ylabel('V(V)');
% title('Potencial Elétrico ao longo do eixo i=13');
% grid on;
% legend('Numérico','Analítico');

%Comparando os três métodos %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
arquivo_femm = load('Dados_femm.txt');
femm_x = Nz/10*arquivo_femm(:,1);
femm_y = arquivo_femm(:, 2);

VDcomp = zeros(1,Nz);
Vancomp = zeros(1,Nz);
i=13; j=13;
for k=1:Nz
    VDcomp(k) = VDcomp(k)+ V(i,j,k);
    for n=1:N
        for m=1:M
            %Definindo Knm
            Knm1 = (1-cos(n*pi/2))*(1-cos(m*pi/2));
            Knm2 = (cos(n*pi)-cos(n*pi/2))*(1-cos(m*pi/2));
            Knm3 = (1-cos(n*pi/2))*(cos(m*pi)-cos(m*pi/2));
            Knm4 = (cos(n*pi)-cos(n*pi/2))*(cos(m*pi)-cos(m*pi/2));
            Knm = 2*Vo/(n*m*pi^2)*(Knm1+Knm2+Knm3+Knm4);
            Vancomp(k) = Vancomp(k)+Knm*(sin(n*pi*i/Lx)*sin(m*pi*j/Ly));
            end
    end
end

k = 1:Nz;
figure(5)
plot(k,Vancomp,'g*');
% plot(femm_x,femm_y,'r',k,VDcomp,'bo',k,Vancomp,'g*');
grid on;
title('Comparação entre Métodos');
xlabel('Eixo x');
ylabel('Eixo y');
legend('Femm','Numérico')
