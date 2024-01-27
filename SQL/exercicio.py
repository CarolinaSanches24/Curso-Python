''' 1 - Crie uma tabela chamada "alunos" com os seguintes campos: id
(inteiro), nome (texto), idade (inteiro) e curso (texto).
2 - Insira pelo menos 5 registros de alunos na tabela que você criou no
exercício anterior.
3 - Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos". ok
b) Selecionar o nome e a idade dos alunos com mais de 20 anos. ok
c) Selecionar os alunos do curso de "Engenharia" em ordem 
alfabética. ok
d) Contar o número total de alunos na tabela ok

4 - Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela. ok 
b) Remova um aluno pelo seu ID. ok

5 - 5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela.

6 -  Consultas e Funções Agregadas
7 - Atualização e Remoção com Condições
8 - Junção de Tabelas
'''

import sqlite3

conexao = sqlite3.connect('banco');

cursor = conexao.cursor();

dados = [
    (1, 'Maria Julia',15,'Técnico em informática'),
    (2, 'Natanael Costa', 20, 'Engenharia'),
    (3, 'Marcio José', 21, 'Engenharia'),
    (4, 'Lucas Felipe', 5, 'pré - escola'),
    (5, 'Monkey D luffy', 10, 'ensino fundamental')
]
# cursor.execute('CREATE TABLE alunos (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, curso VARCHAR(100))');
# cursor.executemany('INSERT INTO alunos (id, nome, idade, curso) VALUES(?,?,?,?)', dados)

# dados = cursor.execute('SELECT * FROM alunos') 

# dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20');


# dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ')

    
# cursor.execute('UPDATE alunos SET idade ="18" WHERE id="1"')

# cursor.execute('DELETE FROM alunos WHERE id="5"');
# dados = cursor.execute('SELECT * FROM alunos') 
# for aluno in dados:
#     print(aluno);
# dados = cursor.execute('SELECT COUNT(*) AS numero_de_alunos FROM alunos');
# dados = cursor.fetchone() # pega o primeiro resultado da consulta
# numero_de_alunos = dados[0]

# print (f'Total de Alunos :{numero_de_alunos}');

# cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), idade INT , saldo FLOAT )')

# dadosClientes = [
#     ("Ana Claúdia",30,1000.0),
#     ("José Messias",25,1500.0),
#     ("Juliana Fonseca", 35, 1200.0),
# ]

# cursor.executemany("INSERT INTO clientes (nome, idade, saldo) VALUES (?,?,?)", dadosClientes);

#! Selecione o nome e a idade dos clientes com idade superior 30 anos.

# tabela_clientes = cursor.execute('SELECT nome , idade FROM clientes WHERE idade>30 ')

# for cliente in tabela_clientes:
#     print(cliente);
    
#!  Calcule o saldo médio dos clientes.

# tabela_clientes = cursor.execute('SELECT AVG(saldo) as media_saldo_clientes FROM clientes');
# tabela_clientes= cursor.fetchone();
# media_saldo_clientes = tabela_clientes[0];

# print(f'Saldo médio dos clientes {media_saldo_clientes:.2f}');

#! Encontre o cliente com o saldo máximo.

# tabela_clientes = cursor.execute('SELECT MAX(saldo) as saldo_maximo FROM clientes');
# tabela_clientes = cursor.fetchone();
# saldo_maximo = tabela_clientes[0];

# print(f'Saldo máximo :{saldo_maximo}');

#! Conte quantos clientes têm saldo acima de 1000

# tabela_clientes = cursor.execute('SELECT COUNT(saldo) as saldo_acima_mil FROM clientes WHERE saldo>1000');
# tabela_clientes = cursor.fetchone();
# saldo_acima_mil = tabela_clientes[0];

# print(f'Total de clientes com saldo acima de 1000: {saldo_acima_mil}');

#! Atualize o saldo de um cliente específico.

# cursor.execute('UPDATE clientes SET saldo="1800.0" WHERE id="1"');
# tabela_clientes = cursor.execute('SELECT * FROM clientes');
# for cliente in tabela_clientes:
#     print(cliente);

#! Remova um cliente pelo seu ID.

# cursor.execute('DELETE FROM clientes WHERE id="3"');

# tabela_clientes = cursor.execute('SELECT* FROM clientes');

# for cliente in tabela_clientes:
#     print(cliente);

#! criar uma tabela chamada compras

# cursor.execute('CREATE TABLE compras(id INTEGER PRIMARY KEY AUTOINCREMENT,produto VARCHAR(200),valor FLOAT,cliente_id INTEGER, FOREIGN KEY (cliente_id) REFERENCES clientes(id) )');

#! Insira algumas compras associadas a clientes existentes na tabela "clientes".

# compras = [
#     ("Camisa Azul",55.00,2),
#     ("Blusa Lilas",38.99,1),
#     ("Short Vermelho",25.99,1)
# ]
# cursor.executemany('INSERT INTO compras (produto, valor, cliente_id) VALUES(?,?,?)', compras);

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

tabela = cursor.execute('SELECT clientes.nome AS nome_cliente, compras.produto, compras.valor FROM compras INNER JOIN clientes ON compras.cliente_id == clientes.id ')

for cliente in tabela:
    print(cliente);
    
conexao.commit();
conexao.close();
