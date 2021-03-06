import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import control.matlab as cm
'''
flag = 0 ->não plota nada
flag = 1 -> pzmap de malha aberta e fechada e RL sem controlador
flag = 2 ->resposta ao degrau unitário de malha aberta e fechada
flag = 3 and selb = 0 ->LR sem e com controlador
flag = 3 and selb = True ->LR e bode (malha aberta) sem e com controlador mais bode de malha fechada
flag = 4 ->nyquist, pzmap mais resposta ao degrau unitário de malha fechada com pré-filtro
flag = 4 and siso = True -> acrescenta o sisotool
nyti = True = Apenas nyquist variando o ganho K de 1 até nk
'''
s = cm.tf('s')
flag, selb, siso, nyti, nk = 3, True, False, False, 10
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
Fs = 5/(s+5)
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
    plt.plot(tmf, ymf, label='$T(s)$') #resposta ao degrau unitário de malha fechada com controlador
    plt.grid(True)
    tmf2 = np.zeros(len(tmf))
    for i in range(len(ymf)):
        for j in range(i, len(ymf)):
            if(round(ymf[-1], 2) == 0):
                if((ymf[j]<0.02) and (ymf[j]>-0.02)):
                    tmf2[j] = tmf[j]
                else:
                    tmf2 = np.zeros(len(tmf))
            else:
                if((ymf[j]<ymf[-1]+0.02*ymf[-1]) and (ymf[j]>ymf[-1]-0.02*ymf[-1])):
                    tmf2[j] = tmf[j]
                else:
                    tmf2 = np.zeros(len(tmf))
        if(max(ymf) == ymf[0]):
            if (ymf[i]==min(ymf)):
                tp = tmf[i]
                yp = ymf[i]
        else:
            if (ymf[i]==max(ymf)):
                tp = tmf[i]
                yp = ymf[i]
    for i in range(len(tmf)):
        if(tmf2[i]>0):
            ts = tmf2[i]
            break
    plt.axvline(tp, ls='-.', color='red', label=f'$t_p=${round(tp, 3)}\n$y_p=${round(yp, 3)}')
    plt.axvline(ts, ls='-.', color='blue', label=f'$t_s(2\%)=${round(ts, 3)}')
    plt.title('Resposta ao Degrau Unitário de Malha Fechada com Controlador')
    plt.xlabel('Tempo [s]')
    plt.axis([min(tmf), max(tmf), min(ymf), max(ymf)+0.05*max(ymf)])
    plt.legend()
    ysc, tsc = cm.step(Ts_sc)
    
    plt.figure()
    plt.plot(tsc, ysc, label='$T(s)$') #resposta ao degrau unitário de malha fechada sem controlador
    plt.grid(True)
    tsc2 = np.zeros(len(tsc))
    for i in range(len(ysc)):
        for j in range(i, len(ysc)):
            if(round(ysc[-1], 2) == 0):
                if((ysc[j]<0.02) and (ysc[j]>-0.02)):
                    tsc2[j] = tsc[j]
                else:
                    tsc2 = np.zeros(len(tsc))
            else:
                if((ysc[j]<ysc[-1]+0.02*ysc[-1]) and (ysc[j]>ysc[-1]-0.02*ysc[-1])):
                    tsc2[j] = tsc[j]
                else:
                    tsc2 = np.zeros(len(tsc))
        if(max(ysc) == ysc[0]):
            if (ysc[i]==min(ysc)):
                tpsc = tsc[i]
                ypsc = ysc[i]
        else:
            if (ysc[i]==max(ysc)):
                tpsc = tsc[i]
                ypsc = ysc[i]
    for i in range(len(tsc)):
        if(tsc2[i]>0):
            tssc = tsc2[i]
            break
    plt.axvline(tpsc, ls='-.', color='red', label=f'$t_p=${round(tpsc, 3)}\n$y_p=${round(ypsc, 3)}')
    plt.axvline(tssc, ls='-.', color='blue', label=f'$t_s(2\%)=${round(tssc, 3)}')
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
    if selb:
        mag1, phase1, w1 = cm.bode(GHs, plot=False, Hz=False, margins=True) #bode de malha aberta sem controlador
        mag1, phase1 = 20*np.log10(mag1), phase1*180/np.pi
        for i in range(len(mag1)):
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
        for i in range(len(mag2)):
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
        for i in range(len(mag3)):
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
elif flag==4:
    if nyti:
        cor = list(('blue', 'red', 'orange', 'green', 'purple', 'black', 'yellow', 'gray', 'violet', 'silver'))
        plt.figure()
        for k in range(1, nk+1):
            re, imag, w = cm.nyquist(k*GHs, plot=False) #nyquist - sem controlador
            plt.plot(re, imag, color=f'{cor[k-1]}', label=f'k={k}')
            plt.plot(re, -imag, color=f'{cor[k-1]}')
            plt.title('Nyquist')
            plt.grid(True)
            plt.xlabel('Real axis', size=11)
            plt.ylabel('Imaginary axis', size=11)
            plt.title('Nyquist')
        plt.axvline(1, color='black', ls='--', label='Real=1')
        plt.legend()
    
    else:
        plt.figure()
        cm.nyquist(GHs) #nyquist - sem controlador
        plt.title('Nyquist')

        if siso:
            plt.figure()
            cm.sisotool(As) #sisotool
        
        plt.figure()
        cm.pzmap(TsFs) #pzmap malha fechada com pré-filtro
        plt.grid(True)
        plt.title('pzmap Malha Fechada com Pré-Filtro')
        
        plt.figure()
        ypf, tpf = cm.step(TsFs) #resposta ao degrau unitário de malha fechada com pré-filtro
        plt.plot(tpf, ypf, label='$T(s).F(s)$', color='blue')
        ymf, tmf = cm.step(Ts)
        plt.plot(tmf, ymf, label='$T(s)$', color='orange') #resposta ao degrau unitário de malha fechada com controlador
        plt.grid(True)
        tpf2 = np.zeros(len(tpf))
        for i in range(len(ypf)):
            for j in range(i, len(ypf)):
                if(round(ypf[-1], 2) == 0):
                    if((ypf[j]<0.02) and (ypf[j]>-0.02)):
                        tpf2[j] = tpf[j]
                    else:
                        tpf2 = np.zeros(len(tpf))
                    if((ymf[j]<0.02) and (ymf[j]>-0.02)):
                        tmf2[j] = tmf[j]
                    else:
                        tmf2 = np.zeros(len(tmf))
                else:
                    if((ypf[j]<ypf[-1]+0.02*ypf[-1]) and (ypf[j]>ypf[-1]-0.02*ypf[-1])):
                        tpf2[j] = tpf[j]
                    else:
                        tpf2 = np.zeros(len(tpf))
                    if((ymf[j]<ymf[-1]+0.02*ymf[-1]) and (ymf[j]>ymf[-1]-0.02*ymf[-1])):
                        tmf2[j] = tmf[j]
                    else:
                        tmf2 = np.zeros(len(tmf))
            if(max(ypf) == ypf[0]):
                if (ypf[i]==min(ypf)):
                    tppf = tpf[i]
                    yppf = ypf[i]
            else:
                if (ypf[i]==max(ypf)):
                    tppf = tpf[i]
                    yppf = ypf[i]
            if(max(ymf) == ymf[0]):
                if (ymf[i]==min(ymf)):
                    tpmf = tmf[i]
                    ypmf = ymf[i]
            else:
                if (ymf[i]==max(ymf)):
                    tpmf = tmf[i]
                    ypmf = ymf[i]
        for i in range(len(tpf)):
            if(tpf2[i]>0):
                tspf = tpf2[i]
                break
        for i in range(len(tmf)):
            if(tmf2[i]>0):
                tsmf = tmf2[i]
                break
        plt.axvline(tppf, ls='--', color='blue', label=f'$t_p=${round(tppf, 3)}\n$y_p=${round(yppf, 3)}')
        plt.axvline(tspf, ls='-.', color='blue', label=f'$t_s(2\%)=${round(tspf, 3)}')
        plt.axvline(tpmf, ls='--', color='orange', label=f'$t_p=${round(tpmf, 3)}\n$y_p=${round(ypmf, 3)}')
        plt.axvline(tsmf, ls='-.', color='orange', label=f'$t_s(2\%)=${round(tsmf, 3)}')
        plt.title('Resposta ao Degrau Unitário de Malha Fechada com Pré-Filtro')
        plt.xlabel('Tempo [s]')
        plt.xlim([min(tpf), max(tpf)])
        plt.legend()

plt.show()
