close all
clear all
clc

#set(0,'DefaultFigureWindowStyle','docked') %Figuras dockadas

gn = [0 1 2 1 0];
g = [7 8 9 10 11];
fn = [0, 1, 1, 0];
f = [6, 7, 8, 9];

figure(1)
stem(g, gn,'k', 'LineWidth', 1)
grid on
xlim([6, 12]);ylim([0, 2.2])
xlabel('n');ylabel('g[n]')
title('Sinal g[n]')

figure(2)
stem(f, fn,'k', 'LineWidth', 1)
grid on
xlim([5, 10]);ylim([0, 1.2])
xlabel('n'); ylabel('f[n]')
title('Sinal f[n]')
