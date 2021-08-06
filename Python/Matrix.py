import numpy as np  # para trabalhar numericamente
# import matplotlib.pyplot as plt  # para plotar
# import sympy as sp

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
inve = [[1, 2, 3], [0, 1, 4], [0, 0, 1]]
# for i in range(len(A)):
#     print(f'{A[i]}')
tr, N, k, t = 0, 3, 0, 0
M = np.zeros((3, 3))
B = M.copy()
# DP = np.arange(N)
DP = list()
DS = list()
#Matriz Transposta
for i in range(N):
    for j in range(N):
        B[i][j] = A[j][i]
#Multiplicação de Matriz
C = np.dot(A, B)
#Matriz inversa
I = np.linalg.inv(inve)
# print(I)

for i in range(1, N+1):
    for j in range(1, N+1):
        # Diagonal principal
        if i == j:
            # DP[k] = A[i-1][j-1]
            DP.append(A[i-1][j-1])
            tr = tr + A[i-1][j-1]
        # Diagonal secundária
        if i+j == N+1:
            DS.append(A[i-1][j-1])

print(f'Os elementos da Diagonal Principal sao: {DP}')
print(f'O traco da matriz eh: {tr}')
print(f'Os elementos da Diagonal Secundaria sao: {DS}')

# for i in range(0, 3):
#     for j in range(0, 3):
#         M[i, j] = float(input())
# print(M)

# vet = [[0, 1, 2, 3, 4]]
# vet = np.arange(0, 10)
# print(vet)
# vet[0] = 10
# print(vet)
# # x = np.linspace(0, 1, 10)         #definindo o número de divisões no intervalo
# x = np.arange(0, 1, 0.01)           #definindo o passo no intervalo
# print(x)

# x = float(input('Valor de x:\n'))
# x = x**2
# print(x)
