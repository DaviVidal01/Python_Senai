#Crie um programa para representar funcionários em um sistema de gestão de pessoas.

#É necessário que nesta modelagem seja feito de uso de no mínimo duas classes e com uma associação entre elas

class Empresa:
    def __init__(self,nome_empresa:str) -> None:
        self.nome_empresa = nome_empresa
        self.numero_de_funcionarios = 0
        self.funcionarios = []

    def Contratar(self, funcionarios:Funcionario) -> None:
        self.funcionarios.append(funcionarios)
        self.numero_de_funcionarios += 1
    
    def Demitir(self, funcionarios:Funcionario) -> None:
        self.funcionarios.remove(funcionarios)
        self.numero_de_funcionarios -= 1

class Funcionario:
    def __init__(self,nome:str,cargo:str,gmail:str,senha:int):
        self.nome = nome
        self.cargo = cargo
        self.gmail = gmail
        self.senha = senha


