import sys

try:
    f = open('meuarquivo.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("Erro no OS: ", err)
except ValueError:
    print("Não foi possivel converter o dado para inteiro.")
except Exception as err:
    print(f"Inesperado {err=}, {type(err)=}")
    raise