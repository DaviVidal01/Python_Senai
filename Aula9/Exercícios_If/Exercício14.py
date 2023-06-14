#  Dada a atual crise hídrica do país, as pessoas começaram a construir reservatórios para
# armazenar água em suas propriedades. Faça um programa em linguagem Python que
# auxilie os utilizadores do reservatório a controlarem seu consumo. Obtenha do teclado as
# dimensões de um reservatório (altura, largura e comprimento, em centímetros) e o consumo
# médio diário dos utilizadores do reservatório (em litros/dia).
# Assuma que o reservatório esteja cheio, tenha formato cúbico e informe:

# (a) A capacidade total do reservatório, em litros;
# (b) A autonomia do reservatório, em dias;
# (c) A classificação do consumo, de acordo com a quantidade de dias de autonomia:
# 
# Consumo elevado, se a autonomia for menor que 2 dias; Consumo moderado, se a
# autonomia estiver entre 2 e 7 dias; Consumo reduzido, se a autonomia maior que 7 dias.
# Observação: Considere que cada litro equivale a 1000 cm3 ou 1 dm3

altura = float(input("Digite a altura (cm): "))
largura = float(input("Digite a largura (cm): "))
comprimento = float(input("Digite a comprimeto (cm): "))
c_diario = float(input("DIgite o valor do consumo médio diário (litros/dia): "))

cap_total =(altura*largura*comprimento)/1000;
#O resultado deve ser dividido por mil para passar cm3 para litros

auton_reser=cap_total/c_diario
print("Capacidade do Reservatório= ", cap_total, " Litros")
print("Autonomia do Reservatório= ", auton_reser," Dias")

#Classificando o consumo
if auton_reser < 2:
    print("Consumo Elevado")
elif auton_reser >= 2 and auton_reser <= 7:
    print("Consumo Moderado")
elif auton_reser > 7:
    print("Consumo Baixo")