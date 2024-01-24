class Brinquedo:
    def __init__(self, nome):
        self.nome = nome
        print(f"{self.nome} foi criado!")

    def __del__(self):
        print(f"{self.nome} está sendo removido!")

# Criando um objeto (brinquedo)
meu_brinquedo = Brinquedo("Boneca")

# O objeto será removido quando sair do escopo ou quando for explicitamente deletado
# A mensagem do destrutor será exibida automaticamente