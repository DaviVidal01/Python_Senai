#  Faça um programa em Python que leia n números inteiros e positivos a partir do teclado,
# até que o usuário digite 0. Ao final, informe o maior número digitado
maior = 0
num = 1
while num != 0:
    num = int(input("Digite número ou finalize 0: "))
    if num > 0:
        num > maior
        maior = num
print("O Numero maior: {}".format(maior))