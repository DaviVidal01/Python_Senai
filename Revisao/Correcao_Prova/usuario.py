class Usuario:
    def __init__(self, id:int, nome:str, login:str, senha:str)->None:
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha
    
    def __str__(self)->str:
        return "id={}, nome={}, login={}, senha={}".format(self.id, self.nome, self.login, self.senha)