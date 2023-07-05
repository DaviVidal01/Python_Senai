import os

print("------------------------------")
operations = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Mutiplicação",
    "/": "Divisão",
    "^": "Exponenciação"
}

while True:
    os.system("cls") # pois é windows
    i = 0
    for op, name in operations.items():
        print(i, ":", name)
        i+=1
    print("")
    print("Escolha a operação que deseja realizar:")
    op = int(input())
    op_string = list(operations.keys())[op]

    print("")
    print("{} escolhida.".format(op_string))
    print("")
    print("Qual é o primeiro valor?")
    v1 = float(input())
    print("Qual o segundo valor ?")
    v2 = float(input())

    if op == 0:
        result = v1 + v2
    elif op == 1:
        result = v1 - v2
    elif op == 2:
        result = v1 * v2
    elif op == 3:
        result = v1 / v2
    elif op == 4:
        result = v1 ** v2

    print("")