def calculadora(num1:float, operator:str, num2:float)->float:
    match operator:
        case '+' :
            return num1 + num2
        case '-' :
            return num1 - num2
        case '/':
            return num1 / num2
        case '*':
            return num1 * num2
        case '^':
            return num1 ** num2
        case _:
            return "Operadores errados"

reutilizar = "não"
calcular = "sim"
calc = 0
while calcular == "sim":
    if reutilizar == "não":
        num1 = float(input("Digite o primeiro numero:"))
    elif reutilizar == "sim":
        num1 = calc
    operador = input("Digite operador:")
    num2 = float(input('Digite o segundo numero:'))
    calc = calculadora(num1,operador,num2)
    print(calc,"\n")
    reutilizar = input("Deseja reutilizar o resultado na outra operação? 'sim' ou 'não'")
    calcular = input("Deseja fazer outra operação? 'sim' ou 'não'")