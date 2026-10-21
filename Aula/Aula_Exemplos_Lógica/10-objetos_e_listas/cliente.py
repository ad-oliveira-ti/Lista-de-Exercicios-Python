from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade, endereco, telefone):
        super().__init__(nome, cpf, idade)
        self.endereco = endereco
        self.telefone = telefone
        self.veiculos_comprados = []

    # def registrar_compra(self, veiculo):
    #     self.veiculos_comprados.append(veiculo)
    #     return "Compra realizada com sucesso!"


    def comprar_carro(self, carro):
        self.veiculos_comprados.append(carro)
        print(f"{self.nome} comprou um {carro.modelo}, {carro.marca} por R${carro.preco:.2f}")