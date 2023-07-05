from endereco import Endereco
from pessoa import Pessoa

luciano = Pessoa("Luciano",'123456789', 18)
endereco_residencial = Endereco("Rua da Mina", "Centro", 14,"SJN","MG")
endereco_comercial = Endereco("Carlos Stibler", "Jujuba", 39, "SJN","MG")
luciano.adicionar_endereco(endereco_comercial)
luciano.adicionar_endereco(endereco_residencial)
print(luciano.nome)
print(luciano.enderecos)
for endereco in luciano.enderecos:
    print("Rua: ", endereco.rua, "numero: ", endereco.numero, "Bairro: ", endereco.bairro)
    print("CIDADE: ",endereco.cidade, "Estado: ", endereco.estado)