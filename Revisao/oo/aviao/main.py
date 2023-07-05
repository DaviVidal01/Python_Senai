from aviao import Aviao
from coordenadas import CoordenadaGeografica

coordenadaRN = CoordenadaGeografica(-6.889579, -38.543901)
aviaoRN = Aviao("Boing 733", "GOL-1234", coordenadaRN)

coordenadaSJN = CoordenadaGeografica(-7.134814, -34.874397)
aviaoSJN = Aviao("Embraer A320", "Azul-3456", coordenadaSJN)

print("A distancia entre os aviões é : ", aviaoRN.distancia(aviaoSJN), "km")