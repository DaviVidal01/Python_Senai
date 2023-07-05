class Pessoa:
    nome = ""
    idade = 0
    peso = 0
    altura = 0

    def __init__(self,nome:str,idade:int,peso:float,altura:float) -> None:
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.peso = peso

    def envelhecer(self)-> None:
        if self.idade < 21 :
            self.crescer()
        self.idade += 1    

    def engorda(self):
        pass

    def emagrecer(self):
        pass

    def crescer(self)-> None:
        self.altura += 0.05


