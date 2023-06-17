class Pessoa:
    __nome = ""
    __idade = 0
    __peso = 0
    __altura = 0

    def __init__(self,nome:str,idade:int,peso:float,altura:float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    #Nome--------------
    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self,nome:str) -> None:
        self.__nome = nome

    #Idade--------------
    @property
    def idade(self) -> int:
        return self.__idade
    @idade.setter
    def idade(self,idade:int) -> None:
        self.__idade = int(idade)

    #Altura--------------
    @property
    def altura(self) -> float:
        return self.__altura
    @altura.setter
    def altura(self,altura:float) -> None:
        self.__altura = float(altura)

    #Peso--------------
    @property
    def peso(self) -> float:
        return self.__peso
    @peso.setter
    def peso(self,peso:float) -> None:
        self.__peso = float(peso)

    def envelhecer(self):
        if self.__idade <= 21:
            self.__crescer()
        self.__idade += 1

    def engordar(self, engordou:float):
        self.__peso += engordou

    def emagrecer(self, emagreceu:float):
        self.__peso -= emagreceu

    def __crescer(self):
        self.__altura += 0.05

Davi = Pessoa("Davi",17,65,1.80)
print(Davi)
Davi.envelhecer()
Davi.emagrecer(5)
Davi.engordar(10)
print(Davi.nome)
print(Davi.idade)
print(Davi.peso)
print(Davi.altura)