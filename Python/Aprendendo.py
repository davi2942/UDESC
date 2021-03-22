import numpy as np  # para trabalhar numericamente
import matplotlib.pyplot as plt  # para plotar
import sympy as sp
import functools as fc

# l = list(np.arange(0, 20, 1))   #Criando uma lista 'l' com 20 posições
# print(l)
# l.append('Teste')               #Adicionando 'Teste' na última posição da lista
# l.pop(5)                        #Retirando o elemento da 6 sexta posição
# print(l)
# l.reverse()                     #Invertando a ordem da lista
# print(l)
# l.pop(0)                        #Retirando o elemento da posição zero
# l.sort()                        #Ordenando a lista em ordem crescente
# print(l)
# letras = list(['a', 'b', 'c', 'd', 'f', 'j', 'k', 'x'])
# letras.reverse()
# print(letras)
# letras.sort()
# print(letras)
#
# square = lambda x: x**2         #Função lambda
# x = square(5)
# print(type(square))
#
#
# class Cube:
#     def __init__(self, base):
#         self.base = base
#     def area(self):
#         return 6*self.base**2
#     def volume(self):
#         return self.base**3
#
# c = Cube(4)
# A = c.area()
# V = c.volume()
# print("Área:", A)
# print("Volume:", V)

listap = [x for x in 'word']
print(listap)

listnum = [x**2+2*x-5 for x in range(0, 10)]
print(listnum)

max_term = lambda a, b: a if (a > b) else b
y = fc.reduce(max_term, listnum)
print(y)
