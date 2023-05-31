#  Faça um programa em que o usuário informe o salário recebido e o total gasto com
# despesas. Deverá ser exibido na tela “Gastos dentro do orçamento” caso o valor gasto não
# ultrapasse o valor do salário e “Orçamento estourado” se o valor gasto
# ultrapassar o valor do salário.

sal = float(input("Salário recebido: "))
des = float(input("Total gasto com Despesas: "))

if sal >= des:
    print("Gastos dentro do orçamento")
else:
    print("Orçamento estourado")
