num = int(input("Digite um Número: "))
saida = 0
for ix in range(1,num+1,1):
    saida = ix + saida

print("A Soma do Número 1 até o {} = {}".format(num,saida))