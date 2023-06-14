# Crie um programa em Python para verificar a validade de uma senha do usuário.
# As regras de validação são as seguintes:
# - A senha deve ter no mínimo 6 caracteres.
# - A senha deve ter no máximo 12 caracteres.
# - A senha deve ter pelo menos 1 letra minúscula entre [az] e 1 letra maiúscula entre [AZ].
# - A senha deve ter pelo menos 1 número entre [0-9].
# - A senha deve ter pelo menos 1 caractere especial [$ # @]
x = "Inválida"
while x != "Correta":
    senha = input("Digite uma Senha: ")
    if len(senha) <= 6 and len(senha) >= 12: #Testando tamanho
        print("Senha Incorreta - Tamanho Incorreto")
    for ix in senha:
        if ix.isnumeric() == True: #Testando número
            validador = True
            break
        else:
            validador = False
    if validador != True:
        print("Senha Incorreta - Faltam Letras")
    for ix in senha:
        if ix == "#" or ix == "$" or ix == "@": #Testando Especial
            validador = True
            break
        else:
            validador = False
    if validador != True:
        print("Senha Incorreta - Faltam Caractere Especial")
    for ix in senha:
        validador = False
        if ix.isalpha() == True:
            if ix == ix.lower():
                validador = True
        else:
            break
        if ix.isalpha() == True:
            if ix == ix.upper():
                validador = True
        else:
            break
    if validador != True:
        print("Não possui letras Maiúsculas e nem Minúsculas")
    else:
        x = "Correta"
print(f"A Senha está {x}")
        