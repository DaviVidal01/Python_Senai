qi = 0
fi = 0
for x in range(1,11,1):
    n = int(input("Digite um número: "))
    if n >= 10 and n <= 20:
        qi +=1
    else:
        fi +=1
print("====> Resultado:")
print("\nQuantidade Dentro do Intervalo [10/20]: {}".format(qi))
print("\nQuantidade Fora do Intervalo [10/20]: {}".format(fi))