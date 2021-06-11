import numpy as np
import matplotlib.pyplot as plt
 
A = np.genfromtxt('Polarizacao_fonte_corrente_ground.txt')
B = np.genfromtxt('Polarizacao_fonte_corrente_sin.txt')
C = np.genfromtxt('Resistor_emissor_zero.txt')
D = np.genfromtxt('Resistor_emissor_sin.txt')

gv0c = A[:, 1]
gvsc = B[:, 1]
gv0r = C[:, 1]
gvsr = D[:, 1]

fgv0c = A[:, 0]
fgvsc = B[:, 0]
fgv0r = C[:, 0]
fgvsr = D[:, 0]

agv0c = A[:, 2]
agvsc = B[:, 2]
agv0r = C[:, 2]
agvsr = D[:, 2]

for i in np.arange(0, len(agvsr)):
    if (agvsr[i] > 0) :
        agvsr[i] = -agvsr[i]

# Gráfico Fonte de Corrente V2=0V
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_ylabel('Ganho $V_o/V_g[dB]$', color=color)
ax1.set_xlabel('Frequência [Hz]')
ax1.semilogx(fgv0c, gv0c, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.grid(True, which="both", ls="-")

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('$Graus[^\circ]$', color=color)
ax2.semilogx(fgv0c, agv0c, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
ax2.set_yticks((3.2, 18.4, 33.2, 48, 63.4, 78))
# plt.title('Polarização com Fonte de Corrente e $V_2=0$ mV')

# Gráfico Fonte de Corrente V2=20mV
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_ylabel('Ganho $V_o/V_g[dB]$', color=color)
ax1.set_xlabel('Frequência [Hz]')
ax1.semilogx(fgvsc, gvsc, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.grid(True, which="both", ls="-")

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('$Graus[^\circ]$', color=color)
ax2.semilogx(fgvsc, agvsc, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
ax2.set_yticks((-181.5, -168.7, -156, -143.6, -131.6, -118.5, -106.5, -94, -81))
# plt.title('Polarização com Fonte de Corrente e $V_2=20$ mV')

# Gráfico Resistor Emissor V2=0V
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_ylabel('Ganho $V_o/V_g[dB]$', color=color)
ax1.set_xlabel('Frequência [Hz]')
ax1.semilogx(fgv0r, gv0r, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.grid(True, which="both", ls="-")

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('$Graus[^\circ]$', color=color)
ax2.semilogx(fgv0r, agv0r, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
ax2.set_yticks((1.6, 16.5, 31.4, 46.1, 60.8, 75.4))
# plt.title('Polarização com Resistor Emissor e $V_2=0$ mV')

# Gráfico Resistor Emissor V2=20mV
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_ylabel('Ganho $V_o/V_g[dB]$', color=color)
ax1.set_xlabel('Frequência [Hz]')
ax1.semilogx(fgvsr, gvsr, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.grid(True, which="both", ls="-")

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('$Graus[^\circ]$', color=color) 
ax2.semilogx(fgvsr, agvsr, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
ax2.set_yticks((-173.5, -162, -150,-138 , -126, -114))
# plt.title('Polarização com Resistor Emissor e $V_2=20$ mV')

plt.show()
