class MinhaClasse:
    def __init__(self, nome) :
       self.nome = nome;
       print(f'MinhaClasse1: Chamou o construtor parametrizado de {nome}');
    def __del__(self):
        print(f'Minha Classe 1: Chamou o destrutor de {self.nome}');
print('Começou a execução do programa');
objeto1= MinhaClasse('objeto1');
del objeto1;
print('Vai terminar a execução do programa');