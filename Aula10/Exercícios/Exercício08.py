# Tendo uma matriz 5×5 preenchida com valores aleatórios entre 0 e 99, mostre qual é o
# segundo maior valor existente na matriz

import random
tam = 5
mat = [0]*tam
for i in range(tam):
    mat[i] = [0]*tam
for i in range(tam):
    for j in range(tam):
        mat[i][j] = random.randint(0,99)
print("\n Exibindo Matriz: ")
print(mat)
maior = mat[0][0]
for i in range(tam):
    for j in range(tam):
        if mat[i][j] > maior:
            maior2 = mat[i][j]
print("O segundo maior entre eles é: ", maior2)