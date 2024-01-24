class Humano:
    def falar_oi(self, nome):
        self.__nome = nome;
        print(f'Oi, meu nome é {self.__nome}')

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
pessoa = Humano()
pessoa.falar_oi('Carol');