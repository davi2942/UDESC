import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

#Dados da malha de discretização
Lx, Ly, Nx, Ny, Vo = 10e-2, 10e-2, 20, 20, 1
dx, dy = Lx/Nx, Ly/Ny

#Condições de contorno
Vx1, VxNx, Vy1, VyNy = 0, 0, 0, Vo
Var, x, y = list(), list(), list()
V = np.ones((Nx, Ny))

#Inicializando matriz de potencial
for i in range(1, Nx+1):
    for j in range(1, Ny+1):
        V[i-1, j-1] = Vo

#Inicializando variáveis auxiliares
Va, varmax, ct, tol = V, 1, 0, 1e-6

#Calculo do potencial pelo método interativo de Gauss-Seidel
while varmax>tol:
   ct +=1
   varmax = 0
   for i in range(1, Nx+1):
      for j in range(1, Ny+1):
         #Acrescenta potencial V(i-1,j)
         if i>1:
            V[i-1,j-1] = dy**2*V[i-2, j-1]
         else:
            V[i-1,j-1] = dy**2*Vx1
         #Acrecenta potencial V(i+1,j)
         if i<Nx:
            V[i-1,j-1] = V[i-1,j-1]+dy**2*V[i, j-1]
         else:
            V[i-1,j-1] = V[i-1,j-1]+dy**2*VxNx
         #Acrecenta potencial V(i,j-1)
         if j>1:
            V[i-1,j-1] = V[i-1,j-1]+dx**2*V[i-1, j-2]
         else:
            V[i-1,j-1] = V[i-1,j-1]+dx**2*Vy1
         #Acrecenta potencial V(i,j+1)
         if j<Ny:
            V[i-1,j-1] = V[i-1,j-1]+dx**2*V[i,j+1]
         else:
            V[i-1,j-1] = V[i-1,j-1]+dx**2*VyNy
         #Potencial na posição (i,j)
         V[i-1,j-1] = V[i-1,j-1]/(2*(dx**2+dy**2))
         #Variação do potencial entre duas iterações sucessivas
         dif = abs(V[i-1,j-1]-Va[i-1,j-1])
         if dif>varmax:
             varmax = dif
   Va = V                #Atualiza a matriz anterior
   Var[ct] = varmax

#Definindo os eixos
for i in range(1, Nx+1):
   x[i-1] = dx+(i-1)*(Lx-2*dx)/(Nx-1)

for j in range(1, Ny+1):
   y[j-1] = dy+(j-1)*(Ly-2*dy)/(Ny-1)

#Gráfico de superfície
plt.figure(1)
# surf(x,y,V);
plt.xlabel('y(m)')
plt.ylabel('x(m)')
ax.set_zlabel('V(V)')
plt.title('Distribuição de Potencial Elétrico')
# colorbar;
