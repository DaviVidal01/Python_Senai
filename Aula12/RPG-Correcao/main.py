from anao import Anao
from elfo import Elfo
from barbaro import Barbaro
from draconato import Draconato
from gnomo import Gnomo
from humano import Humano
from ladrao import Ladrao

anao = Anao("Bigode",1000,10,5,5,10,10,1)
elfo = Elfo("Orelha",1000,10,5,5,10,10,1)
barbaro = Barbaro("Barbudo",1000,10,5,5,10,10,1)
print(anao.atacar())
print(elfo.atacar())
print(barbaro.atacar())