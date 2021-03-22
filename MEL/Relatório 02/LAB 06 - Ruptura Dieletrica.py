import numpy as np
import matplotlib.pyplot as plt

a = np.genfromtxt('ruptura_ABS.txt')
b = np.genfromtxt('ruptura_borracha.txt')
c = np.genfromtxt('ruptura_fenolite.txt')
v15 = np.genfromtxt('ruptura_fibra_vidro.txt')
v17 = np.genfromtxt('ruptura_vidro_1,7.txt')
v3 = np.genfromtxt('ruptura_vidro_3.txt')

vin_a, vout_a, io_a = a[:, 0], a[:, 2], a[:, 3]
vin_b, vout_b, io_b = b[:, 0], b[:, 2], b[:, 3]
vin_f, vout_f, io_f = c[:, 0], c[:, 2], c[:, 3]

vreal_a, ireal_a = vout_a[0:11], io_a[0:11]
vreal_b, ireal_b = vout_b[0:11], io_b[0:11]
vreal_f, ireal_f = vout_f[0:11], io_f[0:11]

d, d_b, d_v17, d_v3 = 1.5e-3, 2e-3, 1.7e-3, 3e-3
E_a, E_b, E_f = vout_a/d, vout_b/d_b, vout_f/d
E_v15, E_v17, E_v3 = v15[:, 2]/d, v17[:, 2]/d_v17, v3[:, 2]/d_v3

p_a, p_b, p_f = np.polyfit(vreal_a, ireal_a, 1), np.polyfit(vreal_b, ireal_b, 1), np.polyfit(vreal_f, ireal_f, 1)

itende_a, itende_b, itende_f = np.polyval(p_a, vout_a), np.polyval(p_b, vout_b), np.polyval(p_f, vout_f)

plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(vout_a/1000,io_a*1000, label='Curva $V_oxi_o$')
plt.grid(True)
plt.plot(vout_a/1000,itende_a*1000, color='k', label='Curva de tendência')
plt.xlabel('$V_0$ [$KV$]', size=12)
plt.ylabel('$i_0$ [$\mu A$]', size=12)
# plt.title('Tensão x Corrente - ABS', size=14)
plt.legend()
plt.axis([0.5, 5, 4.8, 102.5])
plt.subplot(2, 1, 2)
plt.plot(vout_a/1000,E_a*1e-6,'-ob')
plt.grid(True)
plt.xlabel('$V_0$ [$KV$]', size=12)
plt.ylabel('$E$ [$MV/m$]', size=12)
# plt.title('Tensão x Campo Elétrico - ABS',size=14)
plt.axis([0.4, 5, 0.2, 3.42])

plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(vout_b/1000,io_b*1000, label='Curva $V_oxi_o$')
plt.grid(True)
plt.plot(vout_b/1000,itende_b*1000, color='k', label='Curva de tendência')
plt.xlabel('$V_0$ [$KV$]', size=12)
plt.ylabel('$i_0$ [$\mu A$]', size=12)
# plt.title('Tensão x Corrente - Borracha', size=14)
plt.legend()
plt.axis([0.41, 9.6, -8, 939])
plt.subplot(2, 1, 2)
plt.plot(vout_b/1000,E_b*1e-6,'-ob')
plt.grid(True)
plt.xlabel('$V_0$ [$KV$]', size=12)
plt.ylabel('$E$ [$MV/m$]', size=12)
# plt.title('Tensão x Campo Elétrico - Borracha',size=14)
plt.axis([0.29, 9.64, 0, 5])

plt.figure(3)
plt.subplot(2, 1, 1)
plt.plot(vout_f/1000,io_f*1000, label='Curva $V_oxi_o$')
plt.grid(True)
plt.plot(vout_f/1000,itende_f*1000, color='k', label='Curva de tendência')
plt.xlabel('$V_0$ [$KV$]', size=12)
plt.ylabel('$i_0$ [$\mu A$]', size=12)
# plt.title('Tensão x Corrente - Fenolite', size=14)
plt.legend()
plt.axis([0.38, 9.6, 3, 654])
plt.subplot(2, 1, 2)
plt.plot(vout_f/1000,E_f*1e-6,'-ob')
plt.grid(True)
plt.xlabel('$V_0$ [$KV$]', size=12)
plt.ylabel('$E$ [$MV/m$]', size=12)
# plt.title('Tensão x Campo Elétrico - Fenolite',size=14)
plt.axis([0.3, 9.68, 0, 6.6])

plt.figure(4)
plt.plot(E_a/(1e6), io_a*1e3, label='ABS')
plt.plot(E_b/(1e6), io_b*1e3, label='Borracha')
plt.plot(E_f/(1e6), io_f*1e3, label='Fenolite')
plt.plot(E_v15/(1e6), v15[:, 3]*1e3, label='Vidro 1,5mm')
plt.plot(E_v17/(1e6), v17[:, 3]*1e3, label='Vidro 1,7mm')
plt.plot(E_v3/(1e6), v3[:, 3]*1e3, label='Vidro 3mm')
plt.grid(True)
# plt.title('Campo Elétrico x Corrente')
plt.xlabel('E [MV/m]', size=12), plt.ylabel('i$_o$ $[\mu A]$', size=12)
plt.legend()
plt.axis([0.05, 6.4, 0, 930])
plt.show()
