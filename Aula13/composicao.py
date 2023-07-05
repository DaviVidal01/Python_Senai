class Livro:
    def __init__(self,titulo):
        self.titulo = titulo
        self.numero_de_capitulos = 0
        self.capitulos = []

    def adicionarCapitulos(self, capitulo):
        self.capitulos.append(capitulo)
        self.numero_de_capitulos += 1

class Capitulo:
    def __init__(self,titulo):
        self.titulo = titulo

livro = Livro("Codigo da Vinci")
capitulo1 = Capitulo("Tema1")
capitulo2 = Capitulo("Tema2")
conclusao = Capitulo("Conclusão")
livro.adicionarCapitulos(capitulo1)
livro.adicionarCapitulos(capitulo2)
livro.adicionarCapitulos(conclusao)
print(livro.capitulos)
print(livro.capitulos[0].titulo)
