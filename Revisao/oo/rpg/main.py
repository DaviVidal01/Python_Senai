from anao.anao import Anao
from elfo.elfo import Elfo
from elfo.elfo_negro import ElfoNegro
from barbaro.barbaro import Barbaro
from anao.anao_colina import AnaoDaColina
from draconato import Draconato

anao = Anao("Bigode",1000,10,5,5,10,10,1)
elfo = Elfo("Orelha",1000,10,5,5,10,10,1)
barbaro = Barbaro("Barbudo",1000,10,5,5,10,10,1)
anao_colina = AnaoDaColina("Bigode Pequeno",1000,10,5,5,10,10,1)
elfo_negro = ElfoNegro("Destruidor",500,12,15,5,10,10,1)
print(anao.atacar())
print(elfo.atacar())
print(elfo.nome)
print(barbaro.atacar())
print(anao_colina.atacar())
print(elfo_negro.nome)