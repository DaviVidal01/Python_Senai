# Crie um algoritmo que leia um valor e a partir disso faça: (1) se o valor for 1 e 2, mostre
# o valor elevado ao cubo; (2) se o valor for múltiplo de 3 mostre o fatorial desse número; (3)
# se o valor for os valores 4, 5, 7 ou 8, mostre o valor dividido 9. Caso não seja nenhum dos
# valores, informe como “valor inválido”

import math
num = int(input("Digite um número: "))
if num == 1 or num == 2:
    r = num**3
    print(r)
elif num % 3 == 0:
    r = math.factorial(num)
    print(r)
elif num == 4 or num == 5 or num == 7 or num == 8:
    r = num / 9.0
    print(r)
else:
    print("Número Inválido")