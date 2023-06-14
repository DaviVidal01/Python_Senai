# Tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50, mostre a
# média dos elementos da diagonal secundária.
import random
tam = 10
m = [0]*tam
for x in range(tam):
    m[x] = [0]*tam
for x in range(tam):
    for y in range(tam):
        m[x][y] = random.randint(10,50)
    
m2 = tam-1
s = 0

for x in range(tam):
    s = s + m[x][m2]
    m2 = m2 - 1

for x in range(tam):
    m = s / tam
    print(m[x][:])
print("A Média é igual a: ",m)