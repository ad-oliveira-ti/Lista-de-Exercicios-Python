class Concessionaria:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.vendedores = []
        self.estoque = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"{cliente.nome} registrado como cliente da concessionária.")

    def registrar_vendedor(self, vendedor):
        self.vendedores.append(vendedor)
        print(f"{vendedor.nome} registrado como vendedor da concessionária.")

    def adicionar_carro_ao_estoque(self, carro):
        self.estoque.append(carro)
        print(f"O carro: {carro.modelo} {carro.marca} foi adicionado ao estoque.")

    def listar_carros_em_estoque(self):
        if len(self.estoque) == 0:
            print("Não há carros em estoque.")
        else:
            print("Carros em estoque:")
            for carro in self.estoque:
                print(f"{carro.modelo} {carro.marca} - {carro.ano}")

    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("Não há clientes registrados.")
        else:
            print("Clientes registrados:")
            for cliente in self.clientes:
                print(cliente.nome)

    def listar_vendedores(self):
        if len(self.vendedores) == 0:
            print("Não há vendedores registrados.")
        else:
            print("Vendedores registrados:")
            for vendedor in self.vendedores:
                print(vendedor.nome)

    def encontrar_carro_por_modelo(self, modelo):
        for carro in self.estoque:
            if carro.modelo == modelo:
                print(f"Carro em estoque")
                return carro.marca, carro.modelo, carro.ano, carro.preco, carro.cor, carro.placa
        print(f"Não foi encontrado nenhum carro do modelo {modelo} em estoque.")
        return None

    #def encontrar_vendedor_por_nome(self, nome):
    #    for vendedor in self.vendedores:
    #        if vendedor.nome == nome:
    #            return vendedor
    #    print(f"Não foi encontrado nenhum vendedor com o nome {nome}.")

    def encontrar_funcionario_por_nome(self, nome):
        for funcionario in self.vendedores:
            if funcionario.nome == nome:
                print(f"Funcionario encontrado!")
                print(f"Nome    | Telefone    | Idade    |    Salario")
                return funcionario.nome, funcionario.cpf, funcionario.idade, funcionario.salario
        print(f"Não foi encontrado nenhum vendedor com o nome {nome}.")
