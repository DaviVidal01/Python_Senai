print("----[Tabuada do Número]----")
valor = int(input("Digite um Número: "))

print("\n ---> SOMA")
for ix in range(1,11,1):
    print("{} + {} = {}".format(valor,ix,(valor+ix)))
print("\n ---> SUBTRAÇÃO")
for ix in range(1,11,1):
    print("{} - {} = {}".format(valor,ix,(valor-ix)))
print("\n ---> MULTIPLICAÇÃO")
for ix in range(1,11,1):
    print("{} * {} = {}".format(valor,ix,(valor*ix)))
print("\n ---> DIVISÃO")
for ix in range(1,11,1):
    print("{} / {} = {}".format(valor,ix,(valor/ix))) 