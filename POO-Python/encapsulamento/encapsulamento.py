# Encapsulamneto
class Pessoa:
    def __init__(self, nome, profissao,identidade):
        self._nome = nome; #VARIÁVEL PROTECTED
        self.profissao = profissao; 
        self.__identidade = identidade; #VARIÁVEL PRIVATE
    
    #método exibir uma string    
    def __str__(self):
        return f'Nome: {self._nome} , Profissão: {self.profissao}, Identidade: {self.__identidade}';
    
pessoa = Pessoa('Maria José', 'Estudante','895674');
print(pessoa);
# atributos ou metodos públicos podem ser modificados
pessoa.profissao = 'Programadora';
print(pessoa)
# atributos ou metodos protegidos podem ser modificados
pessoa._nome = 'Carolina Sanches';
print(pessoa);

#atributos ou metodos privados não se modificam
pessoa.__identidade ='415263';
print(pessoa);