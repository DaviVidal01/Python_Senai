class Mae:
    espada = 10
    def ola(self):
        print("Eu sou a classe Mãe")
    
    def pontos(self,pontos):
        self.espada = pontos
    
class Filho(Mae):
    def idade(self):
        print("Eu teho 32 anos")
    def ola(self):
        print("Eu sou o filho")

class SegundoFilho(Mae):
    def ola(self):
        print("Estou aprendendo polimorfismo.")

class TerceiroFilho(Mae):
    def falar(self):
        print("estou falando...")

class Neto(TerceiroFilho):
    pass

filho = Filho()
mae = Mae()
filho2 = SegundoFilho()
neto = Neto()
filho3 = TerceiroFilho()

filho.ola()
filho2.ola()

print(filho2.espada)

neto.ola()
neto.falar()
neto.pontos(30)
print(neto.espada)
