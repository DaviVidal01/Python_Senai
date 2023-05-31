# Escreva um programa em Python para calcular o fatorial de qualquer número inteiro
fatorial = 1
cos = int(input("Digite um Número para fatorar: "))
for ix in range(cos,0,-1):
    fatorial = fatorial * ix
    print(f"{fatorial}")