aluno = "Igor"
estudou = False

if estudou:
    print("Sucesso para você...")
else:
    print("Você tem que estudar mais")

idade = 12

if idade <16:
    print("Boa noite {} você ainda não pode votar...".format(aluno))
elif idade > 16 and idade < 18:
    print("Boa noite {} você é menor de idade mas pode votar.".format(aluno))
elif estudou == false or idade == 30:
    print("Você não está estudando, não pode fazer nada. Vai estudar")
else:
    msg = 10 * "vai estudar em casa\n" + "teste de variavel"
    print(msg.upper())
#print(dir(msg))