# Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 30
# posições. Crie uma função que recebe o vetor preenchido e substitua todas as ocorrência
# de valores positivos por 1 e todos os valores negativos por 0.

v = [None] * 30
def lista(vet:list):
    for x in range(len(v)):
        if vet[x] >=0:
            vet[x] = 1
        else:
            vet[x] = 0
    return vet
for x in range(len(v)):
    v[x] = int(input("Digite um número: "))
print(lista(v))