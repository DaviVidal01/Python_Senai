a = int(input())
b = int(input())

try:
    print(a/b)
except (TypeError) as error:
    print(error)
else:
    print("Executou sem erros")
finally:
    print("Essa parte sempre será executada")