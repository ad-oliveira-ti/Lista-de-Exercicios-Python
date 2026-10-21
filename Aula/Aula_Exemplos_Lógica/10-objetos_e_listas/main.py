from carro import Carro
from cliente import Cliente
from concessionaria import Concessionaria
from funcionario import Funcionario
from pessoa import Pessoa
from veiculo import Veiculo

def main():
    # Criando um cliente
    cliente1 = Cliente("Maria Santos", 25, "987.654.321-00", "Rua A, 123", "(11) 99999-9999")
    cliente1 = Cliente("thiago", 86766557834, 25, "av. zero hora", 986233688)
    # Adicionando um carro ao estoque
    carro1 = Carro("Volkswagen", "Golf", 2021, 120000.00, "Branco", "ABC-1234")
    carro1 = Carro("nissan", "skyline", 1997, 70000, "preto", "IXV9876")
    carro2 = Carro("mazda", "RX7", 1998, 50000, "branco", "IRE3977")
    # Criando um vendedor
    funcionario1 = Funcionario("João Silva", 35, "123.456.789-00", 3500.00)
    funcionario1 = Funcionario("henrrique", 98865743522, 30, 50000)
    # Criando uma concessionária
    concessionaria = Concessionaria("Concessionária ABC")
    concessionaria1 = Concessionaria("NewCars")
    # Comprando um carro
    concessionaria.encontrar_carro_por_modelo("Golf")
    Concessionaria.registrar_cliente(concessionaria1, cliente1)
    Concessionaria.adicionar_carro_ao_estoque(concessionaria1, carro1)
    Concessionaria.adicionar_carro_ao_estoque(concessionaria1, carro2)
    Concessionaria.listar_carros_em_estoque(concessionaria1)
    Concessionaria.registrar_vendedor(concessionaria1, funcionario1)
    Concessionaria.encontrar_carro_por_modelo(concessionaria1, "skyline")
    Concessionaria.encontrar_funcionario_por_nome(concessionaria1, "henrrique")
    concessionaria.registrar_vendedor(funcionario1)
    concessionaria.registrar_cliente(cliente1)
    concessionaria.adicionar_carro_ao_estoque(carro1)
    # Listando carros em estoque
    concessionaria.listar_carros_em_estoque()
    cliente1.comprar_carro(carro1)
    # Listando clientes e vendedores
    concessionaria.listar_clientes()
    concessionaria.listar_vendedores()
    
if __name__ == "__main__": 
    main()

