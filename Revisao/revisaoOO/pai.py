class Pai:
    _nome = ""
    __divida = 0
    __salario = 0
    __patrimonio = 0
    relogio = False
    def __init__(self,nome:str, divida:float, salario:float, patrimonio:int)->None:
        self.divida = divida
        self.salario = salario
        self.patrimonio = patrimonio
        self._nome = str(nome)

    @property
    def divida(self)->float:
        return self.__divida
    @divida.setter
    def divida(self, valor:float)->None:
        self.__divida = float(valor)

    @property
    def salario(self)->float:
        return self.__salario
    @salario.setter
    def salario(self, salario:float)->None:
        self.__salario = float(salario)

    @property
    def patrimonio(self)->float:
        return self.__patrimonio
    @patrimonio.setter
    def patrimonio(self, total:int)->None:
        self.__patrimonio = int(total)
    
        
    def receber_salario(self, valor:float)->None:
        self.salario = valor

    def pagar_contas(self, total:float)->None:
        if self.__salario < total or self.__salario == 0:
            self.__patrimonio -= total
        else:
            self.__salario -= total
    
    def guardar_dinheiro(self)->None:
        if self.__salario > 0:
            self.__patrimonio += self.__salario
            self.__salario = 0
        else:
            print("Não sobrou dinheiro do salario, tem que economizar")

    