# Construtor padrão 
class MinhaClasse1:
    def __init__(self):
        print('MinhaClasse1: Chamou o construtor padrão');

objeto1 = MinhaClasse1();

class MinhaClasse2:
    pass # não faz nada

objeto2 = MinhaClasse2();

#Construtor Parametrizado

class MinhaClasse3:
    def __init__(self,param):
        print(f'Minha Classe3: Chamou o construtor parametrizado com o parâmetro:{param}');
objecto3 = MinhaClasse3('João');