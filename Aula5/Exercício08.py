msg = input("Digite uma Palavra\Frase: ")
qn = 0
ql = 0
for ix in range(0,len(msg),1):
    tst = msg[ix]
    if tst.isnumeric():
        qn +=1
    else:
        ql +=1
print("\nTamanho da String: {}".format(len(msg)))
print("\nQuantidade de Dígitos: {}".format(qn))
print("\nQuantidade de Letras: {}".format(ql))