candidatos = {
    "nome": "Igor",
    "idade": 24,
    "profissão": "Instrutor",
    "salário": "R$ 1.800,00",
    "peso": 98.90,
    "sexo": "masculino",
    "certificados": ["Sql","IA","Security", "DBA", "PHP", "Python"],
}

for keys, value in candidatos.items():
    if keys == "certificados":
        print(keys+": ")
        for x in value:
            print("                 -"+x)
    else:
        print("{} : {}".format(keys,value))