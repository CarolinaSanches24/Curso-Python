''' Suponha que estamos criando uma função chamada
 saudacao que cumprimenta uma pessoa.
 A função pode receber um nome como argumento comum 
 e também aceitar argumentos de palavra-chave para personalizar a saudação.'''


def saudacao(nome, **opcoes):
    if 'saudacao_personalizada' in opcoes:
        print(opcoes['saudacao_personalizada'], nome + '!')
    else:
        print('Olá, ' + nome + '!')

# Exemplo de uso
saudacao('Maria')
saudacao('João', saudacao_personalizada='E aí')

''' nome é um argumento comum, pois é passado diretamente sem especificar o nome do parâmetro.
**opcoes é um argumento de palavra-chave variável. O uso de ** permite que você passe 
qualquer número de argumentos de palavra-chave,
que são capturados como um dicionário chamado opcoes.'''