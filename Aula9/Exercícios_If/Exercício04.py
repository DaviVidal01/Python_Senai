# Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do
# novo salário, reajustado de acordo com a tabela abaixo:

# Salário atual               Reajuste
# Abaixo de R$500,00              15%
# de R$500,00 até R$1000,00       10%
# Acima de R$1000,00               5%

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