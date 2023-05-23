qp = 0
qi = 0
qn = int(input("Digite uma quantidade de Números: "))

for ix in range(1,qn+1):
    if ix % 2 == 0:
        qp +=1
    else:
        qi +=1
print("=====> Resultados:")
print("\nDo 1 ao {}".format(qn))
print("Quantidade de Pares: {}".format(qp))
print("Quantidade de Impares: {}".format(qi))