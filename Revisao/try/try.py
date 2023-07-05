while True:
    try:
        numero = int(input("Digite o numero: "))
        print(numero)
        break
    except ValueError:
        print("Você não digitou um numero. Isso gerou um erro!")