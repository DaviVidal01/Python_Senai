# Crie um código em linguagem Python que peça o nome do usuário por meio da função
# input (). Se o nome for "Optimus Prime", imprima "Bem-vindo, você é um guerreiro de
# Cybertron". Caso contrário, imprima "Bom dia, NOME". (Substitua o NOME pelo nome do
# usuário)

nome = input("Digite seu nome: ")

if nome.lower() == "optimus prime":
    print("Bem-vindo, você é um guerreiro de Cybertron")
else:
    print(f"Bom dia, {nome}")