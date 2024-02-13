import sqlite3

class Pessoa:
    # método construtor inicialização
    def __init__(self, nome, telefone, endereco):
        self.nome = nome;
        self.telefone = telefone;
        self.endereco = endereco;
        
    # método de representação de string
    def __str__(self):
        return f'Nome: {self.nome}, "Telefone: {self.telefone}, "Endereco: {self.endereco}'
    
class Responsavel(Pessoa): #Herda membros da classe Pessoa
    pass

class Parceiro_vet(Pessoa): #Herda membros da classe Pessoa
    def __init__(self, nome, telefone, especialidade):
        super(Parceiro_vet, self).__init__(
            nome=nome, telefone=telefone, endereco=None
        )
        self.especialidade = especialidade;

class Animal:
    def __init__(self, nome, especie, raca, idade, cuidados, responsavel):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.cuidados = cuidados;
        self.responsavel = responsavel

    @property
    #Verifica se o animal está disponível
    def esta_disponivel(self):
        if self.responsavel:
        # se o animal tem um responsavel 
            return False #não está disponivel
        return True #está disponivel

class Doacao_comida:
    def __init__(self, especie, produto, quantidade):
        self.especie = especie;
        self.produto = produto;
        self.quantidade = quantidade;

class Abrigo:
    def __init__(self, nome):
        self.nome = nome;
        self.responsaveis = {}
        self.animais = {}
        self.adocoes = [];
        self.produtos = [];
        self.parceiros = [];
        
    def registrar_tutor(self, responsavel_id, nome, telefone, endereco ):
        tutor = Responsavel(nome, telefone,endereco);
        self.responsaveis[responsavel_id] = tutor;
            
    def cadastrar_animal(self, animal_id, nome,especie, raca, idade, cuidados =None, responsavel=None):
        animal = Animal(nome=nome,especie=especie,raca=raca,idade=idade,cuidados=cuidados,responsavel=responsavel)
        self.animais[animal_id] = animal

    def adotar_animal(self,animal, responsaveis, data_adoção):
        if animal.responsavel ==True:
            adocao = {"data": data_adocao,"responsaveis":responsaveis,"animal":animal}
            self.adocoes.append(adocao);
        else:
            None
    
    def receber_doacao(self, especie, produto, quantidade):
        produto = Doacao_comida(especie,produto,quantidade)
        self.produtos.append(produto);
        
    def parceiro(self, nome, telefone,especialidade):
        parcerias = Parceiro_vet(nome, telefone, especialidade)
        self.parceiros.append(parcerias);
    
#instancia da classe Pessoa
pessoa1 = Pessoa("Carla", "84237428","Travessa eduardo Pontes");
print(pessoa1);

abrigo = Abrigo("Cães e gatos City");
abrigo.registrar_tutor(1,"Carolina", "9584785","travessa dois amores");