import numpy as np                  #Para trabalhar numericamente
import matplotlib.pyplot as plt     # Para plotar
import sympy as sp
# import random

x = sp.symbols('x')
y= x**4+5*x**3-2*x**2+x-2+sp.sin(x)**2-sp.cos(x)
print('y =')
sp.pprint(y)
dy = sp.diff(y, x)         #Derivada de y em relação a x
print('\nA derivada de y é dy/dx = ')
sp.pprint(dy)
I = sp.integrate(dy)         #Integral indefinida de dy
print(f'\nA integral de dy é y = ')
sp.pprint(I)
Int = sp.integrate(dy, (x, 0, 1))
print(f'\n A Integral definida é: {Int}')
dy1 = sp.diff(y, x, 3)
print(f'\nd3y/dx3 =')
sp.pprint(dy1)

#t=np.linspace(0,4*np.pi,100)
# h=sp.simplify(sp.sin(x)**2+sp.cos(x)**2)    #comando para simplificar uma expressão
# print(f'A simplificação de t é t = {h}')

# t, rho0, L, w, pi, a, R, r = sp.symbols('t,rho0,L,w,pi,a,R,r')
#
# I = r**2*sp.exp(-a*r)
# jc = sp.integrate(I, r)
# print(f'jc = {jc}')

#x = np.arange(0, 1.5, 0.1)
#y = np.piecewise(x, [(x >= 0) & (x < 1/2), (x >= 1/2) & (x < 1)], [lambda x:1, lambda x:-1, lambda x:0])
#plt.figure(1)
#plt.stem(x, y)
#plt.grid(True)
#plt.figure(2)
#plt.plot(x, y)
#plt.grid(True)
#plt.show()
