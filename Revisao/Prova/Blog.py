from Postagem import Postagem, Usuario
from datetime import date
class Blog(Postagem,Usuario):
    def __init__(self):
        self.postagens = []
        self.publicadas = []
        self.po = 0
        self.pu = 0
        self.data_atual = date.today()
    
    def adicionarPostagem(self,Postagem:Postagem):
        self.po += 1
        return self.postagens.append(Postagem)
    
    def publicarPostagem(self,Postagem:Postagem):
        self.pu += 1
        return self.publicadas.append(Postagem)

    def listarPostagensPublicadas(self):
        
        for ix in range(self.pu):
            if self.publicadas[ix].dataPublicacao >= self.data_atual:
                print(self.publicadas[ix].titulo)
        
    
    def listarTodasAsPostagens(self):
        for ix in range(self.po):
            print(self.publicadas[ix].titulo)