#  Faça um programa em linguagem Python que lê um número n digitado pelo usuário(esse
# número vai ser a quantidade de termos) e imprime os n primeiros números da sequência de
# Fibonacci

n = int(input("Digite um Número: "))

lt = 1
st = 0

for ix in range(1, n + 1, 1):
    print("{}".format(st))
    aux = lt + st
    st = lt
    lt = aux