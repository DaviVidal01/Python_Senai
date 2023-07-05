try:
    print("Ola turma.")
    print(x)
except ValueError:
    print("Dados inteiros não encontrados. ")
except NameError:
    print("Variavel não existe.")
except:
    print("Algum erro inesperado ocorreu.")
