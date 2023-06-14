#  Crie uma função que retorne o valor da expressão: 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m, para
# um valor de n definido pelo usuário. Verifique se o valor de n definido pelo usuário é positivo
# e, caso não seja, solicite outro valor até ser fornecido um valor positivo

def expressao():
    n = int(input("Digite um valor: "))
    while n <=0:
        print("O valor digitado não deve ser menor que 0!")
        n = int(input("Digite novamente: "))
    m = 3
    result = 0
    for ix in range(2,n+1):
        termo = ix / m
        result = termo + result
        m += 2
    return result

# def calcular_expressao():
#     n = int(input("Digite um valor: "))
#     while n <=0:
#         print("O valor digitado não deve ser menor que 0!")
#         n = int(input("Digite novamente: "))
#     soma = 0
#     m = 3
#     for i in range(2,n+1):
#         termo = i / m
#         soma += termo
#         m += 2
#     return soma
# resultado = calcular_expressao()
resultado = expressao()
# print("O valor da expressão é: ",resultado)
print("O valor da expressão é: ",resultado)