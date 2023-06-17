class BombaCombustivel:
    __tipoCombustivel = ""
    __valorLitro = 5.21
    __quantidadeCombustivel = 1
#----------{Property and Init}-------------
    #Valor---------------
    @property
    def valorLitro(self) -> float:
        return self.__valorLitro
    @valorLitro.setter
    def valorLitro(self, valorLitro:float) -> None:
        self.__valorLitro = float(valorLitro)
    
    #Tipo---------------
    @property
    def tipoCombustivel(self) -> str:
        return self.__tipoCombustivel
    @tipoCombustivel.setter
    def tipoCombustivel(self,tipoCombustivel:str) -> None:
        self.__tipoCombustivel = str(tipoCombustivel)

    #Quantidade---------------
    @property
    def quantidadeCombustivel(self) -> float:
        return self.__quantidadeCombustivel
    @quantidadeCombustivel.setter
    def quantidadeCombustivel(self,quantidadeCombustivel:float) -> None:
        self.__quantidadeCombustivel = float(quantidadeCombustivel)

    #Init---------------
    def __init__(self,tipoCombustivel:str,valorLitro:float,quantidadeCombustivel:float) -> None:
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
#---------------{Métodos}------------------

    def abastecerPorValor(self):
        preco = self.__valorLitro
        self.quantidadeCombustivel((self.__valorLitro/preco))
        print(self.__quantidadeCombustivel)
    
    def abastecerPorLitro(self):
        
        self.valorLitro((self.__valorLitro * self.__quantidadeCombustivel))
        print(self.__valorLitro)

PorValor = BombaCombustivel("Gasolina",10.42,1)
PorLitro = BombaCombustivel("Gasolina",5.21,5)
print(PorValor.quantidadeCombustivel)
print(PorLitro.valorLitro)