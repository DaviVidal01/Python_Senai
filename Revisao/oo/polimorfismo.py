class Mae:
    espada = 10
    def ola(self):
        print("Eu sou a classe mãe.")
    
    def pontos(self, pontos):
        self.espada = pontos

class Filho(Mae):
    def idade(self):
        print("Eu tenho 32 anos.")
    
    def ola(self):
        print("Eu sou o filho.")

class SegundoFilho(Mae):
    def ola(self):
        print("Estou aprendendo polimorfismo.")
  

class TerceiroFilho(Mae):
    def falar(self):
        print("estou falando...")

class Neto(TerceiroFilho):
    pass

filho = Filho()
filho.ola()
filho2 = SegundoFilho()
filho2.ola()
print(filho2.espada)

net = Neto()
net.ola()
net.falar()
net.pontos(30)
print(net.espada)



"""
class Person(object):      
    def __init__(self, name, idnumber):     
        self.name = name  
        self.idnumber = idnumber  
    
    def display(self):  
        print(self.name)  
        print(self.idnumber)  
    
class Employee(Person):             
    def __init__(self, name, idnumber, salary):  
        self.salary = salary  
        Person.__init__(self, name, idnumber)   
    
    def show(self): 
        print(self.salary) 
              
a = Employee('Rahul', 886012, 30000000)      
print(a.name)    
a.show()  
"""