from Personagem import Personagem


class Ladrao(Personagem):
    def __init__(self,nome,hp,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma):
        Personagem.__init__(self,hp,nome,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma)