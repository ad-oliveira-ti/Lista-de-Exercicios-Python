from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco, cor, placa):
        super().__init__(marca, modelo, ano, preco)
        self.cor = cor
        self.placa = placa