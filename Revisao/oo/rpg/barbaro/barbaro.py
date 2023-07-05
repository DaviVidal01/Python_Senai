from random import randint
from Personagem import Personagem

class Barbaro(Personagem):
    def __init__(self,nome,hp,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma):
        Personagem.__init__(self,hp,nome,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma)
    
    def desviarAtaque(self):
        Personagem.desviarAtaque()+ 2

    def raciocinar(self):
        print("O seu raciocinio não é muito bom")
        return randint(1,5)*self.inteligencia
    