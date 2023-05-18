n = int(input("Digite um Número: "))

lt = 1
st = 0

for ix in range(1, n + 1, 1):
    print("{}".format(st))
    aux = lt + st
    st = lt
    lt = aux
    