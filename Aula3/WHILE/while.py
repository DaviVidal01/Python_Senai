amor = True
quantidade_de_amor = int(input("Digite a quantidade de amor: "))
msg = str(input("Digite a frase escrita: "))

while amor:
    print(msg)
    quantidade_de_amor = quantidade_de_amor - 1
    if quantidade_de_amor == 0:
        amor = False
        print("Final do while. {}".format(msg))

x = 1
while x < 10:
    print("Em execução: {}".format(x))
    x+=1