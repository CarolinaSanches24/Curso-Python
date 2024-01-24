# Definindo a primeira classe pai
class Animal:
    def __init__(self, nome):
        self.nome = nome;
    def fazer_som(self):
        pass
    def __str__(self):
        return f'O nome do animal é: {self.nome}';
coelho = Animal('Oracio');
print(coelho);

# Definindo a segunda classe pai

class Mamifero:
    def alimentar_filhotes(self):
        pass

# Definindo a classe filha que herda de Animal e Mamifero

class Cachorro(Animal, Mamifero):
    def __init__(self, nome, raca):
        # Chamando os construtores das classes pai
        Animal.__init__(self,nome)
        Mamifero.__init__(self)
        self.raca = raca;
    def fazer_som(self):
        return "Au au"
    def alimentar_filhotes(self):
        return "cachorro alimentando filhotes"
# Criando uma instância da classe Cachorro
dog = Cachorro(nome = 'Rex',raca ='Labrador');
# Acessando métodos da classe pai Animal
print(f"{dog.nome} faz o som: {dog.fazer_som()}")

# Acessando métodos da classe pai Mamifero
print(dog.alimentar_filhotes())