from random import randint
from Personagem import Personagem

class Anao(Personagem):
    def __init__(self,hp,nome,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma):
        Personagem.__init__(self,hp,nome,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma)
    
    def atacar(self):
        hp = randint(1,6) * self.forca
        print("O seu ataque vai tirar %d de HP" %hp)
        return hp
    
    def defender(self)->None:
        Personagem.defender()+2