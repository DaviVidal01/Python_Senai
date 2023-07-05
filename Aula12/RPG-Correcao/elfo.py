from random import randint
from personagem import Personagem

class Elfo(Personagem):
    def __init__(self,nome,hp,forca,dest,
    const,sab,inte,car):
        Personagem.__init__(self,hp,nome,forca,dest,
        const,sab,inte,car)

    def atacar(self):
        hp = randint(1,6) * self.forca + self.dest
        print("O seu ataque vai tirar %d de HP" %hp)
        return hp

    def esquivar(self):
        Personagem.esquivar()+2