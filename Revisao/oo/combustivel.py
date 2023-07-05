class BombaCombustivel:
    __tipo_combustivel = "Gasolina"
    __valor_combustivel = 5.0
    __quantidade_combustivel = 5000
    __tamanho_da_bomba = 10000

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel
    @tipo_combustivel.setter
    def tipo_combustivel(self, combustivel):
        self.__tipo_combustivel = str(combustivel)
    
    @property
    def valor_combustivel(self):
        return self.__valor_combustivel
    @valor_combustivel.setter
    def valor_combustivel(self, valor):
        self.__valor_combustivel = float(valor)
    
    @property
    def quantidade_combustivel(self):
        return self.__quantidade_combustivel
    @quantidade_combustivel.setter
    def quantidade_combustivel(self, quantidade):
        self.__quantidade_combustivel = float(quantidade)


    def __init__(self, combustivel:str, valor:float, quantidade:float)->None:
        self.tipo_combustivel = combustivel
        self.quantidade_combustivel = quantidade
        self.valor_combustivel = valor
        self.__tamanho_da_bomba = self.__quantidade_combustivel

    def abastecer_por_valor(self, valor:float)->str:
        abastecimento = valor / self.valor_combustivel
        self.alterar_quantidade_combustivel(abastecimento,False)
        return "O total de litros abastecido foi: ", abastecimento, " litros"

    def abastercer_por_litro(self,litro:float)->str:
        total = litro * self.valor_combustivel
        self.alterar_quantidade_combustivel(litro,False)
        return "O total a ser pago é: R$", total

    def alterar_valor(self,valor:float)->None:
        self.valor_combustivel = valor
    
    def alterar_combustivel(self,combustivel:str)->None:
        self.tipo_combustivel = combustivel

    def alterar_quantidade_combustivel(self,quantidade:float,recarga:bool)->None:
        if recarga:
            self.quantidade_combustivel += quantidade
            if self.quantidade_combustivel > self.__tamanho_da_bomba:
                self.quantidade_combustivel = self.__tamanho_da_bomba
        else:
            self.quantidade_combustivel -= quantidade


bomba_alcool = BombaCombustivel("Alcool", 4.0, 5000.0)
bomba_gasolina = BombaCombustivel("Gasolina", 5.5, 10000.0)
print(bomba_alcool.quantidade_combustivel)
print(bomba_gasolina.quantidade_combustivel)
print(bomba_gasolina.abastecer_por_valor(36.5))
print(bomba_alcool.abastercer_por_litro(10.0))
print(bomba_gasolina.abastercer_por_litro(72))
bomba_alcool.abastecer_por_valor(598.80)
print(bomba_alcool.quantidade_combustivel)
print(bomba_gasolina.quantidade_combustivel)
bomba_alcool.alterar_quantidade_combustivel(2000.0,True)
print(bomba_alcool.quantidade_combustivel)