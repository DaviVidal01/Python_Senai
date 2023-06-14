# Crie um programa em linguagem Python que permite ao usuário inserir os valores dos
# produtos comprados por um cliente. O programa deve terminar quando o usuário inserir o
# valor 0. Se o usuário digitar um valor negativo não deve ser processado e um novo valor
# deve ser solicitado como entrada. Ao final, informe o valor total a pagar, lembrando que,
# caso as vendas ultrapassem o total de R$ 1.000,00, deverá ser aplicado um desconto de
# 10%
vl = 1
total = 0
desconto = 0
while vl != 0:
    vl = float(input("Digite o valor do produto ou Finalize 0: "))
    if vl < 0:
        print("Outro Valor deve ser Inserido!")
    else:
        total = vl + total
    if total >= 1000:
        desconto = total * 0.1
    
print("RESULTADO:")
print("Total a Pagar: R${}".format(total))
print("Desconto: R${}".format(desconto))
print("Total Descontado: R${}".format(total-desconto))
