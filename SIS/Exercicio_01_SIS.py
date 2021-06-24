import matplotlib.pyplot as plt

gn = [0, 1, 2, 1, 0]
g = [7, 8, 9, 10, 11]
fn = [0, 1, 1, 0]
f = [6, 7, 8, 9]

plt.figure(1)
plt.stem(g, gn, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
plt.xlim([6, 12])
plt.ylim([-0.1, 2.2])
plt.xlabel('n', size=12)
plt.ylabel('g[n]', size=10)
# plt.title('Sinal g[n]')

plt.figure(2)
plt.stem(f, fn, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
plt.xlim([5, 10])
plt.ylim([-0.1, 1.1])
plt.xlabel('n', size=12)
plt.ylabel('f[n]', size=10)
# plt.title('Sinal f[n]')

f1 = [6+8, 7+8, 8+8, 9+8]
f2 = [6+9, 7+9, 8+9, 9+9]
f3 = [16, 17, 18, 19]
fn1 = [0, 1, 1, 0]
fn2 = [0, 2, 2, 0]
fn3 = [0, 1, 1, 0]

plt.figure(3)
plt.subplot(3, 1, 1)
plt.stem(f1, fn1, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
# plt.xlim([6, 12])
# plt.ylim([0, 2.2])
plt.xlabel('n', size=12)
plt.ylabel('f[n-8]', size=10)
plt.subplot(3, 1, 2)
plt.stem(f2, fn2, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
# plt.xlim([6, 12])
# plt.ylim([0, 2.2])
plt.xlabel('n', size=12)
plt.ylabel('2f[n-9]', size=10)
plt.subplot(3, 1, 3)
plt.stem(f3, fn3, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
# plt.xlim([6, 12])
# plt.ylim([0, 2.2])
plt.xlabel('n', size=12)
plt.ylabel('f[n-10]', size=10)
plt.grid(True)

yn = [0, 1, 3, 3, 1, 0]
y = [14, 15, 16, 17, 18, 19]

plt.figure(4)
plt.stem(y, yn, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
plt.xlabel('n', size=12)
plt.ylabel('y[n]', size=10)
plt.xlim([13.5, 19.5])
plt.ylim([-0.1, 3.2])

fk = [-2, -1, 0, 1, 2]

fnk1 = [0, 1, 1, 0, 0]
fnk2 = [0, 0, 1, 1, 0]
fnk3 = [0, 0, 0, 1, 1]
fnk4 = [0, 0, 0, 0, 1]

plt.figure(5)
plt.subplot(2, 2, 1)
plt.stem(fk, fnk1, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
plt.xlabel('n', size=12)
plt.ylabel('y[n]', size=10)
plt.xlim([-2.5, 2.5])
plt.ylim([-0.1, 1.1])
plt.title('f[8-k]')

plt.subplot(2, 2, 2)
plt.stem(fk, fnk2, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
plt.xlabel('n', size=12)
plt.ylabel('y[n]', size=10)
plt.xlim([-2.5, 2.5])
plt.ylim([-0.1, 1.1])
plt.title('f[9-k]')

plt.subplot(2, 2, 3)
plt.stem(fk, fnk3, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
plt.xlabel('n', size=12)
plt.ylabel('y[n]', size=10)
plt.xlim([-2.5, 2.5])
plt.ylim([-0.1, 1.1])
plt.title('f[10-k]')

plt.subplot(2, 2, 4)
plt.stem(fk, fnk4, linefmt='k', basefmt='k', markerfmt='ko')
plt.grid(True)
plt.xlabel('n', size=12)
plt.ylabel('y[n]', size=10)
plt.xlim([-2.5, 2.5])
plt.ylim([-0.1, 1.1])
plt.title('f[11-k]')

plt.show()
