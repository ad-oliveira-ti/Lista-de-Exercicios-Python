class ContaCorrente:
    
    def __init__(self, numero_cc, saldo, pessoa, agencia, categoria):
        self._numero_cc = numero_cc
        self._saldo = saldo 
        self._pessoa = pessoa
        self._agencia = agencia
        self._categoria = categoria


    # Metodo TO STRING devolve valores especificados
    def __str__(self):
        return 'Conta corrente %s e o saldo %s' % (self._numero_cc , self._saldo)  
    
    # Metodo TO STRING devolve nome da classe
    #def __str__(self):
    #     return self.__class__.__name__
