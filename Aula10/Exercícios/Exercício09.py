# Crie um algoritmo que leia um valor e a partir disso faça: (1) se o valor for 1, 2 ou 3,
# mostre o valor elevado ao quadrado; (2) se o valor for o número 4 ou 9, mostre a raiz
# quadrada do número; (3) se for os valores 6, 7 e 8, mostre o valor dividido 9

num = int(input("Digite um número: "))
if num == 1 or num == 2 or num == 3:
    q = num * num
    print("O número {} elevado ao quadrado é igual a {}".format(num,q))
elif num == 4 or num == 9:
    r = num ** (1/2)
    print("A raíz quadrada de {} é {}".format(num,r))
else:
    d = num/9
    print("{} divido por 9 é igual a {} =".format(num,d))