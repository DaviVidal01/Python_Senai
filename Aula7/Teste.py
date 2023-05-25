def mat():
    ix = int(input("IX: "))
    q = int(input("Repetidor: "))
    for ix in range(ix,q):
        x = input("Testador: ")
        v = input("Valor: ")
        if x == v:
            print("X == V")
        else:
            pass


print("{}".format(mat()))