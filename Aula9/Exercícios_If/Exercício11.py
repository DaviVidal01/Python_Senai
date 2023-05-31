# Faça um programa em Python para encontrar a mediana de três valores inseridos pelo
# usuário

vl1 = int(input("Valor 1: "))
vl2 = int(input("Valor 2: "))
vl3 = int(input("Valor 3: "))

if vl1 > vl2 and vl1 > vl3:
    if vl2 > vl3:
        print(f"Valor 2: {vl2} Mediano")
    else:
        print(f"Valor 3: {vl3} Mediano")
elif vl2 > vl1 and vl2 > vl3:
    if vl3 > vl1:
        print(f"Valor 3: {vl3} Mediano")
    else:
        print(f"Valor 1: {vl1} Mediano")
else:
    if vl1 > vl2:
        print(f"Valor 1: {vl1} Mediano")
    else:
        print(f"Valor 2: {vl2} Mediano")




