# Crie um programa em Linguagem Python que solicite a senha de um usuário e depois,
# peça para digitar novamente até que as duas senhas sejam correspondente

name = input("Name:")
senha= input("Senha:")
senha2= input(("Confirmar Senha: "))
while senha != senha2:
    senha2= input(("Confirmar Senha Novamente: "))