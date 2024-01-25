class Ave ():
    def andar(self):
        print('andando');
        
    def voar(self):
        print('voando');

class Calopsita(Ave):
    def piar(self):
        print('piuuu');

class Pato(Ave):
    def quack(self):
        print('quack')
        
    def nadar(self):
        print('nadando');
    
def executar_pato(animal):
    try:
        animal.quack()
        animal.andar()
        animal.voar()
        animal.nadar()
    except AttributeError as e:
        print('O animal não é um pato:', e);

pato = Pato()
calopsita = Calopsita();

executar_pato(pato);
executar_pato(calopsita);