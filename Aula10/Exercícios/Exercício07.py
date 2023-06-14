# Tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50, mostre qual é
# o maior valor existente na matriz desconsiderando os elementos da diagonal principal.

import random
mat = [0]*3

for i in range(3):
    for j in range(3):
        mat[i][j] = random.randint(10, 50)
print("Exibindo Valores: ")
print(mat)

maior = mat[1][0]
for i in range(3):
    for j in range(3):
        if i != j:
            if mat[i][j] > maior:
                maior = mat[i][j]
print( "O maior valor entre os números é: {}".format(maior))