# Escrever um programa em linguagem Python que lê um valor i, inteiro e positivo e 3
# valores a, b e c. Se o valor de i é par então calcular e imprimir na tela a média aritmética de
# a, b e c. Caso contrário, se i>10 então calcular e imprimir na tela a média aritmética e
# ponderada de a, b e c. Os pesos dos valores são respectivamente 2, 3 e 4.

i = int(input("Digite um valor inteiro: "))
a = int(input("Valor: "))
b = int(input("Valor: "))
c = int(input("Valor: "))
ap = 2
bp = 3
cp = 4

if i % 2 == 0:
    print(f"Média Aritmética: {(a+b+c)/3}")
elif i > 10:
    print(f"Média Aritmética Ponderada: {(ap*a + bp * b + cp * c)/9}")
