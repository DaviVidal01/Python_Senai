# Crie um algoritmo que leia um valor e a partir disso faça: (1) se for um valor negativo,
# mostre o módulo (valor sem sinal) do valor; (2) se for um valor maior do que 10, solicite
# outro valor e mostre a diferença entre eles; (3) Caso o valor não seja de nenhuma condição
# anterior, mostre o valor dividido por 5

n1 = int(input("Digite um valor: "))
if n1 < 0:
    r = 1 * -n1
    print(r)
elif n1 > 10:
    n2 = int(input("Digite outro valor: "))
    r = n1 - n2
    print(r)
else:
    r = n1/5
    print(r)