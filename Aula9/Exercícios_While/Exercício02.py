# Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o
# resultado. Por exemplo, se o número é 201 , então a saída deve ser 3.
ix = 0
num = input("Digite um Número: ")
for x in num:
    ix+=1
print(f"Possui {ix} dígitos")
