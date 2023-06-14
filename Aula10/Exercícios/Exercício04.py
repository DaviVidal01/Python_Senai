# crie um algoritmo que solicite 3 valores que representarão os lados de um triângulo.
# Considere que não importa a ordem que serão fornecidos os valores, podendo ser fornecido
# primeiro a hipotenusa e depois os catetos, ou primeiro os catetos e depois a hipotenusa,
# etc. Crie também uma função que recebe o vetor e retorna se os lados informados formam
# um triângulo retângulo. Você pode utilizar o teorema de Pitágoras para auxiliar na
# resolução: hiponusa2 = cateto12 + cateto22

import math
def t(vet):
    if vet[0] > vet[1] and vet[0] > vet[2]:
        h = vet[0]
        c1 = vet[1]
        c2 = vet[2]
    elif vet[1] > vet[0] and vet[1] > vet[2]:
        h = vet[1]
        c1 = vet[0]
        c2 = vet[2]
    else:
        h = vet[2]
        c1 = vet[0]
        c2 = vet[1]
    if h == match.sqrt(c1**2 + c2**2):
        return 1
    else:
        return 0

vet = [0]*3
for x in range(len(vet)):
    vet[x] = int(input("Digite um número: "))
if t(vet) == 1:
    print("RETÂNGULO!")
else:
    print("NÃO É RETÂNGULO!")