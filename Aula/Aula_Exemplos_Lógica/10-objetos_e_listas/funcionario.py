from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade, salario):
        super().__init__(nome, cpf, idade)
        self.salario = salario

    # def vender(self, veiculo, cliente):
    #     cliente.registrar_compra(veiculo)
    #     return "Venda realizada com sucesso!"

    def vender_carro(self, cliente, carro):
        self.carros_vendidos.append(carro)
        cliente.carros_comprados.append(carro)
        print(f"{self.nome} vendeu um {carro.modelo} {carro.marca} para {cliente.nome} por R${carro.preco:.2f}")
