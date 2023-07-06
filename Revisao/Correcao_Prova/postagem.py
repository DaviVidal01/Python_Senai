class Postagem:
    def __init__(self,id:int, titulo:str, data_publicacao)->None:
        self.id = int(id)
        self.titulo = titulo
        self.texto = texto
        self.data_publicacao = data_publicacao
    
    def __str__(self) ->str:
        return "id={}, titulo={}, texto={}, Data Publicação={}".format(\
            self.id,self.titulo,self.texto,self.data_publicacao)