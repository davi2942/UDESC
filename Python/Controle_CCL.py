import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import control.matlab as cm
'''
flag = 0 ->não plota nada
flag = 1 -> pzmap de malha aberta e fechada e RL sem controlador
flag = 2 ->resposta ao degrau unitário de malha aberta e fechada
flag = 3 and selb=0 ->LR sem e com controlador
flag = 3 and selb=1 ->LR e bode (malha aberta) sem e com controlador mais bode de malha fechada
flag = 4 ->nyquist, sisotool, pzmap mais resposta ao degrau unitário de malha fechada com pr-e-filtro
'''
s = cm.tf('s')
flag, selb = 2, 1
Gs, Cs, Hs = 100/(s*(s+5)*(s+8)), 4.48*(s+5), 1
# Gs, Cs, Hs = 1/((s+1)*(s+10)), 69.49*(s+1)/s, 1
# Gs, Cs, Hs = 200/((s+10)*(s+30)), (s+0.135)*(s+0.01), 1
print(f'Gs={Gs}\nCs={Cs}\nHs={Hs}\n')

# Conexões
GHs = Gs*Hs #Malha aberta sem controlador
As = Cs*GHs #Malha aberta com contorlador
Ts = cm.feedback(Cs*Gs, Hs) #Malha fechada com controlador
Ts_sc = cm.feedback(Gs, Hs) #Malha fechada sem controlador
print(f'GsHs={GHs}\tMalha aberta sem controlador\n\nGsHsCs={As}\tMalha aberta com contorlador\n\n{Ts}Malha fechada com controlador\n')

#dcgain(sys), retorna o ganho \n pole(sys), retorna os polos \n zero(sys), retorna os zeros
print(f'Ganho_dc_T(s)={cm.dcgain(Ts)}\nPolos_T(s)={cm.pole(Ts)}\nZeros_T(s)={cm.zero(Ts)}')

#Pré-Filtro
Fs = s/(s+1)
TsFs = Ts*Fs #Malha fechada com pré-filtro

if (flag==1):
    plt.figure()
    cm.pzmap(As) #pzmap de malha aberta
    plt.grid(True)
    plt.title('Pzmap de Malha Aberta com Controlador')
    plt.figure()
    cm.pzmap(Ts) #pzmap de malha fechada
    plt.grid(True)
    plt.title('Pzmap de Malha Fechada com Controlador')
    plt.figure()
    ctl.rlocus(GHs) #Lugar das Raízes - LR
    plt.grid(True)
elif (flag==2):
    plt.figure()
    yma, tma = cm.step(As)
    plt.plot(tma, yma, label='$T(s)$') #Resposta ao degrau unitário de malha aberta com controlador
    plt.grid(True)
    plt.title('Resposta ao Degrau Unitário de Malha Aberta com Controlador')
    plt.xlabel('Tempo [s]')
    plt.axis([min(tma), max(tma), min(yma), max(yma)+0.05*max(yma)])
    plt.legend()
    plt.figure()
    ymf, tmf = cm.step(Ts)
    plt.plot(tmf, ymf, label='$T(s)$') #resposta ao degrau unitário de malha fechada
    plt.grid(True)
    for i in range(0, len(ymf)):
        ymf[i] = ymf[i]
        if (ymf[i]==max(ymf)):
            tp = tmf[i]
    plt.axvline(tp, ls='-.', color='red', label=f'$t_p=${round(tp, 3)}\n$y_p=${round(max(ymf), 3)}')
    # plt.axvline(ts, ls='-.', color='blue', label=f'$t_s(2\%)=${round(ts, 3)}')
    plt.title('Resposta ao Degrau Unitário de Malha Fechada com Controlador')
    plt.xlabel('Tempo [s]')
    plt.axis([min(tmf), max(tmf), min(ymf), max(ymf)+0.05*max(ymf)])
    plt.legend()
    ysc, tsc = cm.step(Ts_sc)
    plt.figure()
    plt.plot(tsc, ysc, label='$T(s)$')
    plt.grid(True)
    for i in range(0, len(ysc)):
        ysc[i] = ysc[i]
        if (ysc[i]==max(ysc)):
            tp_sc = tsc[i]
        if (ysc[i]-ysc[-1]<=0.02):
            ts = tsc[i]
    plt.axvline(tp_sc, ls='-.', color='red', label=f'$t_p=${round(tp_sc, 3)}\n$y_p=${round(max(ysc), 3)}')
    plt.axvline(ts, ls='-.', color='blue', label=f'$t_s(2\%)=${round(ts, 3)}')
    plt.title('Resposta ao Degrau Unitário de Malha Fechada sem Controlador')
    plt.xlabel('Tempo [s]')
    plt.axis([min(tsc), max(tsc), min(ysc), max(ysc)+0.05*max(ysc)])
    plt.legend()
elif (flag==3):
    plt.figure()
    cm.rlocus(GHs) #lugar das raizes sem controlador
    plt.title('LR sem Controlador')
    plt.figure()
    cm.rlocus(As) #lugar das raizes com controlador
    plt.title('LR com Controlador')
    if (selb==1):
        mag1, phase1, w1 = cm.bode(GHs, plot=False, Hz=False, margins=True) #bode de malha aberta sem controlador
        mag1, phase1 = 20*np.log10(mag1), phase1*180/np.pi
        for i in range(0, len(mag1)):
            if(mag1[i]<=0):
                phase11 = phase1[i]
                mag11 = mag1[i]
                w11 = w1[i]
                break
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(w1, mag1, label='Mag')
        plt.axvline(w11, color='black', ls='--', label=f'$\omega=${round(w11, 2)}rad/s\nmag=0 dB')
        plt.grid(True, which="both")
        plt.title('Bode de Malha Aberta sem Controlador')
        plt.ylabel('Magnitude [dB]')
        plt.axis([min(w1), max(w1), min(mag1), max(mag1)+2])
        plt.legend()
        plt.subplot(2, 1, 2)
        plt.semilogx(w1, phase1, label='Phase')
        plt.axvline(w11, color='black', ls='--', label=f'$\omega=${round(w11, 2)} rad/s\nphase={round(phase11, 2)}$^\circ$')
        plt.grid(True, which="both")
        plt.ylabel('Phase [deg]')
        plt.xlabel('Frequência [rad/s]')
        plt.axis([min(w1), max(w1), min(phase1), max(phase1)+5])
        plt.legend()
        
        mag2, phase2, w2 = cm.bode(As, plot=False, Hz=False, margins=True) #bode de malha aberta com controlador
        mag2, phase2 = 20*np.log10(mag2), phase2*180/np.pi
        for i in range(0, len(mag2)):
            if(mag2[i]<=0):
                phase22 = phase2[i]
                mag22 = mag2[i]
                w22 = w2[i]
                break
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(w2, mag2, label='Mag')
        plt.axvline(w22, color='black', ls='--', label=f'$\omega=${round(w22, 2)}rad/s\nmag=0 dB')
        plt.grid(True, which="both")
        plt.title('Bode de Malha Aberta com Controlador')
        plt.ylabel('Magnitude [dB]')
        plt.axis([min(w2), max(w2), min(mag2), max(mag2)+2])
        plt.legend()
        plt.subplot(2, 1, 2)
        plt.semilogx(w2, phase2, label='Phase')
        plt.axvline(w22, color='black', ls='--', label=f'$\omega=${round(w22, 2)} rad/s\nphase={round(phase22, 2)}$^\circ$')
        plt.grid(True, which="both")
        plt.ylabel('Phase [deg]')
        plt.xlabel('Frequência [rad/s]')
        plt.axis([min(w2), max(w2), min(phase2), max(phase2)+5])
        plt.legend()
        
        mag3, phase3, w3 = cm.bode(Ts, Hz=False, plot=False, margins=True) #bode de malha fechada com controlador
        mag3, phase3 = 20*np.log10(mag3), phase3*180/np.pi
        for i in range(0, len(mag3)):
            if(mag3[i]<=0):
                phase33 = phase3[i]
                mag33 = mag3[i]
                w33 = w3[i]
                break
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(w3, mag3, label='Mag')
        plt.axvline(w33, color='black', ls='--', label=f'$\omega=${round(w33, 2)}rad/s\nmag=0 dB')
        plt.grid(True, which="both")
        plt.title('Bode de Malha Fechada com Controlador')
        plt.ylabel('Magnitude [dB]')
        plt.axis([min(w3), max(w3), min(mag3), max(mag3)+2])
        plt.legend()
        plt.subplot(2, 1, 2)
        plt.semilogx(w3, phase3, label='Phase')
        plt.axvline(w33, color='black', ls='--', label=f'$\omega=${round(w33, 2)} rad/s\nphase={round(phase33, 2)}$^\circ$')
        plt.grid(True, which="both")
        plt.ylabel('Phase [deg]')
        plt.xlabel('Frequência [rad/s]')
        plt.axis([min(w3), max(w3), min(phase3), max(phase3)+5])
        plt.legend()
elif (flag==4):
    plt.figure()
    cm.nyquist(GHs) #nyquist - sem controlador
    plt.title('Nyquist')
    plt.figure()
    cm.sisotool(As) #sisotool
    plt.figure()
    cm.pzmap(TsFs) #pzmap malha fechada com pré-filtro
    plt.grid(True)
    plt.title('pzmap Malha Fechada com Pré-Filtro')
    plt.figure()
    ypf, tpf = cm.step(TsFs) #resposta ao degrau unitário de malha fechada com pré-filtro
    plt.plot(tpf, ypf)
    plt.grid(True)
    plt.title('Resposta ao Degrau Unitário de Malha Fechada com Pré-Filtro')
    plt.xlabel('Tempo [s]')

plt.show()
