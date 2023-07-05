try:
    #verifica todo o código executado aqui dentro
    pass
except:
    #se aquele código retorna erro ele joga para essa parte do código
    pass

try:
    i = int(input("Digite um numero: "))
    
except:
    i = 0
print(i)

try:
    i = int(input("Digite um numero: "))
    print(i)
except:
    print("Erro você não digitou um numero inteiro")