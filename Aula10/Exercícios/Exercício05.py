#  Faça um algoritmo que solicite ao usuário números e os armazene em uma matriz 6×6.
# Em seguida, crie um vetor que armazene os elementos da diagonal principal da matriz
mat = [0] * 3
vet = [0] * 3
for x in range(3): #Criando matriz
    mat[x] = [0]*3

for lin in range(3): #Colocando valor em cada quadrado da matriz
    for col in range(3):
        mat[lin][col] = input("Digite um valor: ")
print(mat)

for lin in range(3):
    for col in range(3):
        print(lin,col)
        if lin == col:
            print(lin,col)
            vet[lin] = mat[lin][col]
print(vet)
