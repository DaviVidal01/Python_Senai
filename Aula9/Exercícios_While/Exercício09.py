# Faça um programa em Python para calcular a soma e a média de n números inteiros
# inseridos pelo usuário. Digite 0 para terminar.
num = 1
media = 0
soma = 0
while num != 0:
    num = int(input("Digite um número ou Finalize 0: "))
    if num != 0:
        soma = num + soma
        media +=1
    else:
        pass
print("Resultado: ")
print("Média: {}".format(soma/media))