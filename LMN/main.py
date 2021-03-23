import p2


#? Definição de dados
x = [5.5, 1.3, 1.2, 1.6, 6.3, 4.7, 0.3, 1.1, 0.8]
y = [9.4, 8.1, 7.9, 8.8, 9.6, 9.2, 6.5, 8.7, 7.3]

#? Chamando a classe
a = p2.Ajustamento_de_curvas(x,y)

#? Utilizando a classe
a.calculo_r()
a.calculo_r2()
a.ajustamento_linear()
a.ajustamento_quadratico()
a.ajustamento_exponencial()
a.melhor_expressão_ajustamento()
