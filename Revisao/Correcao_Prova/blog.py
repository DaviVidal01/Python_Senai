from datetime import datetime

class Blog:
    def __init__(self)->None:
        self.postagens = []
    
    def adicionar_postagem(self,postagem)->None:
        self.postagens.append(postagem)
    
    def publicar_postagem(self,postagem)->None:
        postagem.data_publicacao = datetime.now()
        for postagem_existente in self.postagens:
            if postagem_existente.id == postagem.id:
                self.postagens.remove(postagem_existente)
        self.postagens.append(postagem)
    
    def listar_postagens_publicadas(self)->list:
        postagem_publicadas = []
        for postagem in self.postagens:
            if postagem.data_publicacao < datetime.now():
                postagem_publicadas.append(postagem)
        return postagem_publicadas

    def listar_todas_as_postagens(self)->list:
        return self.postagens
    
    def apagar_postagem(self,postagem)->None:
        for postagem_existe in self.postagens:
            if postagem_existe.id == postage.id:
                self.postagens.remove(postagem)