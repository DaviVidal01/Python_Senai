from filho import Filho
from pai import Pai


igor = Pai("Igor",32000.00,2000.00,500000)
print("Divida total é R$ ",igor.divida)
print("Meu salario inicial é: ", igor.salario)
igor.pagar_contas(1590.90)
print("Me restou : ", igor.salario)
igor.receber_salario(4000.00)
igor.pagar_contas(570.00)
print("Estou com : ", igor.salario, " na minha carteira")
print("Patrimonio inicial é: ", igor.patrimonio)
igor.guardar_dinheiro()
print("Estou com : ", igor.salario, " na minha carteira")
print("Patrimonio agora é: ", igor.patrimonio)
igor.pagar_contas(4800.70)
print("Patrimonio agora é: ", igor.patrimonio)
leo = Filho("Leo", igor)
print("A mesada do",leo.nome, "é: R$",leo._mesada)
leo.pai.salario = leo._mesada
leo.pai.guardar_dinheiro()
print(leo.pai.patrimonio)
print(igor.patrimonio)
leo.heranca()
print(igor.patrimonio)
igor.receber_salario(3000.00)
leo.pai.pagar_contas(700.00)
print(igor.salario)