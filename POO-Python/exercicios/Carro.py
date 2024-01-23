class Carro:
    def __init__(self):
        self.ligado = False;
        self.cor ='Vermelho';
        self.modelo = 'Ford';
        self.velocidade = 0;
    
    def ligar(self):
       self.ligado = True;
    def desligar(self):
        self.ligado = False;
        self.velocidade = 0;
    def acelerar(self, valor):
        if self.ligado:
            self.velocidade += valor
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("O carro está desligado. Ligue o carro para acelerar.")
    def desacelerar(self, valor):
        if self.ligado:
            self.velocidade-=valor;
            print(f'O carro desacelerou velocidade atual:{self.velocidade} km/h');
        else:
            print("O carro está desligado. Ligue o carro para desacelerar.")
carro = Carro ();
print(f'O Carro está ligado: {carro.ligado}');

carro.ligar();
print(f'O Carro está ligado: {carro.ligado}');

carro.desligar();
print(f'O Carro está ligado: {carro.ligado}');

carro.ligar();
print(f'O Carro está ligado: {carro.ligado}');
carro.acelerar(10);
# carro.desligar();
carro.desacelerar(5);
