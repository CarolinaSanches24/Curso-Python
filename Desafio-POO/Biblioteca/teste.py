import colorama;
colorama.init();

# encapsulamento 
class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.__nome = nome
        self.__telefone = telefone
        self.__nacionalidade = nacionalidade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
            
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone
    
    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nova_nacionalidade):
        self.__nacionalidade = nova_nacionalidade
        
    def __str__(self):
        return (
        f'Nome: {self.__nome}\n' +
        f'Telefone: {self.__telefone}\n'+
        f'nacionalidade:{self.__nacionalidade}'
    )
class Livro:
    def __init__(self, titulo, editora, numero_maximo_renovacoes):
        self.titulo = titulo
        self.editora = editora
        self.generos = [];
        self.numero_maximo_renovacoes = numero_maximo_renovacoes
        self.autores = []
        self.exemplares = []


    def adicionar_autor(self, autor):
        self.autores.append(autor)

    def adicionar_exemplar(self, exemplar):
        self.exemplares.append(exemplar)
        
    def adicionar_genero(self, genero):
        self.generos.append(genero);
        
    def __str__(self):
       return (
        colorama.Fore.MAGENTA + '[Info Livro]' + colorama.Style.RESET_ALL +
        f'\nTítulo: {self.titulo}\n' +
        f'Editora: {self.editora}\n' +
        f'Número Máximo de Renovações Permitidas: {self.numero_maximo_renovacoes}\n' +
        f'Autores: {self.autores}\n' +
        f'Gêneros: {self.generos}\n' +
        f'Exemplares Disponiveis: {len(self.exemplares)}'
    )
       
class Exemplar:
    def __init__(self, livro):
        self.__livro = livro
        self.__estado = "disponivel"
        self.__data_emprestimo = None
        self.__data_devolucao = None
        self.__renovacoes = 0

    @property
    def livro(self):
        return self.__livro

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def data_emprestimo(self):
        return self.__data_emprestimo

    @data_emprestimo.setter
    def data_emprestimo(self, valor):
        self.__data_emprestimo = valor

    @property
    def data_devolucao(self):
        return self.__data_devolucao

    @data_devolucao.setter
    def data_devolucao(self, valor):
        self.__data_devolucao = valor

    @property
    def renovacoes(self):
        return self.__renovacoes

    def renovar(self):
        if self.__renovacoes < self.__livro.numero_maximo_renovacoes:
            self.__renovacoes += 1
            return 'O emprestimo do Livro foi renovado'
        else:
            return 'O exemplar exceceu o limite de renovações'


usuario = Usuario(" Juliana", "84237428", "Brasileiro")
usuario.nome="Carol";
print(usuario.nome)
livro = Livro("Livro 1", "Editora A", 5)
livro.adicionar_autor('JK Rolling')
livro.adicionar_genero('Ficçao')
livro.adicionar_exemplar(livro)
livro.adicionar_exemplar(livro)
print(livro)
    
exemplar = Exemplar(livro)
print(exemplar.renovar());
print(exemplar.livro.titulo);
   
 