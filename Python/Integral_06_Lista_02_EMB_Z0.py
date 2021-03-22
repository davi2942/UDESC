import numpy as np
import matplotlib.pyplot as plt  # para plotar

#Definindo constantes
R, Z, I, u0, pi2, pi4 = 10e-2, 5e-2, 1, 4*np.pi*1e-7, 2*np.pi, 4*np.pi

#Variando as posições no espaço
x, y, z = np.arange(-1, 1, 0.1), np.arange(-1, 1, 0.1), 0

#Número de discretizações, Números de espiras
N, n = 1000, 1
dphi = 2*np.pi*n/N          #Variável de integração discretizada

#Inicializando as matrizes e definindo o seu tamanho
phi, rho = np.ones((len(x), len(y))), np.ones((len(x), len(y)))
Bx, By, Bz = np.ones((len(x), len(y))), np.ones((len(x), len(y))), np.ones((len(x), len(y)))
Bmod = np.ones((len(x), len(y)))
unx, uny = np.ones((len(x), len(y))), np.ones((len(x), len(y)))

for j in range(1, len(x)+1):
    for k in range(1, len(y)+1):
        Bx1, By1, Bz1 = 0, 0, 0

        rho[j-1][k-1] = (x[j-1]**2+y[k-1]**2)**(1/2)
        phi[j-1][k-1] = np.arctan2(y[k-1], x[j-1])

        #Cálculo da integral
        for i in range(1,N+1):
            Bx1 = Bx1 + (z*R*np.cos(i*dphi)-Z*rho[j-1][k-1]*np.sin(phi[j-1][k-1])/pi2+Z*R*(np.sin(i*dphi)-i*dphi*np.cos(i*dphi))/pi2)/(rho[j-1][k-1]**2+R**2-2*rho[j-1][k-1]*R*np.cos(phi[j-1][k-1]-i*dphi)+(z-Z*i*dphi/pi2)**2)**(3/2)*dphi
            By1 = By1 + (z*R*np.sin(i*dphi)+Z*rho[j-1][k-1]*np.cos(phi[j-1][k-1])/pi2-Z*R*(i*dphi*np.sin(i*dphi)+np.cos(i*dphi))/pi2)/(rho[j-1][k-1]**2+R**2-2*rho[j-1][k-1]*R*np.cos(phi[j-1][k-1]-i*dphi)+(z-Z*i*dphi/pi2)**2)**(3/2)*dphi
            Bz1 = Bz1 + (R-rho[j-1][k-1]*np.cos(phi[j-1][k-1]-i*dphi))/(rho[j-1][k-1]**2+R**2-2*rho[j-1][k-1]*R*np.cos(phi[j-1][k-1]-i*dphi)+(z-Z*i*dphi/pi2)**2)**(3/2)*dphi

        Bx[j-1][k-1] = u0*I/pi4*Bx1
        By[j-1][k-1] = u0*I/pi4*By1
        Bz[j-1][k-1] = u0*I*R/pi4*Bz1
        Bmod[j-1][k-1] = (Bx[j-1][k-1]**2+By[j-1][k-1]**2+Bz[j-1][k-1]**2)**(1/2)
        unx[j-1][k-1] = Bx[j-1][k-1]/Bmod[j-1][k-1]
        uny[j-1][k-1] = By[j-1][k-1]/Bmod[j-1][k-1]

plt.figure(1)
plt.plot(x, Bx)
plt.grid(True)
plt.title('Bx')

plt.figure(2)
plt.plot(x, Bz)
plt.grid(True)
plt.title('Bz/x')

plt.figure(3)
plt.plot(y, Bz)
plt.grid(True)
plt.title('Bz/y')
plt.show()
