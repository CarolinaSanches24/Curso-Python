class Pessoa:
    def falar_oi(self):
        self.nome = 'Carol';
        print(f'Oi, meu nome é {self.nome}');
        
pessoa = Pessoa();
pessoa.falar_oi();
        