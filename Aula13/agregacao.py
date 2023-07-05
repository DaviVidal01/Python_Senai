class Motor:
    def __init__(self,cilindros, cavalos,giro_atual):
        self.cilindros = cilindros
        self.cavalos = cavalos
        self.giro = giro_atual

    def acelerar(self,velocidade):
        self.giro += velocidade/10
        return self.giro
        

class Carro:
    def __init__(self,marca,motor:Motor):
        self.marca = marca
        self.motor = motor
    
    def acelerar(self,velocidade):
        self.motor.acelerar(velocidade)
        return self.motor.giro

ztech = Motor(2000,600,0)
hb20 = Carro("Hyundai", ztech)
print(hb20.acelerar(0))
print(hb20.acelerar(10))
print(hb20.acelerar(100))
print(hb20.acelerar(200))
print(hb20.motor.cavalos,"cv")
zt = Motor(600,40,0)
gol = Carro("Hyundai", zt)
print(gol.motor.giro)
print(gol.acelerar(100))
print(gol.motor.cavalos,"cv")