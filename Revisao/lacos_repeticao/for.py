aluno = ["luiz", "Rafael", "José", "Davi", "Adriana", "Antonia", "Guilherme", "Rebeca"]
dias = ('Domingo', 'Segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado')
candidatos = {
    'nome':'Igor',
    'idade': 24,
    'profissão': 'Instrutor',
    'salário': 'R$ 1.800,00',
    'peso': 98.90,
    'sexo': 'masculino',
    'certificados': ["Sql", "IA", "Security", "DBA", "PHP", 'Python']
}
msg = "Vamos estudar meu povo. Mais produtividade!"


#variavel = "davi"
#print(variavel)
#variavel = "Igor"
#print(variavel)

for i in aluno:
    print(i.capitalize())

for indice in dias:
    print(indice.upper())

for x in range(10):
    print(x)

for y in range(1, 10):
    print(y)


for d in range(1, 20, 2):
    print(d)

for d in range(0, 20, 2):
    print(d)

#decremento
for xi in range(10, 0, -1):
    print(xi)

#decremento
for ix in range(10, 0, -2):
    print(ix)

#for para array associativo
for keys, values in candidatos.items():
    print("{} : {}".format(keys,values))

print(candidatos.get('nome'))
print(candidatos['idade'])
print(msg[::-1])
for m in msg[::-1]:
    print(m)

for keys, values in candidatos.items():
    if keys == "certificados":
        print(keys+": ")
        for x in values:
            print("             -"+x.upper())
    else:
        print("{} : {}".format(keys,values))