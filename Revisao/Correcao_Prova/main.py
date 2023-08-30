from postagem import Postagem
from blog import Blog
from usuario import Usuario
from datetime import datetime
from datetime import timedelta

davi = Usuario(3, 'Davi', 'admin', '12345678')
login = input("Digite o login do usuario: ")
senha = input("Digite a senha do usuario: ")

if login != davi.login or senha != davi.senha:
    print("Dados Inválidos!")
    exit()

blog = Blog()

postagem1 = Postagem(1, "Ola pessoal", "Exercício da prova", datetime.now())
postagem2 = Postagem(23, "Segundo teste", "Vamos ter mais atenção na aula", datetime.now()+timedelta(days=1))
blog.adicionar_postagem(postagem1)
blog.adicionar_postagem(postagem2)
postagem3 = Postagem(45, "Eu criei mais uma","estamos corrigindo",datetime.now())
blog.adicionar_postagem(postagem3)
postagem4 = Postagem(3, "Python", "vamos aprender python", datetime.now()+timedelta(hours=1))
postagem5 = Postagem(12, "Django", "Esse será nosso framework", datetime.now()+timedelta(days=1))
blog.adicionar_postagem(postagem4)
blog.adicionar_postagem(postagem5)
blog.publicar_postagem(postagem3)
blog.apagar_postagem(postagem4)


print("\n\n\n\n\nPostagens Publicadas: ")
for postagem in blog.listar_postagens_publicadas():
    print(postagem,"\n")


print("\n\n\n\n\nTodas postagens Publicadas: ")
for postagem in blog.listar_todas_as_postagens():
    print(postagem,"\n")