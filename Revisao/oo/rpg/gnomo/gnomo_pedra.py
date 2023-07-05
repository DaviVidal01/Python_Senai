from gnomo.gnomo import Gnomo
from random import randint

class GnomoDaPedra(Gnomo):
    
    def raciocinar(self):
        print("O seu raciocinio é muito bom")
        return randint(6,12)*self.inteligencia