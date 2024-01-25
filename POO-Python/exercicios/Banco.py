from abc import ABC, abstractmethod;
class Cliente (ABC):
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente;
        self.telefone_cliente ='';
        self._renda_mensal = 0.0;
        
    @property
    @abstractmethod
    def sexo(self):
        pass
    
class Conta(Cliente):
    def __init__(self, nome_cliente):
        super().__init__(nome_cliente)
        self.__saldo = 0;
        self._numero_conta = '';
        self.lista_saques = [];
        self.lista_depositos = [];
        self._sexo = ''
    @property
    def saldo(self):
        return self.__saldo;
    
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo
    
    @property
    def sexo(self):
        return self._sexo;
    
    @sexo.setter
    def sexo(self, novo_sexo):
        self._sexo = novo_sexo;
    
    def sacar(self, valor_saque):
        if valor_saque>self.__saldo:
            print('Saldo insuficiente para saque!');
        else:
            self.__saldo -=valor_saque;
            self.lista_saques.append(valor_saque);
            
    def depositar(self,valor):
        self.saldo+=valor;
        self.lista_depositos.append(valor);
    def extrato(self):
        print (f'------ Extrato Bancário ------'
               f'\n Cliente :{self.nome_cliente}'
               f'\n Sexo: {self.sexo}'
               f'\n Conta:{self._numero_conta} '
               f'\n Saques :{self.lista_saques} '
               f'\n Depositos :{self.lista_depositos}'
                f'\n Saldo:{self.saldo}');

conta = Conta('Ana Maria');
conta._numero_conta = '345698';
conta.sexo = 'Mulher';
conta.saldo = 500;
for i in range(2):
    conta.depositar(150);
    conta.sacar(40);
conta.extrato();