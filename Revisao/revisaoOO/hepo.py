class Pai:
    _nome = ""
    __salario = 0
    def __init__(self,despesa):
        self._nome = "Igor"
        self.parentesco = "pai"
        self.__salario = 1300
        self.despesas = despesa


    def apresenta(self):
        print("Oi eu sou o", self._nome, self.parentesco)

    def _exibe_salario(self):
        return self.__salario
    
    def __pensamentos(self):
        pass

    @property
    def despesas(self):
        return self.__despesas
    @despesas.setter
    def despesas(self, valor):
        self.__despesas = int(valor)

class Filho(Pai):
    def __init__(self, despesas):
        self._nome = "joao"
        #super().__init__(1000)
        self.despesas = despesas

    def apresenta(self):
        print("Sou o filho")
        



filho1 = Filho(100)
filho1.apresenta()
print(filho1._nome)
print(filho1.despesas)
print(filho1._exibe_salario())
pai1 = Pai(1200)
pai1.apresenta()
print(pai1._nome)
print(pai1._exibe_salario())
print(pai1.despesas)
pai1.despesas = 900
print(pai1.despesas)