#Crie um programa para representar funcionários em um sistema de gestão de pessoas.

#É necessário que nesta modelagem seja feito de uso de no mínimo duas classes e com uma associação entre elas

class Funcionario:
    def __init__(self,nome:str, idade:int, cargo:float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.cargo = cargo

    def salario(self,horas:int) -> float:
        if self.cargo == "Gerente":
            self.recebe = 10 * horas
        elif self.cargo == "Trabalhador":
            self.recebe = 5.50 * horas
        return self.recebe
        

class Trabalho:
    def __init__(self,funcionario:Funcionario) -> None:
        self.__funcionario = funcionario
    
    def salario(self,horas:int) -> float:
        self.__funcionario.salario(horas)
        return self.__funcionario.recebe

cadastro = Funcionario("Davi",17,"Gerente")
Davi = Trabalho(cadastro)
print(cadastro.cargo)
print(Davi.salario(25))