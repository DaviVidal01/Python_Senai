num = input("Digite um Número: ")
saida = 0
x = 0
for ix in num:
    if num[x] != "-" and num[x] != " ":
        saida = 1 + saida
    x = x + 1
print("Quantidade de Dígitos: {}".format(saida))
