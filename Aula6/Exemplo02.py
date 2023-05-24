#Funções Lambda

preco = 100
def calcular_imposto(preco:float) -> int:
    return preco * 0.2
print(calcular_imposto(preco))

calcular_imposto_lambda = lambda preco: preco*0.2
print(calcular_imposto_lambda(preco))

vendas = [180, 300, 500, 20, 56, 290, 48, 90]
impostos_a_ser_pagos = list(map(lambda num: (num*0.15)+num, vendas))
print(impostos_a_ser_pagos)

numeros = [10,20,23,345,234,123,46]
dobro = list(map(lambda x: x*2, numeros))
print(dobro)
num = int(input("Digite um numero: "))
dobro = lambda x : x*2
print(dobro(num))

frases = ["amigos", "lucas está o quartel", "jose", "parem de conversar!"]
maiuscula = list(map(str.upper, frases))
print(maiuscula)

numeros1 = [1,2,3,4,5,6]
numeros2 = [7,6,5,3,23,3]
soma = list(map(lambda x=1, y=10: x+y, numeros1, numeros2))
print(soma)

num1 = [1,2,3,4,5,6,8,19]
num2 = [7,6,5,3,23,3,5]
somas = list(map(lambda x=1, y=10: x+y, num1,num2))
print(somas)

mult = lambda x=10, y=10: x*y
print(mult())
print(mult(20,10))