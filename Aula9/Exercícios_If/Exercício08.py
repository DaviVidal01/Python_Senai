# Escreva um programa em Python para encontrar números entre 100 e 400 (ambos
# inclusos), onde cada dígito de um número é um número par. Os números obtidos devem ser
# impressos em sequência separada por vírgulas

v = ", "
par = ""
for ix in range(100,401,1):
    if ix % 2 == 0:
        par = par + str(ix)
        if ix != 400:
           par = par + v
print(f"{par}")