import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

#configurações padrão
ax = plt.axes(projection='3d')

#Variando o parâmetro
t=np.linspace(-2*np.pi, 2*np.pi, 1000)
#Componentes da parametrização
x=2*np.sin(t)
y=2*np.cos(t)
z=t
#Plotando a função em forma de parâmetros
ax.plot3D(x, y, z, color='b', label='Hélice')
ax.plot3D(t, np.sqrt(4-t**2), 0, color='k', label='Parábola')

#Definindo o nome dos eixos
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
ax.set_zlabel('Eixo z')     #Eixo z se acha especial
plt.title('Hélice')         #Título
plt.legend()                #Legenda está com erro
plt.show()                  #Exibir o gráfico
