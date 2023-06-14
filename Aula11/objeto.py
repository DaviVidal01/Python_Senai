class Pessoa:
    def __init__(self,nome:str,idade:int,peso:float,altura:float) -> None:
        self.nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def __envelhecer(self, envelheceu:int):
        if self.__idade <= 21:
            self.__crescer()
        self.__idade += envelheceu

    def __engordar(self, engordou:float):
        self.__peso += engordou

    def __emagrecer(self, emagreceu:float):
        self.__peso -= emagreceu

    def __crescer(self, altura:float):
        self.__altura += 0.5

Davi = Pessoa("Davi",17,65,1.80)
print(Davi)
print(Davi.__envelhecer(10))
print(Davi.__emagrecer(5))
print(Davi.__engordar(10))
print(Davi.__crescer(0.10))
