import sqlite3;

connect = sqlite3.connect('banco');

cursor = connect.cursor();

# # Inserir vários conjuntos de dados de uma vez
# dados = [
#     (1, 'Ana Beatriz','Rua E,145','ana@gmail.com',145896),
#     (2, 'Fernando Silva', 'Rua A, 123', 'fernando@gmail.com',78898),
#     (3, 'Mariana Souza', 'Rua B, 10', 'souza@gmail.com',4558898),
#     (4, 'Jonas Rafael', 'Rua C, 700', 'jonas@gmail.com',445566)
# ]

# cursor.executemany('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (?, ?, ?, ?,?)', dados)

# #INNER JOIN

# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id ==gerentes.id')

# for usuario in dados:
#     print(usuario);

# # LEFT JOIN 
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id ==gerentes.id')

# for usuario in dados:
#     print(usuario);

# # RIGHT JOIN 
# dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.id ==gerentes.id')

# for usuario in dados:
#     print(usuario);

#FULL JOIN 
dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.id ==gerentes.id')

for usuario in dados:
    print(usuario);
connect.commit()
cursor.close();