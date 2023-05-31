# Escreva um programa Python para verificar se uma letra do Alfabeto(Abecedário) é
# uma vogal ou consoante.

alfabeto = input("Digite uma letra: ")

if alfabeto != "a" and alfabeto != "A" and alfabeto != "e" and alfabeto != "E" and alfabeto != "I" and alfabeto != "i" and alfabeto != "o" and alfabeto != "O" and alfabeto != "u" and alfabeto != "U":
    print("Essa letra é Consoante!")
else:
    print("Essa letra é Vogal!")