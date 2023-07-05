class Personagem:
    def __init__(self,nome,hp,forca,dest,
    const,sab,inte,car):
        self.hp = hp
        self.nome = nome
        self.forca = forca
        self.dest = dest
        self.const = const
        self.sab = sab
        self.inte = inte
        self.car = car
    
    def atacar(self):
        hp = randint(1,20) * self.forca
        print("O seu ataque vai tirar %d de HP" %hp)
        return hp
    
    def defender(self):
        return self.const
    
    def raciocinar(self):
        return self.sab * randint(1,20)
    
    def convencer(self):
        return self.car * randint(1,20)

    def esquivar(self):
        return self.dest