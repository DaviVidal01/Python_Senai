try:
    numero = int(input("Digite um número: "))
    print(numero)
except ValueError:
    print("Você não digitou um número. Isso gerou um Erro!")