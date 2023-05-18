sl = float(input("Valor do Funcionário: "))
if sl < 500 and sl > 0:
    rj = sl * 0.15
    print("Salário Reajustado 15% = R${}0".format(sl + rj))
elif sl >= 500 and sl <= 1000:
    rj = sl * 0.10
    print("Salário Reajustado 10% = R${}0".format(sl + rj))
elif sl > 1000:
    rj = sl * 0.05
    print("Salário Reajustado 5% = R${}0".format(sl + rj))
else:
    print("Não Vale Números Negativos.")