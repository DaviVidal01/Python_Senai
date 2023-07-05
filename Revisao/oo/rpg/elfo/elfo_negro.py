from random import randint
from elfo.elfo import Elfo

class ElfoNegro(Elfo):

        
    def atacar(self):
        hp = randint(1,6) * self.forca + self.destreza
        print("O seu ataque vai tirar %d de HP" %hp)
        return hp
    
    def desviarAtaque(self):
        Elfo.desviarAtaque()+6
