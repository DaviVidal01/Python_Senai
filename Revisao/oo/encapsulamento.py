class Pessoa:
    __nome = ""
    __idade = 0
    __peso = 0
    __altura = 0

    @property
    def nome(self)->str:
        return self.__nome
    @nome.setter
    def nome(self, nome: str)->None:
        self.__nome = str(nome)
    
    @property
    def idade(self)->int:
        return self.__idade
    @idade.setter
    def idade(self, idade)->None:
        self.__idade = int(idade)
    
    @property
    def altura(self)->float:
        return self.__altura
    @altura.setter
    def altura(self, altura)->None:
        self.__altura = float(altura)
    
    @property
    def peso(self)->float:
        return self.__peso
    @peso.setter
    def peso(self, peso)->None:
        self.__peso = float(peso)

    def __init__(self,nome:str,idade:int,peso:float,altura:float) -> None:
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.peso = peso

    def envelhecer(self)-> None:
        if self.idade < 21 :
            self.__crescer()
        self.idade += 1    

    def engorda(self):
        pass

    def emagrecer(self):
        pass

    def __crescer(self)-> None:
        self.altura += 0.05

    
