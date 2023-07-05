from random import randint
import Personagem

class Gnomo(Personagem):
    def __init__(self,nome,hp,forca,dest,
    const,sab,inte,car):
        Personagem.__init__(self,hp,nome,forca,dest,
        const,sab,inte,car)

    def raciocinar(self):
        print("O seu raciocínio não é muito bom")
        return randint(6,12)*self.inte
