candidatos = {
    "nome": "Igor",
    "idade": 24,
    "profissão": "Instrutor",
    "salário": "R$ 1.800,00",
    "peso": 98.90,
    "sexo": "masculino"
}
msg = "Vamos estudar meu povo. Mais produtividade!"

for keys, value in candidatos.items():
    print("{} : {}".format(keys,value))

print(candidatos.get("nome"))
print(candidatos["idade"])
print(msg[::-1])

for m in msg:
    print(m)

for m in msg[::-1]:
    print(m)