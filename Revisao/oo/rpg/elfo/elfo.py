from random import randint
from Personagem import Personagem

class Elfo(Personagem):
    def __init__(self,nome,hp,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma):
        Personagem.__init__(self,hp,nome,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma)
        
    def atacar(self):
        hp = randint(1,6) * self.forca + self.destreza
        print("O seu ataque vai tirar %d de HP" %hp)
        return hp
    
    def desviarAtaque(self):
        Personagem.desviarAtaque()+2
