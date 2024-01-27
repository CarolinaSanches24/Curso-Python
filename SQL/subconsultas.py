import sqlite3

conexao = sqlite3.connect('banco');

cursor = conexao.cursor();

# SUBCONSULTAS
# selecione todos os dados do usuario que que o nome tambem estiver na tabela gerentes
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)');

for usuario in dados:
    print(usuario)

conexao.commit();
conexao.close();

