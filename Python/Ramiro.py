import numpy as np
import matplotlib.pyplot as plt

R1 = 1
R2 = 300e3
C = 1.5e-6
A = 2.5e-3
l = 0.50
N1 = 2
N2 = 1
f = 60
Vol = A * l

# Cria VETORES e não listas
V1 = np.array(
    [2.50E-03, 2.50E-01, 3.50E-01, 5.00E-01, 7.50E-01, 1.00E+00, 1.25E+00, 1.50E+00, 1.75E+00, 2.00E+00, 2.25E+00,
     2.50E+00, 2.00E+00, 1.75E+00, 1.50E+00, 1.25E+00, 1.00E+00, 7.50E-01, 5.00E-01, 2.50E-01, 2.50E-03])
V2 = np.array(
    [-1.26, -0.90, 0.00, 0.90, 1.44, 1.89, 2.16, 2.34, 2.43, 2.52, 2.61, 2.70, 2.61, 2.54, 2.48, 2.43, 2.25, 2.16,
     1.98, 1.62, 1.26])

# Cálculos com vetores
H = N1 / (l * R1) * V1
B = R2 * C / (N2 * A) * V2
Hn = -H
Bn = -B

# Gera gráfico
plt.plot(H, B, Hn, Bn)
plt.grid(True)
plt.show()

# Cálculo da integral de área
integral_1 = np.trapz(H[0:12], B[0:12])
integral_2 = np.trapz(np.flipud(H[11:]), np.flipud(B[11:]))  # A função np.flipud() inverte a ordem de um vetor
A = abs(integral_1 - integral_2)

# Cálculo das Perdas
perdas = 2 * A * f * Vol
print(f'Perdas={perdas}')
