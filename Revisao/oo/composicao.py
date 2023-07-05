class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.numero_de_capitulos = 0
        self.capitulos = []

    def adicionar_capitulo(self, capitulo):
        self.capitulos.append(capitulo)
        self.numero_de_capitulos += 1

class Capitulo:
    def __init__(self, titulo):
        self.titulo = titulo


livro = Livro("Codigo da vinci")
capitulo1 = Capitulo("Tema1")
capitulo2 = Capitulo("Tema2")
conclusao = Capitulo("Conclusão")
livro.adicionar_capitulo(capitulo1)
livro.adicionar_capitulo(capitulo2)
livro.adicionar_capitulo(conclusao)
print(livro.capitulos)
print(livro.capitulos[0].titulo)