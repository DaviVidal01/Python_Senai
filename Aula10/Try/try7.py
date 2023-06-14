try:
    print("Ola turma.")
except ValueError:
    print("Dados inteiros não encontrados. ")
except NameError:
    print("Variável não existe.") 
except:
    print("Algum erro inesperado ocorreu.")