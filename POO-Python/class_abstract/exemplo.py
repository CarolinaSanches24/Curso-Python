from abc import ABC, abstractmethod;

class ClasseAbstrata(ABC):
    @abstractmethod
    def metodo_abstrato(self):
        pass
    
    @property
    @abstractmethod
    def propriedade_abstrata(self):
        pass
class ClasseDerivada(ClasseAbstrata):
    #sobrescreve o método abstrato
    def metodo_abstrato(self):
        print("Boa noite");
    
    #sobrescrevendo a propriedada abstrata
    
    @property
    def propriedade_abstrata(self):
        return 'Noite'
abstrato =  ClasseDerivada();
abstrato.metodo_abstrato();