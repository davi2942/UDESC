import numpy as np              #Para trabalhar numericamente
import matplotlib.pyplot as plt #Para plotar
import sympy as sp              #Para trabalhar com símbolos
import random                   #Para gerar números aleatórios
import Funcoes as Fu
# print('Hello, world!')                    #Printando frase
# x=4                                       #Definindo o valor de x
# input('Digite algo:\n')                   #Entreda de frase
# x=x**4                                    #Fazendo x^4
plt.figure(1)
a = np.linspace(0,4*np.pi,12568)              #Variando "a" de 0 a 4*pi
plt.plot(a, 3*np.sin(a), color='red', label='y=sin(x)')        #Plotando as funções
plt.plot(a, 3*np.cos(a), color='k', label='y=cos(x)')
# plt.plot(a, 3*(1-np.exp(-a)), color='b', label='y=3(1-e^x)')
# plt.plot(a, -3*(1-np.exp(-a)), color='g', label='y=-3(1-e^x)')
plt.xlabel('tempo [s]')                     #Nome no eixo x
plt.ylabel('Tensão [V]')                    #Nome no eixo y
plt.title('Tensão Senoidal')                #Título do gráfico
plt.legend()                                #Habilitando a legenda
plt.grid(True)                              #Habilitando o grid
plt.axis([0, 4*np.pi, -3, 3])               #Limitando os eixos de exibição
# plt.show()                                #Exibir o gráfico

#Criando função
# def funcao():
#     x=15                      #Definindo valor de x
#     return x                  #Retorno da função é a variável x
# print(funcao())               #Chamando valor da função

#Gerando números aleatórios
# y=random.randint(-10,10)      #Gerando números aleatórios e armazenando em x
# print(y)                      #Printando y
#print(f'O valor de a é {a} e o valor de y={y}')      #Printando frase e variável juntos
# print(x)                      #Printando valor de x

#Cálculo de limite
# x = sp.symbols('x')
# a = sp.limit(1/x, x, 0)                     #sp.limit(f(x),variável,limite)
# b = sp.limit(sp.sin(x)/x, x, np.inf)        #Tendendo para infinito
# print(f'{a}\n{b}')

plt.figure(2)
vet = list(np.arange(0, 20))
a = random.randint(-10, 10)
b = random.randint(-10, 10)
c = random.randint(-10, 10)
x = Fu.Bhaskara(a, b, c)            #Chamando a função do arquivo importado
print(f'x = {x}')                            #Printando valores da função
x = np.linspace(-20,20)
if b > 0 and c > 0:
    plt.plot(x, a*x**2+b*x+c, label=f'{a}x^2+{b}x+{c}')
elif b > 0 and c < 0:
    plt.plot(x, a * x ** 2 + b * x + c, label=f'y = {a}x^2+{b}x{c}')
elif b < 0 and c > 0:
    plt.plot(x, a * x ** 2 + b * x + c, label=f'y = {a}x^2{b}x+{c}')
elif b <0 and c < 0:
    plt.plot(x, a * x ** 2 + b * x + c, label=f'y = {a}x^2{b}x{c}')
plt.grid(True)
plt.title('Função Quadrática')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.legend()
plt.show()
