import numpy as np
import matplotlib.pyplot as plt
# import sympy as sp

cabo= np.genfromtxt('cabo.txt')
fenolite= np.genfromtxt('fenolite.txt')
oleo= np.genfromtxt('oleo.txt')

# Dados de frequencia e Impedância (complexa)
fc, Zc = cabo[:, 0], np.multiply(cabo[:, 1],np.exp(1j*np.pi*cabo[:, 2]/180))
ff, Zf = fenolite[:, 0],  np.multiply(fenolite[:, 1],np.exp(1j*np.pi*fenolite[:, 2]/180))
fo, Zo = oleo[:, 0], np.multiply(oleo[:, 1],np.exp(1j*np.pi*oleo[:, 2]/180)) 

# Dados dos dielétricos
a, b, L = 0.35e-3, 1.4e-3, 24e-2 #Cabo coaxial
do, r= 1e-3, 4.5e-3              #Óleo do transformador
df, l = 1.6e-3, 18.8e-3          #Placa de fenolite
e0=8.854e-12

# Cálculo de sigma e epsilon para cada dielétrico
sigma_f, er_f = df/(l**2)*np.real(1/Zf), df/(l**2*2*np.pi*e0)*np.multiply(1/(2*np.pi*ff),np.imag(1/Zf))
sigma_o, er_o = do/(np.pi*r**2)*np.real(1/Zo), do/((np.pi*r**2)*2*np.pi*e0)*np.multiply(1/(2*np.pi*fo),np.imag(1/Zo))
sigma_c, er_c = np.log(b/a)/(2*np.pi*L)*np.real(1/Zc), np.log(b/a)/(2*np.pi*L*e0)*np.multiply(1/(2*np.pi*fc), np.imag(1/Zc))

# Retira os valores <=0 para a plotagem di-log
for i in range(len(fc)):
    if sigma_c[i]<=0:
        sigma_c[i]= None
    if sigma_o[i]<=0:
        sigma_o[i]= None
    if sigma_f[i]<=0:   
        sigma_f[i]= None

#Calculo teórico por tentativa e erro sigma=sigma_dc+Aw^n
sigdc_f, Af, nf = 4.248e-9, 1.04e-12, 1     #Parâmetros fenolite
sigdc_o, Ao, no = 2.455e-8, 1.10e-12, 0.90  #Parâmetros óleo
sigdc_c, Ac, nc = 2.857e-10, 0.90e-12, 0.7  #Parâmetros cabo coaxial

#Sigma teórico
sigma_ft = np.add(sigdc_f*np.ones(len(ff)),Af*np.power(2*np.pi*ff, nf)) 
sigma_ot = np.add(sigdc_o*np.ones(len(fo)),Ao*np.power(2*np.pi*fo, no))
sigma_ct = np.add(sigdc_c*np.ones(len(fc)),Ac*np.power(2*np.pi*fc, nc))

#Tangente de perdas
tg_f, tg_o, tg_c = sigma_ft/(2*np.pi*e0*er_f*ff), sigma_ot/(2*np.pi*fo*e0*er_o), sigma_ct/(2*np.pi*fc*e0*er_c)

plt.figure(1)
plt.loglog(ff, sigma_f, 'b', label= 'Fenolite Experimental')
plt.loglog(ff, sigma_ft, 'b-.', label= 'Fenolite Teórico')
plt.loglog(fc, sigma_c, 'r', label= 'Cabo Coaxial Experimental')
plt.loglog(fc, sigma_ct, 'r-.', label= 'Cabo Coaxial Teórico')
plt.loglog(fo, sigma_o, 'k', label= 'Óleo Experimental')
plt.loglog(fo, sigma_ot, 'k-.', label= 'Óleo Teórico')
plt.grid(True, which='both', ls='-.'), plt.legend(loc= 'lower left')
plt.xlabel('Frequência [Hz]', size=14), plt.ylabel('Condutividade [S/m]', size=14)

plt.figure(2)
plt.semilogx(ff, er_f, 'b', label= 'Placa de Fenolite')
plt.grid(True, which='both', ls='-.'), plt.legend()
plt.axis([3.5*10, 5*10**7, 0.75, 1.16])
plt.xlabel('Frequência [Hz]', size=14), plt.ylabel('$\epsilon_r$', size=18)

plt.figure(3)
plt.semilogx(fc, er_c, 'k', label= 'Cabo Coaxial')
plt.grid(True, which='both', ls='-.'), plt.legend(loc= 'lower right')
plt.xlabel('Frequência [Hz]', size=14), plt.ylabel('$\epsilon_r$', size=18)
plt.axis([3.5*10, 4.5*10**7, -2.3, 9.35])

plt.figure(4)
plt.semilogx(fo, er_o, 'r', label= 'Óleo de Transformador')
plt.grid(True, which='both', ls='-.'), plt.legend(loc= 'lower right')
plt.axis([3.5*10, 4.5*10**7, -30.5, 56.5])
plt.xlabel('Frequência [Hz]', size=14), plt.ylabel('$\epsilon_r$', size=18)

plt.figure(5)
plt.semilogx(ff, tg_f, 'b', label= 'Placa de Fenolite')
plt.semilogx(fc, tg_c, 'k', label= 'Cabo Coaxial')
plt.semilogx(fo, tg_o, 'r', label= 'Óleo de Transformador')
plt.grid(True, which='both', ls='-.'), plt.legend()
plt.xlabel('Frequência [Hz]', size=14), plt.ylabel('Tangente de Perdas', size=14)
plt.axis([3.8*10, 4.5*10**7, -101, 2316])
plt.show()
