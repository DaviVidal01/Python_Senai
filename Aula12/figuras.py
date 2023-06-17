class FormaGeometrica:
    def calc_area(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self,base:int):
        self.base = base

    def calc_area(self):
        return self.base * self.base
    
class Circulo(FormaGeometrica):
    def __init__(self,raio:int):
        self.raio = raio
    
    def calc_area(self):
        return self.raio * self.raio * 3.14

class Triangulo(FormaGeometrica):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        return(self.base*self.altura)/2


triangulo = Triangulo(10,40)
quadrado = Quadrado(30)
circulo = Circulo(40)
# print(triangulo.calc_area()," Area do triangulo")
# print(quadrado.calc_area()," Area do quadrado")
# print(circulo.calc_area()," Area do circulo")
formas_geometricas = [triangulo, quadrado, circulo]

soma = 0

for formas in formas_geometricas:
    soma = soma + formas.calc_area()

print(soma)