from pessoa import Pessoa
from agencia import Agencia
from categoria import Categoria

class ContaCorrente:
    
    def __init__(self, numero_cc, saldo, pessoa, agencia, categoria):
        self._numero_cc = numero_cc
        self._saldo = saldo 
        self._pessoa = pessoa
        self._agencia = agencia
        self._categoria = categoria
        self._codigo_banco = "Meu atributo estatico" # Declarar um atributo estatico
        
    # Criar o metodo estatico
    @staticmethod
    def codigo_banco():
        return "001"
    
    # Metodo estatico com varias colecoes de atributos estaticos
    @staticmethod
    def codigos_bancos():
        return {'Banco do Brasil': 'codigo 111 BB', 'Banrisul': 'condigo 222 Banri'}

    def __str__(self):
        return 'Conta corrente %s e saldo %s' % (self._numero_cc , self._saldo)  
