import numpy as np 
# import matplotlib.pyplot as plt
# import sympy as sp
# import random

#Definindo constantes
R1 = 10*10**-2
R2 = 15*10**-2
I = -1
d = 7*10**-2
u0 = 4*np.pi*10**-7

N = 1000                     #Número de discretizações
dtheta = dphi = (2*np.pi)/N
Fx1 = Fy1 = Fz1 = 0               #Zerando as componentes

#Cálculo da Integral
for i in range(1, N+1):
    for j in range(1, N+1):
        Fx1 = Fx1+dtheta*dphi*(np.cos(j*dphi)*(R1-R2*np.cos(i*dtheta-j*dphi)))/(R1**2+R2**2+d**2-2*R1*R2*np.cos(i*dtheta-j*dphi))**(3/2)
        Fy1 = Fy1+dtheta*dphi*(np.sin(j*dphi)*(R1-R2*np.cos(i*dtheta-j*dphi)))/(R1**2+R2**2+d**2-2*R1*R2*np.cos(i*dtheta-j*dphi))**(3/2)
        Fz1 = Fz1+dtheta*dphi*(d*np.cos(i*dtheta-j*dphi))/(R1**2+R2**2+d**2-2*R1*R2*np.cos(i*dtheta-j*dphi))**(3/2)
#Multiplicando a integral pelas constantes
Fx = u0*I*R1*R2/(4*np.pi)*Fx1
Fy = u0*I*R1*R2/(4*np.pi)*Fy1
Fz = -u0*I*R1*R2/(4*np.pi)*Fz1
#Pintando o valor das integrais
print(f'Fx = {Fx}\nFy = {Fy}\nFz = {Fz}')
