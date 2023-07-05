from random import randint
from personagem import Personagem

class Humano(Personagem):
    def __init__(self,nome,hp,forca,dest,
    const,sab,inte,car):
        Personagem.__init__(self,hp,nome,forca,dest,
        const,sab,inte,car)