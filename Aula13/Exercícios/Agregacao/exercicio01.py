#A classe Avião poderia ter uma associação com a classe Coordenada Geográfica, pois esta
# ultima consegue representar a latitude, longitude e permite ainda indicar a
# distância em km entre duas Coordenada Geográfica

#A associação entre essas classes seria do tipo Agregação ou Composição? Agregação

#Quais atributos e métodos deverão permanecer na classe Avião? Coordenada, Percorrer
class Coordenada_Geográfica:
    def __init__(self,latitude:float, longitude:float, distancia:float) -> None:
        self.__latitude = latitude
        self.__longitude = longitude
        self.distancia = distancia

    def Percorrer(self, percorreu:float):
        return self.distancia - percorreu

class Aviao:
    def __init__(self,Coordenada_Geográfica:Coordenada_Geográfica) -> None:
        self.Coordenada = Coordenada_Geográfica
    
    def Percorrer(self, percorreu:float):
        return self.Coordenada.Percorrer(percorreu)

coordenada = Coordenada_Geográfica(60,20,2000)
Airbus = Aviao(coordenada)
print(coordenada.distancia)
print(Airbus.Percorrer(1400))