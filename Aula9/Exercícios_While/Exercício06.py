# Faça um programa em Python que leia n números inteiros a partir do teclado, até que o
# usuário digite 0. Ao final, mostre a soma de todos os números digitados.
soma = 0
while num != 0:
    num = int(input("Digite Numero Inteiro: "))
    soma = soma + num
print(soma)