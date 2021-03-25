import numpy as np  # para trabalhar numericamente
import matplotlib.pyplot as plt  # para plotar
import sympy as sp

def Bhaskara(a,b,c):
    raiz1 = raiz2 = 0
    Delta = flag = 0

    Delta = complex(b**2-4*a*c)
    if a == 0 and b == 0 and c == 0:
        print('Polinômio nulo')
        flag = 1
    elif a == 0 and b == 0:
        print('Não existem raízes!')
        flag = 1
    elif a == 0 and b != 0 and c != 0:
        raiz1 = -c/b
        raiz2 = 0
        flag = 1
    elif flag == 0:
        raiz1 = complex((-b+np.sqrt(Delta))/(2*a))
        raiz2 = complex((-b-np.sqrt(Delta))/(2*a))
    return raiz1, raiz2

def Fatorial(n):
    fat=i=1
    if n==0 or n==1:
        fat=1
    elif n<0:
        print('Não existe fatorial negativo!')
    else:
        while i<=n:
            fat=fat*i
            i=i+1
    return fat

def Taylor():
    resultado=list()
    x = sp.symbols('x')
    f = input('Digite a função desejada em termos de x:\n')
    a = float(input('Digite onde sua série será centrada:\n'))
    N = int(input('Digite quantos termos da série você deseja:\n'))
    vet = np.ones(N)
    veti = np.ones(N)
    ft=0

    #Somatório
    for i in range(0,N):
        fn=sp.diff(f,x,i)
        ft=fn.subs(x,a)
        veti[i]=Fatorial(i)
        vet[i]=ft

    for i in range(0,N):
        y=vet[i]*(x-a)**i
        y=1/veti[i]*y
        resultado.append(y)
    print('Sua série de Taylor é:\n')
    return resultado

def Fibonacci(n):
    soma=np.ones(n)
    if n<=0:
        soma = elemento = 0
        print('NaN!')
    else:
        for i in range(0, n):
            if i>1:
                soma[i] = soma[i-1]+soma[i-2]
        elemento = 1/np.sqrt(5)*((1+np.sqrt(5))/2)**n-1/np.sqrt(5)*((1-np.sqrt(5))/2)**n
        elemento = int(elemento)
    return elemento, soma

def n_esima_raiz_unidade(n, plotar = False):
    r, r_real, r_imaginario = np.zeros([n]), np.zeros([n]), np.zeros([n])
    r = np.complex_(r)
    for i in range(1, n+1):
        r[i-1] = np.cos(2*np.pi/i)+np.complex(1j)*np.sin(2*np.pi/i)
        r_real[i-1] = np.cos(2*np.pi/i)
        print(r_real[i-1])
        r_imaginario[i-1] = np.sin(2*np.pi/i)
        print(r_imaginario[i-1])
    if plotar:
        x = np.arange(-1, 1, 0.001)
        y = np.sqrt(1-x**2)
        plt.figure(1)
        plt.plot(x, y, color='k', label='$x^2+y^2=1$')
        plt.plot(x,-y, color='k')
        plt.plot(r_real, r_imaginario, 'ro', label='Raízes')
        plt.grid(True)
        plt.legend()
        plt.show()
    return r

raizes = n_esima_raiz_unidade(5, True)
print(f'As raizes são:\n{raizes}')

# r_real, r_imaginario = np.cos(2*np.pi/1), np.sin(2*np.pi/1)
# x = np.arange(-1, 1, 0.001)
# y = np.sqrt(1-x**2)
# plt.figure(1)
# plt.plot(x, y, color='k', label='$x^2+y^2=1$')
# plt.plot(x,-y, color='k')
# plt.plot(r_real, r_imaginario, 'ro', label='Raízes')
# plt.grid(True)
# plt.legend()
# plt.show()
