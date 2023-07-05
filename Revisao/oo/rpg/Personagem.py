from random import randint

class Personagem:
    def __init__(self,hp,nome,
                 forca,destreza,constituicao,
                 sabedoria, inteligencia,carisma):
        self.hp = hp
        self.nome = nome
        self.forca = forca
        self.constituicao = constituicao
        self.sabedoria = sabedoria
        self.inteligencia = inteligencia
        self.carisma = carisma
        self.destreza = destreza

    def atacar(self):
        hp = randint(1,20) * self.forca
        print("O seu ataque vai tirar %d de HP" %hp)
        return hp
    
    def defender(self):
        return self.constituicao
    
    def raciocinar(self):
        return self.sabedoria * randint(1,20)
    
    def convencer(self):
        return self.carisma * randint(1,20)
    
    def desviarAtaque(self):
        return self.destreza











    

    
