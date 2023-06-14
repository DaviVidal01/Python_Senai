# Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 20
# posições. Crie uma função que recebe o vetor preenchido e substitua todas as ocorrências
# de valores negativos por zero, as ocorrências de valores menores do que 10 por 1 e as
# demais ocorrências por 2.

def substitua(vetor:list):
    for x in range(20):
        if vetor[x] < 0:
            vetor[x] = 0
        elif vetor[x] <= 10:
            vetor[x] = 1
        else:
            vetor[x] = 2
    return vetor
v = [0]*20
for ix in range(len(v)):
    v[ix] = int(input("Digite número: "))
print(substitua(v))