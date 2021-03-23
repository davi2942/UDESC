import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# mu, i, L, a, b, vo = 4*np.pi*10**(-7), 1, 5, 2, 4, 10
# rho = np.arange(0.01, 1/2, 0.0001)

# Um = -(mu*i*L*a*b)/(4*np.pi)*vo*(2*rho+L**2/4)/(rho**2*(rho**2+L**2/4)**(3/2))

# plt.figure(1)
# plt.plot(rho, Um, color='r',label='Energia Encontrada')
# plt.grid(True)
# plt.title('Força Eletromotriz')
# plt.legend()
# plt.axis([0, 0.5, -0.16, 0.001])

# plt.figure(2)
# plt.plot(rho, -Um, color='b',label='Energia Esperada')
# plt.grid(True)
# plt.title('Força Eletromotriz')
# plt.legend()
# plt.axis([0, 0.5, -0.001, 0.16])

""" s, t = sp.symbols('s, t')
G1, G2, G3 = 2/(s**2+2*s+2), 173/(s**2+12*s+173), 10/(s**2+s+10)

wn1, wn2, wn3 = np.sqrt(2), np.sqrt(173), np.sqrt(10)
qsi1, qsi2, qsi3 = 2/(2*wn1), 12/(2*wn2), 1/(2*wn3)

#Transformada Inversa de Laplace
g1, g2, g3 = sp.inverse_laplace_transform(G1, s, t), sp.inverse_laplace_transform(G2, s, t), sp.inverse_laplace_transform(G3, s, t)

sp.plot(g1, (t, 0, 5))
sp.plot(g2, (t, 0, 1))
sp.plot(g3, (t, 0, 10))
plt.plot(h, (t, 0, 3))
plt.show() """

t = np.arange(0, 10, 0.001)
y = 3-2*np.exp(-2*t)
plt.plot(t, y, color='r', label='$y=3-2e^{-2t}$')
plt.grid(True)
plt.legend()
plt.axis([-0.05, 10, 1, 3.05])
plt.show()
