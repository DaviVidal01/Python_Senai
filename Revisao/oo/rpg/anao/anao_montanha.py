from random import randint
from anao.anao import Anao

class AnaoDaMontanha(Anao):
    
    def atacar(self):
        hp = randint(1,6) * self.forca
        print("O seu ataque vai tirar %d de HP" %hp)
        return hp
    
    def defender(self)->None:
        Anao.defender()+2