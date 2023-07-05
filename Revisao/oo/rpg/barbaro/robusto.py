from random import randint
from barbaro.barbaro import Barbaro

class Robusto(Barbaro):

    
    def desviarAtaque(self):
        Barbaro.desviarAtaque()+ 5

    def raciocinar(self):
        print("O seu raciocinio não é muito bom")
        return randint(1,5)*self.inteligencia