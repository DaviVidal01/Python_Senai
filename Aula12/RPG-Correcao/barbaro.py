from random import randint
from personagem import Personagem

class Barbaro(Personagem):
    def __init__(self,nome,hp,forca,dest,
    const,sab,inte,car):
        Personagem.__init__(self,hp,nome,forca,dest,
        const,sab,inte,car)

    def esquivar(self):
        Personagem.esquivar()+2    

    def raciocinar(self):
        print("O seu raciocínio não é muito bom")
        return randint(1,5)*self.inte
