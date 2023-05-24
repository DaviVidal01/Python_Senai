def github(frase:str,forca:int) -> str:
    forca = forca * 2 * 5 / 6
    return frase

def davi(msg:str) -> str:
    print("Olá eu me chamo ", msg)

def star(idade:int, profissao:str) -> str:
    print("Olá mundo eu tenho ",idade," e minha profissão é: ",profissao)

def repository(gols:int, jogos: int) -> int:
    if jogos > gols:
        return jogos
    else:
        return gols

a = github("Sou DaviVidal01",10)
print(a.upper())
print(github("Sou DaviVidal01",1))
github("SOS.",5)
davi("DaviVidal01")
star(28,"Professor")
repository(11,30)
github("Davi", 1)
print()
print("oi")

def somar(a=1,b=1) -> int:
    return a + b

b = somar(10,10)
print(b)

def exibir(msg="", sep=" ", final="\n"):
    return msg + sep + final

exibir()
print(exibir("10 amigos", " ola"))