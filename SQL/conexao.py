import sqlite3

conexao = sqlite3.connect('banco')

cursor = conexao.cursor()

# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100) )');
# cursor.execute('ALTER TABLE usuarios RENAME TO usuario');
# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT');
# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone');
# cursor.execute('CREATE TABLE produtos (id INT, descricao VARCHAR(200))');
# cursor.execute('DROP TABLE produtos')
# cursor.execute('INSERT INTO usuario (id,nome,endereco,email,telefone) VALUES(1,"Carolina Sanches","novo buritizal","carol@gmail.com",4582369)');
# cursor.execute('INSERT INTO usuario (id,nome,endereco,email,telefone) VALUES(5,"Ana Beatriz","santana","ana@gmail.com",45658)');
# conexao.execute('DELETE FROM usuario where id=1');

# dados = cursor.execute('SELECT nome, email FROM usuario WHERE id==2');
# for usuario in dados:
#     print(usuario)

# cursor.execute('UPDATE usuario SET nome="José Francisco Junior" WHERE id==2');

#Ordem Descrescente

# dados = cursor.execute('SELECT * FROM usuario ORDER BY id DESC')
# for usuario in dados:
#     print(usuario)
    
# # EXAMPLE LIMIT

# dados = cursor.execute('SELECT * FROM usuario LIMIT 2')
# for usuario in dados:
#     print(usuario)
    
# EXAMPLE DISTINCT

# dados = cursor.execute('SELECT DISTINCT * FROM usuario ')
# for usuario in dados:
#     print(usuario)

# EXAMPLE GROUP BY
dados = cursor.execute('SELECT nome, id FROM usuario GROUP BY nome HAVING id>3')
for usuario in dados:
    print(usuario)


conexao.commit()
conexao.close
