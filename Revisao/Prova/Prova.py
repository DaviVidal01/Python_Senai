from Usuario import Usuario
from Blog import Blog
from Postagem import Postagem
from datetime import date

Davi = Usuario(12345,"Davi","davividal01","40028922doido")
Postagem1 = Postagem(54321,"T - Seguem","DaviVidal01",date.fromisoformat("2005-06-22"),Davi)
Postagem2 = Postagem(54321,"T - Esse","DaviVidal01",date.fromisoformat("2015-06-22"),Davi)
Postagem3 = Postagem(54321,"T - Github","DaviVidal01",date.fromisoformat("2025-06-22"),Davi)
Blog = Blog()

Blog.adicionarPostagem(Postagem1)
Blog.adicionarPostagem(Postagem2)
Blog.adicionarPostagem(Postagem3)
print(Blog.listarPostagensPublicadas)
print(Blog.postagens[0].titulo)
print(Blog.postagens[0].texto)
print(Blog.postagens[0].usuario.nome)
print(Blog.postagens[1].dataPublicacao)

Blog.publicarPostagem(Postagem1)
Blog.publicarPostagem(Postagem2)
Blog.publicarPostagem(Postagem3)
print(Blog.listarPostagensPublicadas())

print(Blog.listarTodasAsPostagens())
