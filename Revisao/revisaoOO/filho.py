from pai import Pai

class Filho(Pai):
    def __init__(self,nome:str,pai:Pai,mesada=100)->None:
        self.nome = nome
        self._mesada = mesada
        self.pai = pai
        self.__heranca = 0

    def heranca(self):
        heranca = float(self.pai.patrimonio * 0.2)
        self.__heranca = heranca
        self.pai.patrimonio -= heranca
