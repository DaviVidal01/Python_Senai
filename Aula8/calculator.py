# Crie uma calculadora que faça operações de soma, subtração, divisão, multiplicação e exponenciação
# A função deve receber 2 números e as operações que serão realizadas.
def calculando(num1:float,operacao:str,num2:float):
    valor = 0
    match operacao:
        case "*":
            valor = num1*num2
            return valor
        case "**":
            valor = num1**num2
            return valor
        case "/":
            valor = num1/num2
            return valor
        case "+":
            valor = num1+num2
            return valor
        case "-":
            valor = num1-num2
            return valor

cal = calculando(float(input("Digite um número [1]: ")), input("Digite a operação [*,/,-,+,**]: "), float(input("Digite um número [2]: ")))
print(cal)