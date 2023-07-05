import os
amor = True
quantidade_de_amor = int(input("Digite a quantidade: "))
msg = input("Digite o nome e uma frase para sua mãe: ")

while amor:
    print(msg)
    #print("Eu te amo muito mãe...")
    quantidade_de_amor = quantidade_de_amor - 1
    if quantidade_de_amor == 0:
        amor = False
        print("Final do while. Eu te amo muito.")


x = 1
while x < 10:
    print("Em execução: {}".format(x))
    x+=1

os.system("cls")