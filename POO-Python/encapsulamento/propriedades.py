class Quadrado:
    def __init__(self, medida):
        self.altura = medida;
        self.largura = medida;
        
    @property #declaração de uma propriedade
    def altura(self):
        print('getter de altura');
        return self.__medida
    
    @altura.setter
    def altura(self, valor):
        print('setter de altura');
        if valor <0:
            raise ValueError('A medida tem que ser maior que 0');
        self.__medida = valor;  # altera a altura para 3 com quadrado.altura = 3;
    @property
    def largura(self):
        print('getter de largura');
        return self.__medida;
    @largura.setter
    def largura(self, valor):
        print('setter de largura');
        if valor<0:
           raise ValueError('A medida tem que ser maior que 0');
    def area(self):
        return self.largura*self.altura;
    
quadrado = Quadrado(2);
quadrado.altura = 3;
print(quadrado.area());