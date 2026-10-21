class Carro:
    
    def __init__(self, marca, modelo, cor, cc, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.cc = cc
        self.ano = ano

    def calcular_ipva(self, ano_atual, valor_fipe):
        idade = ano_atual - self.ano
        ipva = idade * valor_fipe
        return ipva

    def ligar(self):
        print('ligando o carro')

    def acelerar(self):
        print('Acelerando o carro')

    def parar(self):
        print('Parando o carro')

c1 = Carro('Fiat','Punto','Vermelho',130, 2020)
c1.acelerar()
print(c1.calcular_ipva(2023, 40.50))