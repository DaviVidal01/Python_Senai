from coordenadas import CoordenadaGeografica
class Aviao:
    def __init__(self, nome, numero,coordenada:CoordenadaGeografica):
        self.nome = nome
        self.numero = numero
        self.coordenada = coordenada

    def distancia(self, aviao):
        return self.coordenada.calcular_distancia(aviao.coordenada)

    