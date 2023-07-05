from Personagem import Personagem
from random import randint

class Gnomo(Personagem):
    def __init__(self,nome,hp,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma):
        Personagem.__init__(self,hp,nome,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma)
    
    def raciocinar(self):
        print("O seu raciocinio é muito bom")
        return randint(6,12)*self.inteligencia