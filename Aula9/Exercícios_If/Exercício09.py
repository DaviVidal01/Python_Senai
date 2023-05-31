# Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols
# de cada time) e informe se o resultado foi um empate, se a vitória foi do primeiro time ou do
# segundo time.

gol1 = int(input("Digite o placar do Primeiro Time"))
gol2 = int(input("Digite o placar do Segundo Time"))

if gol1 == gol2:
    print("Empate!")
elif gol1 > gol2:
    print("Vitória do Primeiro Time!")
elif gol2 > gol1:
    print("Vitória do Segundo Time!")