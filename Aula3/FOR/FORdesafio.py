candidatos = {
    "nome": "Igor",
    "idade": 24,
    "profissão": "Instrutor",
    "salário": "R$ 1.800,00",
    "peso": 98.90,
    "sexo": "masculino",
    "certificados": ["Sql","IA","Security", "DBA", "PHP", "Python"],
}

print(*candidatos["certificados"], sep= "\n") #Pesquisei para encontrar uma forma

print("--------------")

for keys, value in candidatos.items():#Fiz com base em FOR dos programas anteriores...
    if keys == "certificados":
        for x in value:
            print(x)
    else:
        print("{} : {}".format(keys,value))
    
    
