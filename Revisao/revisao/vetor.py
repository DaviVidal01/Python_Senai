tupla = (2,4,6,[],"oi")
lista =[3,45,67,"teste"]
dicionario = {
    'lucas': 21,
    'leo': "oi",
    'teste': {
        'lucas': 35,
        'isa': 40
    }
}

print(dicionario["teste"]["lucas"])

print(lista)
lista.append(1)
lista.append(56)
lista.append("oi")
print(lista)
print(lista[2])
lista[2] = 30
print(lista[2])

print(dicionario)
dicionario["igor"] = "Professor"
print(dicionario)
dicionario["leo"] = "eu errei"
print(dicionario)



lista2 = [
    [1,2,3,4,5,[6,7,8,9]],
    12,
    "oi",
    [9,8,7,6,[[1,4,6],10],23]
]
lista2[0][5][2] = "indice"
print(lista2[0][5][2])
print(lista2[3][4][0][2])
print(lista2[3][4][1])
lista2[3][4][1] = "giselli"
print(lista2[3][4][1])



lista3 =[
    1,
    2,
    "oi",
    ["teste",[1,"oi",35],25],
    "aluno"
]

print(lista3[3][1][1])