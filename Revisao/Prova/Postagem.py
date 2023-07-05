from Usuario import Usuario
class Postagem(Usuario):
    
    def __init__(self,iD:int,Titulo:str,Texto:str,dataPublicacao, Usuario:Usuario) -> None:
        self.id = iD
        self.titulo = Titulo
        self.texto = Texto
        self.dataPublicacao = dataPublicacao
        self.usuario = Usuario