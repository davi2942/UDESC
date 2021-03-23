import numpy as np  # para trabalhar numericamente
# import matplotlib.pyplot as plt  # para plotar
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

# x = np.arange(0, 11)
# a = list(map(Fibonacci, x))         #Função 'map' faz um sequência de leituras
# print(a)
