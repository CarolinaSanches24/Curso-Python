# Exemplo de lista

lista_frutas = [];
lista_frutas.append('Maça');
lista_frutas.append('Uva');
lista_frutas.append('Banana');

print(lista_frutas);

#Adicionando elementos de forma Dinâmica

lista_alunos = [];

while len(lista_alunos)<5:
    aluno = input("Digite um nome do Aluno:");
    lista_alunos.append(aluno);
    
print(f'Lista de Alunos Matrículados {lista_alunos}');

planets = ['Terra', 'Marte','Jupyter'];
print(planets[-1]); #Retorna o último elemento da lista

# Para Ordenar um lista utilizamos a função sort()
numeros = [4,3,5,6,1];