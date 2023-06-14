import sys

try:
    f = open("Meuarquivo.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as error:
    print("Erro no OS: ", error)
except ValueError:
    print("Não foi possível converter o dado para inteiro.")
except Exception as error:
    print(f"Inesperado {error=}, {type(error)=}")
    raise