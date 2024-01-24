class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular  # Atributo protegido
        self.__saldo = saldo_inicial  # Atributo privado

    # Propriedade para encapsular o acesso e validação do saldo
    @property
    def saldo(self):
        return self.__saldo

    # Setter da propriedade para validar o novo saldo
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print('O saldo não pode ser negativo');
      
    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: { self.__saldo}")

    def sacar(self, valor):
        if  self.__saldo >= valor:
            self.__saldo-= valor
            print(f"Saque de {valor} realizado. Novo saldo: { self.__saldo}")
        else:
            print("Saldo insuficiente. Saque não realizado.")

# Criando uma conta bancária
minha_conta = ContaBancaria(titular="João", saldo_inicial=1000)

# Acessando o saldo usando a propriedade
print(f"Saldo atual: {minha_conta.saldo}")


# Realizando um depósito
minha_conta.depositar(500)

# Realizando um saque
minha_conta.sacar(200)