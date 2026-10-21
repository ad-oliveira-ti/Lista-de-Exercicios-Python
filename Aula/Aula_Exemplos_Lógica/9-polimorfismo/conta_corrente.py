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

    def __str__(self):
        return 'Conta corrente %s e saldo %s' % (self._numero_cc , self._saldo)  
