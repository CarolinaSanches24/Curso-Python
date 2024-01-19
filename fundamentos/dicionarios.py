# Dicionario a sintaxe é {}

dicionario = {'Chave':'Valor'};
dicionario['maca'] = 'É uma fruta';
dicionario['carro'] = 'É um véiculo';
dicionario['Gato'] = 'É um animal';

print(dicionario);

# O método keys () retorna uma visão de todas as chaves no dicionario

livros = {'Harry Potter e a Pedra Filosofal':'J. K. Rowling',
          'O Senhor dos Anéis':'J.R.R. Tolkien',
          'Aventuras de Sherlock Holmes':'Arthur Conan Doyle'}

# Acessando as chaves (titulos dos livros)

titulos = livros.keys()

# Convertendo para lista

lista_titulos = list(titulos);
print(lista_titulos);


# Método get permite recuperar um valor associado a chave

contatos = {
    'Alice': '123-456-7890',
    'Bob': '987-654-3210',
    'Charlie': '555-123-4567',
}

# Pedindo ao usuário para digitar um nome
nome_pesquisado = input("Digite o nome para encontrar o número de telefone: ")

# Usando o método get() para recuperar o número de telefone
numero_telefone = contatos.get(nome_pesquisado)

# Verificando se o nome está no dicionário e exibindo o resultado
if numero_telefone:
    print(f"O número de telefone de {nome_pesquisado} é {numero_telefone}.")
else:
    print(f"Desculpe, o nome {nome_pesquisado} não foi encontrado nos contatos.")
    
# Para remover uma chave de um dicionario utiliza-se o método pop()

alunos = {
    101:'Alice',
    102:'Joaquim',
    103:'Mateus',
    104:'Claudia'
}

print(f'Alunos antes da remoção {alunos}');

id_aluno = int (input("Digite o código do aluno a ser removido: "));

nome_aluno_removido = alunos.pop(id_aluno, None);

if nome_aluno_removido is not None:
    print(f'Aluno removido com sucesso: {nome_aluno_removido}');
else:
    print(f'Desculpe , aluno com código {id_aluno} não foi encontrado');
    
print(f'Alunos após a remoção:{alunos}');