# Faça um programa em Python para calcular a soma e a média de n números inteiros
# inseridos pelo usuário. Digite 0 para terminar
count = 0
soma = 0
x = ""

while x != "0":
    count += 1
    num = int(input("Digite Número: "))
    soma = soma + num
    print(f"Valor da Soma: {soma}")
    x = input("Digite 0 para parar ou prossiga: ")

print(f"Media: {soma / count}")