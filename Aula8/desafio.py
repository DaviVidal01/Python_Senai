# Crie uma calculadora que faça operações de soma, subtração, divisão, multiplicação e exponenciação
# A função deve receber mais números e as operações que serão realizadas.
def calculando(valor:float,operacao:str,num2:float):
    while operacao != "0": 
        match operacao:
            case "*":
                valor = valor*num2
                print(valor)
            case "**":
                valor = valor**num2
                print(valor)
            case "/":
                valor = valor/num2
                print(valor)
            case "+":
                valor = valor+num2
                print(valor)
            case "-":
                valor = valor-num2
                print(valor)
        operacao = input("Digite a operação [*,/,-,+,**] ou Finalize com 0: ")
        return valor
        num2 = float(input("Digite Número: "))

cal = calculando(float(input("Digite um número [1]: ")), input("Digite a operação [*,/,-,+,**]: "), float(input("Digite um número [2]: ")))
print(cal)