import numpy as np

class Ajustamento_de_curvas():
    
    def __init__(self, x: list, y: list):
        self.x = x
        self.y = y
        self.n = len(self.x)
        self.calculo_variaveis()
        
        
    def calculo_variaveis(self):   
        self.x_total = 0
        self.x2_total = 0
        self.x3_total = 0
        self.x4_total = 0

        self.y2_total = 0
        self.y_total = 0
        self.lny_total = 0

        self.xy_total = 0
        self.x2y_total = 0
        self.xlny_total = 0

        for i in range(self.n):
            self.x_total = self.x_total + self.x[i]
            self.x2_total = self.x2_total + self.x[i]**2
            self.x3_total = self.x3_total + self.x[i]**3
            self.x4_total = self.x4_total + self.x[i]**4

            self.y_total = self.y_total +  self.y[i]
            self.y2_total = self.y2_total + self.y[i]**2
            self.lny_total = self.lny_total + np.log(self.y[i])

            self.xy_total = self.xy_total + self.x[i]*self.y[i]
            self.x2y_total = self.x2y_total + self.x[i]**2*self.y[i]
            self.xlny_total = self.xlny_total + self.x[i]*np.log(self.y[i])
        

    def calculo_r(self):
        self.sxx = self.x2_total - self.x_total**2/self.n
        self.syy = self.y2_total - self.y_total**2/self.n
        self.sxy = self.xy_total - (self.x_total*self.y_total)/self.n
        self.r = round(self.sxy/(np.sqrt(self.sxx*self.syy)),5)

        print(f'r = {self.r}')


    def calculo_r2(self):
        print(f'r^2 = {round(self.r**2,5)}')


    def ajustamento_linear(self, mostrar=True):
        A = np.array([[self.n, self.x_total], 
            [self.x_total, self.x2_total]])

        B = np.array([[self.y_total], 
            [self.xy_total]])

        X = np.dot(np.linalg.inv(A), B)
        a = round(X[0][0],5)
        b = round(X[1][0],5)

        self.y_linear = []
        for i in range(self.n):
            self.y_linear.append(a + b*self.x[i])

        if mostrar:
            print(f'y(x) = {a} + {b}*x')
        

    def ajustamento_quadratico(self, mostrar=True):
        A = np.array([[self.n, self.x_total, self.x2_total],
            [self.x_total, self.x2_total, self.x3_total],
            [self.x2_total, self.x3_total, self.x4_total]])

        B = np.array([[self.y_total],
            [self.xy_total],
            [self.x2y_total]])

        X = np.dot(np.linalg.inv(A), B)
        a = round(X[0][0],5)
        b = round(X[1][0],5)
        c = round(X[2][0],5)

        self.y_quadratico = []
        for i in range(self.n):
            self.y_quadratico.append(a + b*self.x[i] + c*self.x[i]**2)

        if mostrar:
            print(f'y(x) = {a} + {b}*x + {c}*x^2')
        

    def ajustamento_exponencial(self, mostrar=True):
        A = np.array([[self.n, self.x_total], 
            [self.x_total, self.x2_total]])

        B = np.array([[self.lny_total], 
            [self.xlny_total]])

        X = np.dot(np.linalg.inv(A), B)
        A = X[0][0]
        a = round(np.exp(A),5)
        b = round(X[1][0],5)

        self.y_exponencial = []
        for i in range(self.n):
            self.y_exponencial.append(a*np.exp(b*self.x[i]))
        
        if mostrar:
            print(f'y(x) = {a}*e^({b}*x)')

        
    def melhor_expressão_ajustamento(self):
        self.ajustamento_linear(mostrar=False)
        self.ajustamento_quadratico(mostrar=False)
        self.ajustamento_exponencial(mostrar=False)

        sigma2_linear = 0
        sigma2_quadratica = 0
        sigma2_exponencial = 0

        for i in range(self.n):
            sigma2_linear = sigma2_linear + (self.y_linear[i] - self.y[i])**2 / self.n
            sigma2_quadratica = sigma2_quadratica + (self.y_quadratico[i] - self.y[i])**2 / self.n
            sigma2_exponencial = sigma2_exponencial + (self.y_exponencial[i] - self.y[i])**2 / self.n
        sigma = [sigma2_linear, sigma2_quadratica, sigma2_exponencial]

        menor = id_menor = 0
        for i in range(len(sigma)):
            if i == 0:
                menor = round(sigma[i],5)
                id_menor = i
            elif sigma[i] < menor:
                menor = round(sigma[i],5)
                id_menor = i

        if id_menor == 0:
            print(f'O ajustamento linear é o melhor modelo pois tem a menor variância residual sigma = {menor}')
        elif id_menor == 1:
            print(f'O ajustamento quadrático é o melhor modelo pois tem a menor variância residual sigma = {menor}')
        else:
            print(f'O ajustamento exponencial é o melhor modelo pois tem a menor variância residual sigma = {menor}')






