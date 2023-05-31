#Faça um programa que recebendo um valor inteiro, informe se o número é positivo,
#negativo ou neutro

n = int(input("Digite um Número Inteiro: "))
if n > 0:
    print(f"O número {n} é POSITIVO")
elif n < 0:
    print(f"O número {n} é NEGATIVO")
elif n == 0:
    print(f"O número {n} é NEUTRO")
