class Tv: #PascalCasing
    def __init__(self):
        self.ligada = False;
        self.canal = 3;
        self.canal_min = 1;
        self.canal_max = 99;
        self.volume = 30;
        self.volume_min = 0;
        self.volume_max = 100;
        
    def ligar(self):
        self.ligada = True;
    def desligar(self):
        self.ligada = False;
    def mudar_canal_pra_cima(self):
        if not self.ligada:
            return ;
        if self.canal<self.canal_max:
            self.canal +=1;
    def mudar_canal_pra_baixo(self):
        if not self.ligada:
            return ;
        if self.canal<self.canal_max:
            self.canal -=1;
    def aumentar_volume(self):
        if not self.ligada:
            return;
        if self.volume<self.volume_max:
            self.volume+=10;
    def diminuir_volume(self):
        if not self.ligada:
            return;
        if self.volume>self.volume_min:
            self.volume-=10;
    def __str__(self)->str:
        return f' Televisão - ligada: {self.ligada} - canal: {self.canal} - volume: {self.volume}';

# Criando instancia 
tv_sala = Tv();
tv_quarto = Tv();

print('Estado Inicial da TV');
print(f'A televisão da sala está ligada: {tv_sala.ligada}');
print('tv_quarto está ligada? {}'.format(tv_quarto.ligada));

tv_sala.ligar();
print(f'A televisão da sala está ligada: {tv_sala.ligada}');
print('tv_quarto está ligada? {}'.format(tv_quarto.ligada));
            
for i in range(3):
    tv_sala.aumentar_volume();

print(f'Volume atual tv sala: {tv_sala.volume}');
print(f'Volume atual tv quarto: {tv_quarto.volume}');
print(f'tv_sala{tv_sala}');
print(f'tv_quarto{tv_quarto}');
